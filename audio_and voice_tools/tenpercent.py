#make the metadata_eval set

import pandas as pd
import numpy as np

# File paths
train_file_path = r"path\to\metadata_train.csv"
eval_file_path = r"C:\path\metadata_eval.csv"


train_df = pd.read_csv(train_file_path, delimiter="|")
num_rows_to_move = int(len(train_df) * 0.15)
rows_to_move = train_df.sample(n=num_rows_to_move, random_state=42)
train_df = train_df.drop(rows_to_move.index)
eval_df = pd.read_csv(eval_file_path, delimiter="|")
eval_df = pd.concat([eval_df, rows_to_move])
train_df.to_csv(train_file_path, sep="|", index=False)
eval_df.to_csv(eval_file_path, sep="|", index=False)

print(f"Moved {num_rows_to_move} rows from metadata_train.csv to metadata_eval.csv")
