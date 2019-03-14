Note using Deep leanring on BF
---

MNIST
---

full MNIST train and test data

2 layer dnn: 10Kx10k, 10Kx1k
learning_rate = 0.2
num_steps = 500
batch_size = 100
display_step = 100


lenth: 10000 b: 5 num_hash: 10 dis: 5.0 false_positive:  0.0012684416422110425
Step 1, Minibatch Loss= 72833256.0000, Training Accuracy= 0.200
Step 100, Minibatch Loss= 1466498.1250, Training Accuracy= 0.770
Step 200, Minibatch Loss= 1000122.5625, Training Accuracy= 0.760
Step 300, Minibatch Loss= 347235.4062, Training Accuracy= 0.880
Step 400, Minibatch Loss= 128672.2422, Training Accuracy= 0.920
Step 500, Minibatch Loss= 257864.4062, Training Accuracy= 0.870
Optimization Finished!
Testing Accuracy: 0.8616

lenth: 10000 b: 10 num_hash: 5 dis: 5.0 false_positive:  0.026327154471769722
Step 1, Minibatch Loss= 25968852.0000, Training Accuracy= 0.260
Step 100, Minibatch Loss= 1377663.3750, Training Accuracy= 0.770
Step 200, Minibatch Loss= 346549.6875, Training Accuracy= 0.880
Step 300, Minibatch Loss= 576059.9375, Training Accuracy= 0.910
Step 400, Minibatch Loss= 279022.0625, Training Accuracy= 0.870
Step 500, Minibatch Loss= 280012.4375, Training Accuracy= 0.820
Optimization Finished!
Testing Accuracy: 0.8881