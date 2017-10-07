 #---------------Libs----------------------
import sys  
from Tkinter import *
import numpy as np
import os.path
from subprocess import call

#--------------Ex-Vars----------------
ip="192.168.0.107"
sz=10
x1=""

#----------Main Window-------------------
root = Tk()
root.title("Bravia Remote")

 #-------------------Sender-----------------------

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

#  ------------------Button Matrix----------------------------------------------------


#--------------NumPad---------------------------------------------
Button(root, text='1',command=lambda: caller("'1'"), font=(None, sz)).grid(row=2,column=0)
Button(root, text='2',command=lambda: caller("'2'"),font=(None, sz)).grid(row=2,column=1)
Button(root, text='3',command=lambda: caller("'3'"),font=(None, sz)).grid(row=2,column=2)
Button(root, text='4',command=lambda: caller("'4'"),font=(None, sz)).grid(row=3,column=0)
Button(root, text='5',command=lambda: caller("'5'"),font=(None, sz)).grid(row=3,column=1)
Button(root, text='6',command=lambda: caller("'6'"),font=(None, sz)).grid(row=3,column=2)
Button(root, text='7',command=lambda: caller("'7'"),font=(None, sz)).grid(row=4,column=0)
Button(root, text='8',command=lambda: caller("'8'"),font=(None, sz)).grid(row=4,column=1)
Button(root, text='9',command=lambda: caller("'9'"),font=(None, sz)).grid(row=4,column=2)

#-----------------------Controls-----------------------------


power=Button(root, text='p',command=lambda: caller("'p'"),font=(None, sz),bg="green",foreground="yellow")
power.grid(row=0,column=0)

tvan= Button(root, text='o',command=lambda: caller("'!'"),font=(None, sz))
tvan.grid(row=2,column=3)

help=Button(root, text='i',command=lambda: caller("'i'"),font=(None, sz))
help.grid(row=0,column=3)

info=Label(root,font=(None, sz),text="Hi !",bg="yellow")
info.grid(row=0,column=1)

stim=Button(root, text='t',command=lambda: caller("'U'"),font=(None, sz))
stim.grid(row=3,column=3)

am=Button(root, text='m',command=lambda: caller("'O'"),font=(None, sz))
am.grid(row=4,column=3)

up=Button(root, text='^',command=lambda: caller("'w'"),font=(None, sz))
up.grid(row=5,column=1)
Button(root, text='0',command=lambda: caller("'0'"),font=(None, sz)).grid(row=5,column=2)

left=Button(root, text='<',command=lambda: caller("'a'"),font=(None, sz))
left.grid(row=6,column=0)

ok=Button(root, text='ok',command=lambda: caller("'q'"),font=(None, sz))
ok.grid(row=6,column=1)

right=Button(root, text='>',command=lambda: caller("'d'"),font=(None, sz))
right.grid(row=6,column=2)

down=Button(root, text='|',command=lambda: caller("'s'"),font=(None, sz))
down.grid(row=7,column=1)

volp=Button(root, text='+',command=lambda: caller("'+'"),font=(None, sz))
volp.grid(row=8,column=0)

volm=Button(root, text='-',command=lambda: caller("'-'"),font=(None, sz))
volm.grid(row=9,column=0)

chf=Button(root, text='+',command=lambda: caller("'*'"),font=(None, sz))
chf.grid(row=8,column=2)

chd=Button(root, text='-',command=lambda: caller("'/'"),font=(None, sz))
chd.grid(row=9,column=2)

home=Button(root, text='H',command=lambda: caller("'h'"),font=(None, sz))
home.grid(row=10,column=0)

tv=Button(root, text='T',command=lambda: caller("'z'"),font=(None, sz))
tv.grid(row=10,column=1)

mute=Button(root, text='M',command=lambda: caller("'m'"),font=(None, sz))
mute.grid(row=10,column=2)

back= Button(root, text='B',command=lambda: caller("'\x1b'"),font=(None, sz))
back.grid(row=10,column=3)

hdmi1=Button(root, text='_',command=lambda: caller("'Z'"),font=(None, sz))
hdmi1.grid(row=11,column=0)

sleep=Button(root, text='S',command=lambda: caller("'S'"),font=(None, sz))
sleep.grid(row=11,column=1)

exit= Button(root, text='Q',command= root.destroy,font=(None, sz))
exit.grid(row=11,column=2)

wake= Button(root, text='W',command=lambda: caller("'W'"),font=(None, sz))
wake.grid(row=11,column=3)

#-------------------------------On-Hover-Button-----------------------------

back.bind("<Enter>", lambda event:info.config(text="Back"))
back.bind("<Leave>", lambda event: info.config(text="    "))

hdmi1.bind("<Enter>", lambda event:info.config(text="HDM1"))
hdmi1.bind("<Leave>", lambda event: info.config(text="    "))

power.bind("<Enter>", lambda event:info.config(text="Power"))
power.bind("<Leave>", lambda event: info.config(text="    "))

tv.bind("<Enter>", lambda event:info.config(text="Tv  "))
tv.bind("<Leave>", lambda event: info.config(text="    "))

chf.bind("<Enter>", lambda event:info.config(text="Ch +"))
chf.bind("<Leave>", lambda event: info.config(text="    "))

chd.bind("<Enter>", lambda event:info.config(text="Ch -"))
chd.bind("<Leave>", lambda event: info.config(text="    "))

volp.bind("<Enter>", lambda event:info.config(text="Vol +"))
volp.bind("<Leave>", lambda event: info.config(text="    "))

volm.bind("<Enter>", lambda event:info.config(text="Vol -"))
volm.bind("<Leave>", lambda event: info.config(text="    "))

mute.bind("<Enter>", lambda event:info.config(text="Mute"))
mute.bind("<Leave>", lambda event: info.config(text="    "))

up.bind("<Enter>", lambda event:info.config(text="Up  "))
up.bind("<Leave>", lambda event: info.config(text="    "))

down.bind("<Enter>", lambda event:info.config(text="Down"))
down.bind("<Leave>", lambda event: info.config(text="    "))

left.bind("<Enter>", lambda event:info.config(text="Left"))
left.bind("<Leave>", lambda event: info.config(text="    "))

right.bind("<Enter>", lambda event:info.config(text="Right"))
right.bind("<Leave>", lambda event: info.config(text="    "))

ok.bind("<Enter>", lambda event:info.config(text="Ok  "))
ok.bind("<Leave>", lambda event: info.config(text="    "))

help.bind("<Enter>", lambda event:info.config(text="Help"))
help.bind("<Leave>", lambda event: info.config(text="    "))

home.bind("<Enter>", lambda event:info.config(text="Home"))
home.bind("<Leave>", lambda event: info.config(text="    "))

tvan.bind("<Enter>", lambda event:info.config(text="AnTv"))
tvan.bind("<Leave>", lambda event: info.config(text="    "))

stim.bind("<Enter>", lambda event:info.config(text="STim"))
stim.bind("<Leave>", lambda event: info.config(text="    "))

am.bind("<Enter>", lambda event:info.config(text="Ac.M"))
am.bind("<Leave>", lambda event: info.config(text="    "))

wake.bind("<Enter>", lambda event:info.config(text="Wake"))
wake.bind("<Leave>", lambda event: info.config(text="    "))


sleep.bind("<Enter>", lambda event:info.config(text="Slp."))
sleep.bind("<Leave>", lambda event: info.config(text="    "))

exit.bind("<Enter>", lambda event:info.config(text="Exit"))
sleep.bind("<Leave>", lambda event: info.config(text="    "))



mainloop()














