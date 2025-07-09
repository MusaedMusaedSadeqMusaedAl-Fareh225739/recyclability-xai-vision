from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
import numpy as np

def lr_sweep(build_fn, X_train, y_train,
             X_val, y_val, lrs=(1e-2,1e-3,1e-4),
             epochs=10, batch=32):

    histories, best_losses = [], []
    for lr in lrs:
        model = build_fn()
        model.compile(optimizer=Adam(lr),
                      loss="categorical_crossentropy",
                      metrics=["accuracy"])
        es = EarlyStopping("val_loss", patience=2, restore_best_weights=True)
        H = model.fit(X_train, y_train,
                      validation_data=(X_val, y_val),
                      epochs=epochs, batch_size=batch,
                      callbacks=[es], verbose=0)
        histories.append(H)
        best_losses.append(min(H.history["val_loss"]))
        print(f"lr={lr:.0e}  best_val_loss={best_losses[-1]:.4f}")
    return lrs, best_losses, histories
