import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

# 不初始化的矩阵
x = tourch.empty(5, 3)
print(x)

# 随机数组的矩阵
x = torch.rand(5, 3)
print(x)

# 
x = torch.zeros(5, 3, dtype=torch.long)
print(x)

# 构造一个张量
x = torch.tensor([5.5, 3])
print(x)

