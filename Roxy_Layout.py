# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Roxy_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Roxy(object):
    def setupUi(self, Roxy):
        Roxy.setObjectName("Roxy")
        Roxy.resize(1017, 745)
        font = QtGui.QFont()
        font.setPointSize(12)
        Roxy.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("female-virtual-assistant-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Roxy.setWindowIcon(icon)
        self.Quit_Button = QtWidgets.QPushButton(Roxy)
        self.Quit_Button.setGeometry(QtCore.QRect(540, 540, 251, 131))
        self.Quit_Button.setStyleSheet("color: rgb(255, 0, 0);\n"
"text-decoration: underline;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.Quit_Button.setObjectName("Quit_Button")
        self.Start_Button = QtWidgets.QPushButton(Roxy)
        self.Start_Button.setGeometry(QtCore.QRect(160, 540, 241, 131))
        self.Start_Button.setStyleSheet("color: rgb(255, 0, 0);\n"
"text-decoration: underline;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.Start_Button.setObjectName("Start_Button")
        self.label = QtWidgets.QLabel(Roxy)
        self.label.setGeometry(QtCore.QRect(20, 110, 341, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/ASUS/Pictures/female-virtual-assistant-icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Roxy)
        self.label_4.setGeometry(QtCore.QRect(640, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Roxy_Talk = QtWidgets.QTextEdit(Roxy)
        self.Roxy_Talk.setGeometry(QtCore.QRect(370, 60, 641, 431))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Roxy_Talk.setFont(font)
        self.Roxy_Talk.setObjectName("Roxy_Talk")

        self.retranslateUi(Roxy)
        QtCore.QMetaObject.connectSlotsByName(Roxy)

    def retranslateUi(self, Roxy):
        _translate = QtCore.QCoreApplication.translate
        Roxy.setWindowTitle(_translate("Roxy", "Dialog"))
        self.Quit_Button.setText(_translate("Roxy", "Quit"))
        self.Start_Button.setText(_translate("Roxy", "Start"))
        self.label_4.setText(_translate("Roxy", "Chat Box"))
        self.Roxy_Talk.setHtml(_translate("Roxy", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Roxy = QtWidgets.QDialog()
    ui = Ui_Roxy()
    ui.setupUi(Roxy)
    Roxy.show()
    sys.exit(app.exec_())
