import seaborn as sea
import matplotlib.pyplot as plt
import pandas as pd

# Reads the mtcars.csv file into a dataframe called mtcars
mtcars = pd.read_csv("Statistics/mtcars.csv")

# Prints the first few lines of mtcars
print(mtcars.head())

# summary statistics
mtcars.wt.describe() 


# Plots a box plot
sea.boxplot(data=mtcars.wt, width=0.35, whis=1.5)
plt.show()