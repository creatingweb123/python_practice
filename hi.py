# 16926

import sys
N,M,R = map(int, sys.stdin.readline().rstrip().split())

array = [ 0 for j in range(N)]
check_box = [[False for i in range(M)] for j in range(N)]
for i in range(N):
    array[i] = list(map(int, sys.stdin.readline().rstrip().split()))

x = 0
y = 0

def change(sx, sy, value):

    return sx, sy, value

while not check_box[x+1][y+1]:
    s_x = 0 
    s_y = 0
    start_value = array[s_x][s_y]
    while not check_box[x][y]:
        # 시작점
        change(sx, sy)
        sx = s_x+1 
        sy = s_y
        next_value = array[sx][sy]
        array[sx][sy] = start_value




        
    