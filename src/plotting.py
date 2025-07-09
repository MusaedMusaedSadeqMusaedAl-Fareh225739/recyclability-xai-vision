import matplotlib.pyplot as plt

def plot_history(history):
    """
    Plot train vs. validation accuracy & loss from a Keras History object.
    """
    for metric in ("accuracy", "loss"):
        plt.figure(figsize=(6, 3))
        plt.plot(history.history[metric], label=f"train_{metric}")
        plt.plot(history.history[f"val_{metric}"], label=f"val_{metric}")
        plt.title(metric.capitalize())
        plt.legend()
        plt.tight_layout()
        plt.show()

