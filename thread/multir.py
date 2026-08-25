import multiprocessing
import math
import sys
import time
sys.set_int_max_str_digits(100000)

def computer_factorial(number):
    print("COmputing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial  of {number} is {result}")

    return result
if __name__=="__main__":
    numbers=[5000,6000,7000,8000]
    start_time=time.time()
    with multiprocessing.Pool() as pool:
        result=pool.map(computer_factorial,numbers)
    end_time=time.time()-start_time