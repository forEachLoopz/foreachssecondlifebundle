import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("forEach's Second Life Bundle")

        # Création d'un widget central avec un layout vertical
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Label de titre
        self.title_label = QLabel("forEach's Second Life", self)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(self.title_label, alignment=Qt.AlignCenter)

        # Label d'instruction
        self.label = QLabel("forEach's Second Life Bundle launcher", self)
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Bouton pour lancer le premier script
        self.script1_button = QPushButton("Cleanux")
        self.script1_button.setObjectName("launcherButton")
        self.script1_button.clicked.connect(self.launch_script1)
        layout.addWidget(self.script1_button, alignment=Qt.AlignCenter)

        # Bouton pour lancer le deuxième script
        self.script2_button = QPushButton("Process Checker")
        self.script2_button.setObjectName("launcherButton")
        self.script2_button.clicked.connect(self.launch_script2)
        layout.addWidget(self.script2_button, alignment=Qt.AlignCenter)

        # Bouton pour lancer le troisième script
        self.script3_button = QPushButton("Compo Book")
        self.script3_button.setObjectName("launcherButton")
        self.script3_button.clicked.connect(self.launch_script3)
        layout.addWidget(self.script3_button, alignment=Qt.AlignCenter)

        # Application de la feuille de style CSS
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                color: #333;
            }
            QPushButton#launcherButton {
                background-color: #4CAF50;
                border: 2px solid #4CAF50;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 10px;
                cursor: pointer;
                border-radius: 10px;
            }
            QPushButton#launcherButton:hover {
                background-color: #45a049;
                border: 2px solid #45a049;
            }
        """)

    def launch_script1(self):
        # Code pour lancer le premier script
        print("Cleanux")
        os.system("python3 scripts/cleanux/cleanuxfront.py")

    def launch_script2(self):
        # Code pour lancer le deuxième script
        print("Process Checker")
        os.system("python3 scripts/processchecker/main.py")

    def launch_script3(self):
        # Code pour lancer le troisième script
        print("Compo Book")
        os.system("python3 scripts/compo-book/compo_book.py")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 250)
    window.show()
    sys.exit(app.exec_())
