from tkinter import *
win=Tk()
def showadd():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    l4.config(text=""+str(c))
    win.config(bg="pink")
def showsub():
    a = int(t1.get())
    b = int(t2.get())
    c = a - b
    l4.config(text=""+str(c))
    win.config(bg="orange")
def showmul():
    a = int(t1.get())
    b = int(t2.get())
    c = a * b
    l4.config(text="" +str(c))
    win.config(bg="skyblue")
def showdiv():
    a = int(t1.get())
    b = int(t2.get())
    c = a // b
    l4.config(text=""+str(c))
    win.config(bg="beige")
win.title("ARITHMETIC CALCULATOR")
f1=("Algerian",12,"bold","italic")
head=Label(win,text="ARITHMETIC CALCULATOR",font=f1)
head.place(x=90,y=10)
t1=Entry(win,bd=3,font=("arial",12,"bold"))
t1.place(x=150,y=50)
t2=Entry(win,bd=3,font=("arial",12,"bold"))
t2.place(x=150,y=100)
l1=Label(win,text="Enter  X",font=f1)
l1.place(x=10,y=50)
l1=Label(win,text="Enter  Y",font=f1)
l1.place(x=10,y=100)
l3=Label(win,text="Ans :-",font=f1)
l3.place(x=100,y=150)
l4=Label(win,text="-------",font=f1)
l4.place(x=230,y=150)

b1=Button(win,text="ADD",
          bg="black",fg="white",
          font=f1,
          command=showadd)
b1.place(x=100,y=200)
b2=Button(win,text="SUB",
          bg="black",fg="white",
          font=f1,
          command=showsub)
b2.place(x=153,y=200)
b3=Button(win,text="MUL",
          bg="black",fg="white",
          font=f1,
          command=showmul)
b3.place(x=203,y=200)
b4=Button(win,text="DIV",
          bg="black",fg="white",
          font=f1,
          command=showdiv)
b4.place(x=255,y=200)
win.geometry("400x250+100+200")
win.mainloop()