def hanoi(n, start, temp, end):
    if n == 1:
        print(f"{start} -> {end}")
        return

    hanoi(n-1, start, end, temp)

    print(f"{start} -> {end}")

    hanoi(n-1, temp, start, end)


t = int(input())

for _ in range(t):
    n = int(input())
    hanoi(n, 'A', 'B', 'C')