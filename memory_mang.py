import sys
a=[]
print(sys.getrefcount(a))
b=a
print(sys.getrefcount(a))

import gc
gc.enable()
gc.disable()
print(gc.collect()) 