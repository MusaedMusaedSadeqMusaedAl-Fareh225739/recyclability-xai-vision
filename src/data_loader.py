import os
import cv2
import numpy as np

def load_images(folder_paths, class_names, target_size=(64, 64)):
    """
    Load and resize images from multiple class folders.

    Parameters
    ----------
    folder_paths : list[str]
        Each entry is a directory containing images of ONE class.
    class_names  : list[str]
        Human-readable labels, must align with folder_paths order.
    target_size  : tuple[int,int]
        Final (width, height) to resize every image.

    Returns
    -------
    X : np.ndarray  (N, H, W, 3)  dtype=uint8
    y : np.ndarray  (N,)          string labels
    ignored : int   how many files failed to read
    """
    X, y, ignored = [], [], 0
    for label, folder in enumerate(folder_paths):
        for fname in os.listdir(folder):
            if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            path = os.path.join(folder, fname)
            img = cv2.imread(path)
            if img is None:
                ignored += 1
                continue
            img = cv2.resize(img, target_size)
            X.append(img)
            y.append(class_names[label])
    return np.array(X), np.array(y), ignored



