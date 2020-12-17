#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---

# Import required modules 
from lxml import html 
import requests 
import time
import random
import tkinter as tk
from tkinter import ttk
import threading

def Datos(Ticker,simbol,root):
    page = requests.get('https://finance.yahoo.com/quote/'+Ticker+'/') 
    tree = html.fromstring(page.content) 
    x="/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span"
    # Get element using XPath 
    Num = tree.xpath(x+"[1]") 
    Porcen = tree.xpath(x+"[2]") 
    print(Num[0].text)
    print(Porcen[0].text.split(" "))
    values = Porcen[0].text.split(" ")
    porcent = float(values[1][1:-2])

    if porcent> 5:
        uni = '{}   {} {:6s} {:10.1f}% \n'.format(simbol[5],simbol[1], "$"+Ticker, porcent)
        second = "$"+Ticker+" "+ str(porcent)
    elif porcent > 2:
        second = "$"+Ticker+" "+ str(porcent)
        uni = '{}   {} {:6s} {:10.1f}%\n'.format(simbol[5],simbol[1], "$"+Ticker, porcent)
    elif porcent > 0:
        second = "$"+Ticker+" "+ str(porcent)
        uni = '{}   {} {:6s} {:10.1f}%\n'.format(simbol[5],simbol[0], "$"+Ticker, porcent)
    else:
        second = "$"+Ticker+" "+ str(porcent)
        uni = '{}   {} {:6s} {:10.1f}%\n'.format(simbol[4],simbol[2], "$"+Ticker, porcent)
    
    #enconded_uni=uni.encode("utf8")
    with threading.Lock():

        s = var.get()
        s += uni
        var.set(s)
      
        listaTotal[Ticker].set(second)




        
def texttowrite(lista):
        

        simbol=['📈','🚀','📉','🔥','🔴','🟢']

        AllText = ["🅿🆁🅴-🅼🅰🆁🅺🅴🆃:","ρ᥅ꫀ-ꪑꪖ᥅ᛕꫀꪻ:","𝓟𝓡𝓔-𝓜𝓐𝓡𝓚𝓔𝓣:","卩尺乇-爪卂尺Ҝ乇ㄒ:","[̲̅P][̲̅R][̲̅E][̲̅-][̲̅M][̲̅A][̲̅R][̲̅K][̲̅E][̲̅T][̲̅:]"]


        var.set(AllText[random.randint(0,len(AllText)-1)]+"\n\n")

        for x in lista:
            thread = threading.Thread(target=Datos, args=(x,simbol,root,))
            thread.start()


def boton(root,lista):


    texttowrite(lista)
    
    button = tk.Button(root, text="CopyClipboard", fg="red",command= lambda: copy(root))
    button.pack()

def copy(root):
    root.clipboard_clear()
    root.clipboard_append(var.get())

def secondwin():
    lista = entry.get().split(",")
    for y in lista:
         var2 = tk.StringVar()
         blog = tk.Label(root, textvariable=var2)
         blog.pack()
         listaTotal[y]=var2
    thread = threading.Thread(target=boton, args=(root,lista,))
    thread.start()

def app():

    global var,root,listaTotal,entry
    
    root = tk.Tk()
    root.title("TickerInfo")
    root.geometry("300x250")
    var = tk.StringVar()
    listaTotal = {}
    entry= tk.Entry(root)
    entry.pack()
    entry.insert(0,'TSLA,AAPL,AZN,AMD,CCL,NIO,CNK')
    button1 = tk.Button(root, text="Tickers", fg="red",command= secondwin)
    button1.pack()

    root.mainloop()
app()