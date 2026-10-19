# Fashion Tagger: Clothing Classification and Digital Wardrobe

## 1. Project Overview

Fashion Tagger is an AI-powered digital wardrobe project designed to help users organize their clothing items and support future outfit recommendation features.

The project builds on Loom and the existing Fashion Florence model. Our goal is to improve clothing classification and attribute extraction by fine-tuning the existing model for more detailed and accurate fashion categories.

Rather than building an entirely new vision model from scratch, we aim to adapt an existing fashion-focused model to better meet the needs of our application.

**Current status:** Existing model reproduction and initial experimentation completed. Fine-tuning and model improvement are planned next steps.

## 2. Project Objectives

- Reproduce and run the existing Fashion Florence model locally.
- Analyze its clothing classification and attribute extraction capabilities.
- Prepare a fashion image dataset with consistent category labels.
- Fine-tune the existing model to improve recognition of specific clothing categories.
- Compare the original model with the fine-tuned model.
- Integrate the improved model into the digital wardrobe application.

## 3. Existing Model

**Base project:** Loom  
**Model:** [Fashion Florence](https://huggingface.co/anushreeberlia/fashion-florence)  
**Underlying architecture:** Florence-2-large  
**Framework:** PyTorch and Hugging Face Transformers

Fashion Florence is an existing model fine-tuned for fashion-related image understanding and attribute extraction.

The current Loom implementation provides a local interface for submitting clothing images and returning structured predictions, including clothing category, color, material, and style-related information.

We will retain this implementation as the foundation for subsequent model improvement.

## 4. Dataset

**Dataset source:** [Marqo/iMaterialist on Hugging Face](https://huggingface.co/datasets/Marqo/iMaterialist)

The dataset provides fashion images and attributes such as category, color, material, pattern, sleeve type, neckline, and style.

For our initial experiments, we streamed a subset of the dataset and collected approximately 1,000 images. We mapped the original fine-grained categories into five broad labels:

| Label | Examples |
|---|---|
| `top` | T-shirts, blouses, tank tops, sweaters |
| `bottom` | Pants, jeans, shorts, skirts |
| `dress` | Dresses, jumpsuits, rompers |
| `outerwear` | Jackets, coats, blazers |
| `other` | Swimwear, lingerie, sleepwear, selected footwear |

After correcting several category mappings and excluding five images labeled as Petticoats, the second dataset version contains 995 images.

| Split | Images |
|---|---:|
| Training | 695 |
| Validation | 148 |
| Test | 152 |
| **Total** | **995** |

The full source dataset is not stored in this repository. The data preparation scripts and dataset source will be documented to support reproducibility.

## 5. Work Completed

### Existing Model Reproduction

- Set up the local Python environment.
- Ran the existing Fashion Florence model through the Loom implementation.
- Tested clothing images and inspected the returned predictions.
- Established a starting point for further model evaluation.

### Initial CNN Experiment

To explore the classification task, we implemented a small CNN trained from randomly initialized weights.

This experiment is a preliminary baseline, not the intended final model.

The second experiment achieved:

| Metric | Result |
|---|---:|
| Best validation accuracy | 41.2% |
| Test accuracy | 42.1% |
| Correct test predictions | 64 / 152 |

The model performed unevenly across categories. Test recall for `dress` was only 6.9%, while the model frequently predicted `top` for images belonging to other categories.

These findings suggest that the initial model struggles to distinguish visually similar clothing categories and that the data, model capacity, and training strategy require further investigation.

The CNN experiment helped us establish a reproducible training and evaluation workflow and identify potential challenges in fashion classification.

## 6. Current Challenges

### Fine-Grained Classification

Broad categories do not fully capture the distinctions needed for a digital wardrobe. We ultimately want to distinguish more specific items, such as blouses, T-shirts, cardigans, jackets, skirts, and dresses.

### Attribute Accuracy

The application also needs useful attributes such as color, material, and style. These predictions should be evaluated separately rather than assuming that correct category classification guarantees accurate attributes.

### Dataset Quality

Images may differ in background, composition, pose, and presentation style. Original dataset categories also need consistent mapping to the labels required by our application.

### Model Adaptation

The initial CNN is not sufficiently accurate for our intended application. We plan to investigate fine-tuning Fashion Florence rather than relying on a newly trained CNN as the final solution.

## 7. Planned Approach

### Step 1: Inspect the Existing Model

Review the Fashion Florence architecture, model-loading procedure, inference prompts, and training configuration.

### Step 2: Prepare Fine-Tuning Data

Create a dataset with consistent image-label pairs and more detailed clothing categories. Determine whether category prediction and attribute extraction should be trained as separate tasks or within a structured output format.

### Step 3: Fine-Tune Fashion Florence

Investigate the model's supported training workflow and parameter-efficient fine-tuning methods, such as LoRA, subject to available compute resources.

### Step 4: Evaluate Model Improvements

Compare the original model and the fine-tuned model on the same held-out images using appropriate classification and attribute-level metrics.

### Step 5: Integrate the Improved Model

Connect the selected model to the existing Loom interface and use its predictions to support the digital wardrobe prototype.

## 8. Repository Structure

```text
fashion-tagger-reproduction/
├── space/
│   ├── app.py
│   ├── requirements.txt
│   └── run_local.py
├── training/
│   ├── prepare_dataset.py
│   ├── prepare_labels_v2.py
│   ├── split_dataset_v2.py
│   ├── train_cnn_v2.py
│   ├── evaluate_v2.py
│   ├── inspect_labels_v2.py
│   ├── analyze_errors_v2.py
│   ├── analyze_predictions_v2.py
│   └── diagnose_train_predictions_v2.py
├── results/
│   ├── training_history_v2.csv
│   ├── test_predictions_v2.csv
│   ├── confusion_matrix_v2.csv
│   └── test_summary_v2.json
├── README.md
└── .gitignore
```

The CNN scripts and results document the preliminary baseline experiment. Future training scripts for Fashion Florence fine-tuning will be added after the model's training interface and data requirements have been verified.

## 9. Reproducibility and Resources

The repository is intended to preserve the code, experiment configurations, and evaluation results needed to reproduce our work.

The complete source dataset and local virtual environment are not included in the repository. Users should obtain the dataset from its official source and follow the applicable dataset terms.

The existing model and the planned fine-tuning workflow may require more computational resources than the small CNN baseline. Available hardware and training feasibility will be evaluated before full fine-tuning begins.

## 10. Technologies

- Python
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- Pillow
- NumPy
- Loom

## 11. Project Status

This project is under active development.

The existing Fashion Florence model has been reproduced locally, and an initial CNN experiment has been completed. We have identified limitations in fine-grained clothing classification and are preparing to investigate fine-tuning the existing model.

The fine-tuned model and its performance improvements have **not yet been completed or verified**.

## 12. Dataset Reference

Dataset: [Marqo/iMaterialist](https://huggingface.co/datasets/Marqo/iMaterialist)

The dataset should be cited and used according to its official documentation and applicable terms.
