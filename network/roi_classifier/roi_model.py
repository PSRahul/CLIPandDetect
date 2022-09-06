import torch.nn as nn
import torch
from torchinfo import summary
from network.models.EfficientnetConv2DT.utils import get_bounding_box_prediction
import clip


class RoIModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        layers = []

        layers.append(
            nn.Conv2d(
                in_channels=1,
                out_channels=3,
                kernel_size=3,
                stride=1,
                padding=1,

            ))
        layers.append(nn.ReLU(inplace=True))
        layers.append(nn.MaxPool2d(kernel_size=16,
                                   stride=4,
                                   ))

        layers.append(
            nn.Conv2d(
                in_channels=3,
                out_channels=256,
                kernel_size=3,
                stride=1,

            ))
        layers.append(nn.ReLU(inplace=True))
        layers.append(nn.AvgPool2d(kernel_size=16,
                                   stride=4,
                                   padding=1
                                   ))
        layers.append(nn.Flatten())
        layers.append(nn.Linear(256, 512))

        self.model = nn.Sequential(*layers)

    def forward(self, masked_heatmaps_features):
        return self.model(masked_heatmaps_features)

    def print_details(self):
        pass