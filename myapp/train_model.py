# train_model.py
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

class SimpleDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        return self.texts[idx], self.labels[idx]

class SimpleModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_classes):
        super(SimpleModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.fc = nn.Linear(embed_dim, num_classes)

    def forward(self, x):
        x = self.embedding(x)
        x = torch.mean(x, dim=1)
        x = self.fc(x)
        return x

# Datos de ejemplo
texts = ["ejemplo de texto 1", "ejemplo de texto 2"]
labels = [0, 1]
vocab = {"ejemplo": 0, "de": 1, "texto": 2, "1": 3, "2": 4}
vocab_size = len(vocab)
embed_dim = 10
num_classes = 2

# Preprocesamiento de texto
def preprocess(text, vocab):
    return torch.tensor([vocab[word] for word in text.split()])

texts = [preprocess(text, vocab) for text in texts]

# Crear dataset y dataloader
dataset = SimpleDataset(texts, labels)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Crear modelo, criterio y optimizador
model = SimpleModel(vocab_size, embed_dim, num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entrenar el modelo
for epoch in range(10):
    for text, label in dataloader:
        optimizer.zero_grad()
        output = model(text)
        loss = criterion(output, label.clone().detach())
        loss.backward()
        optimizer.step()
    print(f'Epoch {epoch}, Loss: {loss.item()}')

# Guardar el modelo
torch.save(model.state_dict(), 'simple_model.pth')
print("Modelo guardado en simple_model.pth")
