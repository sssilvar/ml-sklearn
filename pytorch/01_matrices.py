import numpy as np
import torch

arr = [[1,2], [3,4]]

# Create an numpy array
np_arr = np.array(arr)
print('Numpy Array:\n', np_arr)

# Create a torch tensor
torch_arr = torch.Tensor(arr)
print('Torch Tensor:\n', torch_arr)

# Matrices with default values
ones_mat = torch.ones((2, 2))
print('Ones Tensor:\n', ones_mat)

# Set seed for random (CPU)
torch.manual_seed(0)
print('Random matrix (seed fixed) - CPU\n', torch.rand(2,2))

# Set for CUDA
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(0)
    print('Random matrix (seed fixed) - CUDA\n', torch.rand(2,2))