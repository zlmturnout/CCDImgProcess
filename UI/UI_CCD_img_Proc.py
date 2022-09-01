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
    QToolBox, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1786, 1202)
        MainWindow.setMinimumSize(QSize(1200, 830))
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1085, 151, 481, 576))
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Measured_btn = QPushButton(self.widget)
        self.Measured_btn.setObjectName(u"Measured_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Measured_btn.sizePolicy().hasHeightForWidth())
        self.Measured_btn.setSizePolicy(sizePolicy)
        self.Measured_btn.setMinimumSize(QSize(120, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.Measured_btn.setFont(font)
        self.Measured_btn.setStyleSheet(u"background-color: rgb(41, 173, 255);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.Measured_btn)

        self.Background_btn = QPushButton(self.widget)
        self.Background_btn.setObjectName(u"Background_btn")
        sizePolicy.setHeightForWidth(self.Background_btn.sizePolicy().hasHeightForWidth())
        self.Background_btn.setSizePolicy(sizePolicy)
        self.Background_btn.setMinimumSize(QSize(120, 40))
        self.Background_btn.setFont(font)
        self.Background_btn.setStyleSheet(u"background-color: rgb(41, 173, 255);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.Background_btn)

        self.Subtract_btn = QPushButton(self.widget)
        self.Subtract_btn.setObjectName(u"Subtract_btn")
        sizePolicy.setHeightForWidth(self.Subtract_btn.sizePolicy().hasHeightForWidth())
        self.Subtract_btn.setSizePolicy(sizePolicy)
        self.Subtract_btn.setMinimumSize(QSize(120, 40))
        self.Subtract_btn.setFont(font)
        self.Subtract_btn.setStyleSheet(u"background-color: rgb(255, 98, 161);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.Subtract_btn)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Mea_path_line = QLineEdit(self.widget)
        self.Mea_path_line.setObjectName(u"Mea_path_line")
        self.Mea_path_line.setMinimumSize(QSize(280, 40))
        self.Mea_path_line.setMaximumSize(QSize(680, 40))
        palette = QPalette()
        brush = QBrush(QColor(255, 102, 143, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(202, 202, 202, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 85, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.Mea_path_line.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.Mea_path_line.setFont(font1)
        self.Mea_path_line.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"border-size:5px;\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 102, 143);")

        self.gridLayout_3.addWidget(self.Mea_path_line, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.AutoCorrection_btn = QPushButton(self.widget)
        self.AutoCorrection_btn.setObjectName(u"AutoCorrection_btn")
        sizePolicy.setHeightForWidth(self.AutoCorrection_btn.sizePolicy().hasHeightForWidth())
        self.AutoCorrection_btn.setSizePolicy(sizePolicy)
        self.AutoCorrection_btn.setMinimumSize(QSize(120, 40))
        self.AutoCorrection_btn.setFont(font)
        self.AutoCorrection_btn.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.AutoCorrection_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.Save_Substract_btn = QPushButton(self.widget)
        self.Save_Substract_btn.setObjectName(u"Save_Substract_btn")
        sizePolicy.setHeightForWidth(self.Save_Substract_btn.sizePolicy().hasHeightForWidth())
        self.Save_Substract_btn.setSizePolicy(sizePolicy)
        self.Save_Substract_btn.setMinimumSize(QSize(120, 40))
        self.Save_Substract_btn.setFont(font)
        self.Save_Substract_btn.setStyleSheet(u"background-color: rgb(255, 110, 43);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.Save_Substract_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.BGR_path_line = QLineEdit(self.widget)
        self.BGR_path_line.setObjectName(u"BGR_path_line")
        self.BGR_path_line.setMinimumSize(QSize(280, 40))
        self.BGR_path_line.setMaximumSize(QSize(680, 40))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.BGR_path_line.setPalette(palette1)
        self.BGR_path_line.setFont(font1)
        self.BGR_path_line.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"border-size:5px;\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 102, 143);")

        self.gridLayout_3.addWidget(self.BGR_path_line, 1, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_3)


        self.gridLayout_6.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(400, 400))
        self.tabWidget.setMaximumSize(QSize(800, 800))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Mea_box = QGroupBox(self.tab)
        self.Mea_box.setObjectName(u"Mea_box")
        sizePolicy1.setHeightForWidth(self.Mea_box.sizePolicy().hasHeightForWidth())
        self.Mea_box.setSizePolicy(sizePolicy1)
        self.Mea_box.setMinimumSize(QSize(300, 300))

        self.gridLayout_2.addWidget(self.Mea_box, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.BGR_box = QGroupBox(self.tab_2)
        self.BGR_box.setObjectName(u"BGR_box")
        sizePolicy1.setHeightForWidth(self.BGR_box.sizePolicy().hasHeightForWidth())
        self.BGR_box.setSizePolicy(sizePolicy1)
        self.BGR_box.setMinimumSize(QSize(300, 300))

        self.gridLayout_5.addWidget(self.BGR_box, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_9 = QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.Sub_box = QGroupBox(self.tab_3)
        self.Sub_box.setObjectName(u"Sub_box")
        sizePolicy1.setHeightForWidth(self.Sub_box.sizePolicy().hasHeightForWidth())
        self.Sub_box.setSizePolicy(sizePolicy1)
        self.Sub_box.setMinimumSize(QSize(300, 300))

        self.gridLayout_9.addWidget(self.Sub_box, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout_6.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(182, 152, 766, 791))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Row_box = QGroupBox(self.widget1)
        self.Row_box.setObjectName(u"Row_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Row_box.sizePolicy().hasHeightForWidth())
        self.Row_box.setSizePolicy(sizePolicy2)
        self.Row_box.setMinimumSize(QSize(150, 600))
        self.Row_box.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.Row_box, 0, 0, 1, 1)

        self.Main_fig_box = QGroupBox(self.widget1)
        self.Main_fig_box.setObjectName(u"Main_fig_box")
        self.Main_fig_box.setMinimumSize(QSize(600, 600))
        self.Main_fig_box.setCursor(QCursor(Qt.CrossCursor))

        self.gridLayout_4.addWidget(self.Main_fig_box, 0, 1, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolButton_4 = QToolButton(self.widget1)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(45, 25))
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.toolButton_4, 0, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(60, 25))
        self.lineEdit_2.setMaximumSize(QSize(60, 25))

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.toolButton_5 = QToolButton(self.widget1)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setMinimumSize(QSize(45, 25))
        self.toolButton_5.setFont(font)
        self.toolButton_5.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.toolButton_5, 1, 2, 1, 1)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(35, 25))
        self.label.setMaximumSize(QSize(35, 25))
        palette2 = QPalette()
        brush3 = QBrush(QColor(255, 85, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        brush5 = QBrush(QColor(120, 120, 120, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        self.label.setPalette(palette2)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(35, 25))
        self.label_2.setMaximumSize(QSize(35, 25))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        self.label_2.setPalette(palette3)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(60, 25))
        self.lineEdit.setMaximumSize(QSize(60, 25))

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)

        self.horizontalSlider = QSlider(self.widget1)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimumSize(QSize(150, 25))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.horizontalSlider)

        self.horizontalSlider_2 = QSlider(self.widget1)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMinimumSize(QSize(150, 25))
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.horizontalSlider_2)


        self.gridLayout_4.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.Column_box = QGroupBox(self.widget1)
        self.Column_box.setObjectName(u"Column_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Column_box.sizePolicy().hasHeightForWidth())
        self.Column_box.setSizePolicy(sizePolicy3)
        self.Column_box.setMinimumSize(QSize(600, 150))

        self.gridLayout_4.addWidget(self.Column_box, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(308, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(self.widget1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(954, 152, 124, 528))
        self.verticalLayout_8 = QVBoxLayout(self.widget2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.toolBox = QToolBox(self.widget2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(100, 300))
        self.toolBox.setFont(font)
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setAutoFillBackground(False)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 120, 236))
        self.gridLayout_8 = QGridLayout(self.page)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(100, 40))
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.pushButton)

        self.toolButton = QToolButton(self.page)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(100, 40))
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.toolButton)

        self.toolButton_2 = QToolButton(self.page)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(100, 40))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.toolButton_2.setFont(font2)
        self.toolButton_2.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(self.page)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(100, 40))
        self.toolButton_3.setFont(font2)
        self.toolButton_3.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.toolButton_3)


        self.gridLayout_8.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.toolBox.addItem(self.page, u"Tools")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 120, 236))
        self.gridLayout_7 = QGridLayout(self.page_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Add_row_btn = QPushButton(self.page_2)
        self.Add_row_btn.setObjectName(u"Add_row_btn")
        sizePolicy.setHeightForWidth(self.Add_row_btn.sizePolicy().hasHeightForWidth())
        self.Add_row_btn.setSizePolicy(sizePolicy)
        self.Add_row_btn.setMinimumSize(QSize(100, 40))
        self.Add_row_btn.setFont(font)
        self.Add_row_btn.setStyleSheet(u"background-color: rgb(146, 57, 255);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.Add_row_btn)

        self.Save_row_col_btn = QPushButton(self.page_2)
        self.Save_row_col_btn.setObjectName(u"Save_row_col_btn")
        sizePolicy.setHeightForWidth(self.Save_row_col_btn.sizePolicy().hasHeightForWidth())
        self.Save_row_col_btn.setSizePolicy(sizePolicy)
        self.Save_row_col_btn.setMinimumSize(QSize(100, 40))
        self.Save_row_col_btn.setFont(font)
        self.Save_row_col_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.Save_row_col_btn)

        self.Add_col_btn = QPushButton(self.page_2)
        self.Add_col_btn.setObjectName(u"Add_col_btn")
        sizePolicy.setHeightForWidth(self.Add_col_btn.sizePolicy().hasHeightForWidth())
        self.Add_col_btn.setSizePolicy(sizePolicy)
        self.Add_col_btn.setMinimumSize(QSize(100, 40))
        self.Add_col_btn.setFont(font)
        self.Add_col_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.Add_col_btn)


        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_2, u"Action")

        self.verticalLayout_6.addWidget(self.toolBox)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 218, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1786, 31))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.menubar.setFont(font3)
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

        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Measured_btn.setText(QCoreApplication.translate("MainWindow", u"Measured", None))
        self.Background_btn.setText(QCoreApplication.translate("MainWindow", u"Background", None))
        self.Subtract_btn.setText(QCoreApplication.translate("MainWindow", u"Substract", None))
        self.Mea_path_line.setText(QCoreApplication.translate("MainWindow", u"filepath", None))
        self.AutoCorrection_btn.setText(QCoreApplication.translate("MainWindow", u"AutoCorrection", None))
        self.Save_Substract_btn.setText(QCoreApplication.translate("MainWindow", u"Save substract", None))
        self.BGR_path_line.setText(QCoreApplication.translate("MainWindow", u"filepath", None))
        self.Mea_box.setTitle(QCoreApplication.translate("MainWindow", u"Mea", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"MeaTIF", None))
        self.BGR_box.setTitle(QCoreApplication.translate("MainWindow", u"BGR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"BGRTIF", None))
        self.Sub_box.setTitle(QCoreApplication.translate("MainWindow", u"Sub", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"SubTIF", None))
        self.Row_box.setTitle(QCoreApplication.translate("MainWindow", u"Row", None))
        self.Main_fig_box.setTitle(QCoreApplication.translate("MainWindow", u"MainFigure", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"+90", None))
        self.toolButton_5.setText(QCoreApplication.translate("MainWindow", u"-90", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.Column_box.setTitle(QCoreApplication.translate("MainWindow", u"Column", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Draw box", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Tools", None))
        self.Add_row_btn.setText(QCoreApplication.translate("MainWindow", u"Sum_Row", None))
        self.Save_row_col_btn.setText(QCoreApplication.translate("MainWindow", u"Save lines", None))
        self.Add_col_btn.setText(QCoreApplication.translate("MainWindow", u"Sum_COl", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Action", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuanalysise.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

