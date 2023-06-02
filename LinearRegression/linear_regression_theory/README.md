# README

## Function: `plot_data()`

### Description

The `plot_data()` function is a Python function that allows you to visualize your data using a line plot. It takes in two parameters, `x` and `y`, representing the x-axis and y-axis data respectively, and generates a line plot of the data points.

### Usage

```python
def load_data(filename):
	# Read File 
	df = pd.read_csv(filename, sep=",", index_col=False)
	df.columns = ["housesize", "rooms", "price"]
	data = np.array(df, dtype=float)
	plot_data(data[:,:2], data[:, -1])
	normalize(data)
	return data[:,:2], data[:, -1]
