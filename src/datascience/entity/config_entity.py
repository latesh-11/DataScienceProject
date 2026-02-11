from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: Path
    local_data_path: Path
    unzip_dir: Path


@dataclass 
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass
class ModelTrainingConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path 
    model_name: Path
    alpha: float
    l1_ratio: float
    target_column: str 

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: str
    metric_file_name: Path
    target_column: str
    mlflow_uri: str