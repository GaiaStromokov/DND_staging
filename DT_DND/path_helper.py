from pathlib import Path

def get_path(*path_parts):
    """
    Get a path relative to the project root directory.

    Usage:
        get_path("dist", "item_comp.json")
        get_path("manager", "components", "data.txt")

    Returns the absolute path to the file/directory as a string.
    """
    # Find project root by looking for main.py or .git
    current = Path(__file__).parent
    while current != current.parent:
        if (current / "main.py").exists() or (current / ".git").exists():
            project_root = current
            break
        current = current.parent
    else:
        # Fallback: use the directory containing this file
        project_root = Path(__file__).parent

    # Join all path parts and return as string
    return str(project_root / Path(*path_parts))