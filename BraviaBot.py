import readchar
import time
from subprocess import call




call(["clear"])
fn= raw_input("Enter Application name: ")


t=2	
with open(fn, "r") as ins:
    	array = []
	
    	for line in ins:
		if (line=="h"):
			time.sleep(2)
			

		
		
        	call(["./send_command.sh", line ,"7"])
		call(["clear"])
		time.sleep(t)
		t=.05
		print ins

	

