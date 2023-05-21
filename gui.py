from PyQt5 import QtCore, QtGui, QtWidgets
import feature_extractor

class Ui_Spam_detector(object):
    def setupUi(self, Spam_detector):
        Spam_detector.setObjectName("Spam_detector")
        Spam_detector.resize(1024, 521)
        self.centralwidget = QtWidgets.QWidget(Spam_detector)
        self.centralwidget.setObjectName("centralwidget")

        """check button code and its connectivity to button_click function"""
        self.check_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_button.setGeometry(QtCore.QRect(210, 170, 93, 28))
        self.check_button.setObjectName("check_button")
        self.check_button.clicked.connect(self.button_click)

        """check button code and its connectivity to button_click function"""
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 50, 450, 250))
        self.label_3.setObjectName("check_button")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 90, 450, 250))
        self.label_5.setObjectName("check_button")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(550, 130, 450, 250))
        self.label_6.setObjectName("check_button")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 170, 450, 250))
        self.label_7.setObjectName("check_button")
        

        """url input section"""
        self.url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(70, 111, 431, 31))
        self.url_input.setObjectName("url_input")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 110, 81, 31))
        self.label.setObjectName("label")
        
        """output message"""
        self.output_text = QtWidgets.QTextEdit(self.centralwidget)
        self.output_text.setGeometry(QtCore.QRect(30, 241, 461, 121))
        self.output_text.setObjectName("output_text")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 311, 41))
        self.label_2.setObjectName("label_2")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 50, 311, 41))
        self.label_4.setObjectName("label_2")

        Spam_detector.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Spam_detector)
        self.statusbar.setObjectName("statusbar")
        Spam_detector.setStatusBar(self.statusbar)

        self.retranslateUi(Spam_detector)
        QtCore.QMetaObject.connectSlotsByName(Spam_detector)

    def retranslateUi(self, Spam_detector):
        _translate = QtCore.QCoreApplication.translate
        Spam_detector.setWindowTitle(_translate("Spam_detector", "MainWindow"))
        self.check_button.setText(_translate("Spam_detector", "Check "))
        self.label.setText(_translate("Spam_detector", "<html><head/><body><p><span style=\" font-size:10pt;\">URL :</span></p></body></html>"))
        self.label_2.setText(_translate("Spam_detector", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Spam URL Detector</span></p></body></html>"))
        self.label_3.setText(_translate("Spam_detector", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">AYUSH_21BCS3936</span></p></body></html>"))
        self.label_4.setText(_translate("Spam_detector", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">LEADER - AYUSH</span></p></body></html>"))
        self.label_5.setText(_translate("Spam_detector", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">SAURAVRANJAN_21BCS3723</span></p></body></html>"))
        self.label_6.setText(_translate("Spam_detector", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">RAGHAVNAGPAL_21BCS3688</span></p></body></html>"))
        self.label_7.setText(_translate("Spam_detector", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">KESHAVBANSAL_21BCS3471</span></p></body></html>"))

    def button_click(self):
        text = self.url_input.text()
        print(text)
        obj = feature_extractor.feature_extractor(text)
        str1,str2 = obj.extract()

        self.output_text.append("{} \n{}\n\n".format(str1,str2))
        

    #def show_output():

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Spam_detector = QtWidgets.QMainWindow()
    ui = Ui_Spam_detector()
    ui.setupUi(Spam_detector)
    Spam_detector.show()
    sys.exit(app.exec_())

