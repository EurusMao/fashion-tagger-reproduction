# Fashion Tagger: Clothing Classification and Digital Wardrobe

## 1. Project Overview

Fashion Tagger is an AI-powered digital wardrobe project designed to help users organize their clothing items and support future outfit recommendation features.

The project builds on Loom and the existing Fashion Florence model. Our goal is to improve clothing classification and attribute extraction by fine-tuning the existing model for more detailed and accurate fashion categories.

Rather than building an entirely new vision model from scratch, we aim to adapt an existing fashion-focused model to better meet the needs of our application.

**Current Status**: Existing model reproduction and initial experimentation completed. Fine-tuning and model improvement are planned next steps.

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

The current implementation supports CPU execution. CUDA is used automatically when an available CUDA-compatible GPU is detected.

- Download the GitHub repository as a ZIP file and extract it to your computer.
- Open the extracted project folder in your Python environment (e.g., PyCharm).
- Before running the model, install all dependencies listed in space/requirements.txt
- Run the **run_local.py** file, wait for the model to load and the local server to start.
- Once the URL is open:
    Find the POST /analyze endpoint.
    Click Try it out.
    Upload a clothing image.
    Click Execute to run the model.
    View the returned JSON predictions.
The model should return structured fashion attributes, including clothing category, color, material, and style tags.

## 6. Current Challenges

### Fine-Grained Classification

Broad categories do not fully capture the distinctions needed for a digital wardrobe. We want to distinguish more specific items, such as blouses, T-shirts, cardigans, jackets, skirts, and dresses.

### Attribute Accuracy

The application also needs useful attributes such as color, material, and style. These predictions should be evaluated separately rather than assuming that correct category classification guarantees accurate attributes.

## 7. Repository Structure

```text
fashion-tagger-reproduction/
├── space/
│   ├── app.py
│   ├── requirements.txt
│   └── run_local.py
├── training/
│   ├── prepare_dataset.py
│   ├── prepare_labels_v2.py
│   └── split_dataset_v2.py
├── results/
│   └── dataset preparation results
├── README.md
└── .gitignore
```
Dataset: [Marqo/iMaterialist](https://huggingface.co/datasets/Marqo/iMaterialist)

The dataset should be cited and used according to its official documentation and applicable terms.
