from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from undetected import iniciar_webdriver
import time
import re
import json
import random
from decouple import config

#----- Set some important variables ------------------------------------------------------------------------------------------------------------

user_email = config('EMAIL')
user_password = config('PASSWORD')
time_posts = [15, 17, 19, 21, 23]

#----- Count the files on the videos folder ----------------------------------------------------------------------------------------------------

#----- Select randomly the videos to post ------------------------------------------------------------------------------------------------------

#----- Login on youtube ------------------------------------------------------------------------------------------------------------------------

#----- Start a for loop to post each video -----------------------------------------------------------------------------------------------------
