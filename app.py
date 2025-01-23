import numpy as np
import pandas as pd
import gradio
import gradio as gr

def add(a, b):
    return a + b

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [1, 4, 9]})
print(df.head(2))

df.to_csv('sample.csv', index=False)
