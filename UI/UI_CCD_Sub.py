# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_CCD_Sub.ui'
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
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1307, 880)
        MainWindow.setMinimumSize(QSize(1200, 830))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Measured_btn = QPushButton(self.centralwidget)
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

        self.Background_btn = QPushButton(self.centralwidget)
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

        self.Subtract_btn = QPushButton(self.centralwidget)
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
        self.Mea_path_line = QLineEdit(self.centralwidget)
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
        self.AutoCorrection_btn = QPushButton(self.centralwidget)
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

        self.Save_Substract_btn = QPushButton(self.centralwidget)
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

        self.BGR_path_line = QLineEdit(self.centralwidget)
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
        self.tabWidget = QTabWidget(self.centralwidget)
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


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Add_col_btn = QPushButton(self.centralwidget)
        self.Add_col_btn.setObjectName(u"Add_col_btn")
        sizePolicy.setHeightForWidth(self.Add_col_btn.sizePolicy().hasHeightForWidth())
        self.Add_col_btn.setSizePolicy(sizePolicy)
        self.Add_col_btn.setMinimumSize(QSize(150, 40))
        self.Add_col_btn.setFont(font)
        self.Add_col_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.Add_col_btn, 2, 0, 1, 1)

        self.Add_row_btn = QPushButton(self.centralwidget)
        self.Add_row_btn.setObjectName(u"Add_row_btn")
        sizePolicy.setHeightForWidth(self.Add_row_btn.sizePolicy().hasHeightForWidth())
        self.Add_row_btn.setSizePolicy(sizePolicy)
        self.Add_row_btn.setMinimumSize(QSize(150, 40))
        self.Add_row_btn.setFont(font)
        self.Add_row_btn.setStyleSheet(u"background-color: rgb(146, 57, 255);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.Add_row_btn, 0, 0, 1, 1)

        self.Column_box = QGroupBox(self.centralwidget)
        self.Column_box.setObjectName(u"Column_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Column_box.sizePolicy().hasHeightForWidth())
        self.Column_box.setSizePolicy(sizePolicy2)
        self.Column_box.setMinimumSize(QSize(400, 150))

        self.gridLayout_4.addWidget(self.Column_box, 0, 1, 3, 1)

        self.Main_fig_box = QGroupBox(self.centralwidget)
        self.Main_fig_box.setObjectName(u"Main_fig_box")
        self.Main_fig_box.setMinimumSize(QSize(500, 600))

        self.gridLayout_4.addWidget(self.Main_fig_box, 3, 1, 1, 1)

        self.Row_box = QGroupBox(self.centralwidget)
        self.Row_box.setObjectName(u"Row_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Row_box.sizePolicy().hasHeightForWidth())
        self.Row_box.setSizePolicy(sizePolicy3)
        self.Row_box.setMinimumSize(QSize(150, 400))
        self.Row_box.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.Row_box, 3, 0, 1, 1)

        self.Save_row_col_btn = QPushButton(self.centralwidget)
        self.Save_row_col_btn.setObjectName(u"Save_row_col_btn")
        sizePolicy.setHeightForWidth(self.Save_row_col_btn.sizePolicy().hasHeightForWidth())
        self.Save_row_col_btn.setSizePolicy(sizePolicy)
        self.Save_row_col_btn.setMinimumSize(QSize(150, 40))
        self.Save_row_col_btn.setFont(font)
        self.Save_row_col_btn.setStyleSheet(u"background-color: rgb(33, 190, 193);\n"
"border-bottom-color: rgb(139, 139, 139);\n"
"border-right-color: rgb(48, 48, 48);\n"
"selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.Save_row_col_btn, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 218, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(308, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1307, 31))
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

        self.tabWidget.setCurrentIndex(2)


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
        self.Add_col_btn.setText(QCoreApplication.translate("MainWindow", u"Sum_COL", None))
        self.Add_row_btn.setText(QCoreApplication.translate("MainWindow", u"Sum_Row", None))
        self.Column_box.setTitle(QCoreApplication.translate("MainWindow", u"Column", None))
        self.Main_fig_box.setTitle(QCoreApplication.translate("MainWindow", u"MainFigure", None))
        self.Row_box.setTitle(QCoreApplication.translate("MainWindow", u"Row", None))
        self.Save_row_col_btn.setText(QCoreApplication.translate("MainWindow", u"Save row/col", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuanalysise.setTitle(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

