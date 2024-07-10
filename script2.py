import sys
import pandas as pd
import matplotlib.pyplot as plt

def create_bar_chart(table_path):
    # Read the table into a DataFrame
    df = pd.read_csv(table_path, sep='\t')
    df = df.sort_values(by='Count', ascending=False)
    df = df.head(6)
    # Create a bar chart
    plt.figure(figsize=(25 , 15 ))  # Set figure size
    plt.bar(df['CLNDN'], df['Count'])  # Plot bar chart
    plt.xlabel('CLNDN' , fontsize=10)  # Set x-axis label
    plt.ylabel('Frequency')  # Set y-axis label
    plt.title('Frequency of CLNDN')  # Set title

    
    # Save the bar chart as an image file
    plt.savefig('clndn_frequency_chart.png')

if __name__ == "__main__":
    table_path = sys.argv[1]  # Get the table path from command line arguments
    create_bar_chart(table_path)  # Create and save the bar chart
