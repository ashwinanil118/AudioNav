#Project Title: AudioNAV
#GROUP1- Ashwin Anil, Salomon Lara, Jaden Nguyen

import RPi.GPIO as GPIO
import time

# Turn off GPIO warnings and reset all pins to a safe state
GPIO.setwarnings(False)
GPIO.cleanup()

# Use Broadcom (BCM) pin numbering scheme
GPIO.setmode(GPIO.BCM)

# --- Pin assignments for sensors and buzzers ---
TRIG_FRONT = 23
ECHO_FRONT = 24
BUZZER_FRONT = 18

TRIG_BACK = 20
   ECHO_BACK = 21
BUZZER_BACK = 12

# Set TRIG pins as outputs and ECHO pins as inputs
GPIO.setup(TRIG_FRONT, GPIO.OUT)
GPIO.setup(ECHO_FRONT, GPIO.IN)
GPIO.setup(TRIG_BACK, GPIO.OUT)
GPIO.setup(ECHO_BACK, GPIO.IN)

# Set buzzer pins as outputs
GPIO.setup(BUZZER_FRONT, GPIO.OUT)
GPIO.setup(BUZZER_BACK, GPIO.OUT)

def get_distance(TRIG, ECHO):
    """Send an ultrasonic pulse and calculate the distance based on echo time."""
    
    # Trigger a short pulse to start measurement
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Wait for the echo to start and stop
    start = time.time()
    stop = time.time()

    # Detect when the echo pin goes HIGH (sound wave leaving sensor)
    while GPIO.input(ECHO) == 0:
        start = time.time()

    # Detect when the echo pin goes LOW (sound wave returned)
    while GPIO.input(ECHO) == 1:
        stop = time.time()

    # Convert travel time to distance in centimeters
    return (stop - start) * 17150

try:
    while True:
        # Read measured distances from both front and back sensors
        front = get_distance(TRIG_FRONT, ECHO_FRONT)
        back = get_distance(TRIG_BACK, ECHO_BACK)

        # --- FRONT BUZZER FEEDBACK ---
        if front <= 5:
            # Rapid beeps indicate immediate danger or very close object
            for _ in range(3):
                GPIO.output(BUZZER_FRONT, True)
                time.sleep(0.05)
                GPIO.output(BUZZER_FRONT, False)
                time.sleep(0.05)
        elif front <= 100:
            # Slower, spaced beeps indicate caution but not immediate danger
            GPIO.output(BUZZER_FRONT, True)
            time.sleep(0.3)
            GPIO.output(BUZZER_FRONT, False)
            time.sleep(0.3)
        else:
            # No object detected—keep buzzer silent
            GPIO.output(BUZZER_FRONT, False)

        # --- BACK BUZZER FEEDBACK ---
        if back <= 50:
            # Close object behind—rapid warning beeps
            for _ in range(3):
                GPIO.output(BUZZER_BACK, True)
                time.sleep(0.05)
                GPIO.output(BUZZER_BACK, False)
                time.sleep(0.05)
        elif back <= 100:
            # Object detected at a safer distance—slow warning beeps
            GPIO.output(BUZZER_BACK, True)
            time.sleep(0.3)
            GPIO.output(BUZZER_BACK, False)
            time.sleep(0.3)
        else:
            # Clear behind—no sound
            GPIO.output(BUZZER_BACK, False)

        # Brief delay to prevent overly rapid polling
        time.sleep(0.1)

except KeyboardInterrupt:
    # On Ctrl+C, safely reset all GPIO pins before exiting
    GPIO.cleanup()
