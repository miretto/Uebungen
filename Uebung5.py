from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

# --------------------------------------------------------------------------------------
        # layout erzeugen
        # layout = ... # QVBoxLayout, QHBoxLayout, QGridLayout, ...

        layout = QFormLayout()

# --------------------------------------------------------------------------------------
        # gui element erstellen

        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.geburi = QDateEdit()
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.buttonmap = QPushButton("Auf Karte zeigen")
        self.buttonload = QPushButton("Laden")
        self.buttonsave = QPushButton("Speichern")


# --------------------------------------------------------------------------------------
        # gui Elemente dem Layout hinzufügen

        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtstag:", self.geburi)
        layout.addRow("Adresse:", self.adresse)
        layout.addRow("PostLeitZahl:", self.plz) 
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.buttonmap)
        layout.addRow(self.buttonload)
        layout.addRow(self.buttonsave)

# --------------------------------------------------------------------------------------
         # Menu erstellen
        
        menubar = self.menuBar()

        filemenu = menubar.addMenu("File")
        fileview = menubar.addMenu("View")

        self.sichern = QAction("Save", self)
        self.quit = QAction("Quit", self)
        self.karte = QAction("Karte", self)

        filemenu.addAction(self.sichern)
        filemenu.addAction(self.quit)
        fileview.addAction(self.karte)


# --------------------------------------------------------------------------------------
        # connects:
        
        self.sichern.triggered.connect(self.save)
        self.quit.triggered.connect(self.schliessen)
        self.karte.triggered.connect(self.maplink)
        self.buttonmap.clicked.connect(self.maplink)
        self.buttonsave.clicked.connect(self.save)
        self.buttonload.clicked.connect(self.load)

# --------------------------------------------------------------------------------------
        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        self.show()
        self.raise_()

# --------------------------------------------------------------------------------------
    # Funktionen:
    
    def schliessen(self):
        self.close()

    def load(self):
                                                   
        filename, filter = QFileDialog.getOpenFileName(self, "Datei Öffnen", "", "Text Files (*.txt)")

        file = open(f"{filename}")
        
                                                                             
        for parameter in file:
            dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat)
            laender = ["Schweiz", "Deutschland", "Österreich"]
            daten = parameter.split(",")
            self.vorname.setText(daten[0])
            self.name.setText(daten[1])
            self.geburi.setDate(QDate.fromString(daten[2], dformat))
            self.adresse.setText(daten[3])
            self.plz.setText(daten[4])
            self.ort.setText(daten[5])
            self.land.setCurrentText(daten[6])


    def save(self):
        pfad, filter = QFileDialog.getSaveFileName(self, "Datei speichern", "", "Text Datei (*.txt)")

        file = open(pfad, "w", encoding="utf-8")

        vorname = self.vorname.text()
        name = self.name.text()
        geburi = self.geburi.text()
        adresse = self.adresse.text()
        plz = self.plz.text()
        ort = self.ort.text()
        land = self.land.currentText()

        file.write(f"{vorname},{name},{geburi},{adresse},{plz},{ort},{land}")

        file.close()


    def maplink(self):
        link = f"https://www.google.ch/maps/place/{self.adresse.text()}+{self.plz.text()}+{self.ort.text()}"
        QDesktopServices.openUrl(QUrl(link))   # benötigt QtCore & QtGui


        
app = QApplication([])
win = Fenster()
app.exec()