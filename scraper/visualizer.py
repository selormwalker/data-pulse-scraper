import matplotlib.pyplot as plt
import pandas as pd
import datetime
import random
import os

def generate_mock_data(days=30):
    """Generate mock market trend data for visualization."""
    dates = [datetime.datetime.now() - datetime.timedelta(days=x) for x in range(days)]
    dates.reverse()
    values = [100 + random.uniform(-5, 5) + (x * 0.5) for x in range(days)]
    return pd.DataFrame({"Date": dates, "TrendIndex": values})

def visualize_trends(df, output_file="market_trends.png"):
    """Create a plot of the trends and save as an image."""
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["TrendIndex"], marker='o', linestyle='-', color='#00f2fe')
    plt.title("Market Sentiment Trend Analysis", fontsize=16, color='white')
    plt.xlabel("Date", color='white')
    plt.ylabel("Trend Index", color='white')
    
    # Style the plot for a dark theme
    plt.gca().set_facecolor('#0f172a')
    plt.gcf().set_facecolor('#0f172a')
    plt.tick_params(colors='white')
    plt.grid(True, alpha=0.1)
    
    plt.savefig(output_file)
    print(f"Visualization saved to {output_file}")

if __name__ == "__main__":
    print("Generating market trends...")
    data = generate_mock_data()
    visualize_trends(data)
