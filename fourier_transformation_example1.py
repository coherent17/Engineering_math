import math
import matplotlib.pyplot as plt
import numpy as np

iteration=100000

#deal with a_0
a_0=math.pi/4

#deal with a_n,b_n
a_n=[]
b_n=[]
for i in range(1,iteration+1):
    a_n.append((1-(-1)**i)/(i**2)/math.pi)
    b_n.append(1/i)

print(a_n)
print(b_n)

def fourier(a_0,a_n,b_n,iteration,x):
    value=a_0
    for i in range(1,iteration):
        value+=a_n[i-1]*math.cos(i*x)+b_n[i-1]*math.sin(i*x)
    return value

#visualize the fourier transform
discrete_num=1000
x=np.linspace(-math.pi,math.pi,discrete_num)
y=[]
for j in range(discrete_num):
    y.append(fourier(a_0,a_n,b_n,iteration,x[j]))

plt.plot(x,y)
plt.title("realize the fourier transformation (number of summations: %d)" %(iteration))
plt.xlabel("x")
plt.ylabel("y")
plt.text(-3,1,"f(x)=0, for x=-π~0")
plt.text(-3,0.5,"f(x)=π-x, for x=0~π")
plt.show()