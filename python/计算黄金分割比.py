# 计算黄金分割比
i=0
j=1
n=int(input('n='))
for x in range(n):
	k=j
	j+=i
	i=k
	p=i/j
print('%.6f' %p)