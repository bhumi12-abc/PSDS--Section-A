def solve(N, A):
    total = sum(A)

    positive = 0
    negative = 0

    for x in A:
        if x > 0:
            positive += x
        elif x < 0:
            negative += -x

    if total > 0 or 2 * positive > negative:
        return -1

    return -total


# Test cases
T = 2

print(solve(1, [-2]))
print(solve(2, [1, -1]))