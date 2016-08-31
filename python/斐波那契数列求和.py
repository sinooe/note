# 斐波那契数列求和
n=int(input('n='))
i=0
j=1
sum=0
for x in range(n):
	y=j
	j=i+j
	i=y
	sum+=i
print('前%d项和是:%d' %(n,sum))
