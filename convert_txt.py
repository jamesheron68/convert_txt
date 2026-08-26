import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog

import pandas as pd


def select_files():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Select the text files you wish to convert.",
        filetypes=[("Text files", "*.txt")],
    )

    root.destroy()

    # Handle errors if process is quit
    if not file_paths:
        print("File selection cancelled - Process stopped.")
        sys.exit()

    return file_paths


def convert_files(file_paths):
    output_files = []

    for file_path in file_paths:
        # Convert the tab-delimited text file to a DataFrame.
        # keep_default_na=False prevents values such as "NA" being
        # automatically interpreted as missing data.
        try:
            df = pd.read_csv(file_path, sep="\t", keep_default_na=False)
        except Exception as e:
            print(f"Could not process {file_path}: {e}")
            continue

        output_file = Path(file_path).with_suffix(".xlsx")

        df.to_excel(output_file, index=False)

        output_files.append(output_file)

    return output_files


def output_message(output_files):
    if output_files:
        print("Process successful. Excel file(s) saved to:")
        for file in output_files:
            print(file)
    else:
        print("No files were successfully processed.")


def main():
    file_paths = select_files()
    output_files = convert_files(file_paths)
    output_message(output_files)


if __name__ == "__main__":
    main()