# Auto Irrigation System

## Intro

It's a project for course SYSC 3020 of Fall 2018 term of Carleton University. 

Done by Group Tuesday 3.

## How to start

1. Download the Controller folder (https://github.com/AkazaDorian/Auto-Irrigation-System/tree/master/Controller) into Pi 1, rename the folder to be `proj`. 

2. Download the Data folder (https://github.com/AkazaDorian/Auto-Irrigation-System/tree/master/Data) into Pi 2, rename the folder to be `proj`. 

3. Copy the files inside `systemctl` folder into `/etc/systemd/system/`, run `sudo systemctl daemon-reload`. 

4. Modify the IP addresses and ports in piController.py and piData.py to the IP and ports to be used. 

5. Connect the 4 pins of stepper motor with GPIO 31, 33, 35, 37 of Pi 1. 

6. Download the Arduino code and install it onto an Arduino UNO board. 

7. Connect the Arduino UNO board with Pi 2 through USB port. 

8. Download the Android folder (https://github.com/AkazaDorian/Auto-Irrigation-System/tree/master/Android/auto%20irrigate), compile and install onto an Android device. 

9. Run `python3 ~/proj/piController.py` on Pi 1 and `python3 ~/proj/piData.py` on Pi 2. 

10. Start the Android app, follow the instructions on the app to connect it to Pi 1.