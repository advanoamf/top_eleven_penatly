# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 01:31:36 2024

@author: noam1
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:33:44 2024

@author: noam1
"""

import pyautogui
import pyautogui
import time
import subprocess
from PIL import Image
import io

# # Define the RGB color you want to find (Example: Green = (36, 227, 12))
# TARGET_COLOR = (15, 180, 2)  # Replace with the RGB value you're looking for

# def find_color_on_screen(target_color):
#     # Capture the screen image
#     screenshot = pyautogui.screenshot()

#     # Convert screenshot to RGB
#     screenshot_rgb = screenshot.convert('RGB')

#     # Get screen width and height
#     width, height = screenshot.size

#     # Loop through each pixel and check if the color matches
#     for x in range(0, width, 5):  # Check every 5th pixel for faster search
#         for y in range(0, height, 5):  # Check every 5th pixel for faster search
#             r, g, b = screenshot_rgb.getpixel((x, y))
#             if (g >= 180) and (r <20) and (b < 20):
#                 adb_command = f"adb -s RFCX905KBBB shell input swipe {x} {y} {x} {y} 1450"
#                 result = subprocess.run(adb_command, shell=True, check=True, capture_output=True)
#                 print(f"Color found at ({x}, {y})")
#                 return (x, y)  # Return the coordinates of the first match

#     # If no match is found
#     return None

# def tap_on_phone(x, y):
#     # Construct the ADB command for tapping at (x, y)
#     adb_command = f"adb -s RFCX905KBBB shell input swipe {x} {y} {x} {y} 1450"
#     try:
#         # Run the ADB command
#         result = subprocess.run(adb_command, shell=True, check=True, capture_output=True)
#        # result = subprocess.run(adb_command)
#         print(f"Tapped at ({x}, {y}) on the phone.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e}")

# Main loop to repeatedly check for the color
while True:
    image_command = f"adb shell screencap -p"
    result = subprocess.run(image_command, stdout=subprocess.PIPE)
    image_data = result.stdout
    image = Image.open(io.BytesIO(image_data))
    screenshot = image 
   # screenshot = pyautogui.screenshot()
    screenshot_rgb = screenshot.convert('RGB')
    width, height = screenshot.size
    for x in range(0, width, 5):  # Check every 5th pixel for faster search
        for y in range(0, height, 5):  # Check every 5th pixel for faster search
            r, g, b = screenshot_rgb.getpixel((x, y))
            if ((g >= 170) and (g<195)) and (r <20) and (b < 20 ):
                adb_command = f"adb -s RFCX905KBBB shell input swipe {x} {y} {x} {y} 1365"
                result = subprocess.run(adb_command, shell=True, check=True, capture_output=True)
                print(f"Color found at ({x}, {y}) green = {g} blue = {b} red = {r}")
            else:
                print("Color not found. Checking again...")
    time.sleep(0.001)



    
    # color_location = find_color_on_screen(TARGET_COLOR)
    # if color_location:
    #     print(f"Found the color at {color_location}")
    #     # Send a tap command to the phone at the same coordinates
    #     tap_on_phone(color_location[0], color_location[1])
    # else:
    #     print("Color not found. Checking again...")

    # # Add a short delay to reduce CPU usage
    # time.sleep(0.01)
