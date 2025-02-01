from data_loader import load_data
from data_cleaner import DataCleaner
import os

def main():
    # Step 1: Load data
    data = load_data()
    if data is None:
        print("No data to process. Exiting.")
        return

    # Display the selected file path
    print("\nThe selected file has been loaded successfully.")
    
    # Step 2: Initialize DataCleaner
    cleaner = DataCleaner(data)

    # Step 3: Remove duplicates
    cleaner.remove_duplicates()

    # Step 4: Display the cleaned data
    print("\nCleaned Data:")
    print(cleaner.data)

    # Step 5: Automatically save cleaned data
    output_file = os.path.join(os.getcwd(), "cleaned_data.json")
    cleaner.save_clean_data(output_file)

    # Step 6: Inform the user about the saved file
    #print(f"\nCleaned data has been saved automatically to: {output_file}")

if __name__ == "__main__":
    main()
