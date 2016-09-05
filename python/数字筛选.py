#判断是否为素数
def ss(n) :
	x=0
	for i in range(2,n):
		if n%i==0:
			x+=1
		i+=1
	if x==0 and n>1:
		return n

#列出指定范围的素数
def sslist(n):
	return list(filter(ss,range(n)))

#输入
n=int(input())

#输出
print(sslist(n))
print(ss(n))



#回文数
def frg(m):
	n=str(m)
	x=0
	l=len(n)
	for i in range(l):
		if n[i]!=n[l-i-1]:
			x+=1
		i+=1
	if x==0:
		return n


# 回文数判断2
def frg(m):
	return str(m)==str(m)[::-1]

def frglist(n):
	return list(filter(frg,range(n)))

m=int(input())
print(frglist(m))