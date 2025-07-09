<!-- README.md — Recyclability-XAI Vision Project -->
<p align="center">
  <img src="assets/infographic.png" width="600"/>
</p>

# ♻️ Recyclability Image Classifier with XAI  
*A Breda University of Applied Sciences study project (Academic year 2023-2024)*  

End-to-end computer-vision pipeline that labels waste-item images as **recyclable** or **non-recyclable**.  
Built for the *Fair & Explainable AI* course, the project demonstrates model iteration, explainability, bias analysis, and stakeholder alignment.

---

## 📚 Table of Contents
1. [Project Highlights](#highlights)  
2. [Repository Layout](#layout)  
3. [Setup & Quick-start](#setup)  
4. [Model Iterations & Results](#results)  
5. [Stakeholders & Decision Framework](#stakeholders)  
6. [Ethics, Bias & Fairness](#ethics)  
7. [How to Reproduce](#reproduce)  
8. [Next Steps](#next)  
9. [License](#license)  

---

## ✨ <a name="highlights"></a>Project Highlights

| Feature | Details |
|---------|---------|
| **Iterations** | Baseline MLP → Custom CNN → ResNet50 Transfer-Learning → Augmented CNN |
| **Best accuracy** | **94 %** (ResNet50, frozen backbone) |
| **Explainability** | Grad-CAM & saliency maps integrated |
| **Error analysis** | Misclassification heatmaps, top-loss ranking |
| **Bias audit** | Manual IMsitu review (< 1 % Black representation) |
| **Stakeholder docs** | Power-interest grid, DAPS, business value narrative |

---

## 🗂 Repository Layout
```text
recyclability-xai-vision/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── environment.yml
│
├── data/                         # proprietary images removed
│   └── sample_images/           # tiny demo JPGs
│
├── assets/
│   ├── infographic.png
│   ├── wireframe_link.txt
│   └── confusion_matrix_V3.png
│
├── src/                          # reusable python modules
│   ├── data_loader.py
│   ├── data_augmentation.py
│   ├── model_mlp.py
│   ├── model_cnn.py
│   ├── model_resnet.py
│   ├── compile_utils.py
│   ├── plotting.py
│   └── evaluation.py
│
├── notebooks/
│   ├── 01_eda_baseline.ipynb
│   ├── 02_v1_mlp.ipynb
│   ├── 03_v2_cnn.ipynb
│   ├── 04_v3_resnet_transfer.ipynb
│   ├── 05_v4_augmented_final.ipynb
│   ├── 06_error_analysis.ipynb
│   └── 07_final_evaluation.ipynb
│
└── docs/
    ├── stakeholder_analysis.md
    ├── decision_framework.md
    ├── business_value.md
    ├── dataset_bias.md
    ├── fairness_method.md
    ├── tradeoff_analysis.md
    └── model_summary.md
```

## ⚙️ <a name="setup"></a>Setup & Quick-start

```bash
# clone
git clone https://github.com/<your-username>/recyclability-xai-vision.git
cd recyclability-xai-vision

# create environment
conda env create -f environment.yml         # or: pip install -r requirements.txt
conda activate recy-xai

# launch notebooks
jupyter notebook

```
Note – The full dataset is not included for copyright reasons.
Place your own recyclable/ and non_recyclable/ folders under data/ or update the paths in each notebook.


# Model Performance Summary

> **Note** – The full dataset is not included for copyright reasons.  
> Place your own `recyclable/` and `non_recyclable/` folders under `data/` or update the paths in each notebook.

| Model (notebook)           | Val Acc | F1 - Rec | F1 - NonRec |
|----------------------------|---------|----------|-------------|
| Majority baseline (01)     | 0.66    | –        | –           |
| V1 MLP (02)                | 0.79    | 0.80     | 0.77        |
| V2 CNN (03)                | 0.86    | 0.87     | 0.85        |
| V3 ResNet50 (04)           | 0.94    | 0.94     | 0.93        |
| V4 Aug CNN (05)            | 0.91    | 0.91     | 0.89        |

 **Confusion matrices** & **learning curves** are saved in the notebooks.  
 The best-model confusion matrix is stored under: `assets/confusion_matrix_V3.png`



# Decision Framework

- **Waste Management Corporation Netherlands (WMCN)** – operational owner  
- **Dutch Ministry of Infrastructure & Water Management** – regulator

 **Decision-analytic tables** & **DAPS grid** live in: `docs/`

