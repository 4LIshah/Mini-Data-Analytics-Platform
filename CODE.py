import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_dataset(file_path):
    try:
        dataset = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        print(dataset.head(10))
        return dataset
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def clean_dataset(dataset):
    # Handle missing values
    for column in dataset.columns:
        if dataset[column].dtype == 'object':
            dataset[column].fillna(dataset[column].mode()[0], inplace=True)
        else:
            dataset[column].fillna(dataset[column].mean(), inplace=True)

    # Remove duplicates
    dataset.drop_duplicates(inplace=True)

    print("Dataset cleaned successfully!")
    print(dataset.info())
    return dataset

def calculate_statistics(dataset):
    numeric_columns = dataset.select_dtypes(include=['float64', 'int64']).columns
    stats = {}
    for column in numeric_columns:
        stats[column] = {
            'mean': dataset[column].mean(),
            'median': dataset[column].median(),
            'std_dev': dataset[column].std()
        }
    print("Statistics calculated:")
    for column, stat in stats.items():
        print(f"{column} -> Mean: {stat['mean']}, Median: {stat['median']}, Std Dev: {stat['std_dev']}")

def count_unique_values(dataset):
    column = input("Enter the name of the categorical column to analyze: ")
    if column in dataset.columns and dataset[column].dtype == 'object':
        counts = dataset[column].value_counts()
        print(f"Unique value counts for {column}:")
        print(counts)
    else:
        print("Invalid column name or column is not categorical.")

def generate_visualizations(dataset):
    while True:
        print("Visualization Options:")
        print("1. Bar Chart for Categorical Column")
        print("2. Histogram for Numeric Column")
        print("3. Scatter Plot for Two Numeric Columns")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            column = input("Enter the categorical column name: ")
            if column in dataset.columns and dataset[column].dtype == 'object':
                sns.countplot(data=dataset, x=column)
                plt.title(f"Bar Chart for {column}")
                plt.savefig(f"{column}_bar_chart.png")
                plt.show()
            else:
                print("Invalid column name or column is not categorical.")
        elif choice == '2':
            column = input("Enter the numeric column name: ")
            if column in dataset.columns and dataset[column].dtype in ['float64', 'int64']:
                plt.hist(dataset[column], bins=30, color='blue', alpha=0.7)
                plt.title(f"Histogram for {column}")
                plt.savefig(f"{column}_histogram.png")
                plt.show()
            else:
                print("Invalid column name or column is not numeric.")
        elif choice == '3':
            col1 = input("Enter the first numeric column name: ")
            col2 = input("Enter the second numeric column name: ")
            if col1 in dataset.columns and col2 in dataset.columns and \
               dataset[col1].dtype in ['float64', 'int64'] and dataset[col2].dtype in ['float64', 'int64']:
                plt.scatter(dataset[col1], dataset[col2], alpha=0.7)
                plt.title(f"Scatter Plot: {col1} vs {col2}")
                plt.savefig(f"scatter_{col1}_vs_{col2}.png")
                plt.show()
            else:
                print("Invalid column names or columns are not numeric.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

def export_dataset(dataset):
    file_name = input("Enter the file name to save the cleaned dataset (with .csv extension): ")
    try:
        dataset.to_csv(file_name, index=False)
        print(f"Dataset exported successfully as {file_name}")
    except Exception as e:
        print(f"Error exporting dataset: {e}")

def main():
    print("Mini Data Analytics Platform")
    file_path = "C:\\Users\\xlish\\Downloads\\archive\\batting_stats_T20I.csv"
    dataset = None

    while True:
        print("\nMenu:")
        print("1. Load Dataset")
        print("2. Clean Dataset")
        print("3. Calculate Statistics")
        print("4. Count Unique Values")
        print("5. Generate Visualizations")
        print("6. Export Dataset")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            dataset = load_dataset(file_path)
        elif choice == '2' and dataset is not None:
            dataset = clean_dataset(dataset)
        elif choice == '3' and dataset is not None:
            calculate_statistics(dataset)
        elif choice == '4' and dataset is not None:
            count_unique_values(dataset)
        elif choice == '5' and dataset is not None:
            generate_visualizations(dataset)
        elif choice == '6' and dataset is not None:
            export_dataset(dataset)
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice or dataset not loaded. Please try again.")

if __name__ == "__main__":
    main()
