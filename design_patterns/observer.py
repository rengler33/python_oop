"""Demonstration of Observer pattern. AKA "Dependents" or "Publish-Subscribe" pattern. 
Category: Behavioral.

Provides a one-to-many (publisher-to-subscribers) relationship between objects. The publisher
can be updated and the subscribers will be notified. Subscribers can get (or set) state of the
publisher, if desired.

Heavily used in event monitoring.
"""
from abc import ABC, abstractmethod


class AbstractObserver(ABC):
    """Observer that can be initialized with a Subject to Observe. Will require
    Subject parameter and adding self to Subject with Subject.add(self) during
    initialization.
    """

    @abstractmethod
    def update(self):
        """Receive notification that Subject has been updated. Can implement getting
        state of subject to see the update.
        """


class AbstractSubject(ABC):
    """Abstract class for Subjects/Publishers. Methods are actually implemented
    since behavior for adding and removing Observers/Subscribers is similar
    in most circumstances
    """

    def __init__(self):
        self._subscribers = set()

    def add(self, subscriber):
        """Add an Observer to list of subscribers"""
        if not isinstance(subscriber, AbstractObserver):
            raise TypeError
        self._subscribers.add(subscriber)

    def remove(self, subscriber):
        """Remove an Observer from list of subscribers"""
        self._subscribers.remove(subscriber)

    def notify(self):
        """Notify all Observers that Subject has been updated"""
        for subscriber in self._subscribers:
            subscriber.update()


class TownMessageBoard(AbstractSubject):

    _latest_message = None

    @property
    def latest_message(self):
        return self._latest_message

    @latest_message.setter
    def latest_message(self, message):
        """Save latest message and notify Observers that a change has occurred."""
        self._latest_message = message
        self.notify()


class TownCitizen(AbstractObserver):
    def __init__(self, name, message_board):
        self._name = name
        self._message_board = message_board
        message_board.add(self)

    def update(self):
        print(
            f"Notification for {self._name}:",
            self._message_board.latest_message,
        )


def main():
    board = TownMessageBoard()
    bob = TownCitizen(name="Bob", message_board=board)
    jane = TownCitizen(name="Jane", message_board=board)
    willy = TownCitizen(name="Willy", message_board=board)

    board.latest_message = (
        "This is the new notification system for Townville "
        "from the Townville Police department."
    )

    board.latest_message = "We're looking for a suspect, his name is Bob."
    board.remove(bob)

    board.latest_message = "We're also looking for Jane."
    board.remove(jane)

    board.latest_message = "Have you seen Willy? Wanted in connection to Bob and Jane"
    board.remove(willy)

    # Not seen because there are no Observers left
    board.latest_message = "We should probably stop notifying our suspects."


if __name__ == "__main__":
    main()
