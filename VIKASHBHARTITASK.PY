# Create a countdown timer using python
import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    
    print('Time up!')

# Set the timer duration in seconds
duration = 60

countdown_timer(duration)
