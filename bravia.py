import readchar
from subprocess import call



call(["clear"])
while 1:
	
	print("Bravia :")
	a='''               Bravia KDL43W950C Remote Control       EXIT ;


Numbers= 0-9     Back Esc     
Home h           ActionMenu O
Select Enter     ChannelUp *
Tv z             ChannelDown /	
Power p          Input I
VolumeUp +	 TvInput n
VolumeDown -	 TvAntennaCable b
Mute mCursorUp w WakeUp W
CursorDown s	 Sleep S
CursorRight d	 Right R
CursorLeft a	 Left L
Help i		 SleepTimer U
HDMI1 Z 	 TvAnalog !
HDMI2 X 	 Analog2 @	
HDMI3 C 
HDMI4 V


'''
	print a
	
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

	
