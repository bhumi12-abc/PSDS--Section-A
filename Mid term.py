

T = int(input("Enter number of test cases: "))

for _ in range(T):
    S = input("Enter string: ").strip()

    freq = {}
    for ch in S:
        freq[ch] = freq.get(ch, 0) + 1

    ans = sum(count // 2 for count in freq.values())
    print(ans)