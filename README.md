# Fashion Tagger Reproduction

A local reproduction of the Fashion Florence model for clothing attribute prediction.

## Features

Given a clothing image, the API predicts:
- `category`
- `primary_color`
- `material`
- `style_tags`

The API returns the predictions as JSON.

## Requirements

- Python 3.11
- Git
- Internet access for the initial model download
- Sufficient disk space and memory

CPU inference is supported but may be slow.

## Installation on Windows

Clone this repository:

```powershell
git clone https://github.com/EurusMao/fashion-tagger-reproduction.git
cd fashion-tagger-reproduction
```

Create a virtual environment:

```powershell
py -3.11 -m venv .venv
```

Install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r .\space\requirements.txt
```

## Start the API

From the repository root, run:

```powershell
.\.venv\Scripts\python.exe .\space\run_local.py
```

Wait for the model to load. The API should run at `http://127.0.0.1:8000`.

Keep this terminal open.

## Test with an image

Open a second PowerShell window and navigate to the repository folder. Run:

```powershell
curl.exe -X POST `
  -F "file=@path\to\your_image.png" `
  http://127.0.0.1:8000/analyze
```

Replace `path\to\your_image.png` with the actual image path.

The response should contain the predicted clothing attributes in JSON format.

## Model and limitations

The model is downloaded from Hugging Face on first startup. Internet access is required for the initial download, which may take time.

Predictions are estimates and are not guaranteed to be correct. Files in `results/` are example outputs, not a comprehensive accuracy evaluation.

This repository runs inference; it does not retrain the model.
