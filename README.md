# Auto Irrigation System

## Intro

It's a project for course SYSC 3020 of Fall 2018 term of Carleton University. 

Done by Group Tuesday 3.

## How to start

1. Download the Controller folder (https://github.com/AkazaDorian/Auto-Irrigation-System/tree/master/Controller) into Pi 1, rename the folder to be `proj`. 
2. Run `pip3 install cloudinary` to install required libraries.
3. Modify the commented parts of `/proj/basic.py` to the corresponding parts of your own.
4. Download the Data folder (https://github.com/AkazaDorian/Auto-Irrigation-System/tree/master/Data) into Pi 2, rename the folder to be `proj`. 
5. Copy the files inside `systemctl` folder into `/etc/systemd/system/`, run `sudo systemctl daemon-reload`. 
6. Modify the IP addresses and ports in piController.py and piData.py to the IP and ports to be used. 
7. Connect the 4 pins of stepper motor with GPIO 31, 33, 35, 37 of Pi 1. 
8. Download the Arduino code and install it onto an Arduino UNO board. 
9. Connect the Arduino UNO board with Pi 2 through USB port. 
10. Download the Android folder (https://github.com/AkazaDorian/Auto-Irrigation-System/tree/master/Android/auto%20irrigate), compile and install onto an Android device. 
11. Run `python3 ~/proj/piController.py` on Pi 1 and `python3 ~/proj/piData.py` on Pi 2. 
12. Start the Android app, follow the instructions on the app to connect it to Pi 1.