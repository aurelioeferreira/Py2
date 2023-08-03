import tensorflow as tf
import numpy as np
import math
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([1,2,3,4,5,7,12], dtype=int)
ys = np.array([13,18,23,28,33,43,68], dtype=int)

model.fit(xs, ys, epochs=500)


while True:
    num = int(input("Digite um número X para prever o Y: "))
    prediz = model.predict([num])
    print(prediz)
    if num == 0:
        break