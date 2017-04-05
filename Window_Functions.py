__author__ = 'Jake'
import ctypes
import pyautogui
import win_unicode_console
win_unicode_console.enable()

from ctypes import *

dc = windll.user32.GetDC(0)

def getPixel(x,y):
    return windll.gdi32.GetPixel(dc,x,y)

#doesnt work
def GetBValue(colorRef):
    return windll.gdi32.GetBValue(colorRef)

def SetCursorPos(x,y):
    return windll.user32.SetCursorPos(x,y)

#try creating own dll from code so that i can use input
def TypeString(string):
    pyautogui.typewrite(string)

def leftClick():
    pyautogui.click()
