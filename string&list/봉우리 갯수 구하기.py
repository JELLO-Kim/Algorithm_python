import sys
# 내가 푼 코드
n=int(input())
res=0
t=[]
for k in range(n+2):
    if k==0:
        t.append([0]*(n+2))
    elif k==(n+1):
        t.append([0]*(n+2))
    else:
        t.append([0]+list(map(int, input().split()))+[0])

for i in range(1, n+1):
    for j in range(1, n+1):
        if (t[i-1][j]<t[i][j]) and (t[i+1][j]<t[i][j]) and  (t[i][j-1]<t[i][j]) and  (t[i][j+1]<t[i][j]):
            res+=1
print(res)

# 소스 코드 (4방향 탐색법 알아두기!!)
import sys
#sys.stdin = open("input.txt", 'r')
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)