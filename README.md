# Fashion Tagger Reproduction

A local reproduction of the Fashion Florence model for clothing attribute prediction, based on the original [Loom project](https://github.com/anushreeberlia/loom).

This project focuses on running the pretrained model locally to extract structured fashion attributes from clothing images.

## Features

Given a clothing image, the model predicts:

- **Category** — clothing category
- **Primary Color** — the main visible color
- **Material** — predicted material or fabric structure
- **Style Tags** — descriptive style labels

The predictions are returned as structured JSON.

## Project Structure

```text
fashion-tagger-reproduction/
├── space/
│   ├── app.py
│   ├── requirements.txt
│   └── run_local.py
├── results/
│   ├── first_prediction.json
│   └── single_item_prediction.json
├── .gitignore
└── README.md
```

- `space/app.py`: Implements the image-analysis API.
- `space/requirements.txt`: Lists the required Python dependencies.
- `space/run_local.py`: Starts the local API and applies a compatibility workaround for model loading.
- `results/`: Contains example prediction outputs.

## Requirements

- Python 3.11
- Git
- An internet connection for the initial model download
- Sufficient disk space and RAM

The model weights are approximately 3.11 GB. Additional disk space is needed for Python dependencies and cached files.

CPU inference is supported, but processing may be slow.

## Installation

### 1. Clone the Repository

```powershell
git clone https://github.com/EurusMao/fashion-tagger-reproduction.git
cd fashion-tagger-reproduction
```

### 2. Create a Virtual Environment

```powershell
py -3.11 -m venv .venv
```

### 3. Install Dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r .\space\requirements.txt
```

## Run the Local API

From the repository root, run:

```powershell
.\.venv\Scripts\python.exe .\space\run_local.py
```

Wait for the model to load. Once startup is complete, the API should be available at:

`http://127.0.0.1:8000`

Keep the terminal running while using the API.

**Note:** This is a local API service, not a publicly hosted endpoint. The address `127.0.0.1` refers to the computer running the service.

## Test with a Clothing Image

Open a second PowerShell terminal and navigate to the repository directory.

Place a clothing image in the repository root, for example, `test_clothing.png`.

Submit the image to the API:

```powershell
curl.exe -X POST `
  -F "file=@test_clothing.png" `
  http://127.0.0.1:8000/analyze
```

Replace `test_clothing.png` with the path to your own image.

The API should return a JSON response containing the predicted fashion attributes.

## Example Output

```json
{
  "category": "layer",
  "primary_color": "pink",
  "material": "knit",
  "style_tags": [
    "casual",
    "trendy"
  ]
}
```

This is an illustrative example of the response format. Actual predictions depend on the input image.

## Results

The `results/` directory contains example outputs generated during local model inference.

These examples demonstrate the model's ability to generate structured fashion tags. They do not represent a comprehensive accuracy evaluation.

## Limitations

- Predictions are model-generated estimates and may be incorrect.
- Material predictions describe visual appearance and cannot verify the garment's actual fiber composition.
- The current API returns one set of attributes per image. It does not independently detect and classify every garment in a multi-item collage.
- This repository runs inference using a pretrained model; it does not retrain the model.
- The initial model download requires an internet connection and may take time.
- The local compatibility workaround in `run_local.py` bypasses the `flash_attn` import check during model loading. It has been tested in the development environment, but compatibility should be verified on other machines.

## References

- **Original Project:** [Loom](https://github.com/anushreeberlia/loom)
- **Pretrained Model:** [Fashion Florence on Hugging Face](https://huggingface.co/anushreeberlia/fashion-florence)

Please consult the original project and model repositories for their applicable licenses, attribution requirements, and usage conditions.
