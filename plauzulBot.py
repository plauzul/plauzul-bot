import pyautogui
import sys
import time
from tkinter import *
from tkinter import messagebox

mouseXTop = 0
mouseYLeft = 0
mouseXBottom = 0
mouseYRight = 0
getPirateBau = 0

def bt_capture():
    messagebox.showinfo("Selecione a área", "posicione o mouse no canto superior esquerdo")
    global mouseXTop, mouseYLeft
    mouseXTop, mouseYLeft = pyautogui.position()
    messagebox.showinfo("Selecione a área", "posicione o mouse no canto inferior direito")
    global mouseXBottom, mouseYRight
    mouseXBottom, mouseYRight = pyautogui.position()

def bt_start():
    #while 1:
    toTopLeft(50)
    toTopRight(50)
    toBottomRight(50)
    toBottomLeft(50)

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
    verify_img_alien('lordakia')
    verify_img_bonus()
    if getPirateBau == "1":
        verify_img_pirate()
    if distance >= 0:
        pyautogui.moveTo(mouseXTop, mouseYLeft)
        pyautogui.click(clicks=4)
        distance -= 5
        toTopLeft(distance)

def toBottomLeft(distance):
    verify_img_alien('lordakia')
    verify_img_bonus()
    if getPirateBau == "1":
        verify_img_pirate()
    if distance >= 0:
        pyautogui.moveTo(mouseXTop, mouseYRight)
        pyautogui.click(clicks=4)
        distance -= 5
        toBottomLeft(distance)

def toTopRight(distance):
    verify_img_alien('lordakia')
    verify_img_bonus()
    if getPirateBau == "1":
        verify_img_pirate()
    if distance >= 0:
        pyautogui.moveTo(mouseXBottom, mouseYLeft)
        pyautogui.click(clicks=4)
        distance -= 5
        toTopRight(distance)

def toBottomRight(distance):
    verify_img_alien('lordakia')
    verify_img_bonus()
    if getPirateBau == "1":
        verify_img_pirate()
    if distance >= 0:
        pyautogui.moveTo(mouseXBottom, mouseYRight)
        pyautogui.click(clicks=4)
        distance -= 5
        toBottomRight(distance)

def verify_img_bonus():
    try:
        k = pyautogui.locateOnScreen('imgs/bonus-box.png', grayscale=True, confidence=.9)
        s = pyautogui.center(k)
        d = list(s)
        pyautogui.click(d[0], d[1])
        time.sleep(2)
        verify_img_bonus()
    except:
        return 0
    return 0

def verify_img_pirate():
    try:
        k = pyautogui.locateOnScreen('imgs/pirate-box.png', grayscale=True, confidence=.9)
        s = pyautogui.center(k)
        d = list(s)
        pyautogui.click(d[0], d[1])
        time.sleep(6)
        verify_img_pirate()
    except:
        return 0
    return 0

def verify_img_alien(alien):
    try:
        k = pyautogui.locateOnScreen('imgs/'+alien+'.png', grayscale=True, confidence=.9)
        s = pyautogui.center(k)
        d = list(s)
        pyautogui.click(d[0], d[1])
        pyautogui.press('q')
        time.sleep(1)
        verify_img_alien()
    except:
        return 0
    return 0

def setPirateBau():
    global getPirateBau
    if getPirateBau == "1":
        getPirateBau = "0"
    else:
        getPirateBau = "1"

window = Tk()

capture = Button(window, text = "Capturar (1)", command=bt_capture)
capture.pack(side=TOP, fill=BOTH, expand=1)

start = Button(window, text = "Iniciar (2)", command=bt_start)
start.pack(side=TOP, fill=BOTH, expand=1)

stop = Button(window, text = "Parar (3)", command=bt_stop)
stop.pack(side=TOP, fill=BOTH, expand=1)

pirateBau = Checkbutton(window, text="Pegar bau de pirata?", command=setPirateBau)
pirateBau.pack(side=TOP, fill=BOTH, expand=1)

window.bind('<KeyPress>', press)
window.title("PlauzulBot")
window.geometry("300x300+200+200")
window.mainloop()