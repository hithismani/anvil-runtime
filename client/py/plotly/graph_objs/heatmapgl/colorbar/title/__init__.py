
from anvil.util import WrappedObject, WrappedList
from anvil.server import serializable_type


@serializable_type
class Font(WrappedObject):
    _name = "Font"
    _module = "plotly.graph_objs.heatmapgl.colorbar.title"


__all__ = [
    'Font',
]