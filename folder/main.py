import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import ImageTk, Image
from collections import Counter
from datetime import datetime
import time
from database import AttendanceDB
from face_recognition import FaceRecognition
from config import *

class AttendanceGUI:
    def __init__(self,window):
        self.window = window
        self.window.title("Window_Title")