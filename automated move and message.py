import pyautogui
import random
import time

def message():
    t=int(input("enter the times in number :- "))
    msg=input("enter the message : -")
    time.sleep(10)
    for i in range(0,t):
        for i in msg:
            pyautogui.press(i)
        pyautogui.press('enter')

def game():
    time.sleep(10)
    while(True):
        for i in range(0,1):
            randomLetter = random.choice('wasd')
            pyautogui.keyDown(randomLetter)
            time.sleep(2)
            pyautogui.keyUp(randomLetter)
            pyautogui.press('enter')
            pyautogui.write("papa is AFK. it is automated program.")
            pyautogui.press('enter')

choose = input("message or game :- ")

if choose=='game':
    game()
elif choose=='message':
    message()
else:
    print("bye bye")    
    

