# NLP to SQL Query Generator (From Scratch)

This project converts natural language queries into SQL queries using a
sequence-to-sequence LSTM model trained from scratch and executes them
on an SQLite database.

## Features
- NLP to SQL conversion without pretrained models
- LSTM-based Seq2Seq architecture
- Schema-aware input support
- SQLite database execution
- Handles unseen words using <unk> token

## Tech Stack
- Python
- PyTorch
- SQLite
- VS Code

## How to Run

```bash
python create_db.py
python train.py
python inference.py
