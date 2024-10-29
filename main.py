import time


def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        seconds -= 1

    print("Time's up!")


time_input = int(input('Please insert time in seconds: '))
countdown(time_input)



