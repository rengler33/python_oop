"""Demonstration of the Template design pattern. Category: behavioral.

The template pattern defines an abstract base class that defines an
algorithm's skeleton but defers some of the implementations to
subclasses.

A template can consist of abstract methods, concrete methods (if several
subclasses will want the same behavior), and hooks, collectively called
the primitive methods. Ultimately the order of the methods is fixed with
a template method.

The template method defines the order of execution of the "primitive"
methods (). Concrete methods derive from the abstract base class, and
must implement the abstract methods and can optionally override
the concrete or hook methods if needed.

Note: unlike the Strategy pattern, the templates are likely not
interchangeable.

This example shows how the Template pattern can be used to load
files of a different type.
"""

from abc import ABC, abstractmethod
from pathlib import Path


class FileLoaderTemplate(ABC):
    def __init__(self, filepath: Path):
        self._filepath = Path(filepath)

    def load_file(self):
        """Serves as the template method, defining order of
        execution for every derived class
        """
        self._ensure_file_exists()  # concrete method
        self._load()  # abstract method
        self._post_processing()  # hook, concrete, optional
        print("-" * 20)

    def _ensure_file_exists(self):
        """"""
        # assert self._filepath.exists()

    @abstractmethod
    def _load(self):
        """Implement unique loading behavior"""

    def _post_processing(self):
        """Implement optional post-processing behavior"""


class ExcelLoader(FileLoaderTemplate):
    def _load(self):
        print(f"Unique Excel file loading of {self._filepath}")


class PDFLoader(FileLoaderTemplate):
    def _load(self):
        print(f"Unique PDF file loading of {self._filepath}")

    def _post_processing(self):
        print("With some additional post_processing")


if __name__ == "__main__":
    excel = ExcelLoader("file.xlsx")
    excel.load_file()

    pdf = PDFLoader("file.pdf")
    pdf.load_file()
