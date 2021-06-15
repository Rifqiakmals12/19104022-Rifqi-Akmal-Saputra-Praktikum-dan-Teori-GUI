# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataMahasiswa.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Form import *

class Ui_Form(object):
    # Fungsi untuk menyeting ui
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 570)
        self.DataMahasiswa = QtWidgets.QLabel(Form)
        self.DataMahasiswa.setGeometry(QtCore.QRect(200, 30, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        # Label pada data mahasiswa
        self.DataMahasiswa.setFont(font)
        self.DataMahasiswa.setObjectName("DataMahasiswa")

        # listWidget untuk menampilkan data mahasiswa
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(50, 60, 441, 321))
        self.listWidget.setObjectName("listWidget")

        # Label untuk text NIM
        self.NIM = QtWidgets.QLabel(Form)
        self.NIM.setGeometry(QtCore.QRect(50, 400, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NIM.setFont(font)
        self.NIM.setObjectName("NIM")

        # Label untuk text Nama
        self.Nama = QtWidgets.QLabel(Form)
        self.Nama.setGeometry(QtCore.QRect(50, 430, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Nama.setFont(font)
        self.Nama.setObjectName("Nama")

        # Label untuk text Jurusan
        self.Jurusan = QtWidgets.QLabel(Form)
        self.Jurusan.setGeometry(QtCore.QRect(50, 460, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Jurusan.setFont(font)
        self.Jurusan.setObjectName("Jurusan")

        # Label untuk text NoTelp
        self.NoTelp = QtWidgets.QLabel(Form)
        self.NoTelp.setGeometry(QtCore.QRect(50, 490, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NoTelp.setFont(font)
        self.NoTelp.setObjectName("NoTelp")

        # Komponen line edit pada jurusan
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 460, 381, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        # Komponen line edit pada no telp
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 490, 381, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        # Komponen pushbutton pada tambah
        self.Tambah = QtWidgets.QPushButton(Form)
        self.Tambah.setGeometry(QtCore.QRect(151, 521, 80, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Tambah.setFont(font)
        self.Tambah.setObjectName("Tambah")
        self.Tambah.clicked.connect(self.addButtonClick)

        # Komponen pushbutton pada edit
        self.Edit = QtWidgets.QPushButton(Form)
        self.Edit.setGeometry(QtCore.QRect(237, 521, 80, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Edit.setFont(font)
        self.Edit.setObjectName("Edit")
        self.Edit.clicked.connect(self.editButtonClick)

        # Komponen pushbutton pada clear
        self.Clear = QtWidgets.QPushButton(Form)
        self.Clear.setGeometry(QtCore.QRect(323, 521, 80, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")
        self.Clear.clicked.connect(self.listWidget.clear)

        # Komponen pushbutton pada hapus
        self.Hapus = QtWidgets.QPushButton(Form)
        self.Hapus.setGeometry(QtCore.QRect(409, 521, 80, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Hapus.setFont(font)
        self.Hapus.setObjectName("Hapus")
        self.Hapus.clicked.connect(self.deleteButtonClick)

        # Komponen line edit pada nim
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 400, 381, 20))
        self.lineEdit.setObjectName("lineEdit")

        # Komponen line edit pada nama
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 430, 381, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.DataMahasiswa.setText(_translate("Form", "Data Mahasiswa"))
        self.NIM.setText(_translate("Form", "NIM"))
        self.Nama.setText(_translate("Form", "Nama"))
        self.Jurusan.setText(_translate("Form", "Jurusan"))
        self.NoTelp.setText(_translate("Form", "No.Telp"))
        self.Tambah.setText(_translate("Form", "TAMBAH"))
        self.Edit.setText(_translate("Form", "EDIT"))
        self.Clear.setText(_translate("Form", "CLEAR"))
        self.Hapus.setText(_translate("Form", "HAPUS"))

    # Fungsi untuk button tambah
    def addButtonClick(self):
        self.listWidget.addItem(
            self.lineEdit.text() + ' - ' +
            self.lineEdit_2.text() + ' - ' +
            self.lineEdit_3.text() + ' - ' +
            self.lineEdit_4.text())

    # Fungsi untuk button edit
    def editButtonClick(self):
        if self.listWidget.currentRow() < 0: return
        self.entryForm = EntryForm()
        s = str(self.listWidget.currentItem().text())
        idx = s.index('-')
        self.entryForm.nim.setText(s[:(idx - 1)])
        self.entryForm.nama.setText(s[(idx - 2):])
        self.entryForm.jurusan.setText(s[(idx - 3):])
        self.entryForm.telp.setText(s[(idx - 4):])

        if self.entryForm.exec_() == QDialog.Accepted:
            self.listWidget.currentItem().setText(
                self.entryForm.nim.text() + ' - ' +
                self.entryForm.nama.text() + ' - ' +
                self.entryForm.jurusan.text() + ' - ' +
                self.entryForm.telp.text())

    # Fungsi untuk button delete
    def deleteButtonClick(self):
        row = self.listWidget.currentRow()
        if row >= 0:
            self.listWidget.takeItem(row)

# Untuk menjalankan program
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())