# import matplotlib.pyplot as plt

from .parameters import (
    BACKGROUND_COLOR,
    # ORIGINAL_SIGNAL_COLOR,
    # AMPLITUDE_ENVELOPE_COLOR,
    SPINE_COLOR,
    FONTSIZE_TITLE,
    FONTSIZE_SUBTITLE,
)


def configure_plot(ax, title, subtitle):
    """Configure the plot with the given title and subtitle."""
    # Set background color
    ax.figure.patch.set_facecolor(BACKGROUND_COLOR)
    ax.set_facecolor(BACKGROUND_COLOR)

    # Set titles and labels
    ax.set_xlabel("Time [s]", color=SPINE_COLOR)
    ax.set_ylabel("Amplitude", color=SPINE_COLOR)

    # Set the axes spine color
    for spine in ax.spines.values():
        spine.set_color(SPINE_COLOR)

    # Set the tick parameters color
    ax.tick_params(axis="x", colors=SPINE_COLOR)
    ax.tick_params(axis="y", colors=SPINE_COLOR)

    # Add the song title in bold and the subtitle below it
    ax.text(
        0.5,
        1.10,
        title,
        transform=ax.transAxes,
        fontsize=FONTSIZE_TITLE,
        fontweight="bold",
        color=SPINE_COLOR,
        ha="center",
    )
    ax.text(
        0.5,
        1.04,
        subtitle,
        transform=ax.transAxes,
        fontsize=FONTSIZE_SUBTITLE,
        fontweight="normal",
        color=SPINE_COLOR,
        ha="center",
    )

    # Customize the legend
    legend = ax.legend(
        facecolor=BACKGROUND_COLOR,
        edgecolor=SPINE_COLOR,
        labelcolor=SPINE_COLOR,
    )
    for text in legend.get_texts():
        text.set_color(SPINE_COLOR)
