import sys, numpy, itertools

weights = False

N = int(sys.argv[1])
K = int(sys.argv[2])
eps = float(sys.argv[3])
if sys.argv[4] == 1: weights = True

T = [[1,1,1,0,0,0],[1,1,0,0,1,1],[0,0,0,1,1,1],[0,0,1,1,0,0],[1,1,1,1,1,1],[0,0,0,0,1,1],[1,0,0,0,1,1]]
T = [[1,1,0,0,1,0,1],[1,1,0,0,1,0,0],[1,0,0,1,1,0,0],[0,0,0,1,1,0,0],[0,1,1,0,1,1,1],[0,1,1,0,1,1,1]]

A = [numpy.matrix(numpy.diag(T[t][:K])) for t in range(6)]

sizes = numpy.random.randint(2, N, size=K)
print sizes

communities = [numpy.random.permutation(range(N))[:sizes[k]] for k in range(K)]

C = numpy.matrix(numpy.zeros((N, K)))

for n in range(N):
	for k in range(K):
		if n in communities[k]: C[n,k] = (numpy.random.rand() if weights else 1) 

with open("communities.txt", "w") as f:
	for n in range(N):
		for k in range(K):
			f.write(str(C[n,k]))
			if k < K-1: f.write(",")
		if n < N-1: 
			f.write("\n")



X = [numpy.zeros((N,N)) for t in range(6)]

for t in range(6):
	for i in range(N):
		for j in range(N):
			if i == j: continue
			if numpy.random.rand() < 1-numpy.exp(-C[i,:]*A[t]*numpy.transpose(C[j,:])) + eps:
				X[t][i,j] = 1
				X[t][j,i] = 1

for t in range(6):
	with open("t-"+str(t)+".txt", "w") as f:
		for i in range(N):
			for j in range(N):
				f.write(str(int(X[t][i,j])))
				if j < N-1: f.write(",")
			if i < N-1: f.write("\n")

	with open("graph-"+str(t)+".txt", "w") as f:
		for i in range(N):
			for j in range(N):
				if X[t][i,j] == 1: f.write(str(i) + "\t" + str(j) + "\n")



