import pandas as pd

class DataCleaner:
    def __init__(self, data):
        """
        Initialize the DataCleaner with a pandas DataFrame.
        
        Args:
            data (pd.DataFrame): The data to be cleaned.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        self.data = data

    def remove_duplicates(self):
        """
        Remove duplicate rows from the DataFrame.
        """
        initial_count = len(self.data)
        self.data = self.data.drop_duplicates()
        final_count = len(self.data)
        #print(f"Duplicates removed: {initial_count - final_count}")
        print(f" {initial_count - final_count} Duplicates are removed")

    def show_data(self):
        """
        Print the cleaned DataFrame to the console.
        """
        print("\nCleaned Data:")
        print(self.data)

    def save_clean_data(self, file_path):
        """Saves cleaned data in a proper JSON format."""
        if not self.data.empty:
            try:
                self.data.to_json(file_path, orient="records", indent=4)
                print(f" Cleaned data saved successfully to: {file_path}")
            except Exception as e:
                print(f" Error saving JSON file: {e}")
        else:
            print(" No data to save.")
