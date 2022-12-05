from PySide6 import QtWidgets
import sys

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("BTS SNIR2 - QDialog")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()


    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.lbl_nb3 = QtWidgets.QLabel("Résolution d'équation du deuxième degré")

        self.lbl_nb1 = QtWidgets.QLabel("x2")
        self.LEdit_nb1 = QtWidgets.QLineEdit()
        self.LEdit_nb1.setPlaceholderText("a")

        self.lbl_nb2 = QtWidgets.QLabel(" x +")
        self.LEdit_nb2 = QtWidgets.QLineEdit()
        self.LEdit_nb2.setPlaceholderText("b")

        self.lbl_nb4 = QtWidgets.QLabel("= 0")
        self.LEdit_nb4 = QtWidgets.QLineEdit()
        self.LEdit_nb4.setPlaceholderText("c")

        self.btn_Calculcer = QtWidgets.QPushButton("Calculer")
        self.lbl_result = QtWidgets.QLabel("La somme des deux nombre = ....")
        self.btn_Effacer = QtWidgets.QPushButton("Effacer")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

        self.messageBox = QtWidgets.QMessageBox()

    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_nb3)
        self.layoutH2.addWidget(self.LEdit_nb1)
        self.layoutH2.addWidget(self.lbl_nb1)
        self.layoutH2.addWidget(self.LEdit_nb2)
        self.layoutH2.addWidget(self.lbl_nb2)
        self.layoutH2.addWidget(self.LEdit_nb4)
        self.layoutH2.addWidget(self.lbl_nb4)
        
        
        
        self.layoutH3.addWidget(self.btn_Calculcer)
        

        self.layoutH5.addWidget(self.btn_Effacer)
        self.layoutH5.addWidget(self.btn_Quitter)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)

        self.layoutV.addLayout(self.layoutH5)



        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Effacer.clicked.connect(self.clear_Ledit)
        self.btn_Calculcer.clicked.connect(self.calculer)
         
    def clear_Ledit(self):
        self.LEdit_nb1.setText("")
        self.LEdit_nb2.setText("")
        self.LEdit_nb4.setText("")
        self.lbl_result.setText("La somme des deux nombre = ....." )

    def calculer(self):
        try:
            nb1 = float(self.LEdit_nb1.text())
            nb2 = float(self.LEdit_nb2.text())
        except:
            print("message erreur de conversion")
            self.clear_Ledit()
        else:
            self.lbl_result.setText("La somme des deux nombre = " +str(nb1+nb2))
            self.messageBox.setText("La somme des deux nombre = " +str(nb1+nb2))
            self.messageBox.show()

            print("Je vais calculer",nb1+nb2)

    

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MaFenetre()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()