import time
import sys

def type_writer(text, delay=0.0005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    

