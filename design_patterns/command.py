"""Demonstration of Command pattern. AKA "Action" or "Transaction". Category: "Behavioral"

Encapsulates a request that can vary into an object that can be used to parametrize
objects based on the specifics of the request. (principle: "encapsulate what varies")

Useful in command line utilities, GUI menus, building undo/redo capabilities, audit trails, queues,
and logging operations.
"""

from abc import ABC, abstractmethod
from pathlib import Path


class AbstractCommand(ABC):
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass


class RenameFileCommand(AbstractCommand):
    
    def __init__(self, **kwargs):
        self.src = kwargs["src"]
        self.dest = kwargs["dest"]
    
    def execute(self):
        self.src.rename(self.dest)
    
    def undo(self):
        self.dest.rename(self.src)


class CreateFileCommand(AbstractCommand):
    
    def __init__(self, **kwargs):
        self.filepath = kwargs["src"]
    
    def execute(self):
        self.filepath.touch()
    
    def undo(self):
        self.filepath.unlink()


def main():
    
    # Simulating encapsulation of arguments
    kwargs = {
        "src": Path("test.txt"),
        "dest": Path("renamed.txt")
    }

    # Build two commands
    commands = [
        CreateFileCommand(**kwargs),
        RenameFileCommand(**kwargs),
    ]

    # Execute the list of commands
    for command in commands:
        command.execute()

    assert not kwargs["src"].exists()
    assert kwargs["dest"].exists() 

    # Undo the commands performed
    for command in reversed(commands):
        command.undo()

    assert not kwargs["src"].exists() 
    assert not kwargs["dest"].exists()
            

if __name__=="__main__":
    main()