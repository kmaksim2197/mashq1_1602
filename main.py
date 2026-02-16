n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
rotated = list(zip(*matrix[::-1]))
for row in rotated:
    print(*row)
