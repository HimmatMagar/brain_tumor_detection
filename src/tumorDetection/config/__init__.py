from tumorDetection.entity import *
from tumorDetection.constants import *
from tumorDetection import logger
from tumorDetection.utils import *


class ConfigurationManager:

      def __init__(self, config = config, params = params):
            self.config = read_yaml(config)
            self.params = read_yaml(params)


            create_dir([self.config.root_artifact_dir])