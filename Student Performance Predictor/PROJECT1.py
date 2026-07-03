
import pandas as pd 
# Create a simple dataset 
data = { 
'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
'Score': [35, 45, 48, 52, 60, 68, 75, 82, 88, 95] 
} 
df = pd.DataFrame(data) 
# Explore the data 
print("First 5 rows:") 
print(df.head()) 
print("\nData statistics:") 
print(df.describe())
