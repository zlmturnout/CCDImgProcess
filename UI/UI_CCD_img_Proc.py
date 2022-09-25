# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CCD_img_Proc.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QTabWidget,
    QTextEdit, QToolBox, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1322, 1110)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 830))
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QSize(300, 300))
        self.toolBox.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.toolBox.setFont(font)
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setAutoFillBackground(False)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 300, 413))
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Refresh_tool = QPushButton(self.page)
        self.Refresh_tool.setObjectName(u"Refresh_tool")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Refresh_tool.sizePolicy().hasHeightForWidth())
        self.Refresh_tool.setSizePolicy(sizePolicy1)
        self.Refresh_tool.setMinimumSize(QSize(120, 40))
        self.Refresh_tool.setFont(font)
        self.Refresh_tool.setLayoutDirection(Qt.LeftToRight)
        self.Refresh_tool.setAutoFillBackground(False)
        self.Refresh_tool.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.Refresh_tool, 0, 0, 1, 1)

        self.Draw_box_tool = QToolButton(self.page)
        self.Draw_box_tool.setObjectName(u"Draw_box_tool")
        self.Draw_box_tool.setMinimumSize(QSize(120, 40))
        self.Draw_box_tool.setFont(font)
        self.Draw_box_tool.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.Draw_box_tool.setAutoRaise(True)
        self.Draw_box_tool.setArrowType(Qt.NoArrow)

        self.gridLayout_2.addWidget(self.Draw_box_tool, 1, 0, 1, 1)

        self.half_n_input = QLineEdit(self.page)
        self.half_n_input.setObjectName(u"half_n_input")
        sizePolicy1.setHeightForWidth(self.half_n_input.sizePolicy().hasHeightForWidth())
        self.half_n_input.setSizePolicy(sizePolicy1)
        self.half_n_input.setMinimumSize(QSize(120, 40))
        self.half_n_input.setMaximumSize(QSize(100, 40))
        self.half_n_input.setInputMethodHints(Qt.ImhFormattedNumbersOnly|Qt.ImhPreferNumbers)
        self.half_n_input.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.half_n_input, 4, 0, 1, 1)

        self.Select_column_tool = QToolButton(self.page)
        self.Select_column_tool.setObjectName(u"Select_column_tool")
        self.Select_column_tool.setMinimumSize(QSize(120, 40))
        self.Select_column_tool.setFont(font)
        self.Select_column_tool.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.Select_column_tool, 2, 0, 1, 1)

        self.toolButton_4 = QToolButton(self.page)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(120, 40))
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.toolButton_4, 0, 1, 1, 1)

        self.toolButton_5 = QToolButton(self.page)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setMinimumSize(QSize(120, 40))
        self.toolButton_5.setFont(font)
        self.toolButton_5.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.toolButton_5, 1, 1, 1, 1)

        self.Select_row_tool = QToolButton(self.page)
        self.Select_row_tool.setObjectName(u"Select_row_tool")
        self.Select_row_tool.setMinimumSize(QSize(120, 40))
        self.Select_row_tool.setFont(font)
        self.Select_row_tool.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.Select_row_tool, 2, 1, 1, 1)

        self.CV_median_tool = QToolButton(self.page)
        self.CV_median_tool.setObjectName(u"CV_median_tool")
        self.CV_median_tool.setMinimumSize(QSize(120, 40))
        self.CV_median_tool.setFont(font)
        self.CV_median_tool.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.CV_median_tool, 4, 1, 1, 1)

        self.toolBox.addItem(self.page, u"Tools")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 300, 413))
        self.gridLayout_7 = QGridLayout(self.page_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Add_row_btn = QPushButton(self.page_2)
        self.Add_row_btn.setObjectName(u"Add_row_btn")
        sizePolicy1.setHeightForWidth(self.Add_row_btn.sizePolicy().hasHeightForWidth())
        self.Add_row_btn.setSizePolicy(sizePolicy1)
        self.Add_row_btn.setMinimumSize(QSize(120, 40))
        self.Add_row_btn.setFont(font)
        self.Add_row_btn.setStyleSheet(u"background-color: rgb(146, 57, 255);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.Add_row_btn)

        self.Save_row_col_btn = QPushButton(self.page_2)
        self.Save_row_col_btn.setObjectName(u"Save_row_col_btn")
        sizePolicy1.setHeightForWidth(self.Save_row_col_btn.sizePolicy().hasHeightForWidth())
        self.Save_row_col_btn.setSizePolicy(sizePolicy1)
        self.Save_row_col_btn.setMinimumSize(QSize(120, 40))
        self.Save_row_col_btn.setFont(font)
        self.Save_row_col_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.Save_row_col_btn)

        self.Add_col_btn = QPushButton(self.page_2)
        self.Add_col_btn.setObjectName(u"Add_col_btn")
        sizePolicy1.setHeightForWidth(self.Add_col_btn.sizePolicy().hasHeightForWidth())
        self.Add_col_btn.setSizePolicy(sizePolicy1)
        self.Add_col_btn.setMinimumSize(QSize(120, 40))
        self.Add_col_btn.setFont(font)
        self.Add_col_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.Add_col_btn)


        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_2, u"Action")

        self.verticalLayout.addWidget(self.toolBox)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(300, 200))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Imax_Slider = QSlider(self.groupBox)
        self.Imax_Slider.setObjectName(u"Imax_Slider")
        sizePolicy1.setHeightForWidth(self.Imax_Slider.sizePolicy().hasHeightForWidth())
        self.Imax_Slider.setSizePolicy(sizePolicy1)
        self.Imax_Slider.setMinimumSize(QSize(280, 25))
        self.Imax_Slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Imax_Slider, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(60, 30))
        self.label.setMaximumSize(QSize(35, 25))
        palette = QPalette()
        brush = QBrush(QColor(255, 85, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label.setPalette(palette)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.Imin_text = QLineEdit(self.groupBox)
        self.Imin_text.setObjectName(u"Imin_text")
        sizePolicy1.setHeightForWidth(self.Imin_text.sizePolicy().hasHeightForWidth())
        self.Imin_text.setSizePolicy(sizePolicy1)
        self.Imin_text.setMinimumSize(QSize(80, 30))
        self.Imin_text.setMaximumSize(QSize(60, 25))

        self.horizontalLayout.addWidget(self.Imin_text)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(60, 30))
        self.label_2.setMaximumSize(QSize(35, 25))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_2.setPalette(palette1)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.Imax_text = QLineEdit(self.groupBox)
        self.Imax_text.setObjectName(u"Imax_text")
        sizePolicy1.setHeightForWidth(self.Imax_text.sizePolicy().hasHeightForWidth())
        self.Imax_text.setSizePolicy(sizePolicy1)
        self.Imax_text.setMinimumSize(QSize(80, 30))
        self.Imax_text.setMaximumSize(QSize(60, 25))

        self.horizontalLayout_3.addWidget(self.Imax_text)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.Imin_Slider = QSlider(self.groupBox)
        self.Imin_Slider.setObjectName(u"Imin_Slider")
        sizePolicy1.setHeightForWidth(self.Imin_Slider.sizePolicy().hasHeightForWidth())
        self.Imin_Slider.setSizePolicy(sizePolicy1)
        self.Imin_Slider.setMinimumSize(QSize(280, 25))
        self.Imin_Slider.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.Imin_Slider, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.Sub_box = QGroupBox(self.centralwidget)
        self.Sub_box.setObjectName(u"Sub_box")
        sizePolicy1.setHeightForWidth(self.Sub_box.sizePolicy().hasHeightForWidth())
        self.Sub_box.setSizePolicy(sizePolicy1)
        self.Sub_box.setMinimumSize(QSize(300, 300))
        self.Sub_box.setMaximumSize(QSize(300, 300))

        self.verticalLayout.addWidget(self.Sub_box)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Save_ROI_btn = QPushButton(self.centralwidget)
        self.Save_ROI_btn.setObjectName(u"Save_ROI_btn")
        sizePolicy1.setHeightForWidth(self.Save_ROI_btn.sizePolicy().hasHeightForWidth())
        self.Save_ROI_btn.setSizePolicy(sizePolicy1)
        self.Save_ROI_btn.setMinimumSize(QSize(120, 40))
        self.Save_ROI_btn.setFont(font)
        self.Save_ROI_btn.setStyleSheet(u"background-color: rgb(255, 110, 43);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.Save_ROI_btn)

        self.AutoCorrection_btn = QPushButton(self.centralwidget)
        self.AutoCorrection_btn.setObjectName(u"AutoCorrection_btn")
        sizePolicy1.setHeightForWidth(self.AutoCorrection_btn.sizePolicy().hasHeightForWidth())
        self.AutoCorrection_btn.setSizePolicy(sizePolicy1)
        self.AutoCorrection_btn.setMinimumSize(QSize(120, 40))
        self.AutoCorrection_btn.setFont(font)
        self.AutoCorrection_btn.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.AutoCorrection_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.IMG_path_text = QLineEdit(self.centralwidget)
        self.IMG_path_text.setObjectName(u"IMG_path_text")
        self.IMG_path_text.setMinimumSize(QSize(600, 40))
        self.IMG_path_text.setMaximumSize(QSize(2160, 40))
        palette2 = QPalette()
        brush3 = QBrush(QColor(255, 102, 143, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(202, 202, 202, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush5 = QBrush(QColor(255, 85, 127, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.IMG_path_text.setPalette(palette2)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.IMG_path_text.setFont(font1)
        self.IMG_path_text.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"border-size:5px;\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 102, 143);")
        self.IMG_path_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.IMG_path_text)

        self.Main_fig_box = QGroupBox(self.centralwidget)
        self.Main_fig_box.setObjectName(u"Main_fig_box")
        self.Main_fig_box.setMinimumSize(QSize(600, 600))
        self.Main_fig_box.setCursor(QCursor(Qt.CrossCursor))

        self.verticalLayout_2.addWidget(self.Main_fig_box)

        self.Column_box = QGroupBox(self.centralwidget)
        self.Column_box.setObjectName(u"Column_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Column_box.sizePolicy().hasHeightForWidth())
        self.Column_box.setSizePolicy(sizePolicy2)
        self.Column_box.setMinimumSize(QSize(600, 250))

        self.verticalLayout_2.addWidget(self.Column_box)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(308, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_5.addWidget(self.progressBar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Open_img_btn = QPushButton(self.centralwidget)
        self.Open_img_btn.setObjectName(u"Open_img_btn")
        sizePolicy1.setHeightForWidth(self.Open_img_btn.sizePolicy().hasHeightForWidth())
        self.Open_img_btn.setSizePolicy(sizePolicy1)
        self.Open_img_btn.setMinimumSize(QSize(250, 40))
        self.Open_img_btn.setFont(font)
        self.Open_img_btn.setStyleSheet(u"background-color: rgb(41, 173, 255);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.Open_img_btn)

        self.Row_box = QGroupBox(self.centralwidget)
        self.Row_box.setObjectName(u"Row_box")
        sizePolicy.setHeightForWidth(self.Row_box.sizePolicy().hasHeightForWidth())
        self.Row_box.setSizePolicy(sizePolicy)
        self.Row_box.setMinimumSize(QSize(250, 800))
        self.Row_box.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_4.addWidget(self.Row_box)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.info_textbox = QTextEdit(self.centralwidget)
        self.info_textbox.setObjectName(u"info_textbox")

        self.verticalLayout_5.addWidget(self.info_textbox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1322, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.menubar.setFont(font2)
        self.menubar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 235, 235, 206), stop:0.136364 rgba(255, 188, 188, 80), stop:0.329545 rgba(255, 162, 162, 80), stop:0.477273 rgba(255, 132, 132, 156), stop:0.897727 rgba(203, 48, 185, 80));")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuanalysise = QMenu(self.menubar)
        self.menuanalysise.setObjectName(u"menuanalysise")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuanalysise.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menuFile.addSeparator()

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Refresh_tool.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.Draw_box_tool.setText(QCoreApplication.translate("MainWindow", u"Draw box", None))
        self.half_n_input.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.Select_column_tool.setText(QCoreApplication.translate("MainWindow", u"Column", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"Rotate +90", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"Rotate -90", None))
        self.Select_row_tool.setText(QCoreApplication.translate("MainWindow", u"Row", None))
        self.CV_median_tool.setText(QCoreApplication.translate("MainWindow", u"CV_Median", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Tools", None))
        self.Add_row_btn.setText(QCoreApplication.translate("MainWindow", u"Sum_Row", None))
        self.Save_row_col_btn.setText(QCoreApplication.translate("MainWindow", u"Save lines", None))
        self.Add_col_btn.setText(QCoreApplication.translate("MainWindow", u"Sum_COl", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Action", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Color Range", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.Imin_text.setText(QCoreApplication.translate("MainWindow", u"1300", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.Imax_text.setText(QCoreApplication.translate("MainWindow", u"1400", None))
        self.Sub_box.setTitle(QCoreApplication.translate("MainWindow", u"ROI", None))
        self.Save_ROI_btn.setText(QCoreApplication.translate("MainWindow", u"Save ROI", None))
        self.AutoCorrection_btn.setText(QCoreApplication.translate("MainWindow", u"AutoCorrection", None))
        self.IMG_path_text.setText("")
        self.IMG_path_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path", None))
        self.Main_fig_box.setTitle(QCoreApplication.translate("MainWindow", u"MainFigure", None))
        self.Column_box.setTitle(QCoreApplication.translate("MainWindow", u"Column", None))
        self.Open_img_btn.setText(QCoreApplication.translate("MainWindow", u"Open image", None))
        self.Row_box.setTitle(QCoreApplication.translate("MainWindow", u"Row", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuanalysise.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

