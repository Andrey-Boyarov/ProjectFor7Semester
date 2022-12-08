import numpy as np
import matplotlib.pyplot as plt

#   Полученные параметры
L = 8
c = 1.65
alpha = 0.002
T = 200

#   Задание параметров сетки
x_start = 0
x_end = L
t_start = 0
t_end = T

def calculate(I: int, K: int):
    # print("I: " + str(I_calc) + " K: " + str(int(T / c * (2 * alpha * np.power(I_calc, 2) / np.power(L, 2) + D))))
    x = np.linspace(x_start, x_end, I + 1)
    t = np.linspace(t_start, t_end, K + 1)
    hx = L / I
    ht = T / K
    u = np.zeros((I + 1, K + 1))
    u_0=0
    l=L
    k_k=0.59
    S=0.01
    R = np.sqrt(S / np.pi)
    #   Расчёт u[i][k]
    phi = np.sin(np.pi * x / l) ** 2

    def difference_scheme():
        for k in range(0, K):
            u[1:I, 0] = u_0
            u[0, k + 1] = u[0, k] * (
                    1 - 2 * k_k * ht / c / hx / hx - 2 * alpha * ht / c / R) + 2 * k_k * ht / c / hx / hx * u[
                              1, k] + ht / c * phi[0]
            u[1:I, k + 1] = u[1:I, k] * (
                    1 - 2 * k_k * ht / c / hx / hx - 2 * alpha * ht / c / R) + k_k * ht / c / hx / hx * (
                                    u[0:I - 1, k] + u[2:I + 1, k]) + ht / c * phi[1:I]
            u[I, k + 1] = u[I, k] * (
                    1 - 2 * k_k * ht / c / hx / hx - 2 * alpha * ht / c / R - 2 * alpha * ht / c / hx) + 2 * k_k * ht / c / hx / hx * \
                          u[I - 1, k] + ht / c * phi[I]

    difference_scheme()
    return I, K, hx, ht, x, t, u

#   Отрисовка графиков для пункта 3.1
I, K, hx, ht, x, t, u = calculate(20, 4000)
plt.plot(x, u[:, 0], 'blue', linewidth=1, label="t = 0")
plt.plot(x, u[:, int(K / 20)], 'red', linewidth=1, label="t = " + str(ht * K / 20))
plt.plot(x, u[:, int(K / 10)], 'green', linewidth=1, label="t = " + str(ht * K / 10))
plt.plot(x, u[:, int(K - 1)], 'black', linewidth=1, label="t = " + str(ht * K))
plt.xlabel("x, см")
plt.ylabel("u(x, t)")
plt.legend()
plt.show()
plt.plot(t, u[0, :], 'blue', linewidth=1, label="x = 0")
plt.plot(t, u[int(I / 4), :], 'green', linewidth=1, label="x = " + str(hx * I / 4))
plt.plot(t, u[int(I / 2), :], 'red', linewidth=1, label="x = " + str(hx * I / 2))
plt.plot(t, u[int(I / 4 * 3), :], 'orange', linewidth=1, label="x = " + str(hx * I / 4 * 3))
plt.plot(t, u[int(I - 1), :], 'black', linewidth=1, label="x = " + str(hx * I))
plt.xlabel("t, с")
plt.ylabel("u(x, t)")
plt.legend()
plt.show()

#   Отрисовка графиков для пункта 3.2
I1, K1, hx1, ht1, x1, t1, u1 = calculate(5, 100)
I2, K2, hx2, ht2, x2, t2, u2 = calculate(5, 1500)
I3, K3, hx3, ht3, x3, t3, u3 = calculate(5, 2000)
I4, K4, hx4, ht4, x4, t4, u4 = calculate(5, 3000)

plt.plot(t1, u1[int(I1 / 5), :], 'blue', linewidth=1, label="K = " + str(K1))
plt.plot(t2, u2[int(I2 / 5), :], 'red', linewidth=1, label="K = " + str(K2))
plt.plot(t3, u3[int(I3 / 5), :], 'green', linewidth=1, label="K = " + str(K3))
plt.plot(t4, u4[int(I4 / 5), :], 'brown', linewidth=1, label="K = " + str(K4))
plt.xlabel("t, с")
plt.ylabel("u(x, t)")
plt.legend()
plt.show()

I1, K1, hx1, ht1, x1, t1, u1 = calculate(5, 4000)
I2, K2, hx2, ht2, x2, t2, u2 = calculate(10, 4000)
I3, K3, hx3, ht3, x3, t3, u3 = calculate(20, 4000)
I4, K4, hx4, ht4, x4, t4, u4 = calculate(30, 4000)

plt.plot(x1, u1[:, int(K1 / 2)], 'blue', linewidth=1, label="I = " + str(I1))
plt.plot(x2, u2[:, int(K2 / 2)], 'red', linewidth=1, label="I = " + str(I2))
plt.plot(x3, u3[:, int(K3 / 2)], 'green', linewidth=1, label="I = " + str(I3))
plt.plot(x4, u4[:, int(K4 / 2)], 'brown', linewidth=1, label="I = " + str(I4))
plt.xlabel("х, см")
plt.ylabel("u(x, t)")
plt.legend()
plt.show()

I1, K1, hx1, ht1, x1, t1, u1 = calculate(5, 200)
I2, K2, hx2, ht2, x2, t2, u2 = calculate(10, 400)
I3, K3, hx3, ht3, x3, t3, u3 = calculate(20, 2000)
I4, K4, hx4, ht4, x4, t4, u4 = calculate(50, 10000)
# I5, K5, hx5, ht5, x5, t5, u5 = calculate(100, 4000)

plt.plot(t1, u1[int(I1 / 2), :], 'blue', linewidth=1, label="I =" + str(I1) + ", K = " + str(K1))
plt.plot(t2, u2[int(I2 / 2), :], 'red', linewidth=1, label="I =" + str(I2) + ", K = " + str(K2))
plt.plot(t3, u3[int(I3 / 2), :], 'green', linewidth=1, label="I =" + str(I3) + ", K = " + str(K3))
plt.plot(t4, u4[int(I4 / 2), :], 'brown', linewidth=1, label="I =" + str(I4) + ", K = " + str(K4))
# plt.plot(t5, u5[int(I5 / 2), :], 'black', linewidth=1, label="I =" + str(I5) + ", K = " + str(K5))
plt.xlabel("t, с")
plt.ylabel("u(x, t)")
plt.legend()
plt.show()

plt.plot(x1, u1[:, int(K1 / 2)], 'blue', linewidth=1, label="I = " + str(I1) + ", K = " + str(K1))
plt.plot(x2, u2[:, int(K2 / 2)], 'red', linewidth=1, label="I = " + str(I2) + ", K = " + str(K2))
plt.plot(x3, u3[:, int(K3 / 2)], 'green', linewidth=1, label="I = " + str(I3) + ", K = " + str(K3))
plt.plot(x4, u4[:, int(K4 / 2)], 'brown', linewidth=1, label="I = " + str(I4) + ", K = " + str(K4))
# plt.plot(x5, u5[:, int(K5 / 2)], 'black', linewidth=1, label="I = " + str(I5) + ", K = " + str(K5))
plt.xlabel("x, см")
plt.ylabel("u(x, t)")
plt.legend()
plt.show()

#   Расчет погрешности
#   По координате
print("="*10 + "РАСЧЕТ ПОГРЕШНОСТИ ПО КООРДИНАТЕ" + "="*10)
#np.max(np.absolute(U1-U2[::2]))
I1, K1, hx1, ht1, x1, t1, u1 = calculate(3, 6000)
I2, K2, hx2, ht2, x2, t2, u2 = calculate(3 * 2, 6000)
I3, K3, hx3, ht3, x3, t3, u3 = calculate(3 * 4, 6000)
a1 = np.max(np.absolute(u1-u2[::2]))
a2 = np.max(np.absolute(u2-u3[::2]))
print("1.1) " + str(a1))
print("1.2) " + str(a2))

I1, K1, hx1, ht1, x1, t1, u1 = calculate(5, 6000)
I2, K2, hx2, ht2, x2, t2, u2 = calculate(5 * 2, 6000)
I3, K3, hx3, ht3, x3, t3, u3 = calculate(5 * 4, 6000)
a1 = np.max(np.absolute(u1-u2[::2]))
a2 = np.max(np.absolute(u2-u3[::2]))
print("2.1) " + str(a1))
print("2.2) " + str(a2))

I1, K1, hx1, ht1, x1, t1, u1 = calculate(7, 4000)
I2, K2, hx2, ht2, x2, t2, u2 = calculate(7 * 2, 4000)
I3, K3, hx3, ht3, x3, t3, u3 = calculate(7 * 4, 4000)
a1 = np.max(np.absolute(u1-u2[::2]))
a2 = np.max(np.absolute(u2-u3[::2]))
print("3.1) " + str(a1))
print("3.2) " + str(a2))

#   По времени
print("="*10 + "РАСЧЕТ ПОГРЕШНОСТИ ПО ВРЕМЕНИ" + "="*10)
#np.max(np.absolute(U1-U2[::2]))
I1, K1, hx1, ht1, x1, t1, u1 = calculate(20, 1000)
I2, K2, hx2, ht2, x2, t2, u2 = calculate(20, 1000 * 2)
I3, K3, hx3, ht3, x3, t3, u3 = calculate(20, 1000 * 4)
a1 = np.max(np.absolute(u1-u2[:, ::2]))
a2 = np.max(np.absolute(u2-u3[:, ::2]))

print("1.1) " + str(a1))
print("1.2) " + str(a2))

I1, K1, hx1, ht1, x1, t1, u1 = calculate(20, 1500)
I2, K2, hx2, ht2, x2, t2, u2 = calculate(20, 1500 * 2)
I3, K3, hx3, ht3, x3, t3, u3 = calculate(20, 1500 * 4)
a1 = np.max(np.absolute(u1-u2[:, ::2]))
a2 = np.max(np.absolute(u2-u3[:, ::2]))
print("2.1) " + str(a1))
print("2.2) " + str(a2))

I1, K1, hx1, ht1, x1, t1, u1 = calculate(20, 2000)
I2, K2, hx2, ht2, x2, t2, u2 = calculate(20, 2000 * 2)
I3, K3, hx3, ht3, x3, t3, u3 = calculate(20, 2000 * 4)
a1 = np.max(np.absolute(u1-u2[:, ::2]))
a2 = np.max(np.absolute(u2-u3[:, ::2]))
print("3.1) " + str(a1))
print("3.2) " + str(a2))
