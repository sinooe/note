#怕排序的处理
def by_name(L):
	return L[0].lower()

def by_score(L):
	return L[1]

L = [('aob', 75), ('Zdam', 92), ('Bart', 66), ('Lisa', 88)]
M=sorted(L,key=by_name)
N=sorted(L,key=by_score)
print(M)
print(N)