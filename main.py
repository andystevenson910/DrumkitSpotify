
from evdev import InputDevice, categorize, ecodes
from musicActions import *
import os

import subprocess

#
pactlNum = 0
#


print("Please ensure that the drumkit is unplugged, then press enter to continue")
input()


command = "ls /dev/input"
completed_process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

output = completed_process.stdout
unpluggedList = output.split()

input("Please plug in the drumkit, then press enter to continue")
completed_process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

output = completed_process.stdout
pluggedList = output.split()

for i in pluggedList:
	if (i not in unpluggedList) and ("event" in i):
		gamepad = InputDevice('/dev/input/'+i)	

if gamepad == None: 
	gamepad = InputDevice('/dev/input/event'+input('number'))



orangePressed = False
playing = False
n = 50
oldN = 50
def init():

    #TODO add is spotify running check

    pause()
    
    result = "Failed to get sink information: No such entity"
    while result != "0":

        global pactlNum
        pactlNum+= 1
        command = "pactl set-sink-volume "+str(pactlNum)+" 50%"  
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print(result)


def buttonPressed(event):
    if event.code == ecodes.BTN_B:
        if ecodes.BTN_TR in gamepad.active_keys():
                return ("Green")
        else:
            return ("A")
    elif event.code == ecodes.BTN_A:
        if ecodes.BTN_TR in gamepad.active_keys():
                return ("Blue")
        else:
            return ("1")
    elif event.code == ecodes.BTN_NORTH:
        if ecodes.BTN_TR in gamepad.active_keys():
                return ("Yellow")
        else:
            return("2")
    elif event.code == ecodes.BTN_C:
        if ecodes.BTN_TR in gamepad.active_keys():
                return("Red")
        else:
            return("B")
    elif event.code == ecodes.BTN_TR2:
        return("Plus")
    elif event.code == ecodes.BTN_TL2:
        return("Minus")

init()
print ("set up complete")


for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY and event.value ==  1 and event.code == ecodes.BTN_WEST:
        orangePressed=True
    elif event.type == ecodes.EV_KEY and event.value ==  0 and event.code == ecodes.BTN_WEST:
        orangePressed=False
    elif event.type == ecodes.EV_KEY and event.value ==  1 and event.code != ecodes.BTN_TR:
        if (not orangePressed):
            match (buttonPressed(event)):
                case "Green":
                    fast_forward()
                case "Blue":
                    if (not playing):
                        play()
                        playing = True
                    else:
                        pause()
                        playing = False
                case "Yellow":
                    rewind()
                case "Red":
                    if n==0:
                        n= oldN
                        os.system("pactl set-sink-volume "+str(pactlNum)+" "+ str(n) +"%")
                    else:
                        n=0
                        os.system("pactl set-sink-volume "+str(pactlNum)+" 0%")
                case "1":
                    os.system("spt play --uri spotify:track:5bJ1DrEM4hNCafcDd1oxHx") #self care
                case "2":
                    os.system("spt play --uri spotify:track:23wfXwnsPZYe5A1xXRHb3J") #The way I am
                case "A":
                    os.system("spt play --uri spotify:track:0Puj4YlTm6xNzDDADXHMI9") #Sabotage
                case "B":
                    os.system("spt play --uri spotify:track:2MLHyLy5z5l5YRp7momlgw") #Island in the sun
                case "Minus":
                    if n>4:
                        os.system("pactl set-sink-volume "+str(pactlNum)+" "+ str(n-5) +"%")
                        n = n - 5
                        oldN = n
                case "Plus":
                    if n < 96:
                        os.system("pactl set-sink-volume "+str(pactlNum)+" "+ str(n+5) +"%")
                        n = n + 5
                        oldN = n
                case default:
                    pause()
                    playing = False
        elif (orangePressed):
            match (buttonPressed(event)):
                case "Green":
                    if n < 91:
                        os.system("pactl set-sink-volume "+str(pactlNum)+" "+ str(n+10) +"%")
                        n = n + 10
                        oldN = n
                case "Red":
                    if n>9:
                        os.system("pactl set-sink-volume "+str(pactlNum)+" "+ str(n-10) +"%")
                        n = n - 10
                        oldN = n
                case "Yellow":
                    os.system("spt play --uri spotify:playlist:37i9dQZF1F0sijgNaJdgit") #top '22
                case "Blue":
                    os.system("spt play --uri spotify:playlist:6N9EFKRG9SMnJqjJ3kwhxg") #top 10


                case "1":
                    os.system("spt play --uri spotify:track:5bJ1DrEM4hNCafcDd1oxHx") #self care
                case "2":
                    os.system("spt play --uri spotify:track:23wfXwnsPZYe5A1xXRHb3J") #The way I am
                case "A":
                    os.system("spt play --uri spotify:track:0Puj4YlTm6xNzDDADXHMI9") #Sabotage
                case "B":
                    os.system("spt play --uri spotify:track:2MLHyLy5z5l5YRp7momlgw") #Island in the sun
                case "Minus":
                    if n>9:
                        os.system("pactl set-sink-volume "+str(pactlNum)+" 10%")
                        n = 10
                        oldN = n
                case "Plus":
                    if n < 91:
                        os.system("pactl set-sink-volume "+str(pactlNum)+" 100%")
                        n = 100
                        oldN = n
                case default:
                    pause()
                    playing = False
