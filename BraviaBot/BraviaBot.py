import readchar
import time
from Tkinter import *
from subprocess import call
sz=15




call(["clear"])




def caller(fn):
 call(["./send_command.sh", 'z' ,"7"])
 t=2	
 with open(fn, "r") as ins:
    	array = []
	
    	for line in ins:
		

		if (line==")\n"):
			time.sleep(3)
			
			

		
		
        	call(["./send_command.sh", line ,"7"])
        	
		
		time.sleep(t)
		t=.05



root = Tk()
bx1=Button(root, text='1',command=lambda : caller("delhi"), font=(None, sz)).grid(row=2,column=0)
bx2=Button(root, text='ndtv',command=lambda : caller("ndtv"),font=(None, sz)).grid(row=2,column=1)
bx3=Button(root, text='ddnews',command=lambda : caller("ddnews"),font=(None, sz)).grid(row=2,column=2)
bx4=Button(root, text='setmax',command=lambda : caller("set"),font=(None, sz)).grid(row=3,column=0)
bx5=Button(root, text='Nat Geo',command=lambda : caller("natgeo"),font=(None, sz)).grid(row=3,column=1)
bx6=Button(root, text='Discovery',command=lambda : caller("discovery"),font=(None, sz)).grid(row=3,column=2)
bx7=Button(root, text='History',command=lambda : caller("history"),font=(None, sz)).grid(row=4,column=0)
bx8=Button(root, text='Delhi Aaajtk',command=lambda : caller("delhi"),font=(None, sz)).grid(row=4,column=1)
bx9=Button(root, text='ABP',command=lambda : caller("abp"),font=(None, sz)).grid(row=4,column=2)
bx0=Button(root, text='star plus',command=lambda : caller("star"),font=(None, sz)).grid(row=5,column=2)
mainloop()
		
	

