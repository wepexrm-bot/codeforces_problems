import sys 
input = sys.stdin.readline

MOD = 10**9+7
MAXN = 10**5 + 1

def flowers():
    t , k = map(int, input().split())

    #build dp array
    dp = [0] * MAXN
    dp[0] = 1

    for n in range(1, MAXN):
        dp[n]= dp[n-1]
        if n >= k:
            dp[n] = (dp[n]+dp[n-k]) % MOD
    
    prefix = [0]*MAXN
    prefix[0] = dp[0]
    for n in range(1, MAXN):
        prefix[n]=(prefix[n-1]+dp[n]) % MOD
    
    #Queries

    for _ in range(t):
        a,b = map(int, input().split())
        ans = (prefix[b] - prefix[a-1] + MOD) % MOD
        print(ans)
        
flowers()
