import os
import subprocess as sp

while True:
    try:
        sp.run(['python.exe', 'program_name_in_directory.py'], shell=True, timeout=15)
    except sp.TimeoutExpired:
        print("Subprocess timeout")
        os._exit(1)
