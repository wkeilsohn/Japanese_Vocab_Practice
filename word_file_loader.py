# William Keilsohn
# June 12 2026

# Import Packages
import os
import numpy as np
import pandas as pd

# Declare Variables
### Define Files Location
cwd = os.getcwd()
file_folder = os.path.join(cwd, 'files')
word_file = os.path.join(file_folder, 'words.xlsx')

### Define DataFrame
df = pd.read_excel(word_file)

# Clean and reorganize the data
df['Furigana'] = [str(x).replace(" ", "") for x in list(df['Furigana'])]
df['Kanji'] = df['Kanji'].map(lambda x: str(x).replace(" ", "") if pd.notna(x) else x)
df['Meaning'] = [str(x).upper().lstrip() for x in list(df['Meaning'])]

# Run Application (Testing Purposes Only)
# if __name__ == '__main__':
    # print(df.head())