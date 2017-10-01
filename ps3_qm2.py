import numpy as np

Y11 = np.array([[1],[0],[0]])
Y10 = np.array([[0],[1],[0]])
Y1_1 = np.array([[0],[0],[1]])

Y = [Y11, Y10, Y1_1]

Ly = np.array([[0, -1j, 0]
			  ,[1j, 0, -1j]
			  ,[0, 1j, 0]])

Ly *= 1/np.sqrt(2)

u, v = np.linalg.eig(Ly)

W11 = np.array([v[:,0]])
W10 = np.array([v[:,1]])
W1_1 = np.array([v[:,2]])

W = [W11, W10, W1_1]

ms = [1, 0, -1]

print("1a)")

for m in range(3):
	for i in range(3):

		print("\n[%d,%d]= "%(ms[m],i+1))
		print(np.dot(W[m],Y[i]))


print("1b)")

for m in range(3):
	print("[%d]= "%(ms[m]))
	print(np.dot(W[m],Y1_1)*np.conj(np.dot(W[m],Y1_1)))