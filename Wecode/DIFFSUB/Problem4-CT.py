import sys

def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    K = int(data[1])
    a = [0] + list(map(int, data[2:]))

    dp = [0] * (n + 1)
    ans = 0

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[i] += (a[j] != a[j - i + 1])
            if j - i + 1 > K:
                dp[i] -= (a[j - K] != a[j - i + 1 - K])
            ans = max(ans, dp[i])

    print(ans)

if __name__ == "__main__":
    main()
