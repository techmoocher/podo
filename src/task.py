from enum import Enum
from random import choice
from typing import Any


class Status(Enum):
    NOT_STARTED = -1
    IN_PROGRESS = 0
    DONE        = 1

class Task:

    def __init__(self, name: str, desc: str, status: int):
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
            new_id.append(choice(alphabet))

        return "".join(new_id)

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_status(self) -> str:
        return self._status.name

    def get_desc(self) -> str:
        return self._desc

    def set_name(self, new_name: str) -> None:
        if len(new_name) == 0 or len(new_name) > 30:
            raise ValueError("Name must be between 1 and 30 characters long.")

        self._name = new_name

    def set_status(self, new_status: int) -> None:
        if new_status not in [-1, 0, 1]:
            raise ValueError("Invalid status.")

        self._status = Status(new_status)

    def set_desc(self, new_desc: str) -> None:
            if len(new_desc) == 0 or len(new_desc) > 60:
                raise ValueError("Description must be below 60 characters long.")
    
            self._desc = new_desc

    def mark_as_done(self) -> None:
        self.set_status(Status.DONE.value)

    def export_as_dict(self) -> dict[str, Any]:
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
