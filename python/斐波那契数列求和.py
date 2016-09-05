# 斐波那契数列求和
n=int(input('n='))
i=0
j=1
sum=0
# 循环交换赋值
for x in range(n):
	i,j = j,i+j
	sum+=i
print('前%d项和是:%d' %(n,sum))




#递归方式求出通项再求和
def f(n):
	if n==1 or n==2:
		return 1
	return f(n-1)+f(n-2)
def s(n):
	s=0
	while n>0:
		s=s+f(n)
		n=n-1
	return s
print(s(int(input('n='))))



#调用reduce()
def f(n):
	if n==1 or n==2:
		return 1
	return f(n-1)+f(n-2)
def s(m,n):
	return m+n
def S(n):
	from functools import reduce
	return reduce(s,[f(i) for i in range(1,n+1)])
print(S(int(input('n='))))

#调用sum()
def f(n):
	if n==1 or n==2:
		return 1
	return f(n-1)+f(n-2)
print(sum([f(i) for i in range(1,int(input('n='))+1)]))