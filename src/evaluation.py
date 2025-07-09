import seaborn as sns, matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix

def evaluate(model, X, y_onehot, labels):
    """
    Print precision/recall/F1 and plot confusion matrix.
    """
    preds = model.predict(X).argmax(axis=1)
    true  = y_onehot.argmax(axis=1)

    print(classification_report(true, preds, target_names=labels))

    cm = confusion_matrix(true, preds)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted"); plt.ylabel("True")
    plt.tight_layout(); plt.show()
    return cm

