import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def load_data():
    """
    Allow the user to select a JSON file and load the data.
    
    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame, or None if there was an error.
    """
    try:
        root = Tk()
        root.withdraw()
        print("Please select a JSON file...")

        file_path = askopenfilename(filetypes=[("JSON Files", "*.json")], title="Select JSON File")

        if not file_path:
            print("No file was selected. Exiting.")
            return None

        data = pd.read_json(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data

    except ValueError as ve:
        print(f"ValueError: Unable to parse JSON. Ensure the file is in proper JSON format. {ve}")
        return None

    except FileNotFoundError:
        print("FileNotFoundError: The selected file was not found.")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    finally:
        try:
            root.destroy()
        except Exception:
            pass
