'''
Descripttion: 
version: 
Author: LiQiang
Date: 2020-11-22 20:38:13
LastEditTime: 2020-11-22 20:59:23
'''
import math
#n表示原始的雕塑数量；m表示新加入的雕塑数量
n,m=map(int,input().split())
ans=0
for i in range(1,n):
    pos=i/n*(n+m) #计算每个需要移动的雕塑的坐标
    #坐标为pos的雕塑移动到的目标位置是floor(pos+0.5) ,就是pos四舍五入的结果
    ans+=math.fabs(pos-math.floor(pos+0.5))/(n+m) #累加移动距离
print(round(ans*10000,4))

