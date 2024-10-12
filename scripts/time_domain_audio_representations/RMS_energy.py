import os
import sys
import logging
import librosa
import numpy as np
import matplotlib.pyplot as plt

from config.config import audio_config, output_config
from config.parameters import (
    AUDIO_FILE_SAX_A3,
    ORIGINAL_SIGNAL_COLOR,
    RMS_ENERGY_COLOR,
    BACKGROUND_COLOR,
)
from config.logging import setup_logging
from config.matplotlib_plots import configure_plot

# Adjust sys.path to include the root directory
root_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

# Set up logging for this script
notebook_path = os.path.join(os.getcwd(), "RMS_energy.py")
setup_logging(notebook_path)

# Set the audio file to analyse
audio_file_key = AUDIO_FILE_SAX_A3
audio_file_path = audio_config.get_audio_file(audio_file_key)


def analyse_audio(audio_file_path):
    try:
        y, sr = librosa.load(audio_file_path, sr=None)
        rms_energy = librosa.feature.rms(y=y)[0]
        time = np.arange(len(y)) / sr
        t_frames = librosa.frames_to_time(np.arange(len(rms_energy)), sr=sr)
        return y, sr, rms_energy, time, t_frames
    except FileNotFoundError:
        logging.error(f"File not found: {audio_file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


try:
    y, sr, rms_energy, time, t_frames = analyse_audio(audio_file_path)
except Exception as e:
    logging.error(f"Error analysing audio file {audio_file_path}: {e}")
    raise

# Plot the original signal and RMS Energy
fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(time, y, color=ORIGINAL_SIGNAL_COLOR, label="Original Signal")
ax.plot(t_frames, rms_energy, color=RMS_ENERGY_COLOR, label="RMS Energy")
configure_plot(
    ax,
    title=os.path.basename(audio_file_path),
    subtitle="Original Signal and RMS Energy",
)

# Ensure the output directory exists
output_directory = output_config.get_output_directory("time_domain")
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Save the plot
output_path = os.path.join(
    output_directory,
    f"RMS_{os.path.splitext(os.path.basename(audio_file_path))[0]}.png",
)
plt.savefig(output_path, facecolor=BACKGROUND_COLOR)
plt.show()
