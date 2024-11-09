<<<<<<< HEAD
# combine-files
=======
# CombineFiles

**CombineFiles** is a Python class-based tool for traversing directory trees and aggregating text-based files. It allows you to locate, filter, and combine content from files with a specified extension into a single output file. With options for filtering by directory or filename, as well as default exclusions for common development files, CombineFiles streamlines data preparation across projects. The class-based structure makes it easy to configure, reuse, and extend.

---

## Features

- **Class-Based Design**: Encapsulates configuration and logic, making the tool reusable, modular, and easy to integrate into other Python projects.
- **Directory Tree Traversal**: Traverse any directory structure to locate files with a specific extension.
- **Targeted File Aggregation**: Optionally filter by specific directory or file names for precise aggregation.
- **Default Exclusions**: Automatically skips common development directories and files (e.g., `__pycache__`, `node_modules`, `.env`).
- **Custom Exclusions**: Specify additional directories and files to exclude as needed.
- **File Demarcations in Output**: Each file’s content in the output file is prefixed with its path for easy reference.
- **Verbose Logging**: Track the process with detailed logging, ideal for troubleshooting and debugging.

---

## Default Exclusions

The class is preconfigured to exclude common directories and files, especially for Django and Next.js projects.

- **Directories**: `__pycache__`, `migrations`, `static`, `media`, `venv`, `env`, `node_modules`, `.next`, `out`, `public`, `styles`
- **Files**: `package-lock.json`, `yarn.lock`, `.env`, `.DS_Store`, `Thumbs.db`, `.gitignore`, `.editorconfig`

Additional exclusions can be specified during instantiation.

---

## Installation

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/yourusername/CombineFiles.git
cd CombineFiles
```

---

## Usage

### Basic Syntax

You can use `CombineFiles` by running the script with command-line arguments or by directly instantiating and calling the class in your Python code.

### Command-Line Usage

```bash
python combine_files.py <root_directory> <extension> <output_file> [options]
```

### Parameters and Options

1. **root_directory**: The root directory where the search begins.
2. **extension**: File extension to search for (e.g., `.txt`).
3. **output_file**: Path to the output file where contents will be combined.
4. **-t, --target_name**: *(Optional)* Specify a directory or filename to filter by; only matching directories/files will be included.
5. **-x, --exclude_dirs**: *(Optional)* Additional directories to exclude.
6. **-f, --exclude_files**: *(Optional)* Additional filenames to exclude.
7. **-v, --verbose**: *(Optional)* Enables verbose logging for debugging.

---

### Examples

1. **Combine all `.txt` files in a directory tree**:
   ```bash
   python combine_files.py /path/to/root_directory .txt /path/to/output/combined_output.txt
   ```

2. **Combine files with `.txt` extension only within directories named `models`**:
   ```bash
   python combine_files.py /path/to/root_directory models .txt /path/to/output/combined_output.txt
   ```

3. **Exclude additional directories and files**:
   ```bash
   python combine_files.py /path/to/root_directory .txt /path/to/output/combined_output.txt -x logs temp -f config.json
   ```

4. **Enable verbose output for detailed logging**:
   ```bash
   python combine_files.py /path/to/root_directory .txt /path/to/output/combined_output.txt --verbose
   ```

### Directly Using the `CombineFiles` Class

You can also import and use `CombineFiles` directly in your code:

```python
from combine_files import CombineFiles

# Initialize the class with your parameters
combiner = CombineFiles(
    root_directory="/path/to/root_directory",
    extension=".txt",
    output_file="/path/to/output/combined_output.txt",
    target_name="models",
    exclude_dirs=["logs", "temp"],
    exclude_files=["config.json"],
    verbose=True
)

# Run the file combination process
combiner.combine_files()
```

---

## Future Enhancements

- **Support Multiple Extensions**: Aggregate files with multiple extensions in a single run.
- **Config File Support**: Use an external configuration file for exclusions and default settings.
- **Dry-Run Mode**: Preview files to be included before generating the output.
- **Parallel Processing**: Improve performance on large directory trees with multiprocessing.
- **Alternative Output Formats**: Option to output as JSON, CSV, or other structured formats.

---

## Contributing

Contributions are welcome! If you have ideas or feature requests, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

Developed by [Your Name](https://github.com/yourusername)

---

**CombineFiles** is a modular and powerful tool for consolidating files across complex project directories, making it ideal for data preparation, documentation aggregation, and more. Enjoy!
```
>>>>>>> Initial commit
