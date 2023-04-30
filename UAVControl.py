import sim
from pynput import keyboard
import zmq

exit_toggle = False

def exit_loop(key):
    global exit_toggle
    if key == keyboard.KeyCode.from_char('q'):
        exit_toggle = True
    


listener = keyboard.Listener( on_press=lambda *args: None, on_release=exit_loop )


print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
step = 0.007 #Speed of the drone 
direction = 'stop' #Start the simulation with a stationary drone

#Setting up interprocess communication
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

if clientID!=-1:
    print('Connected to CoppeliaSim! Please launch the hand detection program to start using the system.')

    #access to the target object of the CoppeliaSim simulator
    target = sim.simxGetObjectHandle(clientID, 'Quadcopter_target', sim.simx_opmode_blocking)
    
    listener.start()

    while True:
        if exit_toggle:
            break

        #For each iteration, we listen to signals from the gestureDetection.py program
        try:
            direction = socket.recv_string(flags=zmq.NOBLOCK)
            print(direction)
            socket.send(b'received')
        except:
            pass

        #Move the drone in the desired direction
        if direction == 'down':
            sim.simxSetObjectPosition(clientID, target[1], target[1], (0, 0, -step), sim.simx_opmode_oneshot)
        elif direction == 'up':
            sim.simxSetObjectPosition(clientID, target[1], target[1], (0, 0, step), sim.simx_opmode_oneshot)
        elif direction == 'right':
            sim.simxSetObjectPosition(clientID, target[1], target[1], (0, step, 0), sim.simx_opmode_oneshot)
        elif direction == 'left':
            sim.simxSetObjectPosition(clientID, target[1], target[1], (0, -step, 0), sim.simx_opmode_oneshot)
        elif direction == 'forward':
            sim.simxSetObjectPosition(clientID, target[1], target[1], (step, 0, 0), sim.simx_opmode_oneshot)
        elif direction == 'backward':
            sim.simxSetObjectPosition(clientID, target[1], target[1], (-step, 0, 0), sim.simx_opmode_oneshot)
        elif direction == 'stop':
            pass

    #We make sure that the last command sent out had time to arrive before closing CoppeliaSim
    sim.simxGetPingTime(clientID)
    #Close the connection to CoppeliaSim:
    sim.simxFinish(clientID)

else:
    print('Failed to connect to CoppeliaSim. Please check if CoppeliaSim is open and the simulation is running.')