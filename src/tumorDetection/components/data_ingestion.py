import os
import gdown
import zipfile
import urllib.request as r
from tumorDetection import logger
from tumorDetection.entity import DataIngestionConfig


class DataIngestion:

      def __init__(self, config: DataIngestionConfig):
            self.config = config
      

      def download_file(self):
            if not os.path.exists(self.config.zip_file):
                  file_id = "1rxLRPXr-EHbiDgoPBdkB-jLm_EhaNEjo"

                  gdown.download(
                        id=file_id,
                        output=self.config.zip_file,
                        quiet=False
                  )
                  logger.info("File downloaded successfully")
            else:
                  logger.info("Folder already exists")
      

      def extract_zip_file(self):
            file = self.config.unzip_file
            os.makedirs(file, exist_ok=True)
            with zipfile.ZipFile(self.config.zip_file, "r") as f:
                  f.extractall(file)
            
            logger.info("Zip file extracted")