import tensorflow as tf

# Create a MirroredStrategy.
strategy = tf.distribute.MirroredStrategy()

# Create a simple model.
with strategy.scope():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load and prepare the MNIST dataset.
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()  

x_train = x_train.reshape((60000, 784)).astype('float32') / 255
x_test = x_test.reshape((10000, 784)).astype('float32') / 255

# Train the model.
model.fit(x_train, y_train, epochs=5, batch_size=64)

# Evaluate the model.
model.evaluate(x_test, y_test, batch_size=64)  
