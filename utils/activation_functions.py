import torch

def periodic_activation(x):
    return torch.sin(x)

def monotonic_activation(x):
    return torch.tanh(x)