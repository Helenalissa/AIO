
import torch
import torch.nn as nn


class softmax(nn.Module):
    def __init__(self):
        super(softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x)


class softmax_stable(nn.Module):
    def __init__(self):
        super(softmax_stable, self).__init__()

    def forward(self, x):
        x_max = torch.max(x)
        exp_x = torch.exp(x-x_max)
        return exp_x/torch.sum(exp_x)


data = torch.Tensor([1, 2, 3])

softmax = softmax()
output = softmax(data)
print("Softmax output:", output)

softmax_stable = softmax_stable()
output_stable = softmax_stable(data)
print("Stable Softmax output:", output_stable)
