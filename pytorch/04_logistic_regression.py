import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.datasets as dsets
from torch.autograd import Variable

class LogisticRegressionModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LogisticRegressionModel, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)
    
    def forward(self, x):
        return self.linear(x)

def main():
    # 1. Load dataset (MNIST)
    train_dataset = dsets.MNIST(root='./data',
                                train=True,
                                transform=transforms.ToTensor(),
                                download=True)
    test_dataset = dsets.MNIST(root='./data',
                                train=False,
                                transform=transforms.ToTensor())
    print('[  INFO  ] Training set: %d observations | Testing set: %d observations' % 
            (len(train_dataset), len(test_dataset)))

    # 2. Set parameters
    batch_size = 100
    n_iters = 3000

    num_epochs = int(n_iters / (len(train_dataset) / batch_size))
    print('[  INFO  ] Nummber of epochs: %d' % num_epochs)

    # Create iterable object: Training dataset
    train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                                batch_size=batch_size,
                                                shuffle=True)
    test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                                batch_size=batch_size,
                                                shuffle=False)
    
    # Instanciate Model Class
    input_dim = 28 * 28
    output_dim = 10

    model = LogisticRegressionModel(input_dim, output_dim)

    # Loss function
    criterion = nn.CrossEntropyLoss()

    # Optimizer
    learning_rate = 0.001
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    # Train model
    iter = 0
    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(train_loader):
            # Load images as Variable
            images = Variable(images.view(-1, 28*28))
            labels = Variable(labels)

            # Clear gradients w.r.t. parameters
            optimizer.zero_grad()

            # Forward pass to get output/logits
            outputs = model(images)

            # Calculate Loss: softmax ---> cross entropy loss
            loss = criterion(outputs, labels)

            # Getting gradients w.r.t. parameters
            loss.backward()

            # Updating parameters
            optimizer.step()

            iter += 1

            if iter % 500 == 0:
                # Calculate Accuracy
                correct = 0
                total = 0

                # Iterate through test dataset
                for images, labels in test_loader:
                    # Load images to a Torch Variable
                    images = Variable(images.view(-1, 28*28))

                    # Forward pass only to get logits/output
                    outputs = model(images)

                    # Get predictions from the maximum value
                    _, predicted = torch.max(outputs.data, 1)

                    # Total number of labels
                    total += labels.size(0)

                    # Total correct predictions
                    correct += (predicted == labels).sum()
                
                accuracy = 100 * correct / total

                # Print loss
                print('Iteration {} | Loss: {} | Accuracy: {}'.format(iter, loss.data[0], accuracy))
                
if __name__ == '__main__':
    main()