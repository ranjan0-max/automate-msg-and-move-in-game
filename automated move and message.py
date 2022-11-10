import pyautogui
import random
import time

nm=["kese ho","hlo","chal koi na","smj nahi aata tuje","befkuf","tu sahi ha","acha laga","kaha ja raha ha"
,"tu bahot sidha ha","chal koi na","ruk tu","bahot ha acha ha tu","skal maat dikaio apni"
,"kya name ha tera","baat maan mere","chup ho ja","muj maat kar pareshan","suraj","anuj"
,"kam karne de muje apna","game khele","tu nooda hi rahe ga","mujse sikh le"
,"kam kar le kush","life choti si ha","apna time waste maat kar","aao kabi hawali pe","ye maat kar","likhna padna sikh le phele"
,"dimag to maat kar khrab","smjta ku nahi ha tu","dimag ki kami ha tuj mai","life mai kush kar le","vo maat kar","yaha maat ja","vaha maat ja"
,"muje kya hi dikat ha","maan le baat"]

gl=["fuck"]

def message():
    t=int(input("enter the times in number :- "))
    msg=input("enter the message : -")
    time.sleep(10)
    for _ in range(0,t):
        pyautogui.write(msg)
        pyautogui.press('enter')

def difstring(*args):
    t=int(input("enter the times in number :- "))
    time.sleep(4)
    for _ in range(0,t):
        for j in args:
            for i in random.choice(j):
                pyautogui.write(i)
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

choose = input("message or game or dif :- ")

if choose=='game':
    game()
elif choose=='message':
    message()
elif choose=='dif':
    msg=input("nm or gl :-")
    if msg=='nm':
        difstring(nm)
    else:
        difstring(gl)
else:
    print("bye bye")
