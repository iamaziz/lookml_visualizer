# LookML Network Visualizer

[![pypi package](https://img.shields.io/pypi/v/lookml_visualizer.svg)](https://pypi.org/project/lookml_visualizer/)

**TL;DR** Visualize [LookML](https://docs.looker.com/data-modeling/learning-lookml/what-is-lookml) contents as an interactive Plotly figure.

Built on top of `lookml-tools`'s [grapher](https://github.com/ww-tech/lookml-tools/blob/master/lkmltools/grapher/lookml_grapher.py). Requires NetworkX and Plotly.  

### Getting Started

```python
from lookml_visualizer import PlotNetwork

network = PlotNetwork(lkml_paths=['./my_lookml_project/*.lkml'])
```

To save the interactive plot as an HTML file:

```python
network.fig.save_to_html(output_name='my_lookml_network.html')
```

**Example**

![](./examples/lookml_visualizer_sample1.gif)


### Install

```bash
$ pip install lookml_visualizer
```
Also, if not installed, need to install PyGraphviz

```bash
$ brew install graphviz
```
