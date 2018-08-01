import math

T1 = 0.005
T2 = 0.05
w1 = 0.1#変数

P1 = 1/(1 + w1**2 * T1**2)
P2 = (w1**4 * T1**2 * T2**2) + (w1**2 * T1**2) + (w1**2 * T2**2) + 1

G = P1 * math.sqrt(P2)

G1 = 20 * math.log10(G)
print("G=",G)
print("G1=",G1)

P3 = (w1*(T2 - T1))/(w1**2 * T1*T2 + 1)
a = math.atan(P3)
sita = math.degrees(a)
print("位相=",sita)


#<G(jw)について
