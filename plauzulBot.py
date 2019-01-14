import pyautogui
import keyboard
import sys
import time
from tkinter import *
from tkinter import messagebox

mouseXTop = 0
mouseYLeft = 0
mouseXBottom = 0
mouseYRight = 0

def bt_capture():
    messagebox.showinfo("Selecione a área", "posicione o mouse no canto superior esquerdo")
    global mouseXTop, mouseYLeft
    mouseXTop, mouseYLeft = pyautogui.position()
    messagebox.showinfo("Selecione a área", "posicione o mouse no canto inferior direito")
    global mouseXBottom, mouseYRight
    mouseXBottom, mouseYRight = pyautogui.position()
    #time.sleep(5)
    #verify_img_bonus()

def bt_start():
    while 1:
        toTopLeft()
        toTopRight()
        toBottomRight()
        toBottomLeft()

def bt_stop():
    sys.exit(0)

def press(e):
    if e.char == "1":
        bt_capture()
    elif e.char == "2":
        bt_start()
    elif e.char == "3":
        bt_stop()

def toTopLeft():
    distance = 2000
    pyautogui.moveTo(mouseXTop, mouseYLeft)
    while distance >= 0:
        pyautogui.click()
        distance -= 5

def toBottomLeft():
    distance = 1500
    pyautogui.moveTo(mouseXTop, mouseYRight)
    while distance >= 0:
        pyautogui.click()
        distance -= 5

def toTopRight():
    distance = 1000
    pyautogui.moveTo(mouseXBottom, mouseYLeft)
    while distance >= 0:
        pyautogui.click()
        distance -= 5

def toBottomRight():
    distance = 500
    pyautogui.moveTo(mouseXBottom, mouseYRight)
    while distance >= 0:
        pyautogui.click()
        distance -= 5

def verify_img_bonus():
    x, y = pyautogui.locateCenterOnScreen('imgs/bonus.png')
    pyautogui.click(x, y)
    time.sleep(5)
    return 0

window = Tk()

capture = Button(window, text = "Capturar (1)", command=bt_capture)
capture.pack(side=TOP, fill=BOTH, expand=1)

start = Button(window, text = "Iniciar (2)", command=bt_start)
start.pack(side=TOP, fill=BOTH, expand=1)

stop = Button(window, text = "Parar (3)", command=bt_stop)
stop.pack(side=TOP, fill=BOTH, expand=1)

window.bind('<KeyPress>', press)
window.title("PlauzulBot")
window.geometry("300x300+200+200")
window.mainloop()