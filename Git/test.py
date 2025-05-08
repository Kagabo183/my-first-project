import pandas as pd

import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

print(df)

df1 = df.dropna()
print(df1)
print(df)