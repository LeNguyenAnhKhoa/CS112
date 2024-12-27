def solve():
    n, m = map(int, input().split())
    x = [0] + list(map(int, input().split()))
    y = [0] + list(map(int, input().split()))
    
    # Tối ưu phép tính prefix sum 2D
    a = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        curr_sum = 0
        row = list(map(int, input().split()))
        for j in range(1, m + 1):
            curr_sum += row[j-1]
            a[i][j] = curr_sum + a[i-1][j]
    
    res = 0
    # Cache các giá trị tính toán thường xuyên
    for x1 in range(1, n + 1):
        for x2 in range(x1, n + 1):
            d = x[x2] - x[x1]
            Min = float('inf')
            # Tính trước phần không đổi trong vòng lặp
            prev_rows = a[x1-1]
            curr_rows = a[x2]
            
            val = 0
            for j in range(1, m + 1):
                Min = min(Min, val - d * y[j])
                # Tối ưu phép tính val bằng cách sử dụng giá trị cache
                val = curr_rows[j] - curr_rows[0] - prev_rows[j] + prev_rows[0]
                curr_val = val - d * y[j] - Min
                if curr_val > res:
                    res = curr_val
    
    return res

print(solve())
