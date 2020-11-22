'''
Descripttion: 
version: 
Author: LiQiang
Date: 2020-11-22 15:56:52
LastEditTime: 2020-11-22 16:25:08
'''
#初始化金币总数量
total=0
#每个人拥有的金币数存到列表A中
A=[0]
#输入人数n
n=int(input())
for i in range(n):
    a=int(input())
    total+=a
    A.append(a)
#每人最终拥有金币数M
M=total//n
C=[0]*1000000
for i in range(1,n):
    C[i]=C[i-1]+A[i]-M
#排序
C.sort()
#计算x1
x1=C[n//2]
ans=0
for i in range(n):
    ans+=abs(x1-C[i])#把x1代入，计算转手的金币总数
print("转手的金币总数为:{}".format(ans))







