import torch
import torch.nn as nn
import torch.optim as optim

class ModelParallelNetwork(nn.Module):
    def __init__(self):
        super(ModelParallelNetwork, self).__init__()
        self.layer1 = nn.Linear(10, 10).to('cuda:0')  # First layer on GPU 0
        self.layer2 = nn.Linear(10, 5).to('cuda:1')   # Second layer on GPU 1

    def forward(self, x):
        x = x.to('cuda:0')  # Move input to GPU 0
        x = self.layer1(x)  # First layer computation
        x = x.to('cuda:1')  # Move to GPU 1 for the next layer
        x = self.layer2(x)  # Second layer computation
        return x

# Example usage
if __name__ == '__main__':
    model = ModelParallelNetwork()
    optimizer = optim.Adam(model.parameters())
    criterion = nn.MSELoss()

    # Dummy data
    data = torch.randn(5, 10)
    target = torch.randn(5, 5)

    # Forward pass
    output = model(data)
    loss = criterion(output, target)
    print('Loss:', loss.item())
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()