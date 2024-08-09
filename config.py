import os


# Base directory paths
BASE_DIR = os.path.dirname(__file__)  # Top-level directory of your project
DATA_DIR = os.path.join(BASE_DIR, "local_data")
OUTPUT_DIR = os.path.join(DATA_DIR, "output_graphs")

# Raw audio files directory
AUDIO_DIR = os.path.join(DATA_DIR, "raw_audio_files")

# List of audio files available in ./local_data
AUDIO_FILE_SAX_A3 = os.path.join(AUDIO_DIR, "sax-baritone_a3.wav")
AUDIO_FILE_SUNO_WITS = os.path.join(
    AUDIO_DIR, "SUNO_Whispers-in-the-Shadows.mp3"
)

# List of uutput directories organised by analysis type
TIME_DOMAIN_OUTPUT_DIR = os.path.join(
    OUTPUT_DIR, "time_domain_audio_representations"
)
FREQUENCY_DOMAIN_OUTPUT_DIR = os.path.join(
    OUTPUT_DIR, "frequency_domain_audio_representations"
)


# Function to ensure directories exist
def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Ensure the output directories exist
ensure_directory(TIME_DOMAIN_OUTPUT_DIR)
ensure_directory(FREQUENCY_DOMAIN_OUTPUT_DIR)
