# Model Iteration Summary

| ID | Architecture | Data variant | Val Acc | F1 Rec | F1 Non-Rec |
|----|--------------|--------------|--------:|-------:|-----------:|
| 3.1 | **MLP** (flattened) | Raw 64×64 | 0.79 | 0.80 | 0.77 |
| 3.2 | **CNN** (2-conv)   | Raw | 0.86 | 0.87 | 0.85 |
| 3.3 | **ResNet50 TL**    | Raw | **0.94** | 0.94 | 0.93 |
| 3.4 | **CNN + Aug**      | Augmented | 0.91 | 0.91 | 0.89 |

Confusion-matrix PNG for the best model is stored in `assets/confusion_matrix_V3.png`.


