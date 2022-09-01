import time, random, sys, os, math
import matplotlib
import cv2
from collections import namedtuple
import matplotlib.image as mpimage
import pandas as pd

from matplotlib.backends.backend_qtagg import(FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib.pyplot import MultipleLocator
import matplotlib.image as mpimg
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from PIL import Image
from tifffile import tifffile
import time, random, sys, os, math, datetime, traceback
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QGridLayout
from PySide6.QtCore import QTimer, Slot, QThread, Signal, Qt
from PySide6.QtGui import QDoubleValidator, QIntValidator, QTextCursor,QAction
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QHBoxLayout, QVBoxLayout, QMessageBox
# import tools functions
from resource.Tools_functions import get_datetime, my_logger, creatPath, to_log, log_exception, log_exceptions, \
    deco_count_time
# import main UI function
from UI.UI_CCD_Sub import Ui_MainWindow

# save path info
save_path = os.path.join(os.getcwd(), 'save_img')
creatPath(save_path)
log_path = os.path.join(os.getcwd(), 'log_info')
creatPath(log_path)

# logger
log_file = f'{time.strftime("%Y-%m-%d", time.localtime())}.log'
logger = my_logger(log_file=os.path.join(log_path, log_file), logger_name='Limin')


class TIFProcess(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(TIFProcess, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(' CCD image TIF subtraction')
        self._ini_fig()
        self._ini_img_data()
        self._ini_menu()
        self._ini_event_()

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
        OpenTIF.triggered.connect(self.openTif)
        self.menuFile.addAction(OpenTIF)
        # save data
        SaveTIF = QAction('save img(&S)...', self)
        SaveTIF.setIcon(style.standardIcon(QStyle.SP_DialogSaveButton))
        SaveTIF.setShortcut(Qt.CTRL + Qt.Key_S)
        SaveTIF.triggered.connect(self.saveTif)
        self.menuFile.addAction(SaveTIF)
        # show View data in analysis menuBar
        # self.actionView_data.triggered.connect(self.show_full_data)

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    image save/open part
    """

    def _ini_img_data(self):
        # initialize all image data
        self.Mea_img = None
        self.BGR_img = None
        self.Sub_img = None
        self.Main_img = None
        # color bar
        self._cbar_Mea = None
        self._cbar_BGR = None
        self._cbar_Sub = None
        self._cbar_Main = None
        # np array data
        self.Mea_img_data = np.array([])
        self.BGR_img_data = np.array([])
        self.Sub_img_data = np.array([])
        self.Main_img_data = np.array([])
        # row and column data in pd form
        self.row_n=0
        self.column_n=0
        self.pd_row_data=pd.DataFrame()
        self.pd_col_data = pd.DataFrame()

    def open_tif_img(self):
        """
        open a 16bit tif file and return filename,img_data
        :return: filename,img_data in np array
        """
        img_data = np.array([])
        filename, filetype = QFileDialog.getOpenFileName(self, "open measured tif data file(supported 16bit TIF)",
                                                         './', '*.tif')
        print(filename, filetype)
        if os.path.isfile(filename) and filename.endswith('.tif'):
            img = Image.open(filename)
            img_data = np.array(img)
            print(f'shape of the read img={np.shape(img_data)}')
        return filename, img_data

    def save_tif_data(self,img_data:np.array([])):
        """
        save data in the main figure box
        :return:
        """
        filename, filetype = QFileDialog.getSaveFileName(self, "save tif data file(supported filetype:16bit tif)",
                                                         './', '*.tif')
        print(filename, filetype)
        if filename.endswith('.tif'):
            tifffile.imsave(filename, img_data)

    #@log_exceptions(log_func=logger.error)
    def openTif(self):
        self.Main_img_data=np.array([])
        filename,self.Main_img_data=self.open_tif_img()
        self.show_main_img(self.Main_img_data)

    def saveTif(self):
        if self.Main_img_data.size!=0:
            self.save_tif_data(self.Main_img_data)
        else:
            self.report_status('no data to save')

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    fig part
    """

    def _ini_fig(self):
        # add Gridlayout into the Plot box [Mea,BGR,Sub,Mainfig]
        self.Mea_layout = QGridLayout(self.Mea_box)
        self.BGR_layout = QGridLayout(self.BGR_box)
        self.Sub_layout = QGridLayout(self.Sub_box)
        # main layout
        self.Main_layout = QGridLayout(self.Main_fig_box)
        self.Row_layout = QGridLayout(self.Row_box)
        self.Col_layout = QGridLayout(self.Column_box)
        # create matplotlib FigureCanvas for displaying Tif
        Mea_Canvas = FigureCanvas(Figure())
        BGR_Canvas = FigureCanvas(Figure())
        Sub_Canvas = FigureCanvas(Figure())
        Main_Canvas = FigureCanvas(Figure())
        Row_Canvas = FigureCanvas(Figure(figsize=(0.4, 6)))
        Col_Canvas = FigureCanvas(Figure(figsize=(6, 0.4)))
        # add the figure canvas into the Plot box [Mea,BGR,Sub,Mainfig]
        # for measured img
        self.Mea_layout.addWidget(Mea_Canvas)
        self.Mea_layout.addWidget((NavigationToolbar(Mea_Canvas, self)))
        self._Mea_ax = Mea_Canvas.figure.subplots()
        # for background img
        self.BGR_layout.addWidget(BGR_Canvas)
        self.BGR_layout.addWidget((NavigationToolbar(BGR_Canvas, self)))
        self._BGR_ax = BGR_Canvas.figure.subplots()
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

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    '''
    start action button part
    '''

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Measured_btn_clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "open measured tif data file(supported 16bit TIF)",
                                                         './', '*.tif')
        print(filename, filetype)
        self.Mea_path_line.setText(filename)
        if os.path.isfile(filename) and filename.endswith('.tif'):
            self.Mea_img = Image.open(filename)
            self.Mea_img_data = np.array(self.Mea_img)
            print(f'shape of the read img={np.shape(self.Mea_img_data)}')
            self.show_mea_img(self.Mea_img_data)

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Background_btn_clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "open background tif data file(supported 16bit TIF)",
                                                         './', '*.tif')
        print(filename, filetype)
        self.BGR_path_line.setText(filename)
        if os.path.isfile(filename) and filename.endswith('.tif'):
            self.BGR_img = Image.open(filename)
            self.BGR_img_data = np.array(self.BGR_img)
            print(self.BGR_img_data.dtype)
            print(f'shape of the read img={np.shape(self.BGR_img_data)}')
            self.show_BGR_img(self.BGR_img_data)

    @log_exceptions(log_func=logger.error)
    @Slot()
    def on_Subtract_btn_clicked(self):
        """
        subtract img_measured  by img_background
        :return:
        """
        if self.Mea_img_data.size == 0 or self.BGR_img_data.size == 0:
            info = 'import both measured and background tif data first '
            self.report_status(info)
        elif np.shape(self.Mea_img_data) == np.shape(self.BGR_img_data):
            # self.Sub_img_data=self.Mea_img_data-self.BGR_img_data
            # self.Sub_img_data = np.subtract(self.Mea_img_data, self.BGR_img_data)
            # use cv2
            self.Sub_img_data = cv2.subtract(self.Mea_img_data, self.BGR_img_data)
            print(self.Sub_img_data)
            self.show_subtract_img(self.Sub_img_data)

    # @log_exceptions(log_func=logger.error)
    # @Slot()
    # def on_AutoCorrection_btn_clicked(self):
    #     """
    #     find the corrected width of RIXS line from the input image
    #     :return:
    #     """
    #     filename, filetype = QFileDialog.getOpenFileName(self, "open CCD tif data file(supported 16bit TIF)",
    #                                                      './', '*.tif')
    #     print(filename, filetype)
    #     if os.path.isfile(filename) and filename.endswith('.tif'):
    #         matrix = mpimage.imread(filename).astype('float64')
    #         self.Main_img = Image.open(filename)
    #         self.Main_img_data = np.array(self.Main_img,dtype='float64')
    #         print(self.Main_img_data.dtype)
    #         print(f'shape of the read img={np.shape(self.Main_img_data)}')
    #         # print(matrix.dtype)
    #         # print(f'matrix:{matrix}\n tif data:{self.Main_img_data}')

    #         corrected_line,x_out,y_out = calculate_line_width(matrix)
    #         print(corrected_line)
    #         self.show_main_img(self.Main_img_data)
    #         plt.figure(1)
    #         plt.plot(x_out,y_out)
    #         plt.show()




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

    @Slot()
    def on_Save_Substract_btn_clicked(self):
        if not self.Sub_img_data.size == 0:
            self.save_tif_data(self.Sub_img_data)

    '''
        end action button part
    '''
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    data process part
    """

    @staticmethod
    def get_1D_Sum(tif_data):
        """
        sum TIF data in Row or Column
        :param tif_data: shoud be 2D array data M*N
        :return: sum of rows, sum of column
        """
        w, h = np.shape(tif_data)
        if w > 0 and h > 0:
            return [np.sum(tif_data, axis=0), np.sum(tif_data, axis=1)]

    def save_pd_data(self, pd_data: pd.DataFrame(),info=''):
        # save pd data to excel .xlsx file
        if not pd_data.empty:
            filename, filetype = QFileDialog.getSaveFileName(self, info+"(excel file:xlsx)",
                                                             './', '*.xlsx')
            # excel writer
            print(filename, filetype)
            if filename.endswith('.xlsx'):
                excel_writer = pd.ExcelWriter(filename)
                pd_data.to_excel(excel_writer)
                excel_writer.save()
                print('save to excel xlsx file successfully')

    '''
    end of data process part
    '''
    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************

    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    '''
    main plot event handling
    '''
    def _ini_event_(self):
        self.cidpress = self._Main_ax.figure.canvas.mpl_connect(
            'button_press_event', self.on_main_press)

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
        self.show_main_img(self.Main_img_data,show_lines=True,y_line=self.row_n,x_line=self.column_n)
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

    @Slot()
    def on_Save_row_col_btn_clicked(self):
        """
        save the current row and column data
        :return:
        """
        if not self.pd_col_data.empty and not self.pd_row_data.empty:
            self.save_pd_data(self.pd_row_data,info=f'save line data at column: {self.column_n} ')
            self.save_pd_data(self.pd_col_data,info=f'save line data at row: {self.row_n} ')



    # **************************************LIMIN_Zhou_at_SSRF_BL20U**************************************
    """
    display img part
    """
    def show_mea_img(self, mea_img_data: np.array([])):
        """
        display measured TIF img data
        :param mea_img_data:
        :return:
        """
        self._Mea_ax.cla()
        w, h = np.shape(mea_img_data)
        if self._cbar_Mea:
            self._cbar_Mea.remove()
        im = self._Mea_ax.imshow(mea_img_data, cmap=cm.rainbow)
        # self._Mea_ax.axhline(y=h/2,color='magenta',linestyle='--')
        # self._Mea_ax.axvline(x=w/ 2, color='magenta', linestyle='--')
        self._cbar_Mea = self._Mea_ax.figure.colorbar(im, location='bottom', fraction=0.05)
        self._Mea_ax.figure.canvas.draw()

    def show_BGR_img(self, BGR_img_data: np.array([])):
        """
        display background TIF img data
        :param BGR_img_data:
        :return:
        """
        self._BGR_ax.cla()
        if self._cbar_BGR:
            self._cbar_BGR.remove()
        im = self._BGR_ax.imshow(BGR_img_data, cmap=cm.rainbow)
        self._cbar_BGR = self._BGR_ax.figure.colorbar(im, location='bottom', fraction=0.05)
        self._BGR_ax.figure.canvas.draw()

    def show_subtract_img(self, sub_img_data: np.array([])):
        """
        display the img data after subtraction
        :param sub_img_data:
        :return:
        """
        print(f'shape of the read img={np.shape(sub_img_data)}')
        self._Sub_ax.cla()
        if self._cbar_Sub:
            self._cbar_Sub.remove()
        im = self._Sub_ax.imshow(sub_img_data, cmap=cm.rainbow)
        self._cbar_Sub = self._Sub_ax.figure.colorbar(im, location='bottom', fraction=0.05)
        self._Sub_ax.figure.canvas.draw()

    def show_main_img(self, main_img_data: np.array([]), show_lines=False, x_line=0, y_line=0):
        """
        display the img data after subtraction
        :param main_img_data: np.array(img_data)
        :param x_line:
        :param show_lines: show vertical line and horizon line
        :param main_img_data:
        :return:
        """
        print(f'shape of the read img={np.shape(main_img_data)}')
        self._Main_ax.cla()
        if self._cbar_Main:
            self._cbar_Main.remove()
        im = self._Main_ax.imshow(main_img_data, cmap=cm.rainbow,vmin=1300,vmax=1400)
        if show_lines:
            self._Main_ax.axhline(y=y_line , color='deeppink', linestyle='--',linewidth=0.5)
            self._Main_ax.axvline(x=x_line , color='deeppink', linestyle='--',linewidth=0.5)
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
