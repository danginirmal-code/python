from math import *
import os
import random
from package.maths import addition
from package import maths
import math
print(math.sqrt(20))
import numpy as np
print(np.array([1,2,3,4]))
print(pi)
print(addition(2,3))
print(random.randint(1,10))
print(random.choice(['apple','banana',"cherry"]))
print(os.getcwd())


import csv
with open('example.csv',mode='w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['Nirmal',32])
with open('example.csv',mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

from datetime import datetime,timedelta
now=datetime.now()
print(now)
yestarday=now-timedelta(days=2)
print(yestarday)