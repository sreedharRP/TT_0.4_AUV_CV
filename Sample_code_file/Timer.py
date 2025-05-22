import time

#b = 0

def delay(a):
    time.sleep(a)
    return a

def Counter():
    int b = 0
    b += 1
    return b

def Steps():
    delay(1)
    result = Counter()
    print(result)


while True:
    Steps()

