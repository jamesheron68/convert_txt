# TXT to Excel Converter

A small Python practice project that converts one or more tab-delimited `.txt` files into `.xlsx` Excel files.

The project was built as a hands-on exercise to practise Python fundamentals, file handling, `pandas`, `tkinter`, error handling, and working with `pathlib`.

## Features

* Opens a file-selection window using `tkinter`
* Allows multiple `.txt` files to be selected at once
* Reads tab-delimited text files using `pandas`
* Preserves values such as `"NA"` rather than automatically treating them as missing data
* Converts each text file into an Excel `.xlsx` file
* Saves the Excel file in the same directory as the original text file
* Keeps the original filename while changing the extension
* Handles individual file-processing errors without stopping the entire process
* Provides a summary of successfully created files

## Example

Given the following files:

```text
data/
├── survey_results.txt
├── product_data.txt
└── responses.txt
```

After running the program and selecting all three files:

```text
data/
├── survey_results.txt
├── survey_results.xlsx
├── product_data.txt
├── product_data.xlsx
├── responses.txt
└── responses.xlsx
```

## Requirements

* Python 3.9+
* pandas
* openpyxl

`tkinter` is also required. It is included with most standard Python installations on Windows.

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd txt-to-excel
```

Install the required Python packages:

```bash
pip install pandas openpyxl
```

## Usage

Run the script:

```bash
python main.py
```

A file-selection window will appear.

1. Select one or more `.txt` files.
2. Click **Open**.
3. Each selected file will be read as a tab-delimited dataset.
4. An `.xlsx` file will be created in the same location as the original `.txt` file.
5. The terminal will display the files that were successfully created.

### Cancelling file selection

If the file-selection window is cancelled, the program exits with:

```text
File selection cancelled - Process stopped.
```

### File processing errors

If an individual file cannot be read or converted, the error is displayed in the terminal and the program continues attempting to process the remaining selected files.

## How It Works

The program is split into several functions, each handling a different part of the process.

### `select_files()`

Creates a `tkinter` file-selection dialog and allows the user to select multiple `.txt` files.

The selected file paths are returned as a tuple.

If no files are selected, the program exits.

### `convert_files(file_paths)`

Loops through the selected files and:

1. Reads each file with `pandas.read_csv()`
2. Uses `\t` as the separator because the source files are tab-delimited
3. Sets `keep_default_na=False` so values such as `"NA"` remain as text
4. Creates an output filename using `pathlib.Path`
5. Writes the DataFrame to Excel using `to_excel()`
6. Keeps track of successfully created files

### `output_message(output_files)`

Displays a success message containing the paths of the generated Excel files.

If no files were successfully processed, an appropriate message is displayed instead.

### `main()`

Controls the overall program flow:

```text
Select files
     ↓
Convert files
     ↓
Display results
```

The script is started using:

```python
if __name__ == "__main__":
    main()
```

This ensures `main()` runs when the file is executed directly.

## Technologies Used

| Technology | Purpose                                              |
| ---------- | ---------------------------------------------------- |
| Python     | Core programming language                            |
| pandas     | Reading and converting tabular data                  |
| tkinter    | Graphical file-selection dialog                      |
| pathlib    | File path and extension handling                     |
| openpyxl   | Writing Excel `.xlsx` files                          |
| sys        | Exiting the program when file selection is cancelled |

## What I Practised

This project was primarily created as a learning exercise to practise:

* Functions and program structure
* `if __name__ == "__main__"`
* `for` loops
* Lists
* Exception handling with `try` / `except`
* Working with file paths
* `pathlib.Path`
* Reading files with `pandas`
* Exporting DataFrames to Excel
* Using third-party Python libraries
* Basic GUI interaction with `tkinter`
* Handling user cancellation
* Separating a program into logical functions

## Possible Future Improvements

Some potential extensions to this project would be:

* Allow the user to select `.csv` files as well as `.txt`
* Allow the user to choose the output folder
* Add support for different delimiters
* Add a progress indicator for large batches of files
* Prevent accidentally overwriting existing Excel files
* Add more specific error handling instead of catching all `Exception` types
* Add logging rather than relying entirely on `print()`
* Add command-line arguments as an alternative to the GUI
* Create automated tests for the conversion functions
* Package the application as a standalone `.exe`

## Project Status

**Practice / Learning Project**

This project is intended to build practical Python skills rather than serve as a production-ready file conversion tool.
