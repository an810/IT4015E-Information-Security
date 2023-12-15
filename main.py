from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog,QLabel,QAction,QMainWindow,QApplication
from PyQt5.uic import loadUiType
from Encrypter import Encrypter
from Decrypter import Decrypter
from PIL import Image as Img
from PIL import ImageTk as ImgTk
#from tkinter import *
import base64
from Crypto.Cipher import AES
import os
import sys
#import tkinter
#import tkinter.filedialog as tkFileDialog
Qt = QtCore.Qt



# master = Tk()
# master.wm_title("Image Encryption using AES")
# l2=Label(master, text="Key")

# l2.pack()
# e2 = Entry(master)
# e2.pack()
# e2.focus_set()

# label = Label (master, text="")
# label.pack()
# def callback():
#     file = tkFileDialog.askopenfile(parent=master,mode='rb',title='Choose a file')
#     print(type(file))
#     print(file)
#     if file != None:
#         data = file.read()
#         print(data)
#         print(type(data))
#         stri = base64.b64encode(data)     
#     myKey=e2.get()
#     x = Encrypter(stri, myKey)
#     cipher = x.encrypt_image()
#     x = Decrypter(cipher)
#     x.decrypt_image(myKey)
#     label.configure(text= "Cipher: " + cipher.decode('utf-8'),font=("Helvetica", 8))
# b = Button(master, text="Encrypt", width=10, command=callback)
# b.pack()
# master.mainloop()
ui, _ = loadUiType('ui.ui')
def start():
    global m
    m = Main_Window()
    m.show()
    
class encrypt_page():
    def __init__(self):
        self.file={}
        self.stri=""
        self.Handel_Buttons()
        self.pushButton_3.clicked.connect(self.chooseFile)
        self.pushButton_4.clicked.connect(self.onClickEncrypt)
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
    def chooseFile(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open File')
        pixmap = QtGui.QPixmap(self.file[0])
        self.lbl.setPixmap(pixmap.scaledToHeight(201))
        if self.file != None:
            ba = QtCore.QByteArray()
            buff = QtCore.QBuffer(ba)
            buff.open(QtCore.QIODevice.WriteOnly) 
            ok = pixmap.save(buff, "PNG")
            assert ok
            pixmap_bytes = ba.data()
            #print(type(pixmap_bytes))
            #data = self.file[0]
            self.stri = base64.b64encode(pixmap_bytes)
        
    def onClickEncrypt(self):
        if not self.file:
            QMessageBox.warning(self, "Warning", "Please choose image to encrypt")
            return
        myKey=self.lineEdit.text()
        if len(myKey) == 0:
            QMessageBox.warning(self, "Warning", "Please enter key to encrypt")
            return
        # print(type(myKey))
        # print(myKey)

        x = Encrypter(self.stri, myKey)
        cipher = x.encrypt_image()
        # print(type(cipher))
        # name = QFileDialog.getSaveFileName(self, 'Save File')
        # file = open(name,'w')
        # text = cipher
        # file.write(text)
        # file.close()
        #fh.write(base64_decoded.decode('base64'))
        fh = open("cipher.txt", "wb")
        fh.write(cipher)
        fh.close()
        # cipherd = base64.b64decode(cipher.decode('utf-8'))
        # ba = QtCore.QByteArray(cipherd)
        # pixmap = QtGui.QPixmap()
        # ok = pixmap.loadFromData(ba, "PNG")
        #assert ok
        #self.lbl.setPixmap(pixmap.scaledToHeight(201))
        #x = Decrypter(cipher)
        #x.decrypt_image(myKey)
        QMessageBox.information(self, "Success", "The image has been encrypted successfully")

    def resetPage(self):
        # Clear relevant data and UI elements
        self.file = {}
        self.stri = ""
        self.lineEdit.clear()
        self.lbl.clear()
        
class decrypt_page():
    def __init__(self):
        self.cipher={}
        self.Handel_Buttons()
        self.pushButton_5.clicked.connect(self.chooseFile1)
        self.pushButton_6.clicked.connect(self.onClickDecrypt)
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
    def chooseFile1(self):
        file = QFileDialog.getOpenFileName(self, 'Open File')
        text=open(file[0]).read()
        #print(text.encode('utf-8'))
        self.cipher= text.encode('utf-8')
    def onClickDecrypt(self):
        if not self.cipher:
            QMessageBox.warning(self, "Warning", "Please choose cipher text file!")
            return
        myKey=self.lineEdit_2.text()
        x = Decrypter(self.cipher)
        try:
            image=x.decrypt_image(myKey)
        
            ba = QtCore.QByteArray(image)
            pixmap = QtGui.QPixmap()
            ok = pixmap.loadFromData(ba, "PNG")
            assert ok
            self.lbl_2.setPixmap(pixmap.scaledToHeight(201))
        except ValueError as e:
            QMessageBox.critical(self, "Error", f"Decryption failed: {myKey} is not correct key")
        # if image!=None:
        #     ba = QtCore.QByteArray()
        #     buff = QtCore.QBuffer(ba)
        #     buff.open(QtCore.QIODevice.WriteOnly) 
        #     ok = pixmap.save(buff, "PNG")
        #     assert ok
        #     pixmap_bytes = ba.data()
        #     #print(type(pixmap_bytes))
        #     #data = self.file[0]
        #     self.stri = base64.b64encode(pixmap_bytes)
    def resetPage(self):
        # Clear relevant data and UI elements
        self.cipher = {}
        self.lineEdit_2.clear()
        self.lbl_2.clear()
        
class Main_Window(QMainWindow, QWidget, ui,encrypt_page,decrypt_page):
    def __init__(self):
        QMainWindow.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)
        encrypt_page.__init__(self)
        decrypt_page.__init__(self)

        self.Handel_Buttons() 
        self.stackedWidget.setCurrentIndex(0)
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_8.clicked.connect(self.handleBackButton)
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    def handleBackButton(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index == 2 or current_index == 1:  # If transitioning back from decrypt page
            self.resetPage() # Clear relevant data and UI elements for decrypt page

        self.stackedWidget.setCurrentIndex(0)  # Always set the current index to 0 when back button is pressed


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #connect()
    window = start()
    app.exec_()