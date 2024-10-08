import tkinter as tk
from tkinter import messagebox
import json

# ファイル読み込み
with open("List/data.json", mode='r') as json_file:
    data = json.load(json_file)


