"""
succssfully load variable from ckpt file

https://stackoverflow.com/questions/42623978/print-saved-weights-of-particular-layer-tensorflow
python ~/Documents/github_code/tensorflow/tensorflow/python/tools/inspect_checkpoint.py --file_name=/Users/wanli/PycharmProjects/test_tensorflow/tf_save/ckpt
hidden0_weight (DT_FLOAT) [784,1000]
logits_weight (DT_FLOAT) [1000,10]
"""
import tensorflow as tf
import numpy as np
#

save_path="/Users/wanli/PycharmProjects/test_tensorflow/tf_save/"
with tf.Session() as sess:
    new_saver = tf.train.import_meta_graph(save_path+'ckpt.meta')
    new_saver.restore(sess, save_path+'ckpt')
    sess.run(tf.global_variables_initializer())
    graph = tf.get_default_graph()
#    var = [v for v in tf.trainable_variables() if v.name == "hidden0_weight"]
    W1 = graph.get_tensor_by_name('hidden0_weight:0')
    W1_value = sess.run(W1)
    np.save('weight1.npy', W1_value)
    print(W1_value)
    W2 = graph.get_tensor_by_name('logits_weight:0')
    W2_value = sess.run(W2)
    np.save('weight2.npy', W2_value)
    print(W2_value)



#logits_weight 





