# LookML Network Visualizer

**TL;DR** Visualize LookML contents as an interactive Plotly figure.

Built on top of `lookml-tools`'s [grapher](https://github.com/ww-tech/lookml-tools/blob/master/lkmltools/grapher/lookml_grapher.py). Requires NetworkX and Plotly.  

### Getting Started

```python
from lookml_visualizer import PlotNetwork

network = PlotNetwork(lkml_paths=['path-to-lkml-files'])
```

TODO: gif for the example output from Jupyter notebook


To save the interactive plot as an HTML file:

```python
network.fig.save_to_html(output_name='my_lookml_network.html')
```



### Install

```bash
$ pip install lookml_visualizer
```
Also, if not installed, need to install PyGraphviz

```bash
$ brew install PyGraphviz
```
