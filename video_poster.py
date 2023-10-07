from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from undetected import iniciar_webdriver
import time
import re
import json
import random
import os
from decouple import Config

#----- Set some important variables ------------------------------------------------------------------------------------------------------------

user_email = Config('EMAIL')
user_password = Config('PASSWORD')
time_posts = [15, 17, 19, 21, 23]

#----- Count the files on the videos folder ----------------------------------------------------------------------------------------------------

def FilesInFolder(folder: str):
    '''FilesInFolder count the files in the 'videos' folder
    Args:
        folder (str): name of the folder
    Returns:
        [int]: the amount of videos on the folder
    '''

    try:
        files = os.listdir(folder)                                                      # Get the list of files in the folder
        files = [file for file in files if os.path.isfile(os.path.join(folder, file))]  # Filter the list to get only files (not directories)
        file_count = len(files)                                                         # Count how many files there are
        return file_count
    except FileNotFoundError:
        return 0                                                                        # Folder does not exist
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return -1                                                                       # Unknown error

folder = "videos"                                                                       # Path to the folder you want to count files in
file_count = FilesInFolder(folder)                                                      # Call the function to count files in the folder
print(file_count)                                                                       # Print the amount

#----- Select randomly the videos to post ------------------------------------------------------------------------------------------------------

def RandomNumber(minimum: int, maximum: int):
    '''RandomNumber generates a random number between two numbers
    Args:
        minimum (int): the first number of the range
        maximum (int): the second number of the range
    Returns:
        [int]: the random int generated
    '''

    random_number = random.randint(minimum, maximum)                                    # Generates the random number
    return random_number                                                                # Return the random number

#----- Login on youtube ------------------------------------------------------------------------------------------------------------------------

def YouTube():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://youtube.com")
    time.sleep(2)

    button = driver.find_element(By.CLASS_NAME, "yt-spec-button-shape-next")            # Find the login button by its class name
    button.click()                                                                      # Click the button

    email_field = driver.find_element_by_id("identifierId")                             # Find the input field by its ID
    email_field.send_keys(user_email)                                                   # Set the value of the input field to user_email

    email_button = driver.find_element_by_xpath("//button[contains(., 'Siguiente')]")   # Find the button by its text content: 'Siguiente'
    email_button.click()                                                                # Click the button

    password_input = driver.find_element_by_name("Passwd")                              # Find the password input
    password_input.send_keys(user_password)                                             # Send the user_password to the input field

    password_button = driver.find_element_by_xpath("//button[contains(., 'Siguiente')]")# Find the button by its text content: 'Siguiente'
    password_button.click()                                                             # Click the button

    button = driver.find_element_by_xpath("//button[contains(., 'Ahora no')]")          # Find the button by its text content
    button.click()                                                                      # Click the button

    button = driver.find_element_by_class_name("style-scope yt-icon-button")            # Find the button by its class name
    button.click()                                                                      # Click the button

    user_input = input("Write 1... ")                                                   # Get user input
    if input_value == 1:                                                                # Check if the input value is equal to 1
        driver.quit()                                                                   # Quit the driver
        print("Driver has been quit.")                                                  # Print the driver state

YouTube()

#----- Start a for loop to post each video -----------------------------------------------------------------------------------------------------
