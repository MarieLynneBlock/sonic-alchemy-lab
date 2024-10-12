import os
import sys
import logging
import librosa
import matplotlib.pyplot as plt

from config.config import audio_config, output_config
from config.parameters import AUDIO_FILE_SAX_A3, BACKGROUND_COLOR
from config.logging import setup_logging
from config.matplotlib_plots import configure_plot, create_custom_colormap

# Adjust sys.path to include the root directory
root_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

# Set up logging for this script
notebook_path = os.path.join(os.getcwd(), "MFCCs.py")
setup_logging(notebook_path)

# Set the audio file to analyse
audio_file_key = AUDIO_FILE_SAX_A3
audio_file_path = audio_config.get_audio_file(audio_file_key)


def analyse_audio(audio_file_path):
    try:
        y, sr = librosa.load(audio_file_path, sr=None)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        return y, sr, mfccs
    except FileNotFoundError:
        logging.error(f"File not found: {audio_file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


try:
    y, sr, mfccs = analyse_audio(audio_file_path)
except Exception as e:
    logging.error(f"Error analysing audio file {audio_file_path}: {e}")
    raise

# Plot the MFCCs
custom_cmap = create_custom_colormap()
fig, ax = plt.subplots(figsize=(14, 5))
img = librosa.display.specshow(mfccs, x_axis="time", ax=ax, cmap=custom_cmap)
fig.colorbar(img, ax=ax)
configure_plot(ax, title=os.path.basename(audio_file_path), subtitle="MFCCs")

# Ensure the output directory exists
output_directory = output_config.get_output_directory("frequency_domain")
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Save the plot
output_path = os.path.join(
    output_directory,
    f"MFCC_{os.path.splitext(os.path.basename(audio_file_path))[0]}.png",
)
plt.savefig(output_path, facecolor=BACKGROUND_COLOR)
plt.show()
