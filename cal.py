from tkinter import *
from tkinter import messagebox as mb

root = Tk()
f = ("Arial" , 14)
root.resizable(False, False)

ent = Entry(root , width=60, border=2)
ent.grid(row=1,column=1,columnspan=4,pady=20)

def disply(number):
    global k
    y = ent.get()
    ent.delete(0,END)
    #global k 
    k = str(y)+str(number)
    ent.insert(0, k)
    


def clear():
    #using only index it deletes only one item 
    #when using END it deletes whole the content in entry
    # END = index of the last line 
    ent.delete(0,END)

def add():
    global j
    j = ent.get()
    ent.delete(0,END)
    global m
    m=str(j)+"+"
    ent.insert(0, m)
    #k = ent.get()
    #ans = int(k)+int(local_num)
    #if k == "" or k == None:
    #    mb.showerror(title="Error!" , message="Please enter a value before add!!")
    #ent.insert(0, str(ans))

def equals():
    if "+" in m:
        jo = ent.get()
        ent.delete(0,END)
        mo = int()
        ent.insert(0, m)

bu1 = Button(root, text="1",padx=40,pady=40,font=f,bg="#e3dac9",command=lambda:disply(1))
bu2 = Button(root, text="2",padx=40,pady=40,font=f,bg="#e3dac9",command=lambda:disply(2))
bu3 = Button(root, text="3",padx=40,pady=40,font=f,bg="#e3dac9",command=lambda:disply(3))
bu4 = Button(root, text="4",padx=40,pady=40,font=f,bg="#e3dac9",command=lambda:disply(4))
bu5 = Button(root, text="5",padx=40,pady=40,font=f,bg="#e3dac9",command=lambda:disply(5))
bu6 = Button(root, text="6",padx=40,pady=40,font=f,bg="#e3dac9",command=lambda:disply(6))
bu7 = Button(root, text="7",padx=40,pady=40,font=f,bg="#e3dac9",command=lambda:disply(7))
bu8 = Button(root, text="8",padx=40,pady=40,font=f,bg="#e3dac9",command=lambda:disply(8))
bu9 = Button(root, text="9",padx=40,pady=40,font=f,bg="#e3dac9",command=lambda:disply(9))
bu0 = Button(root, text="0",padx=40,pady=40,font=f,bg="#e3dac9",command=lambda:disply(0))
bu_add = Button(root, text="+",padx=40,pady=40,font=f,bg="#5f9ea0",command=add)
bu_sub = Button(root, text="-",padx=43,pady=40,font=f,bg="#5f9ea0")
bu_mul = Button(root, text="x",padx=42,pady=40,font=f,bg="#5f9ea0")
bu_div = Button(root, text="/",padx=43,pady=40,font=f,bg="#5f9ea0")
bu_eq = Button(root, text="=",padx=41,pady=40,font=f,bg="#bdb76b",command=lambda:equals())
bu_clear = Button(root, text="Clear",padx=23,pady=40,font=f,bg="#bc8f8f",command=equals)

bu1.grid(row=3,column=1)
bu2.grid(row=3,column=2)
bu3.grid(row=3,column=3)
bu4.grid(row=4,column=1)
bu5.grid(row=4,column=2)
bu6.grid(row=4,column=3)
bu7.grid(row=5,column=1)
bu8.grid(row=5,column=2)
bu9.grid(row=5,column=3)
bu_add.grid(row=6,column=3) 
bu_sub.grid(row=4,column=4) 
bu_mul.grid(row=5,column=4) 
bu_div.grid(row=6,column=4) 
bu0.grid(row=6,column=1)
bu_clear.grid(row=3,column=4)
bu_eq.grid(row=6,column=2)

root.mainloop()