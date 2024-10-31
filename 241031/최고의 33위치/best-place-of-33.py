N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)] 

def max_coins(N, arr):
    max_coins = 0
    
    for i in range(N - 2):
        for j in range(N - 2):
            current_coins = 0
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    current_coins += arr[x][y]
            
            max_coins = max(max_coins, current_coins)
    
    return max_coins


print(max_coins(N, arr))