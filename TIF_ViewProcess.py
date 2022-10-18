import datetime
import math
import os
import random
import sys
import time
import traceback
from collections import namedtuple
# import tools functions
from resource.Tools_functions import (creatPath, deco_count_time, get_datetime,
                                      log_exception, log_exceptions, my_logger,
                                      to_log)

import cv2
import matplotlib
import matplotlib.cm as cm
import matplotlib.image as mpimage
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.pyplot import MultipleLocator
from PIL import Image
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt, QThread, QTimer, Signal, Slot
from PySide6.QtGui import QAction, QDoubleValidator, QIntValidator, QTextCursor
from PySide6.QtWidgets import (QApplication, QFileDialog, QGridLayout,
                               QHBoxLayout, QMainWindow, QMessageBox,
                               QPushButton, QStyle, QVBoxLayout, QWidget)
from tifffile import tifffile

from Architect.AutoCorrelation_GaussPeak import (correlation_FWHM,
                                                 get_slice_peaks,
                                                 minimal_FWHM_correlation,
                                                 plot_GaussFit_results,get_correlation_img, save_pd_data)
from Architect.PeakCorrection_GECCD import (minimize_FWHM,
                                            partial_peak_correct,
                                            plot_SliceFit_line, tif_preprocess)
# import Gauss peak correction
from Architect.TIF_PeakcorrectScript import Fit_peak_data
# import main UI function
from UI.UI_CCD_img_Proc import Ui_MainWindow

# save path info
save_path = os.path.join(os.getcwd(), 'save_img')
creatPath(save_path)
today_folder=creatPath(os.path.join(save_path,time.strftime("%Y-%m-%d", time.localtime())))
log_path = os.path.join(os.getcwd(), 'log_info')
creatPath(log_path)

# logger
log_file = f'{time.strftime("%Y-%m-%d", time.localtime())}.log'
logger = my_logger(log_file=os.path.join(log_path, log_file), logger_name='Limin')

class RunQThread(QThread):
    """
    run any time consuming operation of func(*args,**kwargs)
    :argument can provide keyword args <timeout:float=1000.0>ms
    :return the signal will send function's return value in list form (return=funcs())
    Notice: if run exception occurs,will emit the <Exception info>
    """
    run_sig = Signal(list)
   
    def __init__(self, func, *args, timeout: float = 1000.0, **kwargs):
        super(RunQThread, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.run_flag = True
        self.run_time = timeout
        self.func = func
        self.result = None

    def run(self):
        t0 = time.time()
        #print('QThread start')
        while self.run_flag and time.time() - t0 < self.run_time:
            try:
                self.result = self.func(*self.args, **self.kwargs)
            except Exception as e:
                # print(e)
                error_info = traceback.format_exc() + str(e) + '\n'
                self.run_sig.emit([error_info])
            else:
                self.run_flag = False
                self.run_sig.emit([self.result])
                print(f'Qthread run cost{time.time()-t0:.2f}s')

    def __del__(self):
        self.run_time = False

class TIFProcess(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(TIFProcess, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(' CCD image TIF subtraction')
        self._ini_fig()
        self._ini_img_data()
        self._ini_menu()
        self._ini_event_()
        self.__ini_viewIMG__()

    def _ini_menu(self):
        """
        for menuBar
        :return:
        """
        style = QApplication.style()
        # open data file
        OpenTIF = QAction('open img(&O)...', self)
        OpenTIF.setIcon(style.standardIcon(QStyle.SP_DialogOpenButton))
        OpenTIF.setShortcut(Qt.CTRL + Qt.Key_O)
        OpenTIF.triggered.connect(self.newTif)
        self.menuFile.addAction(OpenTIF)
        # save data
        SaveTIF = QAction('save img(&S)...', self)
        SaveTIF.setIcon(style.standardIcon(QStyle.SP_DialogSaveButton))
        SaveTIF.setShortcut(Qt.CTRL + Qt.Key_S)
        SaveTIF.triggered.connect(self.saveTif)
        self.menuFile.addAction(SaveTIF)
        self.Open_img_btn.clicked.connect(self.newTif)
        # show View data in analysis menuBar
        # self.actionView_data.triggered.connect(self.show_full_data)

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    image save/open part
    """

    def _ini_img_data(self):
        # initialize all image data
        self.Sub_img = None
        self.Main_img = None
        # color bar
        self._cbar_Sub = None
        self._cbar_Main = None
        # np array data
        self.Sub_img_data = np.array([])
        self.Main_img_data = np.array([])
        self.Box_img_data = np.array([])
        # row and column data in pd form
        self.row_n=0
        self.column_n=0
        self.pd_row_data=pd.DataFrame()
        self.pd_col_data = pd.DataFrame()
        # file title
        self.file_folder=os.getcwd()
        self.fitData_folder=today_folder
        self.file_title=''
        # for fit parameter
        self.fit_para=[0,0,0] #[a,b,c]:y=a+b*x+c*x**2
        self.dispersion_const=29.3

    def open_tif_img(self):
        """
        open a 16bit tif file and return filename,img_data
        :return: filename,img_data in np array
        """
        img_data = np.array([])
        filename, filetype = QFileDialog.getOpenFileName(self, "open measured tif data file(supported 16bit TIF)",
                                                         self.file_folder, '*.tif')
        print(filename, filetype)
        # save raw image datainfo
        self.file_folder,file=os.path.split(filename)
        self.fitData_folder=creatPath(os.path.join(self.file_folder,'CorrectedResults'))
        self.file_title,extension=os.path.splitext(file)
        if os.path.isfile(filename) and filename.endswith('.tif'):
            img = Image.open(filename)
            #matrix = np.array(img,dtype=np.float32)
            img_data = np.array(img,dtype=np.float32)
            print(f'shape of the read img={np.shape(img_data)}')
            # save raw image info
            rawinfo_file=os.path.join(self.file_folder,f'RawImg-{self.file_title}.jpg')
            self.save_raw_img(img_data,rawinfo_file)
        return filename, img_data

    def save_tif_data(self,img_data:np.array([]),tif_file:str):
        """
        save data in the main figure box
        :return:
        """
        
        if tif_file.endswith('.tif'):
            tifffile.imwrite(tif_file, img_data)
    
    def ROI_to_excel(self,img_data:np.array([]),save_folder:str,filename:str):
        """save ROI img tif to excel file 

        Args:
            img_data (np.array): _description_

        Returns:
            _type_: _description_
        """
        pd_img_data=pd.DataFrame(img_data)
        if filename:
            excel_datafile=os.path.join(save_folder,f'ROI-data-{filename}.xlsx')
            excel_writer = pd.ExcelWriter(excel_datafile)
            pd_img_data.to_excel(excel_writer)
            excel_writer.save()
            print(f'save ROI data to excel xlsx file successfully\nfile path: {excel_datafile}')

    #@log_exceptions(log_func=logger.error)
    def newTif(self):
        self.Main_img_data=np.array([])
        filename,self.Main_img_data=self.open_tif_img()
        
        self.IMG_path_text.setText(f'{filename}')
        # img threshold bar
        I_min,I_max=self.get_I_range(self.Main_img_data)
        # min slider bar
        self.Imin_Slider.setRange(I_min,I_max)
        self.Imin_text.setText(str(I_min))
        self.Imin_Slider.setValue(I_min)
        # max slider bar
        self.Imax_Slider.setRange(I_min,I_max)
        self.Imax_text.setText(str(I_max))
        self.Imax_Slider.setValue(I_max)
        self.show_main_img(self.Main_img_data)

    def saveTif(self):
        if self.Main_img_data.size!=0:
            filename, filetype = QFileDialog.getSaveFileName(self, "save tif data file(supported filetype:16bit tif)",
                                                         self.file_folder, '*.tif')
            print(filename, filetype)
            self.save_tif_data(self.Main_img_data,filename)
        else:
            self.report_status('no data to save')

    @Slot()
    def on_Save_ROI_btn_clicked(self):
        if not self.Sub_img_data.size == 0:
            tif_file, filetype = QFileDialog.getSaveFileName(self, "save tif data file(supported filetype:16bit tif)",
                                                         self.file_folder, '*.tif')
            print(tif_file, filetype)
            self.save_tif_data(self.Sub_img_data,tif_file)
            save_folder,file=os.path.split(tif_file)
            filename,extension=os.path.splitext(file)
            self.ROI_to_excel(self.Sub_img_data,save_folder,filename)
            
    
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    fig part
    """

    def _ini_fig(self):
        # add Gridlayout into the Plot box [Sub,Mainfig]
        self.Sub_layout = QGridLayout(self.Sub_box)
        # main layout
        self.Main_layout = QGridLayout(self.Main_fig_box)
        self.Row_layout = QGridLayout(self.Row_box)
        self.Col_layout = QGridLayout(self.Column_box)
        # create matplotlib FigureCanvas for displaying Tif
        Sub_Canvas = FigureCanvas(Figure())
        Main_Canvas = FigureCanvas(Figure())
        Row_Canvas = FigureCanvas(Figure(figsize=(0.4, 6)))
        Col_Canvas = FigureCanvas(Figure(figsize=(6, 0.4)))
        # add the figure canvas into the Plot box [Sub,Mainfig]
        # for subtract img
        self.Sub_layout.addWidget(Sub_Canvas)
        self.Sub_layout.addWidget((NavigationToolbar(Sub_Canvas, self)))
        self._Sub_ax = Sub_Canvas.figure.subplots()
        # for Main img get the ax for plot
        self.Main_layout.addWidget(Main_Canvas)
        self.Main_layout.addWidget((NavigationToolbar(Main_Canvas, self)))
        self._Main_ax = Main_Canvas.figure.subplots()
        # for Row img
        self.Row_layout.addWidget(Row_Canvas)
        # self.Row_layout.addWidget((NavigationToolbar(Row_Canvas, self)))
        self._Row_ax = Row_Canvas.figure.subplots()
        # for Col img
        self.Col_layout.addWidget(Col_Canvas)
        # self.Col_layout.addWidget((NavigationToolbar(Col_Canvas, self)))
        self._Col_ax = Col_Canvas.figure.subplots()
        # timer for progressBar
        self.processBar_timer=QTimer()
        self.start_time=time.time()
        self.processBar_timer.timeout.connect(self.check_imgprocess)

    def set_progress_Bar(self,status:int):
        self.progressBar.setValue(status)
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    '''
    start correction action button part
    '''

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_AutoCorrection_btn_clicked(self):
        """
        find the corrected width of RIXS line from the input image (ROI)
        :return:
        """
        if not self.Sub_img_data.size==0:
            Fit_peak_data(self.Sub_img_data,self.peak_col,self.half_n,self.fitData_folder,self.file_title)
        else:
            print("should select ROI first")

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Peak_Correlation_btn_clicked(self):
        """ find the mininal FWHM by peak Correlation method

        Returns:
            _type_: _description_
        """
        if not self.Sub_img_data.size==0:
            try:
                # timer for img process
                self.processBar_timer.start(1000)
                self.start_time=time.time()
                clean_matrix,median_matrix=tif_preprocess(self.Sub_img_data)
                slice_n=self.set_slice_n()
                self.Peak_correlation_Qthread=RunQThread(minimal_FWHM_correlation,clean_matrix,slice_n,self.peak_col,self.fitData_folder,self.file_title)
                self.Peak_correlation_Qthread.run_sig.connect(self.get_PeakCorelation_results)
                self.Peak_correlation_Qthread.start()
            except Exception as e:
                print(traceback.format_exc()+e)
        else:
            print("should select ROI first")

    @Slot(list)
    def get_PeakCorelation_results(self,result:list):
        #stop timer
        self.set_progress_Bar(100)
        self.processBar_timer.stop()
        # unpack the results
        min_result=result[0]
        slice_n=min_result[-1].get("slice_n")
        p_col=min_result[-1].get("p_col")
        # plot best fit results with minimal FWHM
        plot_GaussFit_results(min_result[0],save_folder=self.fitData_folder,title=f'{self.file_title}_slice_n-{slice_n}_p_col-{p_col}')
        print(f'find minimal FWHM={min_result[1]:.4f} with parameter {min_result[-1]} and\n {min_result[0]["para"]}')
        # fit parameter
        self.fit_para=min_result[0]["fit_para"]
        self.fit_peak_center=p_col
        clean_matrix,median_matrix=tif_preprocess(self.Sub_img_data)
        row_list,col_list=get_slice_peaks(clean_matrix,slice_n=slice_n,p_col=p_col)
        fig3 = plt.figure(figsize =(16, 9)) 
        fig3.canvas.manager.window.setWindowTitle("Display slice peak center")
        plt.imshow(self.Main_img_data,cmap=cm.rainbow,vmin=1300,vmax=1380)
        plt.colorbar(location='bottom', fraction=0.1),plt.title("slice peak center")
        plt.plot(col_list,row_list,'o',label='slice center pixel',markersize=0.5,color='b')
        save_fig=os.path.join(self.fitData_folder,f'CorrelationSlice_Peakcenter_{self.file_title}.jpg')
        plt.savefig(save_fig)
        plt.show()

    @Slot()
    def check_imgprocess(self):
        timeout=60 #1000s for process
        precentage=int(100*(time.time()-self.start_time)/timeout)
        self.set_progress_Bar(precentage)

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Slice_correction_btn_clicked(self):
        """find FWHM of RIXS line by slice the ROI into many parts and fit- addition 

        Returns:
            _type_: _description_
        """
        if not self.Sub_img_data.size==0:
            # timer for img process
            self.processBar_timer.start(1000)
            self.start_time=time.time()
            clean_matrix,median_matrix=tif_preprocess(self.Sub_img_data)
            slice_n=self.set_slice_n()
            self.Peak_SliceCorrect_Qthread=RunQThread(partial_peak_correct,clean_matrix,slice_n,self.peak_col,self.fitData_folder,self.file_title)
            self.Peak_SliceCorrect_Qthread.run_sig.connect(self.get_SliceCorrect_results)
            self.Peak_SliceCorrect_Qthread.start()
            #partial_peak_correct(clean_matrix,slice_n=slice_n,p_col=self.peak_col,save_folder=self.fitData_folder,filename=self.file_title)
            #plt.show()
        else:
            print("should select ROI first")
    
    @Slot(list)
    def get_SliceCorrect_results(self,result:list):
        #stop timer
        self.set_progress_Bar(100)
        self.processBar_timer.stop()
        # unpack the results
        Total_add_result=result[0]
        slice_n=self.set_slice_n()
        plot_SliceFit_line(Total_add_result,index=slice_n+1,save_folder=self.fitData_folder,title=self.file_title)
        plt.show()
    
    @Slot()
    def on_FullSpectrum_btn_clicked(self):
        """get the corrected img and full spectrum with the fit para=[a,b,c] and dispersion const

        Returns:
            _type_: _description_
        """
        if not self.fit_para==[0,0,0]:
            corr_peakdata,pd_spectrum_data=get_correlation_img(self.Main_img_data,fit_para=self.fit_para,p_col=self.fit_peak_center,save_folder=self.fitData_folder,filename=self.file_title)
            plt.show()
            self.save_pd_data(pd_spectrum_data,info="Save Full Spectrum data")
            
    @Slot()
    def on_Add_row_btn_clicked(self):
        if not self.Main_img_data.size == 0:
            self.row_add_data = self.get_1D_Sum(self.Main_img_data)[1]
            self.column_n=0
            self.pd_row_data = pd.DataFrame(self.row_add_data, columns=['Sum_row'])
            self.pd_row_data['row'] = self.pd_row_data.index
            # plot and save data
            x_list, y_list = list(self.pd_row_data.index), list(self.row_add_data)
            self.show_row_plot(y_list, x_list)
            #self.save_pd_data(pd_row_data)

    @Slot()
    def on_Add_col_btn_clicked(self):
        if not self.Main_img_data.size == 0:
            self.col_add_data = self.get_1D_Sum(self.Main_img_data)[0]
            self.row_n=0
            self.pd_col_data = pd.DataFrame(self.col_add_data, columns=['Sum_column'])
            self.pd_col_data['col'] = self.pd_col_data.index
            # plot and save data
            x_list,y_list=list(self.pd_col_data.index),list(self.col_add_data)
            self.show_column_plot(x_list,y_list)
            #self.save_pd_data(pd_col_data)
    '''
        end action button part
    '''
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    data process part
    """

    def median_filter(self,matrix=np.array([]),filter_N:int=3):
        median_matrix=cv2.medianBlur(matrix, filter_N)
        return median_matrix

    @staticmethod
    def get_1D_Sum(tif_data:np.array([])):
        """
        sum TIF data in Row or Column
        :param tif_data: shoud be 2D array data M*N
        :return: sum of rows, sum of column
        """
        w, h = np.shape(tif_data)
        if w > 0 and h > 0:
            return [np.sum(tif_data, axis=0), np.sum(tif_data, axis=1)]
    
    @staticmethod
    def get_I_range(tif_data:np.array([])):
        """get the range of pixel intensity of the image

        Args:
            tif_data (np.array): img array
        Returns:
            (I_min:int,I_max:int):min and max intensity of the img array
        """
        w, h = np.shape(tif_data)
        if w > 0 and h > 0:
            return (int(np.min(tif_data)),int(np.max(tif_data)))


    def save_pd_data(self, pd_data: pd.DataFrame(),info=''):
        # save pd data to excel .xlsx file
        if not pd_data.empty:
            filename, filetype = QFileDialog.getSaveFileName(self, info+"(excel file:xlsx)",
                                                             self.file_folder, '*.xlsx')
            # excel writer
            #print(filename, filetype)
            if filename.endswith('.xlsx'):
                with pd.ExcelWriter(filename) as writer:
                    pd_data.to_excel(writer)
                #print('save to excel xlsx file successfully')

    '''
    end of data process part
    '''
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    # start of img view part

    def __ini_viewIMG__(self):
        self.Imin_Slider.valueChanged.connect(self.Imin_SliderValueChange)
        self.Imin_Slider.sliderReleased.connect(self.update_main_img)
        self.Imax_Slider.valueChanged.connect(self.Imax_SliderValueChange)
        self.Imax_Slider.sliderReleased.connect(self.update_main_img)
        self.Imin_text.returnPressed.connect(self.Imin_input_finished)
        self.Imax_text.returnPressed.connect(self.Imax_input_finished)
        self.Dispersion_const_spinbox.valueChanged['double'].connect(self.set_dispersion_c)
        self.draw_box_flag=False
        self.select_row_flag=False
        self.select_column_flag=False
        self.Peak_img_data=np.array([])
        self.Box_img_data=np.array([])
    
    @Slot(int)
    def Imin_SliderValueChange(self,value:int):
        """repaint the image based on the new Imin and Imax
        """
        print(f'current value: {value}')
        self.Imin_text.setText(str(value))
    
    @Slot(int)
    def Imax_SliderValueChange(self,value:int):
        """repaint the image based on the new Imin and Imax
        """
        print(f'current value: {value}')
        self.Imax_text.setText(str(value))

    @Slot()
    def update_main_img(self):
        """update the main img based on the new threshold Imin-Imax
        """
        Imin=self.Imin_Slider.value()
        Imax=self.Imax_Slider.value()
        self.show_main_img(self.Main_img_data,Imin=Imin,Imax=Imax)

    @Slot()
    def Imin_input_finished(self):
        """update the Imin slider and main image
        """
        input_Imin=int(self.Imin_text.text())
        if input_Imin>self.Imin_Slider.minimum() and input_Imin< self.Imin_Slider.maximum():
            self.Imin_Slider.setValue(input_Imin)
        else:
            self.Imin_Slider.setValue(int(self.Imin_Slider.minimum()))
        Imin=self.Imin_Slider.value()
        Imax=self.Imax_Slider.value()
        self.show_main_img(self.Main_img_data,Imin=Imin,Imax=Imax)
    
    @Slot()
    def Imax_input_finished(self):
        """update the Imin slider and main image
        """
        input_Imax=int(self.Imax_text.text())
        if input_Imax>self.Imin_Slider.minimum() and input_Imax< self.Imin_Slider.maximum():
            self.Imax_Slider.setValue(input_Imax)
        else:
            self.Imax_Slider.setValue(int(self.Imax_Slider.maximum()))
        Imin=self.Imin_Slider.value()
        Imax=self.Imax_Slider.value()
        self.show_main_img(self.Main_img_data,Imin=Imin,Imax=Imax)

    @Slot()
    def half_n_input_finished(self):
        """get the half width of the fit box image

        Returns:
            _type_: _description_
        """
        self.half_n=self.set_half_n()
    
    def set_half_n(self):
        half_n=int(self.half_n_input.text())
        return half_n if half_n>10 and half_n<1024 else 50

    def set_slice_n(self):
        """set the number of slices

        Returns:
           slice_n (int): _description_
        """
        slice_n=int(self.Slice_input.text())
        return slice_n if slice_n>0 and slice_n<1000 else 20
    
    @Slot(float)
    def set_dispersion_c(self,dis_const):
        print(f'get dispersion const: {dis_const} meV')
        #dis_const=float(self.Dispersion_const_spinbox.text().strip(' meV'))
        self.dispersion_const=dis_const
        return dis_const
    
    @Slot()
    def on_Draw_box_tool_clicked(self):
        self.find_peak_flag=False
        self.draw_box_flag=not self.draw_box_flag
        print(f'pressed {self.draw_box_flag}')
        self.update_tools_status()
    
    @Slot()
    def on_Select_column_tool_clicked(self):
        """select the peak from the img

        Returns:
            _type_: _description_
        """
        self.draw_box_flag=False
        self.select_row_flag=False
        self.select_column_flag=not self.select_column_flag
        print(f'find peak {self.select_column_flag} ')
        self.update_tools_status()
    
    @Slot()
    def on_Select_row_tool_clicked(self):
        """select the peak from the img

        Returns:
            _type_: _description_
        """
        self.draw_box_flag=False
        self.select_column_flag=False
        self.select_row_flag=not self.select_row_flag
        print(f'find peak {self.select_row_flag} ')
        self.update_tools_status()

    @Slot()
    def on_Refresh_tool_clicked(self):
        """refresh all
        """
        self.update_tools_status()
        self.update_main_image()

    def update_tools_status(self):
        """update status of all the tool buttons 

        Returns:
            _type_: _description_
        """
        stylesheet=f"background-color: rgb(33, 190, 193);border-bottom-color: rgb(139, 139, 139);border-right-color: rgb(48, 48, 48);selection-color: rgb(255, 85, 127);color: rgb(255, 255, 255);"
        if self.draw_box_flag:
            self.Draw_box_tool.setStyleSheet(stylesheet+"border:2px dashed rgb(255, 84, 17);")
        else:
            self.Draw_box_tool.setStyleSheet(stylesheet)
        if self.select_column_flag:
            self.Select_column_tool.setStyleSheet(stylesheet+"border:2px dashed rgb(255, 84, 17);")
        else:
            self.Select_column_tool.setStyleSheet(stylesheet)
        if self.select_row_flag:
            self.Select_row_tool.setStyleSheet(stylesheet+"border:2px dashed rgb(255, 84, 17);")
        else:
            self.Select_row_tool.setStyleSheet(stylesheet)
    # end of img view part
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    '''
    main plot event handling
    '''
    def _ini_event_(self):
        self.start_col=0
        self.start_row=0
        self.end_col=0
        self.end_row=0
        self.box_width=0
        self.box_height=0
        self.peak_col=0
        self.fit_peak_center=0
        self.half_n=50
        self.cidpress = self._Main_ax.figure.canvas.mpl_connect(
            'button_press_event', self.on_main_press)
        self.ridpress=self._Main_ax.figure.canvas.mpl_connect(
            'button_release_event', self.on_main_release)

    def on_main_press(self,event):
        if event.inaxes != self._Main_ax.axes:
            return
        contains, attrd = self._Main_ax.contains(event)
        if not contains:
            return
        # event handle show status
        if self.Main_img_data.size==0:
            return
        mouse_info=f'mouse pressed\n x: {int(event.xdata)} , y: {int(event.ydata)}'
        self.report_status(mouse_info)
        # image_array[M*N],plot data at row x and column y
        self.column_n=int(event.xdata)
        self.row_n=int(event.ydata)
        # box draw if draw box flag on
        self.start_col=int(event.xdata)
        self.start_row=int(event.ydata)
        if self.draw_box_flag:
            print(f'start({self.start_col},{self.start_row})')
            return
        # find peak flag on
        if self.select_row_flag:
            print(f'start({self.start_col},{self.start_row})')
            self.find_peak_img(self.start_row,self.start_col,pt=0)
            return
        if self.select_column_flag:
            print(f'start({self.start_col},{self.start_row})')
            self.find_peak_img(self.start_row,self.start_col,pt=1)
            return
        self.update_main_image()

    def update_main_image(self):
        # normally, show row and column line
        Imin=self.Imin_Slider.value()
        Imax=self.Imax_Slider.value()
        self.show_main_img(self.Main_img_data,show_lines=True,y_line=self.row_n,x_line=self.column_n,Imin=Imin,Imax=Imax)
        # row data from row_n
        row_list=self.Main_img_data[:,self.column_n]
        row_index=[i for i in range(len(row_list))]
        self.pd_row_data = pd.DataFrame(row_list, columns=['counts'])
        self.pd_row_data['row'] = self.pd_row_data.index
        # self.save_pd_data(pd_row_data)
        self.show_row_plot(row_list,row_index)

        # column data from column_n
        col_list=self.Main_img_data[self.row_n,:]
        col_index = [i for i in range(len(col_list))]
        self.show_column_plot(col_index, col_list)
        #col60_list=self.Main_img_data[49,:]
        self.pd_col_data = pd.DataFrame(col_list, columns=['counts'])
        self.pd_col_data['column'] = self.pd_col_data.index
        #self.save_pd_data(pd_column_data)
        self.show_row_plot(row_list, row_index)

    def on_main_release(self,event):
        """get the end x,y and draw a box

        Args:
            event (_type_): _description_
        """
        if event.inaxes != self._Main_ax.axes:
            return
        contains, attrd = self._Main_ax.contains(event)
        if not contains:
            return
        # event handle show status
        if self.Main_img_data.size==0:
            return
        if self.draw_box_flag:
            self.end_col=int(event.xdata)
            self.end_row=int(event.ydata)
            print(f'end ({self.end_col},{self.end_row})')
            self.box_width=self.end_col-self.start_col
            self.box_height=self.end_row-self.start_row
            self.show_main_img(self.Main_img_data,show_lines=False,show_box=True,Imin=self.Imin_Slider.value(),Imax=self.Imax_Slider.value(),start_col=self.start_col,start_row=self.start_row,box_width=self.box_width,box_height=self.box_height)
            self.Box_img_data=self.get_box_image()
            self.show_Sub_img(self.Box_img_data,Imin=self.Imin_Slider.value(),Imax=self.Imax_Slider.value())
            
    def get_box_image(self):
        start_row=min(self.start_row,self.end_row)
        end_row=max(self.start_row,self.end_row)
        start_col=min(self.start_col,self.end_col)
        end_col=max(self.start_col,self.end_col)

        if self.Main_img_data.size==0:
            return None
        else:
            Box_img_data=self.Main_img_data[start_row:end_row,start_col:end_col]
            # define the input matrix for correction
            self.peak_col=round((start_col+end_col)/2)
            self.fit_peak_center=self.peak_col # set the fit peak center to selected one
            self.half_n=round(abs(end_col-start_col)/2)
            self.Sub_img_data=self.Main_img_data[:,self.peak_col-self.half_n:self.peak_col+self.half_n] 
            ROI_area=f'ROI area box shape=({end_col-start_col},{end_row-start_row})\n center at ({self.peak_col},{round((start_row+end_row)/2)})'
            peak_info=f'peak_col: {self.peak_col}  half_n: {self.half_n}\n'
            self.show_ROI_info(peak_info+ROI_area)
            print(f'peak_col: {self.peak_col}\nhalf_n: {self.half_n}')
            return Box_img_data

    def find_peak_img(self,row:int,col:int,pt:int=0|1):
        """_summary_

        Args:
            row (int): peak at row number
            col (int): peak at column number 
            pt (int, optional): peak direction 0 is row,1 is col Defaults to 0 | 1.
        """
        if self.Main_img_data.size==0:
            return None
        w, h = np.shape(self.Main_img_data)
        if pt==0:
            # peak line in row
            self.half_n=self.set_half_n()
            start_row=max(row-self.half_n,0)
            end_row=min(row+self.half_n,h)
            self.box_width=w
            self.box_height=end_row-start_row
            self.Peak_img_data=self.Main_img_data[start_row:end_row,:]
            self.show_main_img(self.Main_img_data,show_lines=False,show_box=True,start_row=start_row,start_col=0,Imin=self.Imin_Slider.value(),Imax=self.Imax_Slider.value(),box_width=self.box_width,box_height=self.box_height)
            # define the input matrix for correction
            self.peak_col=round((start_row+end_row)/2)
            self.Sub_img_data=self.Main_img_data[:,self.peak_col-self.half_n:self.peak_col+self.half_n] 
            ROI_area=f'ROI area box shape=({w},{2*self.half_n})\n center at ({int(w/2)},{self.peak_col})'
            print(f'peak_col: {self.peak_col} half_n: {self.half_n}\n')
            peak_info=f'peak_col: {self.peak_col}half_n: {self.half_n}\n'
            self.show_ROI_info(peak_info+ROI_area)
        elif pt==1:
            # peak line in column
            self.half_n=self.set_half_n()
            start_col=max(col-self.half_n,0)
            end_col=min(col+self.half_n,h)
            self.box_width=end_col-start_col
            self.box_height=h
            self.Peak_img_data=self.Main_img_data[:,start_col:end_col]
            self.show_main_img(self.Main_img_data,show_lines=False,show_box=True,start_row=0,start_col=start_col,Imin=self.Imin_Slider.value(),Imax=self.Imax_Slider.value(),box_width=self.box_width,box_height=self.box_height)
            # define the input matrix for correction
            self.peak_col=round((start_col+end_col)/2)
            self.Sub_img_data=self.Main_img_data[:,self.peak_col-self.half_n:self.peak_col+self.half_n] 
            ROI_area=f'ROI area box shape=({2*self.half_n},{h})\n center at ({self.peak_col},{int(h/2)})'
            peak_info=f'peak_col: {self.peak_col} half_n: {self.half_n}\n'
            self.show_ROI_info(peak_info+ROI_area)
            print(f'peak_col: {self.peak_col} half_n: {self.half_n}\n')
        self.fit_peak_center=self.peak_col # set the fit peak center to selected one
        self.Sub_img_data=self.Peak_img_data

        self.show_Sub_img(self.Peak_img_data,Imin=self.Imin_Slider.value(),Imax=self.Imax_Slider.value())

    @Slot()
    def on_Save_row_col_btn_clicked(self):
        """
        save the current row and column data
        :return:
        """
        if not self.pd_col_data.empty and not self.pd_row_data.empty:
            self.save_pd_data(self.pd_row_data,info=f'save line data at column: {self.column_n} ')
            self.save_pd_data(self.pd_col_data,info=f'save line data at row: {self.row_n} ')

    @Slot()
    def on_CV_median_tool_clicked(self):
        """CV median filter
        """
        #Median_img_data=self.median_filter(self.Main_img_data,3)
        #self.show_Sub_img(Median_img_data,Imin=self.Imin_Slider.value(),Imax=self.Imax_Slider.value())
        self.Main_img_data=self.median_filter(self.Main_img_data,3)
        self.show_Sub_img(self.Main_img_data,Imin=self.Imin_Slider.value(),Imax=self.Imax_Slider.value())
        self.update_main_image()

    def save_raw_img(self,raw_matrix:np.array([]),img_file:str):
        """

        Args:
            raw_img_data (np.array): _description_
        """
            # plot the raw image
        fig = plt.figure(figsize =(16, 9))
        fig.canvas.manager.window.setWindowTitle("Visualize raw image")
        ax4=plt.subplot(2,2,4)
        plt.subplot(2,2,1),plt.imshow(raw_matrix,cmap=cm.rainbow,vmin=1300,vmax=1400)
        plt.colorbar(location='right', fraction=0.1),plt.title("raw image")
        sum_rows_raw=np.sum(raw_matrix,axis=0)
        row_index=[i for i in range(len(sum_rows_raw)) ]
        sum_cols_raw=np.sum(raw_matrix,axis=1)
        col_index=[j for j in range(len(sum_cols_raw)) ]
        plt.subplot(2,2,3),plt.plot(row_index,sum_rows_raw),plt.title("sum cols")
        plt.subplot(2,2,2),plt.plot(col_index,sum_cols_raw),plt.title("sum rows")
        #save by filename
        folderpath,file=os.path.split(img_file)
        filename,extension=os.path.splitext(file)
        plt.text(0, 0.5, s=f'Image file:\n{filename}',color = "m", transform=ax4.transAxes,fontsize=15)
        plt.savefig(img_file)

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    display img part
    """
    def show_Sub_img(self, Sub_img_data: np.array([]),Imin:int=1300,Imax:int=1400):
        """
        display background TIF img data
        :param Sub_img_data:
        :return:
        """
        self._Sub_ax.cla()
        if self._cbar_Sub:
            self._cbar_Sub.remove()
        im = self._Sub_ax.imshow(Sub_img_data, cmap=cm.rainbow,vmin=Imin,vmax=Imax)
        self._cbar_Sub = self._Sub_ax.figure.colorbar(im, location='bottom', fraction=0.05)
        self._Sub_ax.figure.canvas.draw()


    def show_main_img(self, main_img_data: np.array([]), show_lines=False, x_line=0, y_line=0,Imin:int=1300,Imax:int=1400,show_box=False,start_col=0,start_row=0,box_width=500,box_height=500):
        """
        display the img data after subtraction
        :param main_img_data: np.array(img_data)
        :param x_line:
        :param show_lines: show vertical line and horizon line
        :param main_img_data:
        :return:
        """
        #print(f'shape of the read img={np.shape(main_img_data)}')
        self._Main_ax.cla()
        if self._cbar_Main:
            self._cbar_Main.remove()
        im = self._Main_ax.imshow(main_img_data, cmap=cm.rainbow,vmin=Imin,vmax=Imax)
        if show_lines:
            self._Main_ax.axhline(y=y_line , color='deeppink', linestyle='--',linewidth=0.5)
            self._Main_ax.axvline(x=x_line , color='deeppink', linestyle='--',linewidth=0.5)
        if show_box:
            self._Main_ax.add_patch(Rectangle((start_col,start_row),box_width,box_height,edgecolor='red',
                    facecolor='none',
                    lw=1))
        self._cbar_Main = self._Main_ax.figure.colorbar(im, location='bottom', fraction=0.05)
        self._Main_ax.figure.tight_layout()
        self._Main_ax.figure.canvas.draw()

    def show_row_plot(self,x_list:list,y_list:list):
        """
        plot(x,y) in the row box
        :param x:
        :param y:
        :return:
        """
        self._Row_ax.cla()
        self._Row_ax.plot(x_list, y_list, marker='o', markersize=0.5, markerfacecolor='c',
                              markeredgecolor='c', linestyle='-',linewidth=0.5, color='c')
        self._Row_ax.invert_yaxis()
        self._Row_ax.figure.tight_layout()
        self._Row_ax.figure.canvas.draw()

    def show_column_plot(self,x_list:list,y_list:list):
        """
        plot(x,y) in the row box
        :param x:
        :param y:
        :return:
        """
        self._Col_ax.cla()
        self._Col_ax.plot(x_list, y_list, marker='o', markersize=0.5, markerfacecolor='c',
                              markeredgecolor='c', linestyle='-',linewidth=0.5, color='c')
        #self._Col_ax.invert_xaxis()
        self._Col_ax.figure.tight_layout()
        self._Col_ax.figure.canvas.draw()
    
    def show_ROI_info(self,info_text:str):
        curent_text=self.info_textbox.toPlainText()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.info_textbox.setText(curent_text+'\n'+timestamp+'>\n'+info_text+'\n')

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    status part
    """

    def report_status(self, info):
        """
        show info in the status bar
        :param info:
        :return:
        """
        self.statusBar().showMessage(info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TIFProcess()
    win.show()
    sys.exit(app.exec())
