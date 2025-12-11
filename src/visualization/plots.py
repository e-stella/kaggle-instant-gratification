import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, col):
    plt.figure(figsize=(6,4))
    sns.histplot(df[col])
    plt.title(col)
    plt.show()