import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class LibraryDashboard:

    def __init__(self, file_path): 
        self.data = self.load_data(file_path)
        print("Dataset loaded and validated successfully.")

    def load_data(self, file_path):
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Error: The file '{file_path}' was not found.")
        if not file_path.lower().endswith('.csv'):
            raise ValueError("Error: The provided file is not a CSV file.")

      
        df = pd.read_csv(file_path)

        required_columns = ['Transaction ID', 'Date', 'User ID', 'Book Title', 'Genre', 'Borrowing Duration (Days)']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("Error: CSV file is missing one or more required columns.")
            
        
        if df.isnull().sum().sum() > 0:
            print("Warning: Missing data found. Rows with null values will be dropped.")
            df.dropna(inplace=True)

        try:
            df['Date'] = pd.to_datetime(df['Date'])
        except ValueError as e:
            raise ValueError(f"Error parsing dates: {e}. Ensure 'Date' is in YYYY-MM-DD format.")

        return df
    def calculate_statistics(self):
     
        stats = {}
      
        stats['most_borrowed_book'] = self.data['Book Title'].mode()[0]
        

        borrowing_durations = self.data['Borrowing Duration (Days)'].values
        stats['avg_borrowing_duration'] = np.mean(borrowing_durations)
        stats['std_dev_borrowing_duration'] = np.std(borrowing_durations)
        

        stats['busiest_day'] = self.data['Date'].dt.day_name().mode()[0]
        
        return stats
    def generate_report(self):
     
        stats = self.calculate_statistics()
        print("\n" + "="*40)
        print("        E-Library Analytics Report")
        print("="*40)
        print(f"Total Transactions: {len(self.data)}")
        print(f"Unique Books Borrowed: {self.data['Book Title'].nunique()}")
        print(f"Unique Users: {self.data['User ID'].nunique()}")
        print("-" * 40)
        print("Key Insights:")
        print(f"  - Most Popular Book: '{stats['most_borrowed_book']}'")
        print(f"  - Busiest Borrowing Day: {stats['busiest_day']}")
        print(f"  - Avg. Borrowing Duration: {stats['avg_borrowing_duration']:.2f} days")
        print(f"  - Std. Dev. of Duration: {stats['std_dev_borrowing_duration']:.2f} days")
        print("="*40 + "\n")
    
    def plot_top_books(self, n=5):
   
        plt.figure(figsize=(10, 6))
        top_books = self.data['Book Title'].value_counts().nlargest(n)
        sns.barplot(x=top_books.values, y=top_books.index, palette='viridis')
        plt.title(f'Top {n} Most Borrowed Books', fontsize=16)
        plt.xlabel('Number of Borrows', fontsize=12)
        plt.ylabel('Book Title', fontsize=12)
        plt.tight_layout()
        plt.show()

    def plot_borrowing_trends_over_time(self):
   
        monthly_trends = self.data.set_index('Date').resample('M').size()
        plt.figure(figsize=(12, 6))
        sns.lineplot(x=monthly_trends.index, y=monthly_trends.values, marker='o')
        plt.title('Borrowing Trends Over Months', fontsize=16)
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Number of Transactions', fontsize=12)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_genre_distribution(self):

        genre_counts = self.data['Genre'].value_counts()
        plt.figure(figsize=(10, 8))
        plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140,
                colors=sns.color_palette('pastel'))
        plt.title('Distribution of Books Borrowed by Genre', fontsize=16)
        plt.ylabel('')  
        plt.show()

    def plot_borrowing_heatmap(self):
        
        df_copy = self.data.copy()
        df_copy['Month'] = df_copy['Date'].dt.strftime('%B')
        df_copy['DayOfWeek'] = df_copy['Date'].dt.day_name()
        
   
        activity_pivot = df_copy.pivot_table(
            index='DayOfWeek',
            columns='Month',
            values='Transaction ID',
            aggfunc='count'
        ).fillna(0)
        
       
        days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                        'July', 'August', 'September', 'October', 'November', 'December']
        activity_pivot = activity_pivot.reindex(index=days_order, columns=[m for m in months_order if m in activity_pivot.columns])

        plt.figure(figsize=(14, 8))
        sns.heatmap(activity_pivot, cmap='YlGnBu', annot=True, fmt=".0f", linewidths=.5)
        plt.title('Borrowing Activity: Day of Week vs. Month', fontsize=16)
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Day of Week', fontsize=12)
        plt.show()


def main():
 
    print("Welcome to the E-Library Data Insights Dashboard!")
    
    try:
        file_path = input("Please enter the path to the library transaction CSV file: ")
        dashboard = LibraryDashboard(file_path)
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return

    while True:
        print("\nPlease choose an option:")
        print("1. Display Summary Report")
        print("2. Show Top 5 Borrowed Books (Bar Chart)")
        print("3. Show Borrowing Trends by Month (Line Chart)")
        print("4. Show Genre Distribution (Pie Chart)")
        print("5. Show Borrowing Activity Heatmap")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            dashboard.generate_report()
        elif choice == '2':
            dashboard.plot_top_books()
        elif choice == '3':
            dashboard.plot_borrowing_trends_over_time()
        elif choice == '4':
            dashboard.plot_genre_distribution()
        elif choice == '5':
            dashboard.plot_borrowing_heatmap()
        elif choice == '6':
            print("Thank you for using the E-Library Dashboard. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
    