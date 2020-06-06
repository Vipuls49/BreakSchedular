import time as tm
import webbrowser as web
import random as r
import os
browserExe = "chrome.exe"
wt=float(input("enter working time(in hrs)="))
work=wt*60*60
m=int(input("enter no of times to take a break="))
n=r.random()
t=float(n)*60*60
for i in range(m):
    print('*-*'*20)
    print("Do your work which you want to do!!!")
    print('*-*'*20)
    tm.sleep(work)
    print()
    print()
    print('*-*'*20)
    print("Now its your break time!!!!!!")
    print("Play some fun quizes and just chill!!!!!!")
    print('*-*'*20)
    web.open_new_tab("https://www.quotev.com/quizzes/c/Personality/Time+Pass")
    tm.sleep(t)
    os.system("taskkill /f /im "+browserExe)