import tkinter as tk
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
red= 18
yellow = 23
blue= 24

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

redpwm = GPIO.PWM(red, 1000)
yellowpwm = GPIO.PWM(yellow, 1000)
bluepwm = GPIO.PWM(blue, 1000)

redpwm.start(0)
yellowpwm.start(0)
bluepwm.start(0)


def update_intensities(event):
    redintensity = int(redslider.get())
    yellowintensity = int(yellowslider.get())
    blueintensity = int(blueslider.get())

    redpwm.ChangeDutyCycle(redintensity)
    yellowpwm.ChangeDutyCycle(yellowintensity)
    bluepwm.ChangeDutyCycle(blueintensity)

root = tk.Tk()
root.title("LED Intensity Control")
root.geometry("400x300")

# Red LED intensity slider
redslider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_intensities, label="Red")
redslider.pack(pady=10)

# Yellow LED intensity slider
yellowslider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_intensities, label="Yellow")
yellowslider.pack(pady=10)

# Blue LED intensity slider
blueslider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_intensities, label="Blue")
blueslider.pack(pady=10)

# Exit button
exitbutton = tk.Button(root, text="Exit", command=root.quit)
exitbutton.pack(pady=20)

root.mainloop()

GPIO.cleanup()
