import time

start = time.time()
t_Bool = False

def timer():
    end_time = time.time()
    difference = end_time - start
    value = int(difference)
    return value

    

while True:
    value = timer()
    print(value)

    
 
      

     
