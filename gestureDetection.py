import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import zmq

#Setting up interprocess communication
context = zmq.Context()
print("Connecting to the simulation local server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()

# Initialize the webcam
cap = cv2.VideoCapture(0)

direction = '' #this is the direction the drone will be taking

while True:
    # Read each frame from the webcam
    _, frame = cap.read()
    x , y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    #Convert the frame to the RGB color space
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Get hand landmark prediction
    result = hands.process(framergb)

    className = ''

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)
                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

        # Predict gestures
        prediction = model.predict([landmarks])
        print(prediction)
        classID = np.argmax(prediction)
        className = classNames[classID]

        # show the prediction on the frame
        cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

        #Send the information to the simulation server
        if className == 'up' and direction != 'up':
            direction = 'up'
            socket.send_string(direction)
            socket.recv()
        elif className == 'down' and direction != 'down':
            direction = 'down'
            socket.send_string(direction)
            socket.recv()
        elif className == 'right' and direction != 'right':
            direction = 'right'
            socket.send_string(direction)
            socket.recv()
        elif className == 'left' and direction != 'left':
            direction = 'left'
            socket.send_string(direction)
            socket.recv()
        elif className == 'stop' and direction != 'stop':
            direction = 'stop'
            socket.send_string(direction)
            socket.recv()
        elif className == 'forward' and direction != 'forward':
            direction = 'forward'
            socket.send_string(direction)
            socket.recv()
        elif className == 'backward' and direction != 'backward':
            direction = 'backward'
            socket.send_string(direction)
            socket.recv()

    # Show the final output
    cv2.imshow("Output", frame)
    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()
