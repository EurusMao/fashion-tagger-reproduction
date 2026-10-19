# Fashion Tagger: Clothing Classification and Digital Wardrobe

## Project Overview

This project explores an AI-powered digital wardrobe system that helps users organize clothing items and supports future outfit recommendation features.

The current development focuses on building and evaluating an image classification pipeline for clothing categories. We are experimenting with a small Convolutional Neural Network (CNN) trained from scratch using the PyTorch framework.

The project is currently in the model development and evaluation stage.

## Project Goals

- Build a reproducible clothing image classification pipeline.
- Collect and preprocess fashion images.
- Map fine-grained clothing categories into five broader classes.
- Train and evaluate a CNN model.
- Analyze classification errors and identify areas for improvement.
- Integrate the trained model into the digital wardrobe application in a later stage.

## Dataset

**Dataset:** [Marqo/iMaterialist on Hugging Face](https://huggingface.co/datasets/Marqo/iMaterialist)

The dataset contains clothing images and associated attributes, including category, color, material, pattern, sleeve type, neckline, and style.

We use the original `category` field to create five broad classification labels:

| Label | Examples |
|---|---|
| `top` | T-shirts, blouses, sweaters, tank tops |
| `bottom` | Pants, jeans, shorts, skirts |
| `dress` | Dresses, casual dresses, jumpsuits and rompers |
| `outerwear` | Jackets, coats, blazers |
| `other` | Swimwear, lingerie, sleepwear, selected footwear |

These labels are project-defined categories rather than the original dataset taxonomy.

### Data Processing

The current pipeline:

1. Streams a limited number of records from the original dataset rather than downloading the entire dataset.
2. Selects images belonging to the target clothing categories.
3. Maps the original categories into five broad labels.
4. Resizes images to 128 × 128 pixels.
5. Creates training, validation, and test splits.

The second dataset version excludes five images labeled as `Petticoats` and corrects the mapping of `Dress Shirts` to `top`.

The resulting dataset contains 995 images.

| Split | Images |
|---|---:|
| Training | 695 |
| Validation | 148 |
| Test | 152 |
| **Total** | **995** |

The original dataset is not included in this repository. Users should access it through the official Hugging Face page and follow its applicable usage terms and citation requirements.

## Model

We implemented a small CNN using PyTorch, trained from randomly initialized weights.

Model configuration:

- Input image size: 128 × 128 pixels
- Output classes: 5
- Trainable parameters: 98,565
- Optimizer: Adam
- Batch size: 32
- Training epochs: 15
- Execution device: CPU

The model uses convolutional layers, batch normalization, ReLU activations, max pooling, adaptive average pooling, and a fully connected classification layer.

## Current Results

The second CNN experiment achieved the following results:

| Metric | Result |
|---|---:|
| Best validation accuracy | 41.2% |
| Best checkpoint epoch | 6 |
| Test accuracy | 42.1% |
| Correct test predictions | 64 / 152 |
| Training accuracy at the selected checkpoint | 42.9% |

### Per-Class Test Recall

| Class | Recall |
|---|---:|
| `bottom` | 56.7% |
| `dress` | 6.9% |
| `other` | 60.0% |
| `outerwear` | 30.0% |
| `top` | 54.5% |

These results indicate that the model has not yet learned to distinguish all clothing categories reliably.

### Current Challenges

**1. Prediction imbalance**

The model predicts `top` 63 times in the test set, although only 33 images actually belong to that category. This suggests a strong tendency to overpredict `top`.

**2. Poor dress recognition**

Only 2 of the 29 test images labeled `dress` were correctly classified. The model frequently confuses dresses with tops.

**3. Limited training data and model capacity**

The current experiment uses fewer than 1,000 images and a small CNN trained from scratch. The model may not learn sufficiently robust visual features from this limited dataset.

**4. Variation in image presentation**

The dataset includes different product photography styles, backgrounds, poses, and image compositions. These variations may make classification more difficult.

**5. Category ambiguity**

Some clothing categories have similar visual characteristics. The project needs consistent label definitions and further inspection of potentially ambiguous samples.

## Current Development Status

### Completed

- Dataset streaming and image collection
- Clothing category mapping and data cleaning
- Training, validation, and test split generation
- Baseline CNN implementation and training
- Test-set evaluation
- Confusion matrix and per-class recall analysis
- Error inspection and prediction distribution analysis

### In Progress

- Investigating the CNN's prediction bias
- Improving classification performance, especially for `dress` and `outerwear`
- Reviewing data quality and category definitions
- Comparing potential model improvement strategies

### Future Work

- Experiment with improved training strategies and data augmentation.
- Evaluate class-weighted loss and pretrained image models.
- Compare model performance using consistent evaluation metrics.
- Integrate the selected model into the digital wardrobe prototype.
- Explore additional attributes such as color, material, and style.

## Repository Structure

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

The repository structure may evolve as development continues. Generated datasets, model checkpoints, and local environment files are not necessarily included in version control.

## Reproducibility

The training and evaluation scripts are maintained separately so that each stage can be inspected and rerun.

The intended workflow is:

1. Prepare the dataset.
2. Apply the corrected category mapping.
3. Generate the data splits.
4. Train the CNN.
5. Evaluate the saved model on the test set.
6. Inspect prediction errors and record findings.

Exact execution instructions and dependency versions will be maintained alongside the scripts as the pipeline is finalized.

## Technologies

- Python
- PyTorch
- Hugging Face Datasets
- NumPy
- Pillow
- CSV-based experiment tracking

## Dataset Citation

Guo, S., Huang, W., Zhang, X., Srikhanta, P., Cui, Y., Li, Y., Scott, M. R., Adam, H., & Belongie, S. (2019). *The iMaterialist Fashion Attribute Dataset*. arXiv preprint arXiv:1906.05750.

Dataset: https://huggingface.co/datasets/Marqo/iMaterialist

## Project Status

This is an ongoing academic project. The current CNN is a baseline model, and its classification performance remains limited. The findings reported here represent intermediate experimental results rather than a final production-ready system.
