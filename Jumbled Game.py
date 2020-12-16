# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:06:27 2019

@author: pythor7

"""
import tkinter
import random


def checkAns():
    global words,answers,num
    var=et.get()
    if var == answers[num]:
        tkinter.messagebox.showinfo("Success","This is correct answer")
        res()
    else:
        tkinter.messagebox.showinfo("Failure","This is wrong answer")
#    et.delete(0,len(et.get()))
    
def res():
    global words,answers,num
    num = random.randrange(0,15)
    lbl.config(text=words[num])
    et.delete(0,len(et.get()))
        

answers=["python","java","coral","computer","software","testing","linux","unix",
        "windows","android","eclipse","chrome","mumbai","delhi","india"]

words=["htoynp","avja","rolac","uptmeorc","wtaferos","gistent","unxil","xniu",
       "diwsonw","rodinad","licpese","mrohec","bumiam","helid","dinai"]

num = random.randrange(0,15)
root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Jumbled Game")
root.configure(background="light blue") 

lbl = tkinter.Label(root,text="You are here",font=("Times 18"),bg="black",fg="white")
lbl.pack(pady=30)

ansvar=str()
et = tkinter.Entry(root,font="Times 16",textvariable = ansvar)
et.pack(pady=20,ipadx=5,ipady=5)

btncheck = tkinter.Button(root,text="Check",font=("Cosmic sans ms",16),bg="grey",fg="black",command=lambda:checkAns())
btncheck.pack(pady=10)
btnreset = tkinter.Button(root,text="Reset",font=("Cosmic sans ms",16),bg="grey",fg="black",command=lambda:res())
btnreset.pack(pady=10)

lbl.config(text=words[num])

root.mainloop()