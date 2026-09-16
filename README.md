# AudioNav
Python-based assistive navigation prototype that uses ultrasonic sensors and audio feedback to help visually impaired users detect nearby obstacles.

Project Title: AUDIONAV
Brief description of the project idea: (1 paragraph)

Team Member Names: Ashwin Anil, Salomon Lara, Jaden Nguyen

FULL PROJECT VIDEO LINK: https://youtu.be/1lGxU_E5TcI


/**********************************************************************
 *  Log all help, collaboration, and outside resources you've used for this project. List all external Python library names you used. Add links to the websites you have used as resources.
 **********************************************************************/
1. External Python Libraries Used
a. RPi.GPIO – For controlling Raspberry Pi GPIO pins.
b. time – For handling delays and measuring echo duration.

2. Collaboration & Help
a. Team brainstorming and debugging sessions for buzzer logic and sensor setup.
b. Peer code reviews to ensure distance measurements and buzzer timings were correct.
c. Assistance from online forums and tutorials on Raspberry Pi ultrasonic sensors.

3. Online Resources
a. Raspberry Pi official GPIO documentation: https://www.raspberrypi.com/documentation/usage/gpio/
b. Raspberry Pi ultrasonic sensor tutorials:
   - https://www.modmypi.com/blog/ultrasonic-sensor-hc-sr04-with-raspberry-pi
   - https://www.circuitbasics.com/raspberry-pi-ultrasonic-sensor/

Stack Overflow – For troubleshooting Python RPi.GPIO issues: https://stackoverflow.com/questions/tagged/rpi.gpio


/**********************************************************************
 *  List step by step insturctions on how to use your project. If someone would take your code and your circuit and hardware, how would they start using the application. This should server as a user manual. 
 **********************************************************************/
1. Open the top lid and find the Raspberry Pi 4 Model B, underneath there will be a battery pack and make sure to turn it on
2. Plug in the ethernet cable into the Raspberry Pi and connect the other end into your PC 
3. Place the lid back into the helmet and secure it tight, make sure not to accidently unplug any wiring. BE CAREFUL
4. Open TigerVNC
5. Log in using the login: pi pass:123456789
6. Use the code into the TigerVNC programming code
7. Equip the helmet and start walking, you will start getting audio queues.


/**********************************************************************
 *  Describe any serious problems you encountered while working on this project and how you solved/came around the problems.                  
 **********************************************************************/
Problems Encountered and Solutions

Ultrasonic sensors not wiring properly – The sensors were not functioning because they were not receiving enough voltage.
Solution: Added an extra breadboard to ensure proper power distribution.

Voltage instability issues – Some components experienced inconsistent voltage, causing erratic readings.
Solution: Rechecked connections, stabilized the power supply, and redistributed wiring on the breadboard.

Melted wires due to heat buildup – A few wires melted from extended use and high current flow.
Solution: Ordered new wires rated for proper current and replaced the damaged ones.


/**********************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing this project and whether    
 *  you enjoyed doing it.                                             
 **********************************************************************/
 
