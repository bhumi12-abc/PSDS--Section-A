import heapq

# MIN HEAP
min_heap = []

heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 5)

print("Min Heap:", min_heap)
print("Minimum element:", heapq.heappop(min_heap))

# MAX HEAP
max_heap = []

for x in [30, 10, 20, 5]:
    heapq.heappush(max_heap, -x)

print("Max Heap:", [-x for x in max_heap])
print("Maximum element:", -heapq.heappop(max_heap))

# PRIORITY QUEUE
pq = []

heapq.heappush(pq, (2, "Medium"))
heapq.heappush(pq, (1, "High"))
heapq.heappush(pq, (3, "Low"))

print("\nPriority Queue:")
while pq:
    priority, task = heapq.heappop(pq)
    print(task)

# HEAP SORT
arr = [40, 10, 30, 50, 20]

heapq.heapify(arr)

sorted_arr = []
while arr:
    sorted_arr.append(heapq.heappop(arr))

print("\nOriginal Array: [40, 10, 30, 50, 20]")
print("Heap Sort:", sorted_arr)