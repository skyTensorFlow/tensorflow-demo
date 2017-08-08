# -*- coding: utf-8 -*-
#模拟曲线
#http://www.jianshu.com/p/fe586964ab07

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
def add_layer(inputs,in_size,out_size,activatuib_funaction=None):
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))
    biases=tf.Variable(tf.zeros([1,out_size]))+0.1
    Wx_plus_b=tf.matmul(inputs,Weights)+biases

    if activatuib_funaction is None:
        outputs=Wx_plus_b
    else :
        outputs=activatuib_funaction(Wx_plus_b)
    return outputs


x_data=np.linspace(-1,1,300)[:,np.newaxis]
noise=np.random.normal(0,0.05,x_data.shape)
y_data=np.square(x_data)-0.5+noise

xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])


l1=add_layer(xs,1,10,activatuib_funaction=tf.nn.relu)
predition=add_layer(l1,10,1,activatuib_funaction=None)

loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-predition),reduction_indices=[1]))

train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.scatter(x_data,y_data)
    plt.show(block=False)

    sess.run(init)
    for train in range(50000):

        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
        if train%50==0:

            try:
                ax.lines.remove(lines[0])
            except Exception:
                pass
            print train,sess.run(loss,feed_dict={xs:x_data,ys:y_data})
            predition_value=sess.run(predition,feed_dict={xs:x_data})
            lines=ax.plot(x_data,predition_value,'r-',lw=5)
            plt.pause(0.1)

#为了让程序保持运行，增加以下代码
while(True):
    a=1