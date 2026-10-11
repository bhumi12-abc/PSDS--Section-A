
# Q1. Implement Push and Pop operations on a NumPy array

import numpy as np

arr = np.array([1, 2, 3])

# Push
arr = np.append(arr, 4)
print("After push:", arr)

# Pop
arr = np.delete(arr, -1)
print("After pop:", arr)


# Q2. Implement Queue operations using a NumPy array

import numpy as np

# Queue
queue = np.array([], dtype=int)

# ENQ
for item in [10, 20, 30]:
    queue = np.append(queue, item)
    print("After ENQ", item, ":", queue)

# DEQ
while len(queue) > 0:
    print("Dequeued:", queue[0])
    queue = np.delete(queue, 0)
    print("Queue:", queue)
