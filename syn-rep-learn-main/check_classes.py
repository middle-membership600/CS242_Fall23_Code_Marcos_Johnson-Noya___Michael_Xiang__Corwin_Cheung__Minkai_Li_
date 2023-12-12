import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
import os
# Assuming 'args.data' is the path to your validation data and
# 'val_transform' is the set of transformations you want to apply.
val_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Create the validation dataset
val_dataset = datasets.ImageFolder(os.path.join(args.data, 'val'), val_transform)

# Print out the class_to_idx attribute
print(val_dataset.class_to_idx)
