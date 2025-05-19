n, k = map(int, input().split())
arr = [[0 for j in range(n+1)] for i in range(n+1)]
arr[1][1] = 1
for i in range(2, n+1):
	for j in range(1, n+1):
		arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
	
print(arr[n][k])