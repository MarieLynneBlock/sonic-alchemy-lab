import plotly.graph_objs as go

import os
from .parameters import (
    BACKGROUND_COLOR,
    SPINE_COLOR,
    FONTSIZE_TITLE,
)


def configure_plotly_layout(title, audio_file_path):
    """Configure the layout for plotly plots."""
    layout = go.Layout(
        title={
            "text": f"Interactive Plot: {os.path.basename(audio_file_path)}",
            "x": 0.5,
            "xanchor": "center",
            "font": {
                "size": FONTSIZE_TITLE,
                "color": SPINE_COLOR,
                "family": "Arial",
            },
        },
        xaxis=dict(
            title="Time (s)",
            color=SPINE_COLOR,
            tickfont=dict(color=SPINE_COLOR),
        ),
        yaxis=dict(
            title="Amplitude",
            color=SPINE_COLOR,
            tickfont=dict(color=SPINE_COLOR),
        ),
        plot_bgcolor=BACKGROUND_COLOR,  # background for the plot area
        paper_bgcolor=BACKGROUND_COLOR,  # background for the entire figure
        font=dict(color=SPINE_COLOR),  # Font color for better contrast
        legend=dict(
            bgcolor=BACKGROUND_COLOR,
            bordercolor=SPINE_COLOR,
            font=dict(color=SPINE_COLOR),
        ),
    )
    return layout
