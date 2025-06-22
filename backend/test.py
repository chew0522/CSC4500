import pandas as pd

df = pd.read_csv('C:\\Users\\dcbc0\\Desktop\\UPM\\Sem 4\\csc4500\\backend\\malicious_phish.csv')  # Make sure the CSV file has 'url' and 'label' columns

# Optional mapping, for example
label_map = {0: 'benign', 1: 'defacement', 2: 'phishing'}

for val in df['type'].unique():
    print(f"{val}: {label_map.get(val, 'unknown')}")
