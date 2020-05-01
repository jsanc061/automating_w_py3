import time

# Display program instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. ' + 
      'Press Ctrl-C to quit.')
input()                 # press Enter to begin
print('Started stopwatch')
startTime = time.time() # get first lap's start time 
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying
    print('\n\nDone')