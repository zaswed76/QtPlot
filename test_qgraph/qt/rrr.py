
import numpy as np
import pandas as pd

df = pd.DataFrame({'x': np.random.randn(100), 'y': np.random.randn(100)})
import pdvega  # import adds vgplot attribute to pandas

df.vgplot.scatter(x='x', y='y')
