# LookML Network Visualizer

[![pypi package](https://img.shields.io/pypi/v/lookml_visualizer.svg)](https://pypi.org/project/lookml_visualizer/)

**TL;DR** Visualize [LookML](https://docs.looker.com/data-modeling/learning-lookml/what-is-lookml) contents as a network diagram in an interactive Plotly figure.

Built on top of `lookml-tools`'s [grapher](https://github.com/ww-tech/lookml-tools/blob/master/lkmltools/grapher/lookml_grapher.py). Requires NetworkX, graphviz, and Plotly.

### Getting Started

```python
from lookml_visualizer import PlotNetwork

network = PlotNetwork(lkml_paths=['./my_lookml_project/*.lkml'])
```

To save the interactive plot as an HTML file:

```python
network.fig.save_to_html(output_name='my_lookml_network.html')
```

### Examples

Example1: A tiny project

![](./examples/lookml_visualizer_sample1.gif)

Example2: A large project

![](./examples/lookml_visualizer_sample2.gif)

<hr>

**Plot layouts**

The network plot can have different layouts. The following example shows how to pass a different plot layout:

```python
network = PlotNetwork(paths, plot_layout='fdp')
```
which will display the same network in example 2 (above) in this layout:
![image](https://user-images.githubusercontent.com/3298308/103260846-2838b500-496d-11eb-9f01-ab15704983e6.png)

> `plot_layout` options: 'dot', 'twopi', 'fdp', 'sfdp', 'circo'

### Install

```bash
$ pip install lookml_visualizer
```
Also, if not installed, need to install PyGraphviz

```bash
$ brew install graphviz
```
