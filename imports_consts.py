from PyQt6.QtWidgets import QApplication, QMainWindow,QPushButton, QLabel, QWidget, QGridLayout,QVBoxLayout, QHBoxLayout, QSizePolicy, QStackedWidget
from PyQt6.QtCore import QSize,Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QPixmap, QFont, QFontDatabase, QPainter, QColor,QPen

from controller import AppController
from timer import Timer
from system import System
from user import User

height=600
width=600
round_corners = 25
path = "study_store/"