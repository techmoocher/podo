from enum import Enum
from random import choice
from typing import Any


class Status(Enum):
    NOT_STARTED = -1
    IN_PROGRESS = 0
    DONE        = 1

class Task:

    def __init__(self, name: str, desc: str, status: int):
        """Create a task after validating its name, description, and status.

        Args:
            name: Task name, between 1 and 30 characters.
            desc: Optional task description, up to 60 characters.
            status: Numeric status value: -1, 0, or 1.

        Raises:
            ValueError: If any argument is outside its allowed range.
        """

        if status not in [-1, 0, 1]:
            raise ValueError("Invalid status.")
        if len(name) == 0 or len(name) > 30:
            raise ValueError("Name must be between 1 and 30 characters long.")
        if len(desc) > 60:
            raise ValueError("Description must be below 60 characters long.")

        self._id        = self._gen_id()
        self._name      = name
        self._desc      = desc
        self._status    = Status(status)


    def _gen_id(self) -> str:
        alphabet = list(range(65, 91)) + list(range(97, 123))
        
        new_id = []
        for i in range(5):
            new_id.append(chr(choice(alphabet)))

        return "".join(new_id)

    def get_id(self) -> str:
        """Return the task ID."""

        return self._id

    def get_name(self) -> str:
        """Return the task name."""

        return self._name

    def get_status(self) -> str:
        """Return the task status."""
        return self._status.name

    def get_desc(self) -> str:
        """Return the task description."""
        return self._desc

    def set_name(self, new_name: str) -> None:
        """Update the task name.

        Args:
            new_name: Replacement name, between 1 and 30 characters.

        Raises:
            ValueError: If the replacement name is empty or too long.
        """
        if len(new_name) == 0 or len(new_name) > 30:
            raise ValueError("Name must be between 1 and 30 characters long.")

        self._name = new_name

    def set_status(self, new_status: int) -> None:
        """Update the task status using a numeric status value.

        Args:
            new_status: Numeric status value: -1, 0, or 1.

        Raises:
            ValueError: If the status value is invalid.
        """
        if new_status not in [-1, 0, 1]:
            raise ValueError("Invalid status.")

        self._status = Status(new_status)

    def set_desc(self, new_desc: str) -> None:
        """Update the task description.

        Args:
            new_desc: Replacement description, up to 60 characters.

        Raises:
            ValueError: If the description is empty or too long.
        """
        if len(new_desc) == 0 or len(new_desc) > 60:
            raise ValueError("Description must be below 60 characters long.")
    
        self._desc = new_desc

    def export_as_dict(self) -> dict[str, Any]:
        """Return the task as a dictionary suitable for serialization."""
        result = {
            "ID":           self._id,
            "Name":         self._name,
            "Status":       self._status.name,
            "Description":  self._desc
        }

        return result

    def __str__(self) -> str:
        display = (
            f"ID: {self._id}\n"
            f"Name: {self._name}\n"
            f"Status: {self._status.name}"
        )

        if self._desc != "":
            display += ('\n' + f"Description: {self._desc}")

        return display
