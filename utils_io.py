import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

def load_step(step_name):
    return pd.read_csv(DATA_DIR / f"{step_name}.csv")

def save_step(df, step_name):
    df.to_csv(DATA_DIR / f"{step_name}.csv", index=False)
    print(f"Saved {step_name}.csv")
