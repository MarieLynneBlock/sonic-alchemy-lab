import logging
import os
from .paths import BASE_DIR


def setup_logging(notebook_path):
    """Configure logging for the analysis notebooks."""
    rel_path = os.path.relpath(
        notebook_path, os.path.join(BASE_DIR, "notebooks")
    )
    folder_name = os.path.dirname(rel_path)
    notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]
    log_file_name = (
        f"{folder_name}_{notebook_name}.log"
        if folder_name
        else f"{notebook_name}.log"
    )
    log_dir = os.path.join(BASE_DIR, "local_data", "output_logs")

    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, log_file_name)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s: %(message)s",
        handlers=[
            logging.StreamHandler(),  # Output logs to the console
            logging.FileHandler(log_file),  # Also log to a file
        ],
    )
