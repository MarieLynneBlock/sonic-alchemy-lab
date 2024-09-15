import os

# Base directory paths
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)  # I am ... Root
DATA_DIR = os.path.join(BASE_DIR, "local_data")
OUTPUT_DIR = os.path.join(DATA_DIR, "output_graphs")

# Raw audio files directory
AUDIO_DIR = os.path.join(DATA_DIR, "raw_audio_files")


# Function to dynamically generate audio file paths
def get_audio_file(file_name):
    """Generate the full path for an audio file."""
    return os.path.join(AUDIO_DIR, file_name)


# List of audio files available
AUDIO_FILES = {
    "sax_a3": get_audio_file("sax-baritone_a3.wav"),
    "suno_wits": get_audio_file("SUNO_Whispers-in-the-Shadows.mp3"),
    # Add more audio files here as needed
}


# Function to dynamically generate output directories based on analysis type
def get_output_dir(analysis_type):
    """Generate the output directory path based on analysis type."""
    return os.path.join(OUTPUT_DIR, analysis_type)


# Dictionary of output directories organised by analysis type
OUTPUT_DIRS = {
    "time_domain": get_output_dir("time_domain_audio_representations"),
    "frequency_domain": get_output_dir(
        "frequency_domain_audio_representations"
    ),
}


# Ensure all output directories exist
def ensure_directories():
    """Ensure that all output directories exist."""
    for dir_path in OUTPUT_DIRS.values():
        os.makedirs(dir_path, exist_ok=True)


# Initialize directories
ensure_directories()
