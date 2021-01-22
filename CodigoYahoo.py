#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---

# Import required modules 
from lxml import html 
import requests 
import time
import random
import tkinter as tk
from tkinter import ttk,BOTTOM
import threading

def Datos(Ticker,simbol,root):
    page = requests.get('https://finance.yahoo.com/quote/'+Ticker+'/') 
    tree = html.fromstring(page.content) 

    x='/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/p/span'
    #x="/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span"
    # Get element using XPath 
    # detect premarket or market
    if len(tree.xpath(x+"[1]")) > 0:
        Num = tree.xpath(x+"[1]") 
        Porcen = tree.xpath(x+"[2]/span") 
    else:
        x="/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/div/span"
        Num = tree.xpath(x+"[1]") 
        Porcen = tree.xpath(x+"[2]") 
    print(Ticker)
    print(Num)
    print(Num[0].text)
    print(Porcen[0].text)
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
        
        page = requests.get('https://finance.yahoo.com/quote/AAPL/') 
        tree = html.fromstring(page.content) 
        x='/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div/div[3]/div[1]/p/span'
        if len(tree.xpath(x+"[1]")) > 0:
            AllText = ["🅿🆁🅴-🅼🅰🆁🅺🅴🆃:","ρ᥅ꫀ-ꪑꪖ᥅ᛕꫀꪻ:","𝓟𝓡𝓔-𝓜𝓐𝓡𝓚𝓔𝓣:","卩尺乇-爪卂尺Ҝ乇十:","[̲̅P][̲̅R][̲̅E][̲̅-][̲̅M][̲̅A][̲̅R][̲̅K][̲̅E][̲̅T][̲̅:]"]
        else:
            AllText = ["𝓜𝓪𝓻𝓴𝓮𝓽:","𝕄𝕒𝕣𝕜𝕖𝕥:","🄼🄰🅁🄺🄴🅃:","Ｍａｒｋｅｔ:","🅼🅰🆁🅺🅴🆃:","爪卂尺Ҝ乇ㄒ:"]

        simbol=['📈','🚀','📉','🔥','🔴','🟢']

        

        var.set(AllText[random.randint(0,len(AllText)-1)]+"\n\n")

        for x in lista:
            thread = threading.Thread(target=Datos, args=(x,simbol,root,))
            thread.start()


def boton(root,lista):


    texttowrite(lista)
    
    button = tk.Button(root, text="CopyClipboard", fg="red",command= lambda: copy(root))
    button.grid(row=1,column=1)

def copy(root):
    root.clipboard_clear()
    root.clipboard_append(var.get())

def secondwin():
    lista = entry.get().split(",")
    for y in listaTotal:
        listaTotal[y].set("")
    for z in range(len(lista)):
        y = lista[z]
        if y not in listaTotal.keys():
            var2 = tk.StringVar()
            blog = tk.Label(root, textvariable=var2)
            blog.grid(row=z+2,column=0)
            listaLabels[y]=blog
            listaTotal[y]=var2
    thread = threading.Thread(target=boton, args=(root,lista,))
    thread.start()

def app():

    global var,root,listaTotal,entry,listaLabels
    listaLabels = {}
    root = tk.Tk()
    root.title("TickerInfo")
    root.geometry("300x250")
    var = tk.StringVar()

    listaTotal = {}
    entry= tk.Entry(root)
    entry.grid(row=0,column=0)
    entry.insert(0,'TSLA,AAPL,AZN,AMD,CCL,NIO,CNK')
    button1 = tk.Button(root, text="Tickers", fg="red",command= secondwin)
    button1.grid(row=1,column=0)

    root.mainloop()
app()