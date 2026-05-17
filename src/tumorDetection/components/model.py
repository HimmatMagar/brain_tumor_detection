from tumorDetection import logger
from torchvision import models
import torch.nn as nn

class VGG16:

      def __init__(self):
            self.model = models.vgg16()

      def prepare_model(self):
            self.model.classifier = nn.Sequential(
                  nn.Linear(in_features=25088, out_features=512, bias=True),
                  nn.ReLU(),
                  nn.Dropout(p=0.5),
                  nn.Linear(in_features=512, out_features=4, bias=True)
            )

            for params in self.model.features:
                  params.requires_grad = False

            logger.info(f"Downloaded Model: {self.model}")
            return self.model