# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'as.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore
from PyQt5.QtWidgets import QHBoxLayout,QGroupBox,QGridLayout,QPushButton,QLabel,QCheckBox,QVBoxLayout,QWidget,QTabWidget,QTextEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar
from matplotlib.pyplot import figure

class Ui_Form(object):
    def plot(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(data[6], data[4])
        ax.set_ylim(min(data[4])-0.05,max(data[4])+0.05)
        ax.set_ylabel("i, гр.")
        ax.set_xlabel("n")
        ax.set_title("График зависимости наклонения от количества \n витков КА в плоскости орбиты\n")
        self.canvas.draw()

        self.figure1.clear()
        ax = self.figure1.add_subplot(111)
        ax.plot(data[6], data[3])
        ax.set_ylim(min(data[3])-5,max(data[3])+5)
        ax.set_ylabel("Ω, гр.")
        ax.set_xlabel("n")
        ax.set_title("График зависимости прямого восхождения восходящего \n узла от количества витков КА в плоскости орбиты\n")
        self.canvas1.draw()

        self.figure2.clear()
        ax = self.figure2.add_subplot(111)
        ax.plot(data[6], data[1])
        ax.set_ylim(min(data[1])-0.05,max(data[1])+0.05)
        ax.set_ylabel("e")
        ax.set_xlabel("n")
        ax.set_title("График зависимости эксцентриситета от \n количества витков КА в плоскости орбиты\n")
        self.canvas2.draw()

        self.figure3.clear()
        ax = self.figure3.add_subplot(111)
        ax.plot(data[6], data[0])
        ax.set_ylim(min(data[0])-25,max(data[0])+25)
        ax.set_ylabel("a, км")
        ax.set_xlabel("n")
        ax.set_title("График зависимости большой полуоси от \n количества витков КА в плоскости орбиты\n")
        self.canvas3.draw()

        self.figure4.clear()
        ax = self.figure4.add_subplot(111)
        ax.plot(data[6], data[2])
        ax.set_ylim(min(data[2])-5,max(data[2])+5)
        ax.set_ylabel("ω, гр.")
        ax.set_xlabel("n")
        ax.set_title("График зависимости аргумента широты перигея \n от количества витков КА в плоскости орбиты\n")
        self.canvas4.draw()

        self.figure5.clear()
        ax = self.figure5.add_subplot(111)
        ax.plot(data[6], data[5])
        ax.set_ylim(min(data[5]) - 25, max(data[5]) + 25)
        ax.set_ylabel("R, км")
        ax.set_xlabel("n")
        ax.set_title("График зависимости радиус-вектора \n от количества витков КА в плоскости орбиты\n")
        self.canvas5.draw()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1115, 630)
        self.horizontalLayout = QHBoxLayout(Form)
        self.formGroupBox = QGroupBox(Form)
        self.dop_gridLayout_2 = QGridLayout(self.formGroupBox)
        self.dop2_dop_gridLayout_2 = QGridLayout(self.formGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dop_tabWidget = QTabWidget(self.formGroupBox)
        self.dop_tabWidget.setObjectName("tabWidget")
        self.dop_gridLayout_2.addWidget(self.dop_tabWidget)
        self.dop_tab = QWidget()
        self.dop_tab.setObjectName("dop_tab")
        self.dop_tabWidget.addTab(self.dop_tab, "")
        self.dop2_dop_tab = QWidget()
        self.dop2_dop_tab.setObjectName("dop2_dop_tab")
        self.dop_tabWidget.addTab(self.dop2_dop_tab, "")
        self.formGroupBox.setMinimumSize(QtCore.QSize(270, 460))
        self.formGroupBox.setMaximumSize(QtCore.QSize(270, 460))

        self.gridLayout_2 = QGridLayout(self.dop_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QPushButton(self.formGroupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 9, 0, 1, 2)
        self.label_7 = QLabel(self.dop_tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.checkBox_2 = QCheckBox(self.formGroupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.dop_gridLayout_2.addWidget(self.checkBox_2, 8, 0, 1, 2)
        self.textEdit_7 = QTextEdit(self.dop_tab)
        self.textEdit_7.setMaximumSize(QtCore.QSize(51, 31))
        self.textEdit_7.setObjectName("textEdit_7")
        self.gridLayout_2.addWidget(self.textEdit_7, 6, 1, 1, 1)
        self.checkBox = QCheckBox(self.formGroupBox)
        self.checkBox.setObjectName("checkBox")
        self.dop_gridLayout_2.addWidget(self.checkBox, 7, 0, 1, 2)
        self.textEdit = QTextEdit(self.dop_tab)
        self.textEdit.setMaximumSize(QtCore.QSize(51, 31))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 1, 1, 1)
        self.label_2 = QLabel(self.dop_tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.textEdit_2 = QTextEdit(self.dop_tab)
        self.textEdit_2.setMaximumSize(QtCore.QSize(51, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 1, 1, 1, 1)
        self.label_3 = QLabel(self.dop_tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.textEdit_3 = QTextEdit(self.dop_tab)
        self.textEdit_3.setMaximumSize(QtCore.QSize(51, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_2.addWidget(self.textEdit_3, 2, 1, 1, 1)
        self.label_4 = QLabel(self.dop_tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.textEdit_4 = QTextEdit(self.dop_tab)
        self.textEdit_4.setMaximumSize(QtCore.QSize(51, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_2.addWidget(self.textEdit_4, 3, 1, 1, 1)
        self.label_5 = QLabel(self.dop_tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.textEdit_5 = QTextEdit(self.dop_tab)
        self.textEdit_5.setMaximumSize(QtCore.QSize(51, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_2.addWidget(self.textEdit_5, 4, 1, 1, 1)
        self.label = QLabel(self.dop_tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit_6 = QTextEdit(self.dop_tab)
        self.textEdit_6.setMaximumSize(QtCore.QSize(51, 31))
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout_2.addWidget(self.textEdit_6, 5, 1, 1, 1)
        self.label_6 = QLabel(self.dop_tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)

        self.dop2_gridLayout_2 = QGridLayout(self.dop2_dop_tab)
        self.dop2_gridLayout_2.setObjectName("gridLayout_2")
        self.n_label = QLabel(self.dop2_dop_tab)
        self.n_label.setObjectName("label_7")
        self.dop2_gridLayout_2.addWidget(self.n_label, 6, 0, 1, 1)
        self.dop2_textEdit_7 = QTextEdit(self.dop2_dop_tab)
        self.dop2_textEdit_7.setMaximumSize(QtCore.QSize(81, 31))
        self.dop2_textEdit_7.setObjectName("textEdit_7")
        self.dop2_gridLayout_2.addWidget(self.dop2_textEdit_7, 6, 1, 1, 1)
        self.dop2_textEdit = QTextEdit(self.dop2_dop_tab)
        self.dop2_textEdit.setMaximumSize(QtCore.QSize(81, 31))
        self.dop2_textEdit.setObjectName("textEdit")
        self.dop2_gridLayout_2.addWidget(self.dop2_textEdit, 0, 1, 1, 1)
        self.y_label = QLabel(self.dop2_dop_tab)
        self.y_label.setObjectName("label_2")
        self.dop2_gridLayout_2.addWidget(self.y_label, 1, 0, 1, 1)
        self.dop2_textEdit_2 = QTextEdit(self.dop2_dop_tab)
        self.dop2_textEdit_2.setMaximumSize(QtCore.QSize(81, 31))
        self.dop2_textEdit_2.setObjectName("textEdit_2")
        self.dop2_gridLayout_2.addWidget(self.dop2_textEdit_2, 1, 1, 1, 1)
        self.z_label = QLabel(self.dop2_dop_tab)
        self.z_label.setObjectName("label_3")
        self.dop2_gridLayout_2.addWidget(self.z_label, 2, 0, 1, 1)
        self.dop2_textEdit_3 = QTextEdit(self.dop2_dop_tab)
        self.dop2_textEdit_3.setMaximumSize(QtCore.QSize(81, 31))
        self.dop2_textEdit_3.setObjectName("textEdit_3")
        self.dop2_gridLayout_2.addWidget(self.dop2_textEdit_3, 2, 1, 1, 1)
        self.vx_label = QLabel(self.dop2_dop_tab)
        self.vx_label.setObjectName("label_4")
        self.dop2_gridLayout_2.addWidget(self.vx_label, 3, 0, 1, 1)
        self.dop2_textEdit_4 = QTextEdit(self.dop2_dop_tab)
        self.dop2_textEdit_4.setMaximumSize(QtCore.QSize(81, 31))
        self.dop2_textEdit_4.setObjectName("textEdit_4")
        self.dop2_gridLayout_2.addWidget(self.dop2_textEdit_4, 3, 1, 1, 1)
        self.vy_label = QLabel(self.dop2_dop_tab)
        self.vy_label.setObjectName("label_5")
        self.dop2_gridLayout_2.addWidget(self.vy_label, 4, 0, 1, 1)
        self.dop2_textEdit_5 = QTextEdit(self.dop2_dop_tab)
        self.dop2_textEdit_5.setMaximumSize(QtCore.QSize(81, 31))
        self.dop2_textEdit_5.setObjectName("textEdit_5")
        self.dop2_gridLayout_2.addWidget(self.dop2_textEdit_5, 4, 1, 1, 1)
        self.x_label = QLabel(self.dop2_dop_tab)
        self.x_label.setObjectName("label")
        self.dop2_gridLayout_2.addWidget(self.x_label, 0, 0, 1, 1)
        self.dop2_textEdit_6 = QTextEdit(self.dop2_dop_tab)
        self.dop2_textEdit_6.setMaximumSize(QtCore.QSize(81, 31))
        self.dop2_textEdit_6.setObjectName("textEdit_6")
        self.dop2_gridLayout_2.addWidget(self.dop2_textEdit_6, 5, 1, 1, 1)
        self.vz_label = QLabel(self.dop2_dop_tab)
        self.vz_label.setObjectName("label_6")
        self.dop2_gridLayout_2.addWidget(self.vz_label, 5, 0, 1, 1)
        self.dop2_pushButton = QPushButton(self.formGroupBox)
        self.dop2_pushButton.setObjectName("dop2_pushButton")
        self.dop2_gridLayout_2.addWidget(self.dop2_pushButton, 9, 0, 1, 2)


        self.horizontalLayout.addWidget(self.formGroupBox)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setMinimumSize(600,540)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName("tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.tabWidget.addTab(self.tab_12, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.tabWidget.raise_()
        self.formGroupBox.raise_()
        self.tabWidget.raise_()

        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(30, 40, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.figure = figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.toolbar)

        self.verticalLayout1 = QVBoxLayout(self.tab_2)
        self.verticalLayout1.setContentsMargins(30, 40, 0, 0)
        self.verticalLayout1.setObjectName("verticalLayout1")
        self.figure1 = figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        self.verticalLayout1.addWidget(self.canvas1)
        self.verticalLayout1.addWidget(self.toolbar1)

        self.verticalLayout2 = QVBoxLayout(self.tab_9)
        self.verticalLayout2.setContentsMargins(30, 40, 0, 0)
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.figure2 = figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        self.verticalLayout2.addWidget(self.canvas2)
        self.verticalLayout2.addWidget(self.toolbar2)

        self.verticalLayout3 = QVBoxLayout(self.tab_10)
        self.verticalLayout3.setContentsMargins(30, 40, 0, 0)
        self.verticalLayout3.setObjectName("verticalLayout3")
        self.figure3 = figure()
        self.canvas3 = FigureCanvas(self.figure3)
        self.toolbar3 = NavigationToolbar(self.canvas3, self)
        self.verticalLayout3.addWidget(self.canvas3)
        self.verticalLayout3.addWidget(self.toolbar3)

        self.verticalLayout4 = QVBoxLayout(self.tab_11)
        self.verticalLayout4.setContentsMargins(30, 40, 0, 0)
        self.verticalLayout4.setObjectName("verticalLayout4")
        self.figure4 = figure()
        self.canvas4 = FigureCanvas(self.figure4)
        self.toolbar4 = NavigationToolbar(self.canvas4, self)
        self.verticalLayout4.addWidget(self.canvas4)
        self.verticalLayout4.addWidget(self.toolbar4)

        self.verticalLayout5 = QVBoxLayout(self.tab_12)
        self.verticalLayout5.setContentsMargins(30, 40, 0, 0)
        self.verticalLayout5.setObjectName("verticalLayout5")
        self.figure5 = figure()
        self.canvas5 = FigureCanvas(self.figure5)
        self.toolbar5 = NavigationToolbar(self.canvas5, self)
        self.verticalLayout5.addWidget(self.canvas5)
        self.verticalLayout5.addWidget(self.toolbar5)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Программа для расчета витка конца баллистического существования под воздействием возмущений, обусловленных нецентральностью ГПЗ и атмосферой"))
        self.pushButton.setText(_translate("Form", "Рассчитать"))
        self.dop2_pushButton.setText(_translate("Form", "Рассчитать"))
        self.label_7.setText(_translate("Form", "Количество\n"
"рассматриваемых витков"))
        self.checkBox_2.setText(_translate("Form", "Учитывать возмущения, \n"
"вызванные атмосферой"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">60</p></body></html>"))
        self.textEdit_2.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.1</p></body></html>"))
        self.textEdit_3.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.002</p></body></html>"))
        self.textEdit_4.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6498</p></body></html>"))
        self.textEdit_5.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">90</p></body></html>"))
        self.textEdit_6.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.label_6.setText(_translate("Form", "U"))
        self.textEdit_7.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">50</p></body></html>"))
        self.checkBox.setText(_translate("Form", "Учитытывать нецентральность \n"
"гравитационного поля Земли"))
        self.label_2.setText(_translate("Form", "Прямое восхождение \n"
"восходящего узла"))
        self.label_3.setText(_translate("Form", "Эксцентриситет"))
        self.label_4.setText(_translate("Form", "Большая полуось"))
        self.label_5.setText(_translate("Form", "Аргумент широты \n"
"перигея"))
        self.label.setText(_translate("Form", "Наклонение"))
        self.label_6.setText(_translate("Form", "Аргумент широты\n"
"космического аппарата"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Наклонение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Прямое восхождени восходящего узла"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Form", "Эксцентриситет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("Form", "Большая полуось"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("Form", "Аргумент широты перигея"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("Form", "Радиус-вектор"))
        self.dop_tabWidget.setTabText(self.dop_tabWidget.indexOf(self.dop_tab), _translate("Form", "КЭО"))
        self.dop_tabWidget.setTabText(self.dop_tabWidget.indexOf(self.dop2_dop_tab), _translate("Form", "АГЭСК"))

        self.dop2_textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-5.65923</p></body></html>"))
        self.dop2_textEdit_2.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3242.5</p></body></html>"))
        self.dop2_textEdit_3.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5616.18</p></body></html>"))
        self.dop2_textEdit_4.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-7.8399415</p></body></html>"))
        self.dop2_textEdit_5.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-0.0136978</p></body></html>"))
        self.dop2_textEdit_6.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.vz_label.setText(_translate("Form", "U"))
        self.dop2_textEdit_7.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">50</p></body></html>"))

        self.y_label.setText(_translate("Form", "y, км"))
        self.z_label.setText(_translate("Form", "z, км"))
        self.vx_label.setText(_translate("Form", "vx, км/с"))
        self.vy_label.setText(_translate("Form", "vy, км/с"))
        self.x_label.setText(_translate("Form", "x, км"))
        self.vz_label.setText(_translate("Form", "vz, км/с"))
        self.n_label.setText(_translate("Form", "Количество\n"
"рассматриваемых\nвитков"))
