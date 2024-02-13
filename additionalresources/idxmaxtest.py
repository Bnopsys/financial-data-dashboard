import pandas as pd
import numpy as np
import timeit

# Creating a large DataFrame
data = {'A': np.random.randint(0, 100, 1000000)}
df = pd.DataFrame(data)

# Using idxmax with vectorization
start_time = timeit.default_timer()
idx_of_max = df['A'].idxmax()
elapsed_time = timeit.default_timer() - start_time

print(f"Index of max value: {idx_of_max}")
print(f"Elapsed time with idxmax: {elapsed_time} seconds")

# Using manual iteration to find max value index
start_time = timeit.default_timer()
max_value = max(df['A'])
idx_of_max_manual = df['A'][df['A'] == max_value].index[0]
elapsed_time_manual = timeit.default_timer() - start_time

print(f"Index of max value (manual): {idx_of_max_manual}")
print(f"Elapsed time with manual iteration: {elapsed_time_manual} seconds")
