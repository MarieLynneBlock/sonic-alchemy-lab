import os
import sys
import logging
import librosa

# import numpy as np
import matplotlib.pyplot as plt

from .config import audio_config

# from .logging import setup_logging
# from .matplotlib_plots import configure_plot


def setup_environment():
    root_dir = os.path.abspath(os.path.join(os.getcwd(), "../"))
    if root_dir not in sys.path:
        sys.path.append(root_dir)


def load_audio(audio_file_key):
    audio_file_path = audio_config.get_audio_file(audio_file_key)
    try:
        y, sr = librosa.load(audio_file_path, sr=None)
        return y, sr, audio_file_path
    except FileNotFoundError:
        logging.error(f"File not found: {audio_file_path}")
    except Exception as e:
        logging.error(f"Error loading audio file: {e}")
    return None, None, None


def create_plot(figsize=(14, 5)):
    return plt.subplots(figsize=figsize)
