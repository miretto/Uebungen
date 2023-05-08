from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel08/uebung8.ui", self)

        figure = plt.figure(figsize=(16,9))
        self.canvas = FigureCanvas(figure)
        self.verticalLayout.insertWidget(0,self.canvas)

        self.farbe = self.findChild(QtWidgets.QComboBox, "farbe_eingabe")
        self.farbe.addItem("Rot")
        self.farbe.addItem("Blau")
        self.farbe.addItem("Grün")
        self.farbe.addItem("Violett")
        self.farbe.addItem("Türkis")
        self.farbe.addItem("Gelb")       
        self.farbe.addItem("Schwarz")

        self.plot_button.clicked.connect(self.plot)
        self.show()


    def plot(self):
# Erfassung der Variablen ------------------------------------------------------------------------------- 
        self.min = self.findChild(QtWidgets.QLineEdit, "min_eingabe")
        self.min_value = self.min.text()

        self.max = self.findChild(QtWidgets.QLineEdit, "max_eingabe")
        self.max_value = self.max.text()

        self.anz_pkte = self.findChild(QtWidgets.QLineEdit, "anz_pkte_eingabe")
        self.anz_pkte_value = self.anz_pkte.text()

        self.koeff = self.findChild(QtWidgets.QLineEdit, "koeff_eingabe")
        self.koeff_value = self.koeff.text()

        self.farbe = self.findChild(QtWidgets.QComboBox, "farbe_eingabe")
        self.farbe_value = self.farbe.currentText()
        if self.farbe_value == "Rot":
            farbe_output = "ro-"
        elif self.farbe_value == "Violett":
            farbe_output = "mo-"        
        elif self.farbe_value == "Blau":
            farbe_output = "bo-"
        elif self.farbe_value == "Türkis":
            farbe_output = "co-"
        elif self.farbe_value == "Gelb":
            farbe_output = "yo-"
        elif self.farbe_value == "Grün":
            farbe_output = "go-"
        else:
            farbe_output = "ko-"

# Berechnung ------------------------------------------------------------------------------- 
        plt.clf() #clf = clear figure
       
        try:
            ko0 = self.koeff_value.strip(",") 
            ko = eval(ko0)
            f = np.poly1d(ko)
            x = np.linspace(int(self.min_value),int(self.max_value),int(self.anz_pkte_value))
            y = f(x)
        except:
            QMessageBox.critical(self, "Fehler", "x und y bitte korrekt eingeben")
            return
        try:
            plt.plot(x,y, farbe_output)
            self.canvas.draw()
        except:
            QMessageBox.critical(self, "Fehler", "Bite Eingabe überprüfen")
            return


app = QApplication([])
window = Window()
app.exec()