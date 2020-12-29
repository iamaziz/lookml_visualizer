from __future__ import annotations

from lkmltools.grapher.lookml_grapher import LookMlGrapher


class Grapher:
    """Interface to LookMlGrapher()"""

    @staticmethod
    def run(
        lkml_paths: list[str],
        output: str = "lookml_diagram.png",
        title: str = "Hello, World!",
        **kwargs,
    ):
        # create the LookML grapher
        grapher = LookMlGrapher(config="None")

        # parse LookML and extract graph info from the input files
        grapher.extract_graph_info(lkml_paths)

        # create nx DiGraph object
        g = grapher.create_graph()

        # plot
        args = {}
        args["g"] = g
        args["filename"] = output
        args["title"] = title
        grapher.plot_graph(**args)

        return grapher, g
