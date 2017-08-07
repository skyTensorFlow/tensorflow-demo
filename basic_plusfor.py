import tensorflow as tf

state=tf.Variable(0,name='counter')
one=tf.constant(1)
new_Value=tf.add(state,one) #state和one相加。放到new_Value中
update=tf.assign(state,new_Value) #将new_Value的值赋给state state=new_Value

#初始化
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print sess.run(state)