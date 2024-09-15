"""This file contains configuration parameters for audio analysis and
visualization.

Analysis Parameters:
- DEFAULT_HOP_LENGTH: The number of samples between successive frames.
- DEFAULT_N_FFT: The length of the windowed signal for FFT.
- DEFAULT_FRAME_LENGTH: The length of each frame for analysis.

Visualization Parameters:
- FIGURE_SIZE: Default size for matplotlib figures.
- FONTSIZE_TITLE: Font size for plot titles.
- FONTSIZE_SUBTITLE: Font size for plot subtitles.

Color Schemes:
- Various color constants for different elements in visualizations.

Audio Files:
- Constants for referencing specific audio files used in the project.
"""

# Analysis Parameters
DEFAULT_HOP_LENGTH = 512
DEFAULT_N_FFT = 2048
DEFAULT_FRAME_LENGTH = 1024

# Visualisation Parameters
FIGURE_SIZE = (14, 5)
FONTSIZE_TITLE = 14
FONTSIZE_SUBTITLE = 12

# Color Schemes Matplotlib
BACKGROUND_COLOR = "#2E3440"
ORIGINAL_SIGNAL_COLOR = "#81A1C1"
AMPLITUDE_ENVELOPE_COLOR = "#BF616A"
RMS_ENERGY_COLOR = "#A3BE8C"
SPINE_COLOR = "#D8DEE9"

# Font Sizes Matplotlib
FONTSIZE_TITLE = 14
FONTSIZE_SUBTITLE = 12

# Audio Files
AUDIO_FILE_SAX_A3 = "sax_a3"
AUDIO_FILE_SUNO_WITS = "suno_wits"
