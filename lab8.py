n, k = map(int, input("Enter N and K: ").split())

arr = list(map(int, input("Enter array: ").split()))

window_sum = sum(arr[:k])

max_sum = window_sum

for i in range(k, n):
    window_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)

print("Maximum Sum:", max_sum)