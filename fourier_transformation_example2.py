import math
import matplotlib.pyplot as plt
import numpy as np

iteration=15

#deal with b_n
b_n=[]
for i in range(1,iteration+1):
    b_n.append((2/math.pi)*((1-(-1)**i)/i))

print(b_n)

def fourier(b_n,iteration,x):
    value=0
    for i in range(1,iteration):
        value+=b_n[i-1]*math.sin(i*x)
    return value

#visualize the fourier transform
discrete_num=2000
x=np.linspace(-math.pi+0.1,math.pi-0.1,discrete_num)
y=[]
for j in range(discrete_num):
    y.append(fourier(b_n,iteration,x[j]))

plt.plot(x,y)
plt.title("realize the fourier transformation (number of summations: %d)" %(iteration))
plt.xlabel("x")
plt.ylabel("y")
plt.show()