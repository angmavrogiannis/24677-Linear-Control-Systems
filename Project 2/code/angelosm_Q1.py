import numpy as np 
import matplotlib.pyplot as plt
import control

lr = 1.7
lf = 1.1
Ca = 15000
Iz = 3344
m = 2000

for i in range(3):
	if i == 0:
		xdot = 2
	elif i == 1:
		xdot = 5
	else:
		xdot = 8
	A = np.array([[0, 1, 0, 0], [0, -4*Ca / (m * xdot), 4*Ca/m, (2*Ca*(lr - lf))/(m*xdot)], [0, 0, 0, 1], [0, (2*Ca*(lr - lf)) / (Iz * xdot), (2*Ca*(lf - lr)) / Iz, (-2*Ca*(np.power(lf, 2) + np.power(lr, 2))) / (Iz * xdot)]])
	B = np.array([[0], [2*Ca / m], [0], [(2 * Ca* lf) / Iz]])
	C = np.identity(4)

	P = np.hstack((B, np.matmul(A, B), np.matmul(np.linalg.matrix_power(A, 2), B), np.matmul(np.linalg.matrix_power(A, 3), B)))
	Q = np.vstack((C, np.matmul(C, A), np.matmul(C, np.linalg.matrix_power(A, 2)), np.matmul(C, np.linalg.matrix_power(A, 3))))
	rankP = np.linalg.matrix_rank(P)
	rankQ = np.linalg.matrix_rank(Q)
	print(f'Case #{i+1}: Vx = {xdot}m/s\n')
	print(f'Rank of Controllability matrix = {rankP} --> The system is controllable.')
	print(f'Rank of Observability matrix = {rankQ} --> The system is observable.\n')

x = np.linspace(1, 40, num=1000)
log_vals = []
poles = []
for i in range(4):
	poles.append([])

for i in range(len(x)):
	xdot = x[i]
	A = np.array([[0, 1, 0, 0], [0, -4*Ca / (m * xdot), 4*Ca/m, (2*Ca*(lr - lf))/(m*xdot)], [0, 0, 0, 1], [0, (2*Ca*(lr - lf)) / (Iz * xdot), (2*Ca*(lf - lr)) / Iz, (-2*Ca*(np.power(lf, 2) + np.power(lr, 2))) / (Iz * xdot)]])
	B = np.array([[0], [2*Ca / m], [0], [(2 * Ca* lf) / Iz]])
	C = np.array([1, 1, 1, 1])
	D = np.array([0])
	P = np.hstack((B, np.matmul(A, B), np.matmul(np.linalg.matrix_power(A, 2), B), np.matmul(np.linalg.matrix_power(A, 3), B)))
	_, s, _ = np.linalg.svd(P)
	s1 = max(s)
	sn = min(s)
	log_vals.append(np.log10(s1 / sn))
	sys = control.StateSpace(A, B, C, D)
	p = control.pole(sys)
	for j in range(4):
		poles[j].append(p[j].real)


x = np.asarray(x)
log_vals = np.asarray(log_vals)

plt.plot(x, log_vals)
plt.xlabel('$V (m/s)$')
plt.ylabel('$\log_{10}$ $\dfrac{\sigma_1}{\sigma_n}$')
plt.show()

fig = plt.figure()

plt.subplot(2, 2, 1)
plt.xlabel('$V (m/s)$')
plt.ylabel('$Re(p_1)$')
plt.plot(x, poles[0])

plt.subplot(2, 2, 2)
plt.xlabel('$V (m/s)$')
plt.ylabel('$Re(p_2)$')
plt.plot(x, poles[1])

plt.subplot(2, 2, 3)
plt.xlabel('$V (m/s)$')
plt.ylabel('$Re(p_3)$')
plt.plot(x, poles[2])

plt.subplot(2, 2, 4)
plt.xlabel('$V (m/s)$')
plt.ylabel('$Re(p_4)$')
plt.plot(x, poles[3])

plt.tight_layout()
plt.show()