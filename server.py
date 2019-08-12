import RPi.GPIO as GPIO                 # Importing RPi library to use the GPIO pins
from time import *                      # Used for sleep method
from bluetooth import *                 # Imports libraries that supports Bluetooth
from AlphaBot import AlphaBot
from Buzzer import Buzzer
from Rgb import Rgb
from Temperature import Temperature
import instructions                     # Methods where String commands are translated into separate instructions


# ----------------------------------------- INITIALIZATION -------------------------------------------------------------

Ab = AlphaBot()             # Instance of AlphaBot created    | delivers EcliBot movement methods
b = Buzzer(23)              # Instance of Buzzer created      | buzzer can be switched on/off
t = Temperature(11, 18)     # Instance of Temperature created | temperature can be red from sensor
rgb = Rgb(5, 19, 16)        # Instance of Rgb created         | LED diode can turns red, green, blue, or off

commands = []               # List designed for storing instructions for EcliBot
step = 0                    # Counter, used for keeping track the number of Strings received

GPIO.setmode(GPIO.BCM)      # Referring to the pins by the "Broadcom SOC channel" number
GPIO.setwarnings(False)     # Disable warnings

# ----------------------------------------- CUSTOMIZED MOVE METHODS ----------------------------------------------------


def forward():              # EcliBot moves forward for 0.2 seconds at 50 Duty Cycle then stops
    Ab.forward()            # Going approximately 10cm forward, depends on the surface
    Ab.PWMA.start(50)
    Ab.PWMB.start(50)
    sleep(.2)
    Ab.PWMA.stop()
    Ab.PWMB.stop()


def backward():             # EcliBot moves backward for 0.2 seconds at 50 Duty Cycle then stops
    Ab.backward()           # Going approximately 10cm backward, depends on the surface
    Ab.PWMA.start(50)
    Ab.PWMB.start(50)
    sleep(.2)
    Ab.PWMA.stop()
    Ab.PWMB.stop()


def left():                 # EcliBot turn left for 0.8 seconds at 50 Duty Cycle then stops
    Ab.left()               # Turns by approximately 90 degrees, depends on the surface
    Ab.PWMA.start(50)
    Ab.PWMB.start(50)
    sleep(.8)
    Ab.PWMA.stop()
    Ab.PWMB.stop()


def right():                # EcliBot turns right for 0.8 seconds at 50 Duty Cycle then stops
    Ab.right()              # Turns by approximately 90 degrees, depends on the surface
    Ab.PWMA.start(50)
    Ab.PWMB.start(50)
    sleep(.8)
    Ab.PWMA.stop()
    Ab.PWMB.stop()

# -------------------------------- LEARN MODE - ECLIBOT IMPLEMENTS REQUESTED INSTRUCTIONS ------------------------------


def ecliBotGo(instr):
    print "------ LEARN MODE RUN ------"

    for x in instr:
        if x.lower() == "for":
            forward()
            sleep(.5)
            print "FORWARD"
        elif x.lower() == "bac":
            backward()
            sleep(.5)
            print "BACKWARD"
        elif x.lower() == "lef":
            left()
            sleep(.5)
            print "LEFT"
        elif x.lower() == "rig":
            right()
            sleep(.5)
            print "RIGHT"
        elif x.lower() == "cre":
            rgb.redColour()
            sleep(.5)
            print "RED COLOUR"
        elif x.lower() == "cgr":
            rgb.greenColour()
            sleep(.5)
            print "GREEN COLOUR"
        elif x.lower() == "cbl":
            rgb.blueColour()
            sleep(.5)
            print "BLUE COLOUR"
        elif x.lower() == "cnc":
            rgb.noColour()
            sleep(.5)
            print "NO COLOUR"
        elif x.lower() == "bon":
            b.buzzOn()
            sleep(.5)
            print "BUZZER ON"
        elif x.lower() == "bof":
            b.buzzOff()
            sleep(.5)
            print "BUZZER OFF"

# ----------------- SERVICE DISCOVERY PROTOCOL - BLUETOOTH CONNECTION STARTS HERE --------------------------------------


while True:

    server_sock = BluetoothSocket(RFCOMM)   # It allocates resources for an RFCOMM based communication channel

    server_sock.bind(("", 0))               # Bind takes in a tuple specifying the address of the local Bluetooth
                                            # adapter to use and a port number to listen on
                                            # Empty string indicates that any local Bluetooth adapter is acceptable

    port = server_sock.getsockname()[1]
    server_sock.listen(1)                   # Puts the socket into listening mode; ready to accept incoming connections
    print "Waiting for connection on RFCOMM channel %d" % port

    uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"           # The UUID must always be a string of the form
                                                            # "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" or "xxxxxxxx" or
                                                            # "xxxx", where each 'x' is a hexadecimal digit

    advertise_service(server_sock, "EcliBot Server", uuid)  # Takes a socket that is bound and listening,
                                                            # a service name, and a UUID as input parameters.

    client_sock, address = server_sock.accept()  # Accept a connection. The return value is a pair (conn, address)
                                                 # where conn is a new socket object usable to send and receive data
                                                 # on the connection, and address is the address bound to the socket
                                                 # on the other end of the connection.
    print "Accepted connection from ", address

    while True:
        try:
            data = client_sock.recv(4096)   # Receive data from the socket. The return value is a string representing
                                            # the data received. The maximum amount of data to be received at once is
                                            # specified by argument inside.

            if len(data) == 0:
                break
            step = step + 1

            print "received [%s]" % data

# -------------------------------------READING STREAMED DATA FROM THE USER ---------------------------------------------

            if data == 'FORWARD':                   # FORWARD String was received from user
                forward()
            elif data == 'BACKWARD':                # BACKWARD String was received from user
                backward()
            elif data == 'LEFT':                    # LEFT String was received from user
                left()
            elif data == 'RIGHT':                   # RIGHT String was received from user
                right()
            elif data == 'TEMP':                    # TEMP String was received from user
                temp = t.getTemperature()
                sleep(1)
                # data = str(temp) + "*C"
                print data + " " + str(temp)
                client_sock.send(bytes(temp))
            elif data == 'BUZZER ON':               # BUZZER ON String was received from user
                b.buzzOn()
            elif data == 'BUZZER OFF':              # BUZZER OFF String was received from user
                b.buzzOff()
            elif data == 'Red':                     # Red String was received from user
                rgb.redColour()
            elif data == 'Green':                   # Green String was received from user
                rgb.greenColour()
            elif data == 'Blue':                    # Blue String was received from user
                rgb.blueColour()
            elif data == 'No Colour':               # No Colour String was received from user
                rgb.noColour()
            elif data == 'TRAIN':                   # Changing the mode to Train Mode
                # rgb.stopLED()
                client_sock.close()
                server_sock.close()
                break
            elif data == 'LEARN':                   # Changing the mode to Learn Mode
                # rgb.stopLED()
                client_sock.close()
                server_sock.close()
                break
            elif data == 'DISCONNECT':              # Disconnecting
                # rgb.stopLED()
                client_sock.close()
                server_sock.close()
                break
            elif data == 'DATA':
                print data
            else:
                print data
                print len(data)

                commands = instructions.play(data)  # Extracting commands for EcliBot from stream data (String)
                print "+++++++++++++++"
                print commands
                print "+++++++++++++++"
                ecliBotGo(commands)                 # EcliBot reacts to commands ordered by user
                del commands[:]                     # Clears out the list | commands.clear() available in Python 3

            # client_sock.send(bytes(data))
            print " [%d] [%s]" % (step, data)

        except IOError:
            pass

        except KeyboardInterrupt:

            print "disconnected"
            print "CTRL + C was pressed"

            rgb.stopLED()
            print "RGB LED was stopped"

            client_sock.close()
            server_sock.close()
            print "Client closed\nServer closed"

            break

# client_sock.close()
# server_sock.close()
# GPIO.cleanup()
