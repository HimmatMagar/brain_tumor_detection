from tumorDetection.entity import *
from tumorDetection.constants import *
from tumorDetection import logger
from tumorDetection.utils import *


class ConfigurationManager:

      def __init__(self, config = config):
            self.config = read_yaml(config)


            create_dir([self.config.root_artifact_dir])
      
      def get_data_ingestion_config(self) -> DataIngestionConfig:
            config = self.config.data_ingestion
            create_dir([config.root_dir])

            return DataIngestionConfig(
                  root_dir = config.root_dir,
                  data_path = config.data_path,
                  zip_file = config.zip_file,
                  unzip_file = config.unzip_file
            )

      def get_model_training_config(self) -> ModelBuildingConfig:
            config = self.config.train_model
            create_dir([config.root_dir])

            return ModelBuildingConfig(
                  root_dir = config.root_dir,
                  train_data = config.train_data,
                  model = config.model
            )