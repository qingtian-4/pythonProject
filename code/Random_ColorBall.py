from numpy.random import choice

samples=choice(['R','G','B'],size=100,p=[0.2,0.3,0.5])
print(samples)
x=y=z=0
for i in range(100):
    if samples[i]=='R':
        x=x+1
    elif samples[i] == 'G':
        y=y+1
    else:
        z=z+1
print("红颜色小球的个数为：",x)
print("绿颜色小球的个数为：",y)
print("蓝颜色小球的个数为：",z)
