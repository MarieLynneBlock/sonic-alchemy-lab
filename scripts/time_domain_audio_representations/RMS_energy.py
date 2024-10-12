import os
import sys
import logging
import librosa
import numpy as np
import matplotlib.pyplot as plt

from config.config import audio_config, output_config
from config.utils import setup_environment, load_audio, create_plot
from config.parameters import (
    AUDIO_FILE_SAX_A3,
    ORIGINAL_SIGNAL_COLOR,
    RMS_ENERGY_COLOR,
)
from config.logging import setup_logging
from config.matplotlib_plots import configure_plot

# Code Review: Consider moving this to setup_environment()
# function in config/utils.py
root_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

setup_environment()

# Set up logging for this script
notebook_path = os.path.join(os.getcwd(), "RMS_energy.py")
setup_logging(notebook_path)

# Set the audio file to analyse
audio_file_key = AUDIO_FILE_SAX_A3
audio_file_path = audio_config.get_audio_file(audio_file_key)


def analyse_audio(audio_file_key):
    """Analyze the audio file and compute its RMS energy.

    Args:
        audio_file_key (str): The key of the audio file to analyze.

    Returns:
        tuple: A tuple containing:
            - y (np.ndarray): The audio time series.
            - sr (int): The sampling rate of the audio.
            - rms_energy (np.ndarray): The RMS energy of the audio.
            - time (np.ndarray): The time array for the audio.
            - t_frames (np.ndarray): The time array for the RMS energy frames.
            - audio_file_path (str): The path to the analyzed audio file.
        Returns (None, None, None, None, None, None) if audio loading fails.
    """
    y, sr, audio_file_path = load_audio(audio_file_key)
    if y is None or sr is None:
        return None, None, None, None, None, None

    rms_energy = librosa.feature.rms(y=y)[0]
    time = np.arange(len(y)) / sr
    t_frames = librosa.frames_to_time(np.arange(len(rms_energy)), sr=sr)
    return y, sr, rms_energy, time, t_frames, audio_file_path


def save_plot(fig, audio_file_key):
    """Save the plot to the output directory.

    Args:
        fig (matplotlib.figure.Figure): The figure to save.
        audio_file_key (str): The key of the audio file analyzed.
    """
    file_name = f"script_rms_energy_{audio_file_key}"
    output_path = output_config.get_output_path(
        "time_domain", file_name, "png"
    )
    fig.savefig(output_path)
    logging.info(f"Plot saved to {output_path}")


if __name__ == "__main__":
    y, sr, rms_energy, time, t_frames, audio_file_path = analyse_audio(
        AUDIO_FILE_SAX_A3
    )
    if y is None:
        logging.error("Failed to analyse audio file")
        sys.exit(1)

    # Plot the original signal and RMS Energy
    fig, ax = create_plot()
    ax.plot(time, y, color=ORIGINAL_SIGNAL_COLOR, label="Original Signal")
    ax.plot(t_frames, rms_energy, color=RMS_ENERGY_COLOR, label="RMS Energy")
    configure_plot(
        ax,
        title=os.path.basename(audio_file_path),
        subtitle="Original Signal and RMS Energy",
    )
    plt.legend()
    plt.tight_layout()

    # Save the plot
    save_plot(fig, AUDIO_FILE_SAX_A3)

    # Show the plot
    plt.show()
