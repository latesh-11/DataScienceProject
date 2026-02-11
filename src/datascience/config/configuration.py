from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import (DataIngestionConfig, DataTransformationConfig,
    DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelTrainingConfig)

class ConfigurationManager:
    def __init__ (self,
            config_filepath= CONFIG_FILE_PATH,
            params_filepath= PARAMS_FILE_PATH,
            schema_filepath= SCHEMA_FILE_PATH):

        self.config_filepath = config_filepath
        self.params_filepath = params_filepath
        self.schema_filepath = schema_filepath
    
        self.config= read_yaml(self.config_filepath)
        self.params= read_yaml(self.params_filepath)
        self.schema= read_yaml(self.schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_path = config.local_data_path,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            unzip_data_dir = config.unzip_data_dir,
            all_schema = self.schema.COLUMNS,
            STATUS_FILE= config.STATUS_FILE
        )
        return data_validation_config   
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path= config.data_path
        )

        return data_transformation_config

    def get_model_train_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        schema = self.schema.TARGET_COLUMN
        params = self.params.ElasticNet

        create_directories([config.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=  config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name= config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column=schema.name
        )
        return model_training_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        schema = self.schema.TARGET_COLUMN
        params = self.params.ElasticNet

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            test_data_path = config.test_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name=config.metric_file_name,
            target_column = schema.name,
            mlflow_uri="https://dagshub.com/sharmalatesh125/DataScienceProject.mlflow/"
        )

        return model_evaluation_config