# from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QLabel,QPushButton,QLineEdit,QApplication


class MaFenetre1(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("BTS SNIR2 - QWidget")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()


    def create_layouts(self):
        self.layoutV = QVBoxLayout()
        self.layoutH1 = QHBoxLayout()
        self.layoutH2 = QHBoxLayout()
        self.layoutH3 = QHBoxLayout()
        self.layoutH4 = QHBoxLayout()

    def create_widgets(self):
        self.lbl_login = QLabel("Login :")
        self.LEdit_login = QLineEdit("abdel")
        self.LEdit_login.setPlaceholderText("Saisir votre identifiant")

        self.lbl_password = QLabel("password :")
        self.LEdit_password = QLineEdit("123")
        self.LEdit_password.setPlaceholderText("Saisir votre mot de passe")
        self.LEdit_password.setEchoMode(QLineEdit.Password)
        
        #self.btn_Effacer = QPushButton("Effacer")
        self.btn_connection = QPushButton("Connexion")
        self.lbl_deconnecte = QLabel("Déconecté")

    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_login)
        self.layoutH1.addWidget(self.LEdit_login)

        self.layoutH2.addWidget(self.lbl_password)
        self.layoutH2.addWidget(self.LEdit_password)

        #self.layoutH3.addWidget(self.btn_Effacer)
        self.layoutH3.addWidget(self.btn_connection)
        self.layoutH4.addWidget(self.lbl_deconnecte)

        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)

        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        # self.btn_connection.clicked.connect(quit)
        self.btn_connection.clicked.connect(self.to_connect)
        #self.btn_Effacer.clicked.connect(self.clear_Ledit)

    def to_connect(self):
        if self.LEdit_login.text() =="abdel" and self.LEdit_password.text()=="123":
            form2.show()
            form1.hide()
        else:
            self.LEdit_login.setText("")
            self.LEdit_password.setText("")
            print("I can't")
         
    def clear_Ledit(self):
        self.LEdit_Nom.setText("")




class MaFenetre2(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("Deuxième")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()


    def create_layouts(self):
        self.layoutV = QVBoxLayout()
        self.layoutH1 = QHBoxLayout()
        self.layoutH2 = QHBoxLayout()
        

    def create_widgets(self):
        
        self.btn_connection = QPushButton("Se deconnecter")
        self.lbl_connecter = QLabel("Connecté")

    def addWigets_to_layouts(self):
    
        #self.layoutH3.addWidget(self.btn_Effacer)
        self.layoutH1.addWidget(self.btn_connection)
        self.layoutH2.addWidget(self.lbl_connecter)
        

        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        

        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        #self.btn_connection.clicked.connect(quit)
        self.btn_connection.clicked.connect(self.to_connect)
        #self.btn_Effacer.clicked.connect(self.clear_Ledit)

    def to_connect(self):
       
        form1.show()
        form2.hide()

          



app = QApplication([])
form1 = MaFenetre1()
form2 = MaFenetre2()
form1.show()
form2.hide()
app.exec()

