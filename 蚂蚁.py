'''
Descripttion: 
version: 
Author: LiQiang
Date: 2020-11-23 17:40:21
LastEditTime: 2020-11-23 19:08:55
'''

before=[[]]*10000
after=[[]]*10000
#方向
dirName=["L","Turning","R"]
order=[0]*10000#输入的第i只蚂蚁是终态中的左数第order[i]只蚂蚁
K=int(input())
for k in range(1,K+1):
    print(f"Case {k}")
    L,T,n=map(int,input().split())
    for i in range(n):
        #P代表位置，C代表朝向
        INPUT=input().split()
        p,c=int(INPUT[0]),INPUT[1]
        #d朝向，-1左，1右
        d=(-1 if c=='L' else 1)
        before[i]=[i,p,d]#i代表输入顺序
        after[i]=[0,p+T*d,d]#这里的id是未知的
    
    before=[x for x in before if x]
    before.sort(key=lambda x: x[1])
    # print(before)

    for i in range(n):
        order[before[i][0]]=i
    #计算终态
    after=[x for x in after if x]
    after.sort(key=lambda x: x[1])
    for i in range(n-1):#修改碰撞中蚂蚁的方向
        if after[i][1]==after[i+1][1]:
            after[i+1][2]=0
            after[i][2]=0
    #输出结果
    print(f"Case {k} :输出")
    for i in range(n):
        a=order[i]
        if(after[a][1]<0) or (after[a][1]>L):
            print("Fell off")
        else:
            print(after[a][1],dirName[after[a][2]+1])
    print("\n")
