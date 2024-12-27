from heapq import heappush, heappop

# Input
x, y, z = map(int, input().split())
a = [(1000000000, -1000000000)]  # 1-based indexing
sum_val = 0

# Read array
for i in range(x + y + z):
    k, fi, se = map(int, input().split())
    sum_val += k
    a.append((fi - k, se - k))

# Sort by difference of first and second values
a.sort(key=lambda x: (x[0] - x[1]), reverse=True)

# Calculate prefix sums
pre = [0] * (x + y + z + 1)
res = 0
pq = []  # min heap for Python
for i in range(1, x + y + z + 1):
    if i <= y:
        heappush(pq, a[i][0])
        res += a[i][0]
    elif pq[0] < a[i][0]:
        res += a[i][0] - pq[0]
        heappop(pq)
        heappush(pq, a[i][0])
    pre[i] = res

# Calculate suffix sums
pq = []  # Clear priority queue
suf = [0] * (x + y + z + 2)
res = 0

for i in range(x + y + z, 0, -1):
    if i > x + y:
        heappush(pq, a[i][1])
        res += a[i][1]
    elif pq[0] < a[i][1]:
        res += a[i][1] - pq[0]
        heappop(pq)
        heappush(pq, a[i][1])
    suf[i] = res

# Find maximum result
res = float('-inf')
for i in range(y, x + y + 1):
    res = max(res, pre[i] + suf[i + 1])

print(res + sum_val)
