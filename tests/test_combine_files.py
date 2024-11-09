# CombineFiles/tests/test_combine_files.py
import os
import shutil
import unittest
from pathlib import Path
from src.combine_files import CombineFiles  # Import the CombineFiles class


class TestCombineFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up temporary directories and files for testing."""
        cls.test_dir = Path("test_directory")
        cls.test_dir.mkdir(exist_ok=True)

        # Create subdirectories and files
        (cls.test_dir / "models").mkdir(exist_ok=True)
        (cls.test_dir / "models" / "example.txt").write_text("This is an example text file.")

        (cls.test_dir / "ignore_me").mkdir(exist_ok=True)
        (cls.test_dir / "ignore_me" / "excluded.txt").write_text("This file should be excluded.")

        (cls.test_dir / "example2.txt").write_text("This is another example text file.")

        # Output file path
        cls.output_file = cls.test_dir / "combined_output.txt"

    @classmethod
    def tearDownClass(cls):
        """Clean up temporary directories and files after testing."""
        shutil.rmtree(cls.test_dir)

    def test_combines_files_with_extension(self):
        """Test that files with the specified extension are combined into the output file."""
        combiner = CombineFiles(
            root_directory=self.test_dir,
            extension=".txt",
            output_file=self.output_file,
            exclude_dirs=[],
            exclude_files=[]
        )
        combiner.combine_files()

        with open(self.output_file, 'r') as f:
            content = f.read()

        self.assertIn("This is an example text file.", content)
        self.assertIn("This is another example text file.", content)

    def test_exclude_directory(self):
        """Test that files in excluded directories are not included in the output."""
        combiner = CombineFiles(
            root_directory=self.test_dir,
            extension=".txt",
            output_file=self.output_file,
            exclude_dirs=["ignore_me"],
            exclude_files=[]
        )
        combiner.combine_files()

        with open(self.output_file, 'r') as f:
            content = f.read()

        self.assertNotIn("This file should be excluded.", content)
        self.assertIn("This is an example text file.", content)

    def test_exclude_specific_file(self):
        """Test that specified files are excluded from the output."""
        combiner = CombineFiles(
            root_directory=self.test_dir,
            extension=".txt",
            output_file=self.output_file,
            exclude_dirs=[],
            exclude_files=["example2.txt"]
        )
        combiner.combine_files()

        with open(self.output_file, 'r') as f:
            content = f.read()

        self.assertNotIn("This is another example text file.", content)
        self.assertIn("This is an example text file.", content)

    def test_target_name_filter(self):
        """Test that only files within specified directories (target_name) are included."""
        combiner = CombineFiles(
            root_directory=self.test_dir,
            extension=".txt",
            output_file=self.output_file,
            target_name="models",
            exclude_dirs=[],
            exclude_files=[]
        )
        combiner.combine_files()

        with open(self.output_file, 'r') as f:
            content = f.read()

        self.assertIn("This is an example text file.", content)
        self.assertNotIn("This is another example text file.", content)

if __name__ == "__main__":
    unittest.main()
