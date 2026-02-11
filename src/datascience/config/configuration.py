from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import (DataIngestionConfig,DataValidationConfig)


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