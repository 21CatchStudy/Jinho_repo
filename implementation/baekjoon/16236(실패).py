"""
https://www.acmicpc.net/problem/16236

"""
import sys
input =  sys.stdin.readline

N = int(input())
G = [list(map(int,input().split())) for _ in range(N)]

fish_size = 2
fish_cnt = 0

X = [-1,1,0,0]
Y = [0,0,-1,1]

def can_move(i_x,i_y,fx,fy):
    global fish_size
    global fish_cnt
    visited = [[False for _ in range(N)] for _ in range(N)]
    from collections import deque

    Q = deque()
    Q.append((i_x,i_y,0))
    visited[i_x][i_y] = True
    cnt= 0 
    while Q:
        x,y,cnt = Q.popleft()
        if x == fx and y== fy:
            G[i_x][i_y] = 0
            G[fx][fy] = 9
            fish_cnt+=1
            if fish_cnt == fish_size:
                fish_size+=1
                fish_cnt= 0
            return cnt
        for dx,dy in zip(X,Y):
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N:
                if not visited[nx][ny] and G[nx][ny] <= fish_size:
                    visited[nx][ny] = True
                    Q.append((nx,ny,cnt+1))
    return cnt


def check(x,y,size):
    global fish_size
    global answer

    for i in range(x-size,x+size+1):
        for j in range(y-size,y+size+1):
            if 0<=i < N and 0<=j<N:
                if 0< G[i][j] < fish_size:
                    cnt = can_move(x,y,i,j)
                    answer+=cnt
                    if cnt:
                        solve(i,j)
                        return cnt
    return 0

fish_x,fish_y = 0,0
for i in range(N):
    for j in range(N):
        if G[i][j] == 9:
            fish_x,fish_y = i,j
answer = 0
def solve(fish_x,fish_y):
    global answer
    max_size = max(fish_x,N-fish_x,fish_y,N-fish_y)
    for size in range(1,max_size+1):
        check(fish_x,fish_y,size)
         
            # fish_x,fish_y = feed_x,feed_y
solve(fish_x,fish_y)
print("답",answer)
for row in G:
    print(row)



