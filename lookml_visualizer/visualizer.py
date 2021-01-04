from __future__ import annotations

import plotly.graph_objects as go
from networkx.classes.digraph import DiGraph
from networkx.drawing.nx_pydot import graphviz_layout
from lkmltools.grapher.lookml_grapher import LookMlGrapher

NODES_COLOR = {
    "MODEL": "#b3cde3",  # blue
    "EXPLORE": "#ccebc5",  # green
    "VIEW": "#decbe4",  # purple
    "ORPHAN": "#FFA500",  # orange
}


class Visualizer:
    def __init__(self, grapher: LookMlGrapher, g: DiGraph, **kwargs):
        """Create an interactive Plotly figure for input LookML network

        Args:
            grapher: the result of the parsed LookML
            g: the nx network of the relationships
            **kwargs: i.e. plot_layout: style of the node positions
        """
        color_map = self.build_color_map(grapher, g)
        plot_layout = kwargs.get("plot_layout", "dot")
        self.fig = self.plotly_lookml(g, color_map, plot_layout=plot_layout)

    @staticmethod
    def build_color_map(grapher: LookMlGrapher, g: DiGraph) -> list[str]:
        """Iter nodes in `grapher.node_map` and assign node colors

        LookML node-color map:
            models: blue
            explores: green
            views: purple
            orphans: orange

        Args:
            grapher: The LookMlGrapher() instance that contains mappings of the input LookML project
            g: The DiGraph() network of LookML nodes

        Returns:
            a list of color names for each node in `g` (len == number of nodes)

        """
        color_map = []
        for node in g:
            node_type = grapher.node_map[node].name if node else None
            color = NODES_COLOR.get(node_type, "red")  # default: red
            color_map.append(color)
        return color_map

    @staticmethod
    def plotly_lookml(
        G: DiGraph, color_map: list[str], plot_layout: str = "fdp"
    ) -> go.Figure:
        """Create an interactive plotly figure for the input `DiGraph` network

        Code source: https://plotly.com/python/network-graphs/

        Args:
            G: the DiGraph() network for LookML nodes
            color_map: color names for each node in `G`
            plot_layout: layout of the nodes positions using Pydot and Graphviz (options: 'dot', 'twopi', 'fdp', 'sfdp', 'circo')

        Returns:
            the interactive plotly figure with the LookML network rendered

        """
        # build layout (i.e. node coordinates / positions)
        pos = graphviz_layout(G, prog=plot_layout)

        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]

            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            line=dict(width=0.5, color="#888"),
            hoverinfo="none",
            mode="lines",
        )

        node_x = []
        node_y = []
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)

        node_trace = go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers",
            hoverinfo="text",
            marker=dict(
                # colorscale options
                # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                colorscale="YlGnBu",
                color=[],
                size=10,
                line_width=2,
            ),
        )
        # Color node point
        node_text = []
        for node, adjacencies in G.adjacency():
            node_text.append(node)

        node_trace.marker.color = color_map
        node_trace.text = node_text

        def layout():
            layout = go.Layout(
                title="LookML Content Relationships Network",
                titlefont_size=16,
                showlegend=False,
                hovermode="closest",
                margin=dict(b=20, l=5, r=5, t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            )
            return layout

        # Create Network Graph
        fig = go.Figure(data=[edge_trace, node_trace], layout=layout())
        fig.show()
        return fig

    def save_to_html(self, output_name: str = "interactive_plotly_figure.html"):
        """Save the interactive plotly figure to a local file

        Args:
            output_name: the output file name
        """
        import plotly

        plotly.offline.plot(self.fig, filename=output_name)
