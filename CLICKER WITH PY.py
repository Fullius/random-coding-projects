#Clicker Game
import tkinter
import time
import threading
CookieClick = 1
storeShow = 0
game = 0
cookies = 0
AutoClick = 0
CookieClickPrice = 50
cookies = 0
AutoClickPrice = 100
def onClick(event):
    global cookies
    cookies = int(cookies) + int(CookieClick)
    CookieCounter.configure(text=cookies)
def buyClick1(event):
    global CookieClick
    global CookieClickPrice
    global cookies
    if cookies >= CookieClickPrice:
        CookieClick = CookieClick + 1
        cookies = int(cookies) - int(CookieClickPrice)
        CookieClickPrice = int(CookieClickPrice) * 2
        CookieCounter.configure(text=cookies)
        CookieClickPriceButton.configure(text=CookieClickPrice)
def buyClick2(event):
    global AutoClick
    global AutoClickPrice
    global cookies
    if cookies >= AutoClickPrice:
        AutoClick = AutoClick + 1
        cookies = int(cookies) - int(AutoClickPrice)
        CookieCounter.configure(text=cookies)
        AutoClickPrice = int(AutoClickPrice) * 2
        AutoClickPriceButton.configure(text=AutoClickPrice)
print("CLICKER BEGINING...")
print()
time.sleep(2)
print()
print("CLICKER STARTED")
window = tkinter.Tk()
CookieCounter = tkinter.Button(window, text=int(cookies), width=20)
CookieCounter.pack(padx=5, pady=5)
button = tkinter.Button(window, text="Press this for food", width=20)
button.pack(padx=20, pady=15)
storeButton1 = tkinter.Button(window, text="ExtraClick: Adds one extra cookie per click.", width=50)
CookieClickPriceButton = tkinter.Button(window, text=CookieClickPrice, width=15)
storeButton2 = tkinter.Button(window, text="AutoClick: Adds one extra cookie per 3 seconds.", width=50)
AutoClickPriceButton = tkinter.Button(window, text=AutoClickPrice, width=15)
storeButton1.pack(padx=5, pady=5)
cookiesScreen = tkinter.Button(window, text="Cookies=", width=20)
CookieClickPriceButton.pack(padx=1, pady=1)
storeButton2.pack(padx=5, pady=5)
AutoClickPriceButton.pack(padx=1, pady=1)
button.bind("<ButtonRelease-1>", onClick)
storeButton1.bind("<ButtonRelease-1>", buyClick1)
storeButton2.bind("<ButtonRelease-1>", buyClick2)
print('Now we can continue running code while mainloop runs!')
window.mainloop()
while game != "1":
    time.sleep(3)
    cookies = int(cookies) + int(AutoClick)
    print("COOKIES ADDED")
    CookieCounter.configure(text=cookies)
AutoClick = 0
    

        
