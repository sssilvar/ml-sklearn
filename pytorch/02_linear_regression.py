import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np

class LinearRegressionModel(nn.Module):
    def __init__ (self, input_dim, output_dim):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)

def main():
    if torch.cuda.is_available():
        dev = 'cuda'
        dtype = torch.cuda.FloatTensor
    else:
        dev = 'cpu'
        dtype = torch.FloatTensor
    
    print('Processig with: ' + dev.upper())

    x_train = np.linspace(0, 10, 11).reshape(-1, 1)
    y_train = 2 * x_train + 1

    print(x_train.shape, y_train.shape)

    # Create Linear Regression Model
    model = LinearRegressionModel(1, 1).to(dev)

    # Funtion to optimize (Mean Squared Error): criterion
    # Learning rate for optimizer: lr
    criterion = nn.MSELoss()
    lr = 0.01

    # Define an optimizer
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)

    # Set number of epochs
    epochs = 100
    for epoch in range(epochs):
        # Convert to Tensors
        inputs = Variable(torch.from_numpy(x_train)).type(dtype)
        labels = Variable(torch.from_numpy(y_train)).type(dtype)

        # Clear gradients w.r.t. parameters
        optimizer.zero_grad()

        # Forward to get output
        outputs = model(inputs)

        # Calculate loss
        loss = criterion(outputs, labels)

        # Getting gradients w.r.t. parameters
        loss.backward()

        # Update parameters
        optimizer.step()

        print('Epoch: {}, loss: {}'.format(epoch, loss.data[0]))


if __name__ == '__main__':
    main()