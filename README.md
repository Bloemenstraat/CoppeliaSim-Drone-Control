# UAV Hand gesture controller

## Prerequisites

You need the Edu version of the [CoppeliaSim simulator](https://www.coppeliarobotics.com/downloads). 

You also need to install the following python dependencies (it is preferred to use a virtual environment as MediaPipe needs an old version of some libraries).

```
pip install pynput zmq opencv-python tensorflow mediapipe numpy
```

## Launch

First, open the UAV.ttt file using CoppeliaSim and run the simulation by clicking on the “run”
button.

Then, launch the program that handles drone control by typing the following command:

```
python UAVControl.py
```

Finally, when the program connects to CoppeliaSim, launch the hand gesture detection program
using the following command:

```
python gestureDetection.py
```
## Usage

These are the hand signs that the drone responds to:

![Thumbs up]() : Go up.
![Thumbs down]() : Go down.
![Ok Sign]() : Go left.
![Two]() : Go right.
![Vulcan salute]() : Go forward.
![Fist]() : Go backward.
![Palm]() : Stop.
