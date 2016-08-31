#乘法口诀表
#方式1:数组实现

i=1
for n in range(1,10):
	line=[]
	for i in range(1,n+1):
		line.append('%d*%d=%d' %(i,n,i*n))
	print(line)


#方式2：字符串实现
print('\n')
for i in range(1,10):
	a=''
	for j in range(1,i+1):
		a=a+str(j)+'*'+str(i)+'='+str(i*j)+" "
	print(a)




#方式3：打印不换行
print('\n')
for i in range(1,10):
	for j in range(1,i+1):
		x=str(j)+'*'+str(i)+'='+str(i*j)
		print(x,end=' ')
	print('\t')