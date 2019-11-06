import seaborn as sns
df = sns.load_dataset('coordinates.csv')
sns.jointplot(x=df["x"], y=df["y"], kind='kde')
