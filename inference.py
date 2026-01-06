import torch
import sqlite3
from model import Encoder, Decoder

checkpoint = torch.load("model.pth")
vocab = checkpoint["vocab"]
inv_vocab = {v:k for k,v in vocab.items()}

encoder = Encoder(len(vocab), 64, 128)
decoder = Decoder(len(vocab), 64, 128)
encoder.load_state_dict(checkpoint["encoder"])
decoder.load_state_dict(checkpoint["decoder"])

def predict(sentence):
    tokens = sentence.lower().split()
    x = torch.tensor([[vocab.get(w, vocab["<unk>"]) for w in tokens]])
    h, c = encoder(x)

    y = torch.tensor([[vocab["<sos>"]]])
    result = []

    for _ in range(20):
        out, h, c = decoder(y, h, c)
        token = out.argmax(2).item()
        if inv_vocab[token] == "<eos>":
            break
        result.append(inv_vocab[token])
        y = torch.tensor([[token]])

    return " ".join(result)

def run_sql(query):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

nlp = "show students whose age is less than 18"
sql = predict(nlp)

print("NLP :", nlp)
print("SQL :", sql)
print("Result :", run_sql(sql))
