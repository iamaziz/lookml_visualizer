from __future__ import annotations

from . import Grapher
from . import Visualizer


class PlotNetwork:
    def __init__(self, lkml_paths: list[str], **kwargs):
        self.grapher, self.g = Grapher.run(lkml_paths=lkml_paths, **kwargs)
        self.fig = Visualizer(self.grapher, self.g, **kwargs)
