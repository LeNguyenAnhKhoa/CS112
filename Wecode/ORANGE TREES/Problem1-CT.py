def check_avg(n, k, arr, p):
    prefix_sum = [0] * (n + 1)
    min_prefix = float('inf')
    j = 0
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
        while j < i and prefix_sum[i] - prefix_sum[j] >= k:
            min_prefix = min(min_prefix, prefix_sum[j] - j*p)
            j += 1
        if prefix_sum[i] - p*i >= min_prefix:
            return True
    return False

def max_average_subarray(n, k, arr):
    left, right = min(arr), max(arr)
    
    while left <= right:
        mid = (left + right) // 2
        if check_avg(n, k, arr, mid):
            res = mid
            left = mid + 1 
        else:
            right = mid - 1
    return res

# Nhập vào số nguyên N và K
n, k = map(int, input().split())

# Nhập vào dãy số
arr = list(map(int, input().split()))

# Gọi hàm và in kết quả
result = max_average_subarray(n, k, arr)
print(result)
