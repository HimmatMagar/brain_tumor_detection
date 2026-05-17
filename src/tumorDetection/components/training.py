import os
import torch
import torch.nn as nn
import torch.optim as optim
from tumorDetection import logger
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from tumorDetection.entity import ModelBuildingConfig
from tumorDetection.components.model import VGG16


class TrainModel:

      def __init__(self, config: ModelBuildingConfig):
            self.config = config
      

      def prepare_data(self):
            train_data_transform = transforms.Compose([
                  transforms.Resize((128, 128)),
                  # transforms.RandomHorizontalFlip(p=0.5),
                  # transforms.RandomVerticalFlip(p=0.3),
                  # transforms.RandomRotation(degrees=15),
                  transforms.ToTensor(),
                  transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            ])

            train_dataset = datasets.ImageFolder(self.config.train_data, transform=train_data_transform)
            return DataLoader(train_dataset, batch_size=32, shuffle=True)
      

      def trainModel(self):
            load_model = VGG16()
            model = load_model.prepare_model()
            model.train()

            train_data_loader = self.prepare_data()
            
            device = "cuda" if torch.cuda.is_available() else "cpu"
            
            model.to(device)

            criterion = nn.CrossEntropyLoss()
            optimizer = optim.Adam(model.classifier.parameters(), lr=1e-4)

            for epoch in range(3):

                  total_epochs_loss = 0
                  for image, labels in train_data_loader:
                        image, labels = image.to(device), labels.to(device)
                        
                        optimizer.zero_grad()
                        output = model(image)
                        loss = criterion(output, labels)
                        loss.backward()
                        optimizer.step()
                        total_epochs_loss += loss.item()

                  avg_loss = total_epochs_loss/len(train_data_loader)
                  print(f"Epochs: {epoch + 1}, loss: {avg_loss:.4f}")
            
            model_path = os.path.join(self.config.root_dir, self.config.model)
            with open(model_path, "wb") as f:
                  torch.save(model, f)
            logger.info(f"Model Saved successfully in {model_path}")      