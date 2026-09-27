import typer
from typing import Annotated

from task import Task


app = typer.Typer(
    name = "podo",
    rich_markup_mode = None
)
