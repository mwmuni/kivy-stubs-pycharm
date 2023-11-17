# encoding: utf-8
# module kivy.graphics.tesselator
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\tesselator.cp311-win_amd64.pyd
# by generator 1.147
"""
Tesselator
==========

.. versionadded:: 1.9.0

.. image:: images/tesselator-filled.png
    :align: right
.. image:: images/tesselator-debug.png
    :align: right

.. warning::

    This is experimental and subject to change as long as this warning notice
    is present. Only TYPE_POLYGONS is currently supported.

Tesselator is a library for tesselating polygons, based on
`libtess2 <https://github.com/memononen/libtess2>`_. It renders concave filled
polygons by first tesselating them into convex polygons. It also supports holes.

Usage
-----

First, you need to create a :class:`Tesselator` object and add contours. The
first one is the external contour of your shape and all of the following ones
should be holes::

    from kivy.graphics.tesselator import Tesselator

    tess = Tesselator()
    tess.add_contour([0, 0, 200, 0, 200, 200, 0, 200])
    tess.add_contour([50, 50, 150, 50, 150, 150, 50, 150])

Second, call the :meth:`Tesselator.tesselate` method to compute the points. It
is possible that the tesselator won't work. In that case, it can return
False::

    if not tess.tesselate():
        print("Tesselator didn't work :(")
        return

After the tessellation, you have multiple ways to iterate over the result. The
best approach is using :data:`Tesselator.meshes` to get a format directly usable
for a :class:`~kivy.graphics.Mesh`::

    for vertices, indices in tess.meshes:
        self.canvas.add(Mesh(
            vertices=vertices,
            indices=indices,
            mode="triangle_fan"
        ))

Or, you can get the "raw" result, with just polygons and x/y coordinates with
:meth:`Tesselator.vertices`::

    for vertices in tess.vertices:
        print("got polygon", vertices)
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from array import array


# Variables with simple values

TYPE_BOUNDARY_CONTOURS = 2

TYPE_POLYGONS = 0

WINDING_ABS_GEQ_TWO = 4

WINDING_NEGATIVE = 3
WINDING_NONZERO = 1
WINDING_ODD = 0
WINDING_POSITIVE = 2

# functions

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class Tesselator(object):
    """ Tesselator class. See module for more information about the usage. """
    def add_contour(self, points): # real signature unknown; restored from __doc__
        """
        Tesselator.add_contour(self, points)
        
                Add a contour to the tesselator. It can be:
        
                - a list of `[x, y, x2, y2, ...]` coordinates
                - a float array: `array("f", [x, y, x2, y2, ...])`
                - any buffer with floats in it.
        """
        pass

    def tesselate(self, int_winding_rule=None, int_element_type=None, int_polysize=65535): # real signature unknown; restored from __doc__
        """
        Tesselator.tesselate(self, int winding_rule=WINDING_ODD, int element_type=TYPE_POLYGONS, int polysize=65535) -> int
        
                Compute all the contours added with :meth:`add_contour`, and generate
                polygons.
        
                :Parameters:
                    `winding_rule`: enum
                        The winding rule classifies a region as inside if its winding
                        number belongs to the chosen category. Can be one of
                        WINDING_ODD, WINDING_NONZERO, WINDING_POSITIVE,
                        WINDING_NEGATIVE, WINDING_ABS_GEQ_TWO. Defaults to WINDING_ODD.
                    `element_type`: enum
                        The result type, you can generate the polygons with
                        TYPE_POLYGONS, or the contours with TYPE_BOUNDARY_CONTOURS.
                        Defaults to TYPE_POLYGONS.
                :return: 1 if the tessellation happened, 0 otherwise.
                :rtype: int
        """
        return 0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Tesselator.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Tesselator.__setstate_cython__(self, __pyx_state) """
        pass

    element_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of convex polygon.
        """

    meshes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Iterate through the result of the :meth:`tesselate` to give a result
        that can be easily pushed into Kivy`s Mesh object.

        It's a list of: `[[vertices, indices], [vertices, indices], ...]`.
        The vertices in the format `[x, y, u, v, x2, y2, u2, v2]`.

        Careful, u/v coordinates are the same as x/y.
        You are responsible to change them for texture mapping if you need to.

        You can create Mesh objects like that::

            tess = Tesselator()
            # add contours here
            tess.tesselate()
            for vertices, indices in self.meshes:
                self.canvas.add(Mesh(
                    vertices=vertices,
                    indices=indices,
                    mode="triangle_fan"))
        """

    vertex_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of vertex generated.

        This is the raw result, however, because the Tesselator format the
        result for you with :data:`meshes` or :data:`vertices` per polygon,
        you'll have more vertices in the result
        """

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Iterate through the result of the :meth:`tesselate` in order to give
        only a list of `[x, y, x2, y2, ...]` polygons.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000216F112B7E0>'


# variables with complex values

__all__ = (
    'Tesselator',
    'WINDING_ODD',
    'WINDING_NONZERO',
    'WINDING_POSITIVE',
    'WINDING_NEGATIVE',
    'TYPE_POLYGONS',
    'TYPE_BOUNDARY_CONTOURS',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000216F0D34650>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.tesselator', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000216F0D34650>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\tesselator.cp311-win_amd64.pyd')"

__test__ = {}

