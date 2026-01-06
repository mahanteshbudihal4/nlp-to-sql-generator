import torch
import torch.nn as nn
import pandas as pd
from model import Encoder, Decoder

df = pd.read_csv("data.csv")

def tokenize(s):
    return s.lower().split()

nlp_tokens = [tokenize(x) for x in df["nlp"]]
sql_tokens = [tokenize(x) for x in df["sql"]]

vocab = {"<pad>":0, "<sos>":1, "<eos>":2, "<unk>":3}
for sent in nlp_tokens + sql_tokens:
    for w in sent:
        if w not in vocab:
            vocab[w] = len(vocab)

def encode(sent):
    return [vocab.get(w, vocab["<unk>"]) for w in sent]

    

X = [encode(x) for x in nlp_tokens]
Y = [[vocab["<sos>"]] + encode(y) + [vocab["<eos>"]] for y in sql_tokens]

encoder = Encoder(len(vocab), 64, 128)
decoder = Decoder(len(vocab), 64, 128)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(
    list(encoder.parameters()) + list(decoder.parameters()), lr=0.001
)

for epoch in range(300):
    total_loss = 0
    for x, y in zip(X, Y):
        x = torch.tensor(x).unsqueeze(0)
        y = torch.tensor(y).unsqueeze(0)

        h, c = encoder(x)
        out, _, _ = decoder(y[:, :-1], h, c)

        loss = criterion(
            out.reshape(-1, len(vocab)),
            y[:, 1:].reshape(-1)
        )

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss:.2f}")

torch.save({
    "encoder": encoder.state_dict(),
    "decoder": decoder.state_dict(),
    "vocab": vocab
}, "model.pth")

print("Model trained and saved")
