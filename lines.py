# -*- coding: utf-8 -*-
#模拟直线
#http://www.jianshu.com/p/fe586964ab07

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3

Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases=tf.Variable(tf.zeros([1]))

y=Weights*x_data+biases
loss=tf.reduce_mean(tf.square(y-y_data))

optimizer=tf.train.GradientDescentOptimizer(0.5)
train=optimizer.minimize(loss)

init=tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)
fig = plt.figure()

#add_subplot(1, 1, 1)将画布分割成1行1列，图像画在第1块中。（2，3，4）就是2行3列，图像画在第4块中。就是第2行第1个位置
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()
for step in range(201):
    try:
        ax.lines.remove(lines[0])
    except Exception:
        pass
    sess.run(train)
    if step%2==0:
        print(step,sess.run(Weights),sess.run(biases))
    predition_value = sess.run(Weights)*x_data+sess.run(biases)
    lines = ax.plot(x_data, predition_value, 'r-', lw=3)
    plt.pause(0.1)

while(True):
    a=1