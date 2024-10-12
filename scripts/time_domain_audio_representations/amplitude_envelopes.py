import os
import sys
import logging
import librosa
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.io as pio


# Local imports & configurations
from config.config import audio_config, output_config
from config.parameters import (
    AUDIO_FILE_SAX_A3,
    ORIGINAL_SIGNAL_COLOR,
    AMPLITUDE_ENVELOPE_COLOR,
    BACKGROUND_COLOR,
)
from config.logging import setup_logging
from config.matplotlib_plots import configure_plot
from config.plotly_plots import configure_plotly_layout


# Adjust sys.path to include the root directory
root_dir = os.path.abspath(os.path.join(os.getcwd(), "../../"))
if root_dir not in sys.path:
    sys.path.append(root_dir)

# Ensure the config directory is in the path
config_dir = os.path.join(root_dir, "config")
if config_dir not in sys.path:
    sys.path.append(config_dir)


# Set up logging for this script
script_path = os.path.join(os.getcwd(), "amplitude_envelopes.py")
setup_logging(script_path)


def load_audio_file(audio_file_path):
    """Load an audio file."""
    logging.info(f"Loading audio file from: {audio_file_path}")
    return librosa.load(audio_file_path, sr=None)


def calculate_amplitude_envelope(y, frame_size=2056, hop_length=128):
    """Calculate the amplitude envelope of an audio signal."""
    logging.info("Calculating amplitude envelope")
    frames = librosa.util.frame(
        y, frame_length=frame_size, hop_length=hop_length
    )
    return frames.max(axis=0)


def plot_signals(time, y, t_frames, amplitude_envelope, audio_file_path):
    """Plot the original signal and amplitude envelope using matplotlib."""
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(time, y, color=ORIGINAL_SIGNAL_COLOR, label="Original Signal")
    ax.plot(
        t_frames,
        amplitude_envelope,
        color=AMPLITUDE_ENVELOPE_COLOR,
        label="Amplitude Envelope",
    )
    configure_plot(
        ax,
        title=os.path.basename(audio_file_path),
        subtitle="Original Signal and Amplitude Envelope",
    )
    plt.show()


def save_plot(fig, audio_file_path):
    """Save the plot to the output directory."""
    output_directory = output_config.get_output_directory("time_domain")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_path = os.path.join(
        output_directory,
        f"AE_{os.path.splitext(os.path.basename(audio_file_path))[0]}.png",
    )
    fig.savefig(output_path, facecolor=BACKGROUND_COLOR)


def plot_interactive_signals(
    time, y, t_frames, amplitude_envelope, audio_file_path
):
    """Create an interactive plot of the original signal and amplitude envelope
    using plotly."""

    logging.info("Creating interactive plot")

    # Create traces for the original signal and amplitude envelope
    original_trace = go.Scatter(
        x=time,
        y=y,
        mode="lines",
        name="Original Signal",
        line=dict(color=ORIGINAL_SIGNAL_COLOR),
    )
    envelope_trace = go.Scatter(
        x=t_frames,
        y=amplitude_envelope,
        mode="lines",
        name="Amplitude Envelope",
        line=dict(color=AMPLITUDE_ENVELOPE_COLOR),
    )

    # Use the configure_plotly_layout function
    layout = configure_plotly_layout("Interactive Plot", audio_file_path)

    # Create the figure
    fig = go.Figure(data=[original_trace, envelope_trace], layout=layout)

    # Show the plot
    pio.show(fig)


def analyse_audio(audio_file_path, interactive=False):
    """Analyse the audio file and plot the amplitude envelope."""
    try:
        y, sr = load_audio_file(audio_file_path)
        amplitude_envelope = calculate_amplitude_envelope(y)
        time = np.linspace(0, len(y) / sr, num=len(y))
        frames_count = amplitude_envelope.shape[0]
        t_frames = librosa.frames_to_time(
            range(frames_count), sr=sr, hop_length=128
        )

        # Choose between interactive and static plotting
        if interactive:
            plot_interactive_signals(
                time, y, t_frames, amplitude_envelope, audio_file_path
            )
        else:
            plot_signals(
                time, y, t_frames, amplitude_envelope, audio_file_path
            )

        save_plot(plt.gcf(), audio_file_path)
        return y, sr, amplitude_envelope, time, t_frames
    except FileNotFoundError:
        logging.error(f"File not found: {audio_file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


# Set the audio file to analyse
audio_file_key = AUDIO_FILE_SAX_A3
audio_file_path = audio_config.get_audio_file(audio_file_key)

try:
    # Set interactive=True for plotly, False for matplotlib
    y, sr, amplitude_envelope, time, t_frames = analyse_audio(
        audio_file_path, interactive=True
    )
    logging.info(f"Successfully analysed audio file {audio_file_path}")
except Exception as e:
    logging.error(f"Error analysing audio file {audio_file_path}: {e}")
    raise
