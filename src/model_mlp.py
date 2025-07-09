from keras.models import Sequential
from keras.layers import Dense

def build_mlp(input_dim=64*64*3, classes=2):
    """
    Simple baseline MLP (flattened pixels → Dense layers).
    """
    return Sequential([
        Dense(128, activation="relu", input_shape=(input_dim,)),
        Dense(classes, activation="softmax")
    ])

