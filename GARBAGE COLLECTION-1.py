import sys
a=[1,2,3]
ref_count=sys.getrefcount(a)
print("Reference Count:", ref_count)

import sys
a=[]
b=a
c=b
print("Reference count is:", sys.getrefcount(a))

import gc
collected=gc.collect()
print(f"Garbage Collector collected {collected} objects")

import gc
gc.enable()
gc.disable()
l1=[1,2,3]
d1={'a':1, 'b':2}
s1="Garbage collection"
del l1
del d1
del s1
gc.set_threshold(100, 5, 2)
print("Current Threshold;", gc.get_threshold())
collected= gc.collect()
print(f"Garbage Collector collected {collected} objects")
