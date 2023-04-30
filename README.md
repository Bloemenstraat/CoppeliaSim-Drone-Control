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

![screenshot](https://github.com/Bloemenstraat/CoppeliaSim-Drone-Control/blob/main/docs/example.png)

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

- ![Thumbs up](https://github.com/Bloemenstraat/CoppeliaSim-Drone-Control/blob/main/docs/up.png) : Go up.
- ![Thumbs down](https://github.com/Bloemenstraat/CoppeliaSim-Drone-Control/blob/main/docs/down.png) : Go down.
- ![Ok Sign](https://github.com/Bloemenstraat/CoppeliaSim-Drone-Control/blob/main/docs/ok.png) : Go left.
- ![Two](https://github.com/Bloemenstraat/CoppeliaSim-Drone-Control/blob/main/docs/two.png) : Go right.
- ![Vulcan salute](https://github.com/Bloemenstraat/CoppeliaSim-Drone-Control/blob/main/docs/vulcan.png) : Go forward.
- ![Fist](https://github.com/Bloemenstraat/CoppeliaSim-Drone-Control/blob/main/docs/fist.png) : Go backward.
- ![Palm](https://github.com/Bloemenstraat/CoppeliaSim-Drone-Control/blob/main/docs/hand.png) : Stop.
