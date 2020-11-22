'''
Descripttion: 
version: 
Author: LiQiang
Date: 2020-11-21 22:03:01
LastEditTime: 2020-11-22 13:25:23
'''

#输入数据list(map(int, input().split()))
while True:
    #定义两个列表，分别用 A,B 来存放骑士和恶龙的头
    A=[]
    B=[]
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    # print(n,m)
    for i in range(n):
        B.append(int(input()))
    for j in range(m):
        A.append(int(input()))
    #排序
    A.sort()
    B.sort()
    # print(A,B)
    #当前需要砍掉头的编号cur
    cur=0
    #当前总费用
    cost=0
    for i in range(m):
        if(A[i]>=B[cur]):
            cost+=A[i]#雇佣该骑士
            cur=cur+1
            # print(cur)
            if(cur==n):
                break  #如果头已经砍完，及时退出循环
    print("Loowater is doomed!") if cur<n else print(cost)
