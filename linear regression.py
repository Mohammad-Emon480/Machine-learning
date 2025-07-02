import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Read Excel file
df = pd.read_excel(r"C:\PCA data analysis\PCA_Data1.xlsx")  # Change to your file name

# Print column names to find the correct ones
print(df.columns)

# Replace 'X_column' and 'Y_column' with your actual column names
x = df['coloumb']
y = df['vdW']

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))



plt.xlabel('coloumb')
plt.ylabel('VdW')
plt.title('Linear Regression of VdW vs Coloumb')
plt.grid(True)
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()