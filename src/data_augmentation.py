
import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def augment_folder(in_dir: str, out_dir: str, n: int = 15, target=(64, 64)):
    """
    For every image in `in_dir`, create `n` augmented variants and
    save them to `out_dir`.

    Transforms: random rotation, width/height shift, zoom, horizontal flip.
    """
    os.makedirs(out_dir, exist_ok=True)
    gen = ImageDataGenerator(rotation_range=30,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True)

    for fname in os.listdir(in_dir):
        if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        img = cv2.imread(os.path.join(in_dir, fname))
        if img is None:
            continue
        img = cv2.resize(img, target)

        i = 0
        for batch in gen.flow(np.expand_dims(img, 0), batch_size=1):
            aug_path = f"{out_dir}/{fname.rsplit('.',1)[0]}_aug_{i}.png"
            cv2.imwrite(aug_path, batch[0])
            i += 1
            if i >= n:
                break
