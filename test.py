from tkinter import *
import requests



response = requests.get("https://api.kanye.rest")
quote = response.json()
quote["quote"]
