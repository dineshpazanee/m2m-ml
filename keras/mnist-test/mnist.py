import numpy as np
import os
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

os.environ["KERAS_BACKEND"] = "jax"

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Print dataset details
print("Training data shape:", x_train.shape)  # (60000, 28, 28)
print("Test data shape:", x_test.shape)      # (10000, 28, 28)
print("Training labels shape:", y_train.shape)  # (60000,)
print("Test labels shape:", y_test.shape)      # (10000,)

# Display the first 9 images from the training set
plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.show()
