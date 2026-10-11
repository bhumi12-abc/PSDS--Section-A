def digit_sum(num):
    return sum(map(int, str(num)))


def solve():
    N = 4
    nums = [51, 71, 17, 42]

    freq = {}

    for num in nums:
        s = digit_sum(num)

        if s not in freq:
            freq[s] = 0

        freq[s] += 1

    ans = 0

    for count in freq.values():
        ans += count * (count - 1) // 2

    print(ans)


solve()