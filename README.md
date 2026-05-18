# Brain Tumor Detection using CNN Transfer Learning

An end-to-end pipeline for brain tumor detection using transfer learning with PyTorch. This project includes data ingestion, model training, and a FastAPI endpoint for inference.

## Features

- Data ingestion from Google Drive (zip file extraction)
- Model training using transfer learning (CNN)
- FastAPI backend for serving predictions
- Basic HTML template for frontend (to be implemented)
- Configuration management with YAML
- Logging and artifact organization

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HimmatMagar/brain_tumor_detection.git
   cd brain_tumor_detection
   ```

2. **Create and activate the conda environment**
   ```bash
   conda create -p venv python==3.12 -y
   conda activate venv
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Data Ingestion

Run the data ingestion pipeline to download and extract the dataset:
```bash
python src/tumorDetection/pipeline/data_ingestion_pipeline.py
```

This will download the dataset from Google Drive and extract it to `artifact/data_ingestion/`.

### 2. Model Training

After data ingestion, you can train the model by running the training pipeline (to be implemented). 
Check the `src/tumorDetection/pipeline/` directory for training scripts.

### 3. Start the API

To start the FastAPI server for inference:
```bash
uvicorn api.app:app --reload
```

The API will be available at `http://localhost:8000`.

### 4. Frontend

A basic HTML template is available in `templates/index.html`. 
You can extend it to create a user interface for uploading images and getting predictions.

## Project Structure

```
brain_tumor_detection/
├── artifact/                   # Stores data and models
│   ├── data_ingestion/         # Ingested data (zip and extracted)
│   └── train_model/            # Trained models
├── api/                        # FastAPI application
│   └── app.py                  # API entry point
├── config/                     # Configuration files
│   └── config.yaml             # Data and training configuration
├── src/                        # Source code
│   └── tumorDetection/
│       ├── __init__.py         # Logging setup
│       ├── components/         # Data ingestion component
│       │   ├── __init__.py
│       │   └── data_ingestion.py
│       ├── entity/             # Configuration entities
│       │   ├── __init__.py
│       │   └── config_entity.py
│       ├── pipeline/           # Orchestration pipelines
│       │   ├── __init__.py
│       │   ├── data_ingestion_pipeline.py
│       │   └── ...             # Other pipelines (to be added)
│       ├── config/             # Configuration manager
│       │   └── __init__.py
│       └── utils/              # Utility functions
│           └── __init__.py
├── templates/                  # HTML templates
│   └── index.html
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
├── LICENSE                     # MIT License
└── README.md
```

## Configuration

The configuration is managed via `config/config.yaml`. You can modify the paths and parameters as needed.

```yaml
root_artifact_dir: artifact

data_ingestion:
  root_dir: artifact/data_ingestion
  data_path: "https://drive.google.com/uc?export=download&id=1rxLRPXr-EHbiDgoPBdkB-jLm_EhaNEjo"
  zip_file: artifact/data_ingestion/data.zip
  unzip_file: artifact/data_ingestion

train_model:
  root_dir: artifact/train_model
  train_data: artifact/data_ingestion/Training
  model: artifact/train_model/model.pth
```

## Logging

Logs are stored in the `logging/` directory and also printed to the console.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The dataset used in this project is sourced from [Brain Tumor Dataset](https://drive.google.com/file/d/1rxLRPXr-EHbiDgoPBdkB-jLm_EhaNEjo/view?usp=sharing) (Google Drive link).