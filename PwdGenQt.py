
# Created by: PyQt5 UI code generator 5.13.2
#
___autore___ == "AbdelmounaimOmri AkA tpx1sc"


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, string, random, pyperclip
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 298)

        self.lenght = 0

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(60, 20, 291, 22))
        self.horizontalSlider.setMinimum(8)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 50, 221, 51))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.horizontalSlider.valueChanged.connect(self.get_lenght)

        self.pushButton.clicked.connect(self.generate_password)

    def get_lenght(self):
        self.lenght = int(self.horizontalSlider.value())

    def generate_password(self):
        pwd = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(self.lenght))
        pyperclip.copy(pwd)
        pyperclip.paste()

        msg1 = QMessageBox()
        msg1.setWindowTitle("Password Generata")
        msg1.setText("Password Salvata nella clipboard")
        msg1.setIcon(QMessageBox.Information)
        info = msg1.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Genera "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
