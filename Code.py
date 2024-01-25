import RPi.GPIO as GPIO # GPIO control library
import Adafruit_DHT     # library for temperature and humidity sensor from ADAfruit
import time             # library for time functions
from I2C_driver import lcd  # Import the lcd class

# Define GPIO pins
SERVO_PIN = 17     # GPIO pin for the servo motor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4        # GPIO pin for the DHT sensor
MOISTURE_SENSOR_PIN = 18    # GPIO pin for the soil moisture sensor
RED_LED_PIN = 22        # GPIO pin for the red LED
GREEN_LED_PIN = 23       # GPIO pin for the green LED
FAN_PIN = 24             # GPIO pin for the fan
BUZZER_IO_PIN = 25  # GPIO pin for the buzzer 

# Disable GPIO warnings
GPIO.setwarnings(False)

# Setup for servo
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(5)  # Startint the servo in the closed position

# Setup for DHT22(temperature and humidity) sensor
def read_temperature_and_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

# Setup for moisture sensor
def setup_moisture_sensor():
    GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)

def read_moisture():
    return GPIO.input(MOISTURE_SENSOR_PIN)

# Setup for LEDs
GPIO.setup(RED_LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT, initial=GPIO.LOW)

# Setup for fan
def setup_fan():
    GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)

def turn_on_fan():
    GPIO.output(FAN_PIN, GPIO.HIGH)

def turn_off_fan():
    GPIO.output(FAN_PIN, GPIO.LOW)

# Setup for buzzer
def setup_buzzer():
    global buzzer_pwm
    GPIO.setup(BUZZER_IO_PIN, GPIO.OUT, initial=GPIO.LOW)
    buzzer_pwm = GPIO.PWM(BUZZER_IO_PIN, 1000)  # Create a PWM instance with a frequency of 1000 Hz
    buzzer_pwm.start(0)  # Start with 0% duty cycle (no sound)

def turn_on_buzzer():
    buzzer_pwm.ChangeDutyCycle(50)  # 50% duty cycle (generating sound)
    time.sleep(2)  # Sound for 2 seconds
    buzzer_pwm.ChangeDutyCycle(0)  # Stop sound
    time.sleep(5)  # Pause for 5 seconds

def turn_off_buzzer():
    buzzer_pwm.ChangeDutyCycle(0)  # 0% duty cycle (no sound)

# Track the current servo state
servo_opened = False

def open_servo():
    global servo_opened
    if not servo_opened:
        pwm.ChangeDutyCycle(10)  # Open position
        time.sleep(1)
        servo_opened = True

def close_servo():
    global servo_opened
    if servo_opened:
        pwm.ChangeDutyCycle(5)  # Closed position
        time.sleep(1)
        servo_opened = False

# Initialize the LCD
my_lcd = lcd()

# Set up the moisture sensor, fan, servo, and buzzer
setup_moisture_sensor()
setup_fan()
setup_buzzer()

try:
    while True:
        humidity, temperature = read_temperature_and_humidity()  # fetch the temperature and humidity readings from the sensor
        moisture_level = read_moisture()                         #fetch the moisture reading from the sensor

        if humidity is not None and temperature is not None:
            # Prepare the data to be displayed
            temp_humid_str = f"T:{temperature:.1f}C H:{humidity:.1f}%"
            moisture_str = f"Moisture: {'Wet' if moisture_level == 0 else 'Dry'}"

            # Display the data on the LCD
            my_lcd.lcd_display_string(temp_humid_str, 1)  # Display on line 1
            my_lcd.lcd_display_string(moisture_str, 2)    # Display on line 2

            # Print the data to the console
            print(temp_humid_str + " " + moisture_str)

            # Control the LEDs based on the moisture level
            if moisture_level == 0:
                GPIO.output(GREEN_LED_PIN, GPIO.LOW)  # Turn off the green LED
                GPIO.output(RED_LED_PIN, GPIO.HIGH)  # Turn on the red LED for wet
            else:
                GPIO.output(RED_LED_PIN, GPIO.LOW)  # Turn off the red LED
                GPIO.output(GREEN_LED_PIN, GPIO.HIGH)  # Turn on the green LED for dry

            # Control the fan based on temperature and humidity
            if temperature >= 25 or humidity > 55:
                turn_on_fan()
            else:
                turn_off_fan() 

            # Control the buzzer based on certain conditions  
            if moisture_level == 1:  # 1 = dry
                turn_on_buzzer()  
            else:
                turn_off_buzzer()   # turn off the buzzer 

            # Open or close the servo based on conditions
            if temperature > 25:
                open_servo() # open the window
            else:
                close_servo() # close the window

        else:
            print("Failed to retrieve data from sensors")  
            my_lcd.lcd_display_string("Sensor error!", 1)
            my_lcd.lcd_display_string("", 2)  # Clear the second line

        time.sleep(2)  # Wait for 2 seconds before reading again

except KeyboardInterrupt:
    print("Exiting the program...")
    close_servo()  # Close the servo before exiting
    turn_off_fan()  # Turn off the fan before exiting
    turn_off_buzzer()  # Turn off the buzzer before exiting
    pwm.stop()
    GPIO.cleanup()
    my_lcd.lcd_clear()  # Clear the LCD before exiting

# Clean up GPIO and LCD at the end of the program
GPIO.cleanup()

