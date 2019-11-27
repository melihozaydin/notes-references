# %%
# ^^^ This will mark a cell points you can click 'Run Cell'
# to run each cell
import numpy as np
import matplotlib.pyplot as plt
print('Cell 1')
print('hello Melih')

# %%
print('Cell 2')
x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y)
plt.plot(x, z)
plt.show()

"""
if you run cell 2 befor cell 1 it will raise an error and
not recognize numpy commands because you didn't technically imported it.
"""
