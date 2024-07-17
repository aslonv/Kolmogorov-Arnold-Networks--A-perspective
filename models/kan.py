import torch
import torch.nn as nn

class KAN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(KAN, self).__init__()
        self.layer1 = nn.Linear(input_dim, hidden_dim)
        self.layer2 = nn.Linear(hidden_dim, hidden_dim)
        self.layer3 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = torch.sin(self.layer1(x))  # Periodic activation
        x = torch.tanh(self.layer2(x))  # Monotonic activation
        x = self.layer3(x)
        return x