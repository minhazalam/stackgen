"""
Stackify CLI - Entry Point

This module defines the main CLI application using Typer.
All commands are registered here.

Author: Minhaz Alam
Created: 2026-03
"""

import typer

app = typer.Typer()


@app.command()
def hello() -> None:
    """
    Test command to verify that the CLI is working.

    Returns:
        None
    """
    print("Stackify CLI is working 🚀")


if __name__ == "__main__":
    app()