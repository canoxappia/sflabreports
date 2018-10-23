import pandas as pd

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},'B': {0: 1, 1: 3, 2: 5},'C': {0: 2, 1: 4, 2: 6}})

df.columns = [list('ABC'), list('DEF')]

x = pd.melt(df, id_vars=['D'], value_vars=['F'])

print(x)