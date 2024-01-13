import serial, serial.tools.list_ports
from pynput.mouse import Button, Controller 
from pynput.keyboard import Controller as CONTROLLER
from pynput.keyboard import Key

# intall pyserial and pynput

keyboard = CONTROLLER()
mouse = Controller()

def find_USB_device():
	myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
	print(myports)
	usb_port_list = [p[0] for p in myports]
	
	return usb_port_list
    

def decode(command):
    print(repr(command))
    command = command.strip("\r\n")
    if command == "2F0":
        print("Up")
        mouse.move(0, -20)

    elif command == "AF0":
        print("Down")
        mouse.move(0, 20)

    elif command == "CD0":
        print("Right")
        mouse.move(20, 0)

    elif command == "2D0":
        print("Left")
        mouse.move(-20, 0)

    elif command == "A70":
        print("ok")
        mouse.click(Button.left, 1)

    elif command == "62E9":
        print("return")
        keyboard.press(Key.esc)
        keyboard.release(Key.esc) 

    elif command == "4CE9" or command == "2CE9":
        print("pause/play")
        keyboard.press(Key.media_play_pause)
        keyboard.release(Key.media_play_pause)  

    elif command == "5EE9":
        print("Skip")
        keyboard.press(Key.media_next)
        keyboard.release(Key.media_next) 
         
    elif command == "1EE9":
        print("back")
        keyboard.press(Key.media_previous)
        keyboard.release(Key.media_previous) 

user = ""
connected = False
while(user == "" and not connected):
    find_USB_device()
    print("Select COM port:")
    user = input()
    try:
        ser = serial.Serial(user, 9600)
        connected = True
    except Exception as e:
        print(e)
        connected = False

while (True):
    line = ser.readline().decode('UTF-8')
    try:
        decode(line)
    except Exception as e:
        print(e)
        
ser.close()
