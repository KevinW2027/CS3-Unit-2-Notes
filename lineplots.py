import matplotlib.pyplot as plt
import numpy as np

#set the style for plots
plt.style.use('seaborn-v0_8-pastel')
print(plt.style.available)
# Use Numpy to generate a sample array of data
x_vals = np.linspace(0,10,100)
# line Plots work well when graphing Functions
# For example, y=f(x) or sin cos tan
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals))

# Show figure in the dev environment
#plt.show()
plt.savefig('lineplot.png')
plt.close() # Clear the figure before making another 

# Demo on customization
# function below y=2x
plt.plot(x_vals, 2* x_vals)
plt.title('Y=2X')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('lineplot2.png')
plt.close
