# module / library.py

import math
import random
import os
import datetime
# math.sqrt(16)  # This will return 4.0

math.sqrt(16)
print(math.sqrt(16))  

random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# os exists() checks if a path exists
path = "myfile.txt"
if os.path.exists(path):
    print(f"This {path} exists.")

# datetime.datetime.now()  

today = datetime.datetime.now()
print(f"Today's date and time: {today}")