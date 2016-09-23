import readchar
from subprocess import call




while 1:
	print("Bravia :")
	
	a=repr(readchar.readchar())
	print a

	if( a=="';'"):
		exit()
	if( a=="'\'"):
	 	b=raw_input()
		call(["./send_command.sh", b])
		call(["clear"])

	if( a=="']'"):
	 
		call(["./ad.sh"])
		call(["clear"])

	else:
		call(["./send_command.sh", a])
		call(["clear"])
#	call(["./ad.sh"])
	call(["clear"])

	

