from keras.models import Sequential
from keras.layers import (Conv2D, MaxPooling2D,
                          Flatten, Dense, Dropout)

def build_cnn(shape=(64, 64, 3), classes=2):
    """
    Custom 2-conv CNN for 64×64 images.
    """
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation="relu", input_shape=shape))
    model.add(MaxPooling2D(2, 2))
    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(MaxPooling2D(2, 2))
    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(classes, activation="softmax"))
    return model

