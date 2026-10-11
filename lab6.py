arr = [5, 6, -3, 8, 1, 9, 2]

print("Triplets with sum 0:")

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] == 0:
                print(arr[i], arr[j], arr[k])
                
#Part 2
n = int(input("Enter number of terms: "))

a = 1
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
#Part-3
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

tower_of_hanoi(n, 'A', 'B', 'C')  