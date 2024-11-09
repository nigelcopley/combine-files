import os
import logging
from pathlib import Path

# Default directories to exclude for Django and Next.js projects
DEFAULT_EXCLUDE_DIRS = [
    "__pycache__", "migrations", "static", "media", "venv", "env", "node_modules",
    ".next", "out", "public", "styles", ".venv", ".env", ".next"
]

DEFAULT_EXCLUDE_FILES = [
    "package-lock.json", "yarn.lock", "Pipfile.lock", "poetry.lock",
    ".env", ".env.local", ".env.development", ".env.production",
    ".DS_Store", "Thumbs.db", ".gitignore", ".editorconfig", ".eslintignore",
    ".prettierignore", "webpack.config.js", "tsconfig.json", ".babelrc",
    "babel.config.js", "package.json", "jest.config.js", "jest.setup.js",
    "pytest.ini", "tox.ini", ".coveragerc"
]  # Add any other common files to exclude

class CombineFiles:
    def __init__(self, root_directory, extension, output_file, target_name=None, exclude_dirs=None, exclude_files=None,
                 verbose=False):
        self.root_directory = Path(root_directory)
        self.extension = extension
        self.output_file = Path(output_file)
        self.target_name = target_name
        self.exclude_dirs = set(DEFAULT_EXCLUDE_DIRS + (exclude_dirs or []))
        self.exclude_files = set(DEFAULT_EXCLUDE_FILES + (exclude_files or []))

        # Configure logging
        log_level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def combine_files(self):
        """Combine files based on initialized parameters."""
        logging.info(f"Starting to combine files with extension '{self.extension}' into '{self.output_file}'")
        try:
            with open(self.output_file, 'w', encoding='utf-8') as outfile:
                for root, dirs, files in os.walk(self.root_directory):
                    # Exclude specified directories
                    dirs[:] = [d for d in dirs if d not in self.exclude_dirs]

                    # Check if we're filtering by target_name
                    is_target_dir = self.target_name and os.path.basename(root) == self.target_name

                    for file in files:
                        # Exclude specified files
                        if file in self.exclude_files:
                            logging.debug(f"Skipping excluded file: {file}")
                            continue

                        # Determine if this file should be processed
                        is_target_file = self.target_name and file == self.target_name
                        if (is_target_dir or is_target_file or not self.target_name) and file.endswith(self.extension):
                            file_path = os.path.join(root, file)
                            logging.info(f"Processing file: {file_path}")
                            try:
                                with open(file_path, 'r', encoding='utf-8') as infile:
                                    outfile.write(f"--- Start of {file_path} ---\n")
                                    outfile.write(infile.read())
                                    outfile.write(f"\n--- End of {file_path} ---\n\n")
                            except Exception as e:
                                logging.error(f"Error reading file '{file_path}': {e}")
            logging.info(f"Successfully combined files into '{self.output_file}'")
        except Exception as e:
            logging.error(f"Error writing to output file '{self.output_file}': {e}")


# Example usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Combine contents of files with a specific extension from directories or files with a specific name.")
    parser.add_argument("root_directory", help="Root directory to start the search.")
    parser.add_argument("extension", help="File extension to search for (e.g., '.txt').")
    parser.add_argument("output_file", help="Path to the output file where contents will be combined.")
    parser.add_argument("-t", "--target_name", help="Optional; name of directories or files to search for.")
    parser.add_argument("-x", "--exclude_dirs", nargs='*', default=[], help="Additional directories to exclude.")
    parser.add_argument("-f", "--exclude_files", nargs='*', default=[], help="Additional files to exclude.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging.")

    args = parser.parse_args()

    # Initialize and run the CombineFiles class
    combiner = CombineFiles(
        root_directory=args.root_directory,
        extension=args.extension,
        output_file=args.output_file,
        target_name=args.target_name,
        exclude_dirs=args.exclude_dirs,
        exclude_files=args.exclude_files,
        verbose=args.verbose
    )

    combiner.combine_files()
