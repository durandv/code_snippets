#import antigravity
import sys
#sys.path.append('/home/vvv')

#import my_module as mm
from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

print(sys.path)