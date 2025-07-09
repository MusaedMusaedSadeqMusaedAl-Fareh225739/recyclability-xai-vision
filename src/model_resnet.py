from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model

def build_resnet(shape=(64, 64, 3), classes=2, trainable=False):
    """
    Transfer-learning wrapper around ResNet50 (no top).
    """
    base = ResNet50(weights="imagenet",
                    include_top=False,
                    input_shape=shape)
    base.trainable = trainable            # freeze or fine-tune
    x = GlobalAveragePooling2D()(base.output)
    out = Dense(classes, activation="sigmoid")(x)
    return Model(base.input, out)

