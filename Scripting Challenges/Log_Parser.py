# Objective: Write a script that reads a log file and identifies failed login attempts.

import subprocess
import os

#file = input("name of the log file: ")
path = input("path of the log file: *remember to use the full path* ")

# Accessing directory
directory = os.system("cd" + path)
print (directory)

# if subprocess.Popen == False:
#     print("Error accessing directory")
# else:
#     # read the log file
#     with open(file, 'r') as log:
#         for line in log:
#             if "Failed password":
#                 print(line.strip)