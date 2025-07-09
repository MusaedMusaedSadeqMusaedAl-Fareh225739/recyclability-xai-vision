# XAI vs. Accuracy – Trade-off Evaluation

| Variant | Accuracy | Interpretability | Notes |
|---------|----------|------------------|-------|
| CNN + softmax        | 0.91 | ⭐ (saliency) | Baseline explainability |
| ResNet50 (frozen)    | **0.94** | ⭐⭐ (Grad-CAM) | Slight accuracy ↑, still interpretable |
| ResNet50 fine-tuned  | 0.95 | ⭐ (weaker) | Top layers opaque; saliency noisy |

**Stakeholder outcome**  
WMCN accepted a **≤ 3 %** accuracy sacrifice to gain clear Grad-CAM heatmaps that inspectors can show auditors.

Key finding: At 0.94 accuracy with frozen base, Grad-CAM still highlights label areas (plastic logos, recycling symbols). Fine-tuning all layers hurt clarity without meaningful F1 lift.


