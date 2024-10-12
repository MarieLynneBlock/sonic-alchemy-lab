import os
import sys
import logging
import librosa
import numpy as np
import matplotlib.pyplot as plt

from config.config import audio_config, output_config
from config.parameters import (
    DEFAULT_N_FFT,
    DEFAULT_HOP_LENGTH,
    FIGURE_SIZE,
    BACKGROUND_COLOR,
    SPINE_COLOR,
    AUDIO_FILE_SAX_A3,
)
from config.logging import setup_logging
from config.matplotlib_plots import configure_plot

# Adjust sys.path to include the root directory
root_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

# Set up logging for this script
notebook_path = os.path.join(os.getcwd(), "spectrogram.py")
setup_logging(notebook_path)


def load_audio(file_key):
    audio_file = audio_config.get_audio_file(file_key)
    if not audio_file:
        logging.error(f"Audio file key '{file_key}' not found.")
        raise ValueError(f"Audio file key '{file_key}' not found.")
    try:
        y, sr = librosa.load(audio_file)
        logging.info(f"Loaded audio file: {audio_file}")
        return y, sr
    except Exception as e:
        logging.error(f"Failed to load audio file: {e}")
        raise


def compute_spectrogram(
    y, sr, n_fft=DEFAULT_N_FFT, hop_length=DEFAULT_HOP_LENGTH
):
    D = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length))
    logging.info("Computed spectrogram.")
    return D


def plot_and_save_spectrogram(D, sr, hop_length, output_path):
    fig, ax = plt.subplots(figsize=FIGURE_SIZE)
    fig.patch.set_facecolor(BACKGROUND_COLOR)
    ax.set_facecolor(BACKGROUND_COLOR)
    img = librosa.display.specshow(
        librosa.amplitude_to_db(D, ref=np.max),
        sr=sr,
        hop_length=hop_length,
        x_axis="time",
        y_axis="log",
        ax=ax,
    )
    cbar = fig.colorbar(img, format="%+2.0f dB")
    cbar.ax.set_facecolor(BACKGROUND_COLOR)
    cbar.ax.yaxis.set_tick_params(color=SPINE_COLOR)
    plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color=SPINE_COLOR)
    configure_plot(
        ax, title="Spectrogram", subtitle="Frequency Domain Representation"
    )
    plt.tight_layout()
    plt.savefig(output_path, facecolor=BACKGROUND_COLOR)
    plt.show()
    logging.info(f"Spectrogram plot saved to: {output_path}")


# Load Audio File
y, sr = load_audio(AUDIO_FILE_SAX_A3)

# Compute Spectrogram
D = compute_spectrogram(y, sr)

# Define Output Path
output_dir = output_config.get_output_directory("frequency_domain")
output_path = os.path.join(output_dir, "Spectrogram.png")

# Plot and Save Spectrogram
plot_and_save_spectrogram(D, sr, DEFAULT_HOP_LENGTH, output_path)
