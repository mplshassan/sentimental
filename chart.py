# mpls.hassan
import plotly.graph_objects as go


def compound_color(score: float) -> str:
    if score >= 0.05:
        return "#ffffc5"  # positive: yellow
    elif score <= -0.05:
        return "#c5c5ff"  # negative: blue
    return "#888888"  # neutral: gray


def build_chart(sentences: list[str], scores: list[float]) -> go.Figure:
    colors = [compound_color(s) for s in scores]
    labels = [
        f"{i + 1}. {s[:40]}{'…' if len(s) > 40 else ''}"
        for i, s in enumerate(sentences)
    ]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=list(range(1, len(scores) + 1)),
            y=scores,
            mode="lines+markers",
            line=dict(color="rgba(128,128,128,0.4)", width=1.5),
            marker=dict(
                color=colors, size=10, line=dict(color="rgba(0,0,0,0)", width=2)
            ),
            text=labels,
            hovertemplate="%{text}<br>compound: %{y:.3f}<extra></extra>",
        )
    )

    fig.add_hline(y=0, line=dict(color="rgba(128,128,128,0.25)", width=1, dash="dot"))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Latin Modern Roman, Georgia, serif",
            color="rgba(128,128,128,0.8)",
            size=11,
        ),
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=True,
            tickfont=dict(color="rgba(128,128,128,0.5)"),
            title="",
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(128,128,128,0.1)",
            zeroline=False,
            range=[-1.1, 1.1],
            tickfont=dict(color="rgba(128,128,128,0.5)"),
            title="",
        ),
        showlegend=False,
        height=280,
    )
    return fig
