import time

print(time.time())  # current time in seconds

def calcProd():
    # calculate the product of the first 100,000 numbers
    product = 1
    for i in range(1, 10):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

# The time.sleep() function
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)
    
# rounding numbers
now = time.time()
print(now)
print(round(now, 2))
print(round(now, 4))
print(round(now))