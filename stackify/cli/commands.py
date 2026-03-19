"""
Stackify CLI Commands

This module contains implementations of CLI commands
such as project initialization and module additions.

Author: Minhaz Alam
Created: 2026-03
"""


def init_project(project_name: str) -> None:
    """
    Initialize a new data engineering project.

    Args:
        project_name (str): Name of the project directory to create.

    Returns:
        None
    """
    print(f"Initializing project: {project_name}")