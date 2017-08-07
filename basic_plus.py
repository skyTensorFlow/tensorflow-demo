# -*- coding: utf-8 -*-
#设置编码为utf-8

#引入tensorflow
import tensorflow as tf

#定义baseci_operation函数
def basic_operation():
    v1=tf.Variable(10) #Variable变量
    v2=tf.Variable(5)
    s=v1+v2
    #运行basic_operation()后。print('s='+s) 没有初始化，直接打印报错。

    #Session是用来计算实例的
    #网上使用一下方法，不行。报错。http://blog.csdn.net/a595130080/article/details/56295425
    # 方法1：
    #  sess=tf.Session()
    # tf.global_variables_initializer().run(session=sess)
    # print("变量是需要初始化的")
    # print ('v1+v2='+s.eval(session=sess))
    #print('v1+v2='+sess.run(s))

    #方法2：
    #定义一个session，并且初始化。
    sess = tf.Session()
    init = tf.global_variables_initializer() #初始化
    sess.run(init)

    print("v1+v2="+str(sess.run(s)))
basic_operation()