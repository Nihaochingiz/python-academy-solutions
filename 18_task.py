def transpose_matrix(matrix):
    pass

n, m = map(int, input().strip().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

result = transpose_matrix(matrix)

for row in result:
    print(' '.join(map(str, row)))