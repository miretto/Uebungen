from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

# --------------------------------------------------------------------------------------
        # layout erzeugen
        # layout = ... # QVBoxLayout, QHBoxLayout, QGridLayout, ...

        layout_top = QVBoxLayout()
        layout_bottom = QFormLayout()

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
        self.button2 = QPushButton("Save")

        self.vorname.text()
        self.name.text()
        self.geburi.date()
        self.adresse.text()
        self.plz.text()
        self.ort.text()
        self.land.currentText()


# --------------------------------------------------------------------------------------
        # gui Elemente dem Layout hinzufügen

        layout_bottom.addRow("Vorname:", self.vorname)
        layout_bottom.addRow("Name:", self.name)
        layout_bottom.addRow("Geburtstag:", self.geburi)
        layout_bottom.addRow("Adresse:", self.adresse)
        layout_bottom.addRow("PostLeitZahl:", self.plz) 
        layout_bottom.addRow("Ort:", self.ort)
        layout_bottom.addRow("Land:", self.land)
        layout_bottom.addRow(self.button2)

# --------------------------------------------------------------------------------------
         # Menu erstellen
        
        menubar = self.menuBar()

        filemenu = menubar.addMenu("File")

        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)

        filemenu.addAction(self.save)
        filemenu.addAction(self.quit)

        layout_top.addLayout(layout_bottom)

# --------------------------------------------------------------------------------------
        # connects:
        
        self.button2.clicked.connect(self.speichern)
        self.save.triggered.connect(self.speichern)
        self.quit.triggered.connect(self.schliessen)
# --------------------------------------------------------------------------------------
        center = QWidget()
        center.setLayout(layout_top)

        self.setCentralWidget(center)

        self.show()
        self.raise_()

# --------------------------------------------------------------------------------------
    # Funktionen:
    
    def speichern(self):
        file = open("output.txt", "w", encoding="utf-8")
        datum = self.geburi.date()
        file.write(f"{self.vorname.text()}, {self.name.text()}, {datum.toString('MM/dd/yyyy')}, {self.adresse.text()}, {self.plz.text()}, {self.ort.text()}, {self.land.currentText()}")

        file.close()

    def schliessen(self):
        self.close()

        



app = QApplication([])
win = Fenster()
app.exec()