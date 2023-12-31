from keras import models
from keras import layers
from keras.datasets import mnist
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocessing train data
train_images = train_images.reshape(60000, 28*28)
train_images = train_images.astype('float32') / 255

# Preprocessing test data
test_images = test_images.reshape(10000, 28*28)
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# model architecture
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28, )))
network.add(layers.Dense(10, activation='softmax'))

# model compilation
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# fit model
network.fit(train_images, train_labels, epochs=20, batch_size=10) #batch_size =128, epochs = 10

# calculate test loss and accuracy
test_loss, test_acc = network.evaluate(test_images, test_labels)

# print Test loss and accuracy
print(f"Test Loss: {test_loss}\n Test Acc:{test_acc * 100} %")

network.save('mnist2.h5')
print("Saving the model as mnist2.h5")




