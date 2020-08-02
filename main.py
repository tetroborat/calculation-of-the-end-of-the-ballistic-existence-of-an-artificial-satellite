from sys import argv
from PyQt5.QtWidgets import QApplication,QWidget
import design
import calc
class App(QWidget, design.Ui_Form):
    def schet(self):
        if self.checkBox.isChecked():
            cent=1
        else:
            cent=0
        if self.checkBox_2.isChecked():
            atm=1
        else:
            atm=0
        a, e, w, ww, i, u, sutki = map(float, [self.textEdit_4.toPlainText(), self.textEdit_3.toPlainText(),
                                        self.textEdit_5.toPlainText(), self.textEdit_2.toPlainText(),
                                        self.textEdit.toPlainText(), self.textEdit_6.toPlainText(),self.textEdit_7.toPlainText()])
        data=cursach.ras(self,a,e,w,ww,i,u,sutki,cent,atm)
        design.Ui_Form.plot(self,data)
    def schet2(self):
        if self.checkBox.isChecked():
            cent = 1
        else:
            cent = 0
        if self.checkBox_2.isChecked():
            atm = 1
        else:
            atm = 0
        [a, e, w, ww, i, u], sutki = cursach.AgscToKeo(self,list(map(float, [self.dop2_textEdit.toPlainText(), self.dop2_textEdit_2.toPlainText(),
                                        self.dop2_textEdit_3.toPlainText(), self.dop2_textEdit_4.toPlainText(),
                                        self.dop2_textEdit_5.toPlainText(), self.dop2_textEdit_6.toPlainText()]))),float(self.dop2_textEdit_7.toPlainText())
        data = cursach.ras(self, a, e, w, ww, i, u, sutki, cent, atm)
        design.Ui_Form.plot(self, data)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.schet)
        self.dop2_pushButton.clicked.connect(self.schet2)
def main():
    app = QApplication(argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()