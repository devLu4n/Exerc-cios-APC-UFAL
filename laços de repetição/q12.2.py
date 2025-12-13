p1 = [1,5]
p2 = [3,9]
d = (((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))**(1/2)
print(d)

soma = 0
for i in range(len(p1)):
    soma += (p1[i]-p2[i])**2

d = soma**(1/2)
print(d)