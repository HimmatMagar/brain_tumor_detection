from tumorDetection.entity import *
from tumorDetection.constants import *
from tumorDetection import logger
from tumorDetection.utils import *


class ConfigurationManager:

      def __init__(self, config = config, params = params):
            self.config = read_yaml(config)
            self.params = read_yaml(params)


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