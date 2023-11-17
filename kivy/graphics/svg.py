# encoding: utf-8
# module kivy.graphics.svg
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\svg.cp311-win_amd64.pyd
# by generator 1.147
"""
SVG
===

.. versionadded:: 1.9.0

.. warning::

    This is highly experimental and subject to change. Don't use it in
    production.


Load an SVG as a graphics instruction::

    from kivy.graphics.svg import Svg
    with widget.canvas:
        svg = Svg("image.svg")

There is no widget that can display Svg directly, you have to make your own for
now. Check the `examples/svg` for more information.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import math as math # <module 'math' (built-in)>
import re as re # C:\Users\matthew.muller\AppData\Local\Programs\Python\Python311\Lib\re\__init__.py
from array import array

from kivy._metrics import dpi2px

from time import time

import kivy.graphics.instructions as __kivy_graphics_instructions


# Variables with simple values

hexdigits = '0123456789abcdefABCDEF'

# functions

def parse(source, parser=None): # reliably restored by inspect
    """
    Parse XML document into element tree.
    
        *source* is a filename or file object containing XML data,
        *parser* is an optional parser instance defaulting to XMLParser.
    
        Return an ElementTree instance.
    """
    pass

def _tokenize_path(pathdef): # real signature unknown; restored from __doc__
    """ _tokenize_path(pathdef) """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Svg(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Svg(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class Gradient(object):
    # no doc
    def get_params(self, parent): # real signature unknown; restored from __doc__
        """ Gradient.get_params(self, parent) """
        pass

    def interp(self, float_x, float_y): # real signature unknown; restored from __doc__
        """ Gradient.interp(self, float x, float y) """
        pass

    def tardy_gradient_parsed(self, gradient): # real signature unknown; restored from __doc__
        """ Gradient.tardy_gradient_parsed(self, gradient) """
        pass

    def __init__(self, element, svg): # real signature unknown; restored from __doc__
        """ Gradient.__init__(self, element, svg) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.graphics.svg', '__init__': <cyfunction Gradient.__init__ at 0x00000155D55482B0>, 'interp': <cyfunction Gradient.interp at 0x00000155D56C01E0>, 'get_params': <cyfunction Gradient.get_params at 0x00000155D56C3B90>, 'tardy_gradient_parsed': <cyfunction Gradient.tardy_gradient_parsed at 0x00000155D56EB440>, '__dict__': <attribute '__dict__' of 'Gradient' objects>, '__weakref__': <attribute '__weakref__' of 'Gradient' objects>, '__doc__': None})"


class GradientContainer(dict):
    # no doc
    def call_me_on_add(self, callback, grad_id): # real signature unknown; restored from __doc__
        """
        GradientContainer.call_me_on_add(self, callback, grad_id)
        The client wants to know when the gradient with id grad_id gets
                added.  So store this callback for when that happens.
                When the desired gradient is added, the callback will be called
                with the gradient as the first and only argument.
        """
        pass

    def update(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ GradientContainer.update(self, *args, **kwargs) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ GradientContainer.__init__(self, *args, **kwargs) """
        pass

    def __setitem__(self, key, val): # real signature unknown; restored from __doc__
        """ GradientContainer.__setitem__(self, key, val) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.graphics.svg', '__init__': <cyfunction GradientContainer.__init__ at 0x00000155D54DBD30>, 'call_me_on_add': <cyfunction GradientContainer.call_me_on_add at 0x00000155D54DBED0>, 'update': <cyfunction GradientContainer.update at 0x00000155D5548110>, '__setitem__': <cyfunction GradientContainer.__setitem__ at 0x00000155D55481E0>, '__dict__': <attribute '__dict__' of 'GradientContainer' objects>, '__weakref__': <attribute '__weakref__' of 'GradientContainer' objects>, '__doc__': None})"


class LinearGradient(Gradient):
    # no doc
    def grad_value(self, x, y): # real signature unknown; restored from __doc__
        """ LinearGradient.grad_value(self, x, y) """
        pass

    def __init__(self, element, svg): # real signature unknown; restored from __doc__
        """ Gradient.__init__(self, element, svg) """
        pass

    params = [
        'x1',
        'x2',
        'y1',
        'y2',
        'stops',
    ]


class Matrix(object):
    """ Matrix(string=None) """
    def inverse(self): # real signature unknown; restored from __doc__
        """ Matrix.inverse(self) -> Matrix """
        return Matrix

    def __init__(self, string=None): # real signature unknown; restored from __doc__
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Matrix.__reduce_cython__(self) """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Matrix.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000155D598BED0>'


class RadialGradient(Gradient):
    # no doc
    def grad_value(self, x, y): # real signature unknown; restored from __doc__
        """ RadialGradient.grad_value(self, x, y) """
        pass

    def __init__(self, element, svg): # real signature unknown; restored from __doc__
        """ Gradient.__init__(self, element, svg) """
        pass

    params = [
        'cx',
        'cy',
        'r',
        'stops',
    ]


class Svg(__kivy_graphics_instructions.RenderContext):
    """
    Svg(source=None, anchor_x=0, anchor_y=0, bezier_points=64, circle_points=64, color=None)
    Svg class. See module for more information about the usage.
    """
    def set_tree(self, tree): # real signature unknown; restored from __doc__
        """
        Svg.set_tree(self, tree)
        
                sets the tree used to render the Svg and triggers reloading.
        
                :param xml.etree.cElementTree tree: the tree parsed from the SVG source
        
                .. versionadded:: 2.0.0
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """
        Creates an SVG object from a .svg or .svgz file.
        
                :param str source: The name of the file to be loaded.
                :param float anchor_x: The horizontal anchor position for scaling and
                    rotations. Defaults to 0. The symbolic values 'left', 'center' and
                    'right' are also accepted.
                :param float anchor_y: The vertical anchor position for scaling and
                    rotations. Defaults to 0. The symbolic values 'bottom', 'center' and
                    'top' are also accepted.
                :param int bezier_points: The number of line segments into which to
                    subdivide Bezier splines. Defaults to 10.
                :param int circle_points: The number of line segments into which to
                    subdivide circular and elliptic arcs. Defaults to 10.
                :param color the default color to use for Svg elements that specify "currentColor"
        
                .. note:: if you want to use SVGs from string, you can parse the source yourself
                    using `from xml.etree.cElementTree import fromstring` and pass the result to
                    Svg().set_tree(). This will trigger the rendering of the Svg - as an alternative
                    to assigning a filepath to Svg.source. This is also viable to trigger reloading.
        
                .. versionchanged:: 2.0.0
                    Parameter `filename` changed to `source` and made optional.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Svg.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Svg.__setstate_cython__(self, __pyx_state) """
        pass

    anchor_x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Horizontal anchor position for scaling and rotations. Defaults to 0. The
        symbolic values 'left', 'center' and 'right' are also accepted.
        """

    anchor_y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Vertical anchor position for scaling and rotations. Defaults to 0. The
        symbolic values 'bottom', 'center' and 'top' are also accepted.
        """

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default color

        Used for SvgElements that specify "currentColor"

        .. versionchanged:: 1.10.3

            The color is gettable and settable

        .. versionadded:: 1.9.1
        """

    current_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """current_color: object"""

    gradients = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """gradients: object"""

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """height: 'double'"""

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Filename / source to load.

        The parsing and rendering is done as soon as you set the source.

        .. versionchanged:: 2.0.0
            The property name is now `source` instead of `filename`

        .. versionchanged:: 1.10.3
            You can get the used filename
        """

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """width: 'double'"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000155D598BF30>'


# variables with complex values

hex_colormap = {
    'aliceblue': '#f0f8ff',
    'antiquewhite': '#faebd7',
    'aqua': '#00ffff',
    'aquamarine': '#7fffd4',
    'azure': '#f0ffff',
    'beige': '#f5f5dc',
    'bisque': '#ffe4c4',
    'black': '#000000',
    'blanchedalmond': '#ffebcd',
    'blue': '#0000ff',
    'blueviolet': '#8a2be2',
    'brown': '#a52a2a',
    'burlywood': '#deb887',
    'cadetblue': '#5f9ea0',
    'chartreuse': '#7fff00',
    'chocolate': '#d2691e',
    'coral': '#ff7f50',
    'cornflowerblue': '#6495ed',
    'cornsilk': '#fff8dc',
    'crimson': '#dc143c',
    'cyan': '#00ffff',
    'darkblue': '#00008b',
    'darkcyan': '#008b8b',
    'darkgoldenrod': '#b8860b',
    'darkgray': '#a9a9a9',
    'darkgreen': '#006400',
    'darkgrey': '#a9a9a9',
    'darkkhaki': '#bdb76b',
    'darkmagenta': '#8b008b',
    'darkolivegreen': '#556b2f',
    'darkorange': '#ff8c00',
    'darkorchid': '#9932cc',
    'darkred': '#8b0000',
    'darksalmon': '#e9967a',
    'darkseagreen': '#8fbc8f',
    'darkslateblue': '#483d8b',
    'darkslategray': '#2f4f4f',
    'darkslategrey': '#2f4f4f',
    'darkturquoise': '#00ced1',
    'darkviolet': '#9400d3',
    'deeppink': '#ff1493',
    'deepskyblue': '#00bfff',
    'dimgray': '#696969',
    'dimgrey': '#696969',
    'dodgerblue': '#1e90ff',
    'firebrick': '#b22222',
    'floralwhite': '#fffaf0',
    'forestgreen': '#228b22',
    'fuchsia': '#ff00ff',
    'gainsboro': '#dcdcdc',
    'ghostwhite': '#f8f8ff',
    'gold': '#ffd700',
    'goldenrod': '#daa520',
    'gray': '#808080',
    'green': '#008000',
    'greenyellow': '#adff2f',
    'grey': '#808080',
    'honeydew': '#f0fff0',
    'hotpink': '#ff69b4',
    'indianred': '#cd5c5c',
    'indigo': '#4b0082',
    'ivory': '#fffff0',
    'khaki': '#f0e68c',
    'lavender': '#e6e6fa',
    'lavenderblush': '#fff0f5',
    'lawngreen': '#7cfc00',
    'lemonchiffon': '#fffacd',
    'lightblue': '#add8e6',
    'lightcoral': '#f08080',
    'lightcyan': '#e0ffff',
    'lightgoldenrodyellow': '#fafad2',
    'lightgray': '#d3d3d3',
    'lightgreen': '#90ee90',
    'lightgrey': '#d3d3d3',
    'lightpink': '#ffb6c1',
    'lightsalmon': '#ffa07a',
    'lightseagreen': '#20b2aa',
    'lightskyblue': '#87cefa',
    'lightslategray': '#778899',
    'lightslategrey': '#778899',
    'lightsteelblue': '#b0c4de',
    'lightyellow': '#ffffe0',
    'lime': '#00ff00',
    'limegreen': '#32cd32',
    'linen': '#faf0e6',
    'magenta': '#ff00ff',
    'maroon': '#800000',
    'mediumaquamarine': '#66cdaa',
    'mediumblue': '#0000cd',
    'mediumorchid': '#ba55d3',
    'mediumpurple': '#9370db',
    'mediumseagreen': '#3cb371',
    'mediumslateblue': '#7b68ee',
    'mediumspringgreen': '#00fa9a',
    'mediumturquoise': '#48d1cc',
    'mediumvioletred': '#c71585',
    'midnightblue': '#191970',
    'mintcream': '#f5fffa',
    'mistyrose': '#ffe4e1',
    'moccasin': '#ffe4b5',
    'navajowhite': '#ffdead',
    'navy': '#000080',
    'oldlace': '#fdf5e6',
    'olive': '#808000',
    'olivedrab': '#6b8e23',
    'orange': '#ffa500',
    'orangered': '#ff4500',
    'orchid': '#da70d6',
    'palegoldenrod': '#eee8aa',
    'palegreen': '#98fb98',
    'paleturquoise': '#afeeee',
    'palevioletred': '#db7093',
    'papayawhip': '#ffefd5',
    'peachpuff': '#ffdab9',
    'peru': '#cd853f',
    'pink': '#ffc0cb',
    'plum': '#dda0dd',
    'powderblue': '#b0e0e6',
    'purple': '#800080',
    'red': '#ff0000',
    'rosybrown': '#bc8f8f',
    'royalblue': '#4169e1',
    'saddlebrown': '#8b4513',
    'salmon': '#fa8072',
    'sandybrown': '#f4a460',
    'seagreen': '#2e8b57',
    'seashell': '#fff5ee',
    'sienna': '#a0522d',
    'silver': '#c0c0c0',
    'skyblue': '#87ceeb',
    'slateblue': '#6a5acd',
    'slategray': '#708090',
    'slategrey': '#708090',
    'snow': '#fffafa',
    'springgreen': '#00ff7f',
    'steelblue': '#4682b4',
    'tan': '#d2b48c',
    'teal': '#008080',
    'thistle': '#d8bfd8',
    'tomato': '#ff6347',
    'turquoise': '#40e0d0',
    'violet': '#ee82ee',
    'wheat': '#f5deb3',
    'white': '#ffffff',
    'whitesmoke': '#f5f5f5',
    'yellow': '#ffff00',
    'yellowgreen': '#9acd32',
}

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

NUMERIC_FORMATS = (
    'in',
    'px',
    'dp',
    'sp',
    'pt',
    'cm',
    'mm',
)

Window = None # (!) real value is '<kivy.core.window.window_sdl2.WindowSDL object at 0x00000155D64C6D60>'

__all__ = (
    'Svg',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000155D54A4650>'

__pyx_capi__ = {
    'COMMANDS': None, # (!) real value is '<capsule object "PyObject *" at 0x00000155D598BC30>'
    'RE_COMMAND': None, # (!) real value is '<capsule object "PyObject *" at 0x00000155D598BCC0>'
    'RE_FLOAT': None, # (!) real value is '<capsule object "PyObject *" at 0x00000155D598BCF0>'
    'RE_LIST': None, # (!) real value is '<capsule object "PyObject *" at 0x00000155D598BC90>'
    'RE_POLYLINE': None, # (!) real value is '<capsule object "PyObject *" at 0x00000155D598BD20>'
    'RE_TRANSFORM': None, # (!) real value is '<capsule object "PyObject *" at 0x00000155D598BD50>'
    'UPPERCASE': None, # (!) real value is '<capsule object "PyObject *" at 0x00000155D598BC60>'
    'VERTEX_FORMAT': None, # (!) real value is '<capsule object "struct __pyx_obj_4kivy_8graphics_6vertex_VertexFormat *" at 0x00000155D598BD80>'
    'kv_color_to_int_color': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x00000155D598BDB0>'
    'parse_color': None, # (!) real value is '<capsule object "PyObject *(PyObject *, struct __pyx_opt_args_4kivy_8graphics_3svg_parse_color *__pyx_optional_args)" at 0x00000155D598BE70>'
    'parse_float': None, # (!) real value is '<capsule object "float (PyObject *)" at 0x00000155D598BDE0>'
    'parse_list': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x00000155D598BE10>'
    'parse_style': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x00000155D598BE40>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.svg', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000155D54A4650>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\svg.cp311-win_amd64.pyd')"

__test__ = {}

