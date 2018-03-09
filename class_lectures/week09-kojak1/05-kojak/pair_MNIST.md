## Handwritten Image Detection with Keras using MNIST data

In this pair problem you will work with image data: specifically the famous MNIST data set.  

1) The first objective is to build a neural net classifier using the fully connected neural net
(i.e. ANN (artificial neural net ))

Note: you can work locally for this problem & you wont need a larger machine on EC2.

a) Load data into Keras using:   
```
 from keras.datasets import mnist
```

Note: you'll want to flatten the 28x28 so that input is a vector of 784     

b) Create your first NN using Sequential model w/ a few layers.      

c) Train/ test the model.     

history = model_1.fit(
    ....
    ....
    ....)      

d) Visualize your test/train results.    
Note: that history.history will return loss & accuracy vals.

2) Repeat the above, but make your network much 'wider'.
i.e.: (Dense(400) layer is much wider than Dense(64)).

Compare results of both viz graphs!
