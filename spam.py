import pyautogui
import time

msg = input("Enter the message: ")
n = input("How many times ?: ")

print("Bomb has been planted")

count = 5
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

print("Program has been executed")

for i in range(0,int(n)):
    pyautogui.typewrite(msg + '\n')