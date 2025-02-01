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
        print(f"Duplicates removed: {initial_count - final_count}")

    def show_data(self):
        """
        Print the cleaned DataFrame to the console.
        """
        print("\nCleaned Data:")
        print(self.data)

    def save_clean_data(self, output_file):
        """
        Save the cleaned data to a JSON file.
        
        Args:
            output_file (str): The path to save the cleaned data.
        """
        try:
            self.data.to_json(output_file, orient='records', lines=True)
            print(f"Cleaned data successfully saved to '{output_file}'.")
        except Exception as e:
            print(f"Error saving data: {e}")
