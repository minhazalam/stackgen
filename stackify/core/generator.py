"""
Project Generator Module

Handles the creation of project structure and files
based on selected templates.

Author: Minhaz Alam
Created: 2026-03
"""

import os


def create_project_structure(project_name: str) -> None:
    """
    Create the base folder structure for a new project.

    Args:
        project_name (str): Name of the project.

    Returns:
        None
    """
    os.makedirs(project_name, exist_ok=True)

    folders = [
        "airflow/dags",
        "spark/jobs",
        "config"
    ]

    for folder in folders:
        path = os.path.join(project_name, folder)
        os.makedirs(path, exist_ok=True)