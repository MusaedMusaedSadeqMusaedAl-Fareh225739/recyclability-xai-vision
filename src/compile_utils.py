from keras.optimizers import Adam
from keras.callbacks import EarlyStopping

def compile_model(model, lr=1e-3, loss="categorical_crossentropy"):
    """
    Attach optimizer / loss / metrics and return the compiled model.
    """
    model.compile(optimizer=Adam(lr), loss=loss, metrics=["accuracy"])
    return model

def early_stop(patience=3):
    """
    Early stopping callback (restore best val weights).
    """
    return EarlyStopping(
        monitor="val_loss",
        patience=patience,
        restore_best_weights=True,
        verbose=1
    )
