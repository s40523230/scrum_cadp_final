# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\github\scrum_cadp_final\eric6_project\marble_monitor\ui\Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 300)
        Dialog.setMinimumSize(QtCore.QSize(300, 300))
        Dialog.setMaximumSize(QtCore.QSize(300, 300))
        Dialog.setSizeGripEnabled(True)
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(100, 50, 100, 100))
        self.start.setMinimumSize(QtCore.QSize(100, 100))
        self.start.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.start.setFont(font)
        self.start.setObjectName("start")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.start.setText(_translate("Dialog", "啟動"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

