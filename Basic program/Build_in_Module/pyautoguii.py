import pyautogui
from time import sleep
sleep(0.1)


n= input()
for i in range(1,n):
    for j in range(i,n):
        print('*')