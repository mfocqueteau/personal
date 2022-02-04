from scinum import kg, m, s, new_unit

K1 = 1/2 * 6*kg * (3*m/s)**2
K2 = 1/2 * 9*kg * (2*m/s)**2

print(K1, K2)
print(K1 * K2)
print(K1 + K2)

yiyo = new_unit('yiyo')
