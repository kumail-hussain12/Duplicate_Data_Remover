import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def load_data():
    """
    Allow the user to select a file (CSV, Excel, JSON) and load it into a Pandas DataFrame.
    
    Returns:
        pd.DataFrame: Loaded data, or None if there was an error.
    """
    try:
        root = Tk()
        root.withdraw()
        print("Please select a data file...")

        file_path = askopenfilename(
            filetypes=[
                ("All Supported Files", "*.csv;*.xlsx;*.xls;*.json"),
                ("CSV Files", "*.csv"),
                ("Excel Files", "*.xlsx;*.xls"),
                ("JSON Files", "*.json")
            ],
            title="Select Data File"
        )

        if not file_path:
            print("No file was selected. Exiting.")
            return None

        # Detect file extension and read accordingly
        if file_path.endswith(".csv"):
            data = pd.read_csv(file_path)
        elif file_path.endswith((".xlsx", ".xls")):
            data = pd.read_excel(file_path)
        elif file_path.endswith(".json"):
            try:
                data = pd.read_json(file_path)
            except ValueError:
                print("Standard JSON loading failed. Trying JSON Lines format...")
                data = pd.read_json(file_path, lines=True)
        else:
            print("Unsupported file format. Please select a CSV, Excel, or JSON file.")
            return None

        print(f"Data loaded successfully from {file_path}.")
        return data

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
