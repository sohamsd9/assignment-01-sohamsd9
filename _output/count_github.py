import pandas as pd
import glob

count = 0
for file in glob.glob("*.csv"):
    df = pd.read_csv(file, encoding='utf-8', errors='ignore')
    count += df.apply(lambda row: row.astype(str).str.contains("GitHub", case=False).any(), axis=1).sum()

print(f"Total lines containing 'GitHub': {count}")
