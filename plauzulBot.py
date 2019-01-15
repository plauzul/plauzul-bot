import pyautogui
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

def bt_start():
    #while 1:
    toTopLeft(10)
    toTopRight(10)
    toBottomRight(10)
    toBottomLeft(10)

def bt_stop():
    sys.exit(0)

def press(e):
    if e.char == "1":
        bt_capture()
    elif e.char == "2":
        bt_start()
    elif e.char == "3":
        bt_stop()

def toTopLeft(distance):
    time.sleep(1)
    verify_img_bonus()
    if distance >= 0:
        pyautogui.moveTo(mouseXTop, mouseYLeft)
        pyautogui.click()
        distance -= 5
        toTopLeft(distance)

def toBottomLeft(distance):
    time.sleep(1)
    verify_img_bonus()
    if distance >= 0:
        pyautogui.moveTo(mouseXTop, mouseYRight)
        pyautogui.click()
        distance -= 5
        toBottomLeft(distance)

def toTopRight(distance):
    time.sleep(1)
    verify_img_bonus()
    if distance >= 0:
        pyautogui.moveTo(mouseXBottom, mouseYLeft)
        pyautogui.click()
        distance -= 5
        toTopRight(distance)

def toBottomRight(distance):
    time.sleep(1)
    verify_img_bonus()
    if distance >= 0:
        pyautogui.moveTo(mouseXBottom, mouseYRight)
        pyautogui.click()
        distance -= 5
        toBottomRight(distance)

def verify_img_bonus():
    try:
        k = pyautogui.locateOnScreen('imgs/bonus-box.png', grayscale=True, confidence=.9)
        s = pyautogui.center(k)
        d = list(s)
        pyautogui.click(d[0], d[1])
    except:
        return 0
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