import readchar
from subprocess import call

call(["clear"])
print '''

		Linux-Bravia_Remote By: Himanshu Attri
		  (https://github.com/HimanshuAttri}


Instructions
1. Navigate to: Settingsn Network  Home Network Setup IP Control
2. Set Authentication to Normal and Pre Shared Key
3. There should be a new menu entry Pre-Shared Key. Set it to **0000**. 
   If you choose anything else, you need to change the PSK in the `send_command.   sh` script.




Bravia Tv Local ip: '''
ip=raw_input()



call(["clear"])
while 1:
	
	print("Bravia : "+ip)
	a='''               Bravia KDL43W950C Remote Control       EXIT ;


Numbers= 0-9     Back Esc     
Home h           ActionMenu O
Select Enter     ChannelUp *
Tv z             ChannelDown /	
Power p          Input I
VolumeUp +	 TvInput n
VolumeDown -	 TvAntennaCable b
Mute m           WakeUp W
CursorUp w          
CursorDown s	 Sleep S
CursorRight d	 Right R
CursorLeft a	 Left L
Help i		 SleepTimer U
HDMI1 Z 	 TvAnalog !
HDMI2 X 	 Analog2 @	
HDMI3 C 
HDMI4 V
							By: Himanshu Attri 
'''
	print a
	
	a=repr(readchar.readchar())
	print a

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
#	call(["./ad.sh"])
	call(["clear"])

	
