import matplotlib.pyplot as plt
import numpy as np

#set the style for plots
plt.style.use('seaborn-v0_8-pastel')
print(plt.style.available)
# Use Numpy to generate a sample array of data
x_vals = np.linspace(0,10,100)
# line Plots work well when graphing Functions
# For example, y=f(x) or sin cos tan
plt.plot(x_vals, np.sin(x_vals),label='Y=sin(x)')
plt.plot(x_vals, np.cos(x_vals),label='Y=cos(x)')

# Show figure in the dev environment
#plt.show()
plt.legend()
# Save figure in a PNG file
plt.savefig('lineplot.png')
plt.close() # Clear the figure before making another 

# Demo on customization
# function below y=mx+b
m = 2 # slope
b = 10 # y-intercept
# set the y value to equation
plt.plot(x_vals, (m * x_vals + b), label='y=2x+10',color='m')
plt.plot(x_vals, 3 * x_vals, label='y=3x',color='#379a4e')
plt.plot(x_vals,4 * x_vals, label='y=4x',linestyle='dashed')
plt.plot(x_vals, 0.5 * x_vals,label='y=0.5x',linestyle='dashdot')
plt.plot(x_vals,5 * x_vals,label='y=5x',linestyle='dotted')
# When we have an equation
plt.title('Linear Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('lineplot2.png')
plt.close

