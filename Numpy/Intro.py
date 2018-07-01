# Import numpy as np
import numpy as np

np_height = np.array([1, 2, 3, 4, 5, 6])

np_baseball = np.array([[1, 2, 3, 4, 5, 6],
                        [1, 2, 3, 4, 5, 6]])

# For loop over np_height
for x in np_height:
    print(str(x) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(str(x))
