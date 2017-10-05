 # -*- coding: utf-8 -*-
import sys  
from Tkinter import *
import numpy as np
import os.path
from subprocess import call
ip="192.168.0.107"
sz=10
x1=""

root = Tk()

root.title("Hindi_Dictonary_Builder")

def save():
  text_file = open("ip.br", "w")
  text_file.write(e.get())
  text_file.close()   
 
 

def caller(x):
  a=x
  print a
  5555
  


  

  if( a=="';'"):
    exit()
  if( a=="'\'"):
    b=raw_input()
    call(["./send_command.sh", b ,ip]) 
    call(["clear"])

  if( a=="']'"):
   
    call(["./ad.sh"])
    call(["clear"])

  else:
    call(["./send_command.sh", a ,ip])
    call(["clear"])
    return 0

import os.path
adrst=os.path.exists("ip.br")







Button(root, text='P',command=lambda: caller("'p'"),font=(None, sz)).grid(row=0,column=0)
Button(root, text='0',command=lambda: caller("'1'"),font=(None, sz)).grid(row=0,column=3)







Button(root, text='1',command=lambda: caller("'1'"), font=(None, sz)).grid(row=2,column=0)
Button(root, text='2',command=lambda: caller("'2'"),font=(None, sz)).grid(row=2,column=1)
Button(root, text='3',command=lambda: caller("'3'"),font=(None, sz)).grid(row=2,column=2)
Button(root, text='0',command=lambda: caller("'0'"),font=(None, sz)).grid(row=2,column=3)


Button(root, text='4',command=lambda: caller("'4'"),font=(None, sz)).grid(row=3,column=0)
Button(root, text='5',command=lambda: caller("'5'"),font=(None, sz)).grid(row=3,column=1)
Button(root, text='6',command=lambda: caller("'6'"),font=(None, sz)).grid(row=3,column=2)
Button(root, text='0',command=lambda: caller("'0'"),font=(None, sz)).grid(row=3,column=3)


Button(root, text='7',command=lambda: caller("'7'"),font=(None, sz)).grid(row=4,column=0)
Button(root, text='8',command=lambda: caller("'8'"),font=(None, sz)).grid(row=4,column=1)
Button(root, text='9',command=lambda: caller("'9'"),font=(None, sz)).grid(row=4,column=2)
Button(root, text='0',command=lambda: caller("'0'"),font=(None, sz)).grid(row=4,column=3)
Button(root, text='^',command=lambda: caller("'w'"),font=(None, sz)).grid(row=5,column=1)
Button(root, text='<',command=lambda: caller("'a'"),font=(None, sz)).grid(row=6,column=0)
Button(root, text='ok',command=lambda: caller("'q'"),font=(None, sz)).grid(row=6,column=1)
Button(root, text='>',command=lambda: caller("'d'"),font=(None, sz)).grid(row=6,column=2)
Button(root, text='|',command=lambda: caller("'s'"),font=(None, sz)).grid(row=7,column=1)
Button(root, text='+',command=lambda: caller("'+'"),font=(None, sz)).grid(row=8,column=0)
Button(root, text='-',command=lambda: caller("'-'"),font=(None, sz)).grid(row=9,column=0)
Button(root, text='+',command=lambda: caller("'*'"),font=(None, sz)).grid(row=8,column=2)
Button(root, text='-',command=lambda: caller("'/'"),font=(None, sz)).grid(row=9,column=2)

Button(root, text='H',command=lambda: caller("'h'"),font=(None, sz)).grid(row=10,column=0)
Button(root, text='T',command=lambda: caller("'z'"),font=(None, sz)).grid(row=10,column=1)
Button(root, text='M',command=lambda: caller("'m'"),font=(None, sz)).grid(row=10,column=2)
Button(root, text='B',command=lambda: caller("'\x1b'"),font=(None, sz)).grid(row=10,column=3)

Button(root, text='_',command=lambda: caller("'x'"),font=(None, sz)).grid(row=11,column=0)
Button(root, text='0',command=lambda: caller("'1'"),font=(None, sz)).grid(row=11,column=1)
Button(root, text='0',command=lambda: caller("'1'"),font=(None, sz)).grid(row=11,column=2)
Button(root, text='0',command=lambda: caller("'1'"),font=(None, sz)).grid(row=11,column=3)




#Radiobutton(root, text="One", command=en(1), value=1).grid(row=6,column=1)


#r=Tk()
#app = App(master = r)

mainloop()














