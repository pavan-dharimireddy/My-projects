
What is an Ultrasonic Sensor? 

As the name says, Ultrasonic sensors HC-SR04 measure the distance by using ultrasonic waves. The sensor emits an ultrasonic wave 40,000 Hz (40kHz) and receives the wave reflected back from the object. The Sensor measures the distance to the object by measuring the travelling time and speed of the sound. 


<img src="https://github.com/pavan-dharimireddy/My-projects/blob/5dfaf68f52dba348624d5e332cc9e3c8bb39dd64/Arduino%20Projects/Distance_measuring_using_ultrasonic_sensor/ultra_sonic_sensor/ultra_sonic_sensor.jpg" alt="Ultrasonic sensors HC-SR04" title="Ultrasonic sensors HC-SR04">

The pin configuration of HC-SR04 is:

<p> VCC -- needs to be connected to VCC (5v or VDD) </p>
<p> GND -- needs to be connected to GND (0v or VSS) </p>
<p> TRIG -- this pin receives the signal or pulse from Arduino and emits the signal </p>
<p> ECHO -- this pin sends the signal or pulse to Arduino and Arduino measures the duration of signal to calculate distance. </p>

We can clearly observe these pins in above ultrasonic sensors HC-SR04 diagram 
<br>

===========================================================================================
<br>

HOW IT WORKS? 

<p>1. Arduino (Micro-Controller) generates a signal or pulse on the TRIG pin. </p>
<p>2. Taking the signal from TRIG pin, the ultrasonic sensor emits the ultrasonic waves. </p>
<p>3. The waves get reflected back if they encounter an obstacle on their way.</p>
<p>4. The ultrasonic sensor, detects the reflected ultrasonic wave and measures the traveled time of the wave.</p>
<p>5. Then ultrasonic sensor generates a signal or pulse to the ECHO pin.</p>
<p>6. The duration of the pulse is equal to the traveled time of the ultrasonic wave.</p>
<p>7. Arduino measures the pulse duration in the ECHO pin, and then calculate the distance between the sensor and obstacle. </p>

==========================================================================================
<br>

DISTANCE CALCULATION 

We know,

Pulse duration = the traveled time of the ultrasonic wave (µs)

speed of sound = 340m/s = 0.034cm/µs

Traveled distance of the ultrasonic wave (cm) = pulse duration * 0.034

Distance between sensor and obstacle (cm) = Traveled distance / 2 = (0.034 * pulse duration)/2  = 0.017 * pulse duration


======================================================================================
<br>

WIRING DIAGRAM

<img src = "https://github.com/pavan-dharimireddy/My-projects/blob/5dfaf68f52dba348624d5e332cc9e3c8bb39dd64/Arduino%20Projects/Distance_measuring_using_ultrasonic_sensor/ultra_sonic_sensor/ultra%20sonic%20sensor.jpg" alt = "wiring diagram" title = " wiring diagram of ultra-sonic sensor">


=======================================================================================
<br>
OUTPUT

<img src = "https://github.com/pavan-dharimireddy/My-projects/blob/5dfaf68f52dba348624d5e332cc9e3c8bb39dd64/Arduino%20Projects/Distance_measuring_using_ultrasonic_sensor/ultra_sonic_sensor/output.png" alt = "output" title = "output" >

========================================================================================

<br>

img 1  and img 2 are the images of the project

