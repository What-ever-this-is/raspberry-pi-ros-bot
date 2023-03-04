import rclpy as ros
from sensor_msgs.msg import LaserScan
import RPi.GPIO as gpio

g_node = None

class Drivetrain:
    def __init__(self,ena,enb,in1,in2,in3,in4):
        self.aSpeed = None
        self.bSpeed = None
        self.ena = ena
        self.enb = enb
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        #Setup pins
        gpio.setmode(gpio.BOARD)
        gpio.setup(ena,gpio.OUT)
        gpio.setup(enb,gpio.OUT)
        gpio.setup(in1,gpio.OUT)
        gpio.setup(in2,gpio.OUT)
        gpio.setup(in3,gpio.OUT)
        gpio.setup(in4,gpio.OUT)
        #Setup PWM values
        aSpeed = gpio.PWM(ena,1000)
        bSpeed = gpio.PWM(enb,1000)
        gpio.output(in1,gpio.LOW)
        gpio.output(in2,gpio.LOW)
        gpio.output(in3,gpio.LOW)
        gpio.output(in4,gpio.LOW)
        #FORWARD: odd = HIGH even = low
        aSpeed.start(0)
        bSpeed.start(0)

    def setSpeed(self,motor,speed):
        if(motor == 1):
            self.aSpeed.changeDutyCycle(speed)
        elif(motor == 2):
            self.bSpeed.changeDutyCycle(speed)

    def setDirection(self,motor,direction):
        if(motor == 1):
            if(direction=="forward"):
                gpio.output(self.in1,gpio.HIGH)
                gpio.output(self.in2,gpio.LOW)
            elif(direction=="backward"):
                gpio.output(self.in1,gpio.LOW)
                gpio.output(self.in2,gpio.HIGH)
        elif(motor == 2):
            if(direction=="forward"):
                gpio.output(self.in3,gpio.HIGH)
                gpio.output(self.in4,gpio.LOW)
            elif(direction=="backward"):
                gpio.output(self.in3,gpio.LOW)
                gpio.output(self.in4,gpio.HIGH)
    def stop(self,motor):
        if(motor==1):
            gpio.output(self.in1,gpio.LOW)
            gpio.output(self.in2,gpio.LOW)
        elif(motor==2):
            gpio.output(self.in3,gpio.LOW)
            gpio.output(self.in4,gpio.LOW)
    


def main(args=None):
    global g_node
    print("WOW")
    motors = Drivetrain(11,12,13,15,16,18)
    motors.setDirection(1,"forward")
    motors.setDirection(2,"forward")
    motors.setSpeed(1,100)
    motors.setSpeed(2,100)



if __name__ == '__main__':
    main()
    