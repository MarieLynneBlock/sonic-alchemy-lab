import os
from dotenv import load_dotenv
from .paths import (
    BASE_DIR,
    DATA_DIR,
    OUTPUT_DIR,
    AUDIO_DIR,
    AUDIO_FILES,
    OUTPUT_DIRS,
)

# from .parameters import *

# Load environment variables from a .env file
load_dotenv()


# Override default paths with environment variables if provided
BASE_DIR = os.getenv("BASE_DIR", BASE_DIR)
DATA_DIR = os.getenv("DATA_DIR", DATA_DIR)
OUTPUT_DIR = os.getenv("OUTPUT_DIR", OUTPUT_DIR)
AUDIO_DIR = os.getenv("AUDIO_DIR", AUDIO_DIR)


def get_output_path(analysis_type, file_name, extension="png"):
    """Generate the full path for output files based on analysis type and file
    name."""
    output_dir = OUTPUT_DIRS.get(analysis_type)
    if not output_dir:
        raise ValueError(f"Unknown analysis type: {analysis_type}")
    return os.path.join(output_dir, f"{file_name}.{extension}")


class AudioConfig:
    """Configuration for audio files."""

    def __init__(self):
        self.audio_dir = AUDIO_DIR
        self.audio_files = AUDIO_FILES

    def get_audio_file(self, key):
        return self.audio_files.get(key)


class OutputConfig:
    """Configuration for output directories."""

    def __init__(self):
        self.output_dirs = OUTPUT_DIRS

    def get_output_directory(self, analysis_type):
        return self.output_dirs.get(analysis_type)

    def get_output_path(self, analysis_type, file_name, extension="png"):
        return get_output_path(analysis_type, file_name, extension)


# Instantiate configuration classes
audio_config = AudioConfig()
output_config = OutputConfig()
