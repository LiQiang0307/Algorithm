'''
Descripttion: 
version: 
Author: LiQiang
Date: 2020-11-22 13:00:02
LastEditTime: 2020-11-22 13:48:36
'''
from operator import itemgetter
#定义两个列表，列表J用来存放任务时间，用B来存放布置任务时间
kase=0
while True:
    J=[]
    B=[]
    n=int(input())
    if n==0:
        break
    else:
        for i in range(n):
            b,j=map(int,input().split())
            B.append(b)
            J.append(j)
        #J列表排序后对应原来所引位置
        index=[index for index, value in sorted(enumerate(J),reverse=True, key=itemgetter(1))]
        #对J列表进行排序
        J.sort(reverse=True)
        #按照J原有所引，重新改变B中元素的位置，目的是让任务执行时间J与任务布置时间B保持原位置对应
        c=[]
        for j in index:
            c.append(B[j])
        # print(J,c)
        s,ans=0,0
        for i in range(n):
            s+=c[i] #当前任务的开始执行时间
            ans=max(ans,s+J[i])#更新任务执行完毕时的最晚时间
        kase=kase+1
        print("Case {}:{}".format(kase,ans))
