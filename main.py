import pandas as pd
import numpy as np

data = {'name' : ['Alice','Bob', 'Charlie', 'Jane',' Rose'], 'age' : [16, 21, 18, 25, 30]}
df = pd.DataFrame(data)
df.head()