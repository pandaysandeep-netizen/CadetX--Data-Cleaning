
import pandas as pd
import json
df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna('Unknown', inplace=True)
df.to_csv('cleaned_data.csv', index=False)
