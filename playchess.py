import sys
import subprocess
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QImage, QColor, QFont
from PyQt5.QtCore import Qt, QTimer

class ChessGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Welcome to chess!")
        self.label.setFont(QFont("Arial", 20))
        # self.button_guest = QPushButton("Play as Guest")
        # self.button_guest.clicked.connect(self.on_guest_button_click) # Connect the guest button click event to the on_guest_button_click function
        self.button_signin = QPushButton("Sign in")
        self.button_signin.clicked.connect(self.on_signin_button_click) # Connect the sign in button click event to the on_signin_button_click function

        # Set up the main layout
        layout = QHBoxLayout()
        layout.addSpacing(10)
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.label)
        right_layout.addStretch(1)
        # right_layout.addWidget(self.button_guest)
        right_layout.addWidget(self.button_signin)
        layout.addLayout(right_layout)

        # Set the main widget
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def on_guest_button_click(self):
        # Open the chess_gui.py file using subprocess
        subprocess.Popen(["python", "chess_gui.py"])
        subprocess.Popen(["python", "unit_tests.py"])
        self.close()

    def on_signin_button_click(self):
        # Open the signin_gui.py file using subprocess
        subprocess.Popen(["python", "signin_gui.py"])
        subprocess.Popen(["python", "unit_tests.py"])
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chess_gui = ChessGUI()
    chess_gui.show()
    sys.exit(app.exec_())
