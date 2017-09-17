import numpy as np

def dagger(v):
	return np.conj(v.T)

A = np.array([[3,0,-1j]
			 ,[0,2,-1]
			 ,[1j,-1,0]])

B = np.array([[0,1j,0]
			 ,[-1j,0,1]
			 ,[0,1,-2]])

u = np.array([[1j],[2],[-1j]])

v = np.array([[0],[2],[1+1j]])


print("[A,B]=\n", np.dot(A,B)-np.dot(B,A))

print("\nA.dagger=\n",dagger(A))

print("\ndet(A)=\n", np.linalg.det(A))

print("\ndet(B)=\n", np.linalg.det(B))

print("\nTr(B)=\n", np.trace(B))

print("\ninv(B)=\n", np.linalg.inv(B))

print("\nB|u>=\n", np.dot(B,u))

print("\n<u|v>=\n", np.dot(dagger(u),v))

print("\n<u|A|v>=\n", np.dot(dagger(u),np.dot(A,v)))

print("\n|u><v|=\n", np.dot(u,dagger(v)))