# encoding: utf-8
# module kivy.graphics.vertex_instructions
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\vertex_instructions.cp311-win_amd64.pyd
# by generator 1.147
"""
Vertex Instructions
===================

This module includes all the classes for drawing simple vertex objects.

Updating properties
-------------------

The list attributes of the graphics instruction classes (e.g.
:attr:`Triangle.points`, :attr:`Mesh.indices` etc.) are not Kivy
properties but Python properties. As a consequence, the graphics will only
be updated when the list object itself is changed and not when list values
are modified.

For example in python:

.. code-block:: python

    class MyWidget(Button):

        triangle = ObjectProperty(None)
        def __init__(self, **kwargs):
            super(MyWidget, self).__init__(**kwargs)
            with self.canvas:
                self.triangle = Triangle(points=[0,0, 100,100, 200,0])

and in kv:

.. code-block:: kv

    <MyWidget>:
        text: 'Update'
        on_press:
            self.triangle.points[3] = 400

Although pressing the button will change the triangle coordinates,
the graphics will not be updated because the list itself has not
changed. Similarly, no updates will occur using any syntax that changes
only elements of the list e.g. self.triangle.points[0:2] = [10,10] or
self.triangle.points.insert(10) etc.
To force an update after a change, the list variable itself must be
changed, which in this case can be achieved with:

.. code-block:: kv

    <MyWidget>:
        text: 'Update'
        on_press:
            self.triangle.points[3] = 400
            self.triangle.points = self.triangle.points
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import itertools as itertools # <module 'itertools' (built-in)>
import kivy.graphics.instructions as __kivy_graphics_instructions


# Variables with simple values

platform = 'win'

# functions

def __pyx_unpickle_Bezier(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Bezier(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_BorderImage(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_BorderImage(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Ellipse(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Ellipse(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Line(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Line(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Point(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Point(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Quad(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Quad(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Rectangle(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Rectangle(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_RoundedRectangle(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_RoundedRectangle(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_SmoothLine(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_SmoothLine(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_StripMesh(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_StripMesh(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Triangle(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Triangle(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class Bezier(__kivy_graphics_instructions.VertexInstruction):
    """
    Bezier(**kwargs)
    A 2d Bezier curve.
    
        .. versionadded:: 1.0.8
    
        :Parameters:
            `points`: list
                List of points in the format (x1, y1, x2, y2...)
            `segments`: int, defaults to 180
                Define how many segments are needed for drawing the curve.
                The drawing will be smoother if you have many segments.
            `loop`: bool, defaults to False
                Set the bezier curve to join the last point to the first.
            `dash_length`: int
                Length of a segment (if dashed), defaults to 1.
            `dash_offset`: int
                Distance between the end of a segment and the start of the
                next one, defaults to 0. Changing this makes it dashed.
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Bezier.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Bezier.__setstate_cython__(self, __pyx_state) """
        pass

    dash_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the length of the dashes in the curve.
        """

    dash_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the offset between the dashes in the
        curve.
        """

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/settings the points of the triangle.

        .. warning::

            This will always reconstruct the whole graphic from the new points
            list. It can be very CPU intensive.
        """

    segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the number of segments of the curve.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDA850>'


class Rectangle(__kivy_graphics_instructions.VertexInstruction):
    """
    Rectangle(**kwargs)
    A 2d rectangle.
    
        :Parameters:
            `pos`: list
                Position of the rectangle, in the format (x, y).
            `size`: list
                Size of the rectangle, in the format (width, height).
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Rectangle.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Rectangle.__setstate_cython__(self, __pyx_state) """
        pass

    pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/settings the position of the rectangle.
        """

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/settings the size of the rectangle.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDAB50>'


class BorderImage(Rectangle):
    """
    BorderImage(**kwargs)
    A 2d border image. The behavior of the border image is similar to the
        concept of a CSS3 border-image.
    
        :Parameters:
            `border`: list
                Border information in the format (bottom, right, top, left).
                Each value is in pixels.
    
            `auto_scale`: string
                .. versionadded:: 1.9.1
    
                .. versionchanged:: 1.9.2
    
                    This used to be a bool and has been changed to be a string
                    state.
    
                Can be one of 'off', 'both', 'x_only', 'y_only', 'y_full_x_lower',
                'x_full_y_lower', 'both_lower'.
    
                Autoscale controls the behavior of the 9-slice.
    
                By default the border values are preserved exactly, meaning that
                if the total size of the object is smaller than the border values
                you will have some 'rendering errors' where your texture appears
                inside out. This also makes it impossible to achieve a rounded
                button that scales larger than the size of its source texture. The
                various options for auto_scale will let you achieve some mixes of
                the 2 types of rendering.
    
                'off': is the default and behaves as BorderImage did when auto_scale
                was False before.
    
                'both': Scales both x and y dimension borders according to the size
                of the BorderImage, this disables the BorderImage making it render
                the same as a regular Image.
    
                'x_only': The Y dimension functions as the default, and the X
                scales to the size of the BorderImage's width.
    
                'y_only': The X dimension functions as the default, and the Y
                scales to the size of the BorderImage's height.
    
                'y_full_x_lower': Y scales as in 'y_only', Y scales if the
                size of the scaled version would be smaller than the provided
                border only.
    
                'x_full_y_lower': X scales as in 'x_only', Y scales if the
                size of the scaled version would be smaller than the provided
                border only.
    
                'both_lower': This is what auto_scale did when it was True in 1.9.1
                Both X and Y dimensions will be scaled if the BorderImage is
                smaller than the source.
    
                If the BorderImage's size is less than the sum of its
                borders, horizontally or vertically, and this property is
                set to True, the borders will be rescaled to accommodate for
                the smaller size.
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ BorderImage.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ BorderImage.__setstate_cython__(self, __pyx_state) """
        pass

    auto_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for setting if the corners are automatically scaled
        when the BorderImage is too small.
        """

    border = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the border of the class.
        """

    display_border = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the border display size.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDABB0>'


class Cache(object):
    """ See module documentation for more information. """
    def append(category, key, obj, timeout=None): # reliably restored by inspect
        """
        Add a new object to the cache.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `key`: str
                        Unique identifier of the object to store.
                    `obj`: object
                        Object to store in cache.
                    `timeout`: double (optional)
                        Time after which to delete the object if it has not been used.
                        If None, no timeout is applied.
        
                :raises:
                    `ValueError`: If `None` is used as `key`.
        
                .. versionchanged:: 2.0.0
                    Raises `ValueError` if `None` is used as `key`.
        """
        pass

    def get(category, key, default=None): # reliably restored by inspect
        """
        Get a object from the cache.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `key`: str
                        Unique identifier of the object in the store.
                    `default`: anything, defaults to None
                        Default value to be returned if the key is not found.
        """
        pass

    def get_lastaccess(category, key, default=None): # reliably restored by inspect
        """
        Get the objects last access time in the cache.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `key`: str
                        Unique identifier of the object in the store.
                    `default`: anything, defaults to None
                        Default value to be returned if the key is not found.
        """
        pass

    def get_timestamp(category, key, default=None): # reliably restored by inspect
        """
        Get the object timestamp in the cache.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `key`: str
                        Unique identifier of the object in the store.
                    `default`: anything, defaults to None
                        Default value to be returned if the key is not found.
        """
        pass

    def print_usage(): # reliably restored by inspect
        """ Print the cache usage to the console. """
        pass

    def register(category, limit=None, timeout=None): # reliably restored by inspect
        """
        Register a new category in the cache with the specified limit.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `limit`: int (optional)
                        Maximum number of objects allowed in the cache.
                        If None, no limit is applied.
                    `timeout`: double (optional)
                        Time after which to delete the object if it has not been used.
                        If None, no timeout is applied.
        """
        pass

    def remove(category, key=None): # reliably restored by inspect
        """
        Purge the cache.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `key`: str (optional)
                        Unique identifier of the object in the store. If this
                        argument is not supplied, the entire category will be purged.
        """
        pass

    def _purge_by_timeout(dt): # reliably restored by inspect
        # no doc
        pass

    def _purge_oldest(category, maxpurge=1): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _categories = {
        'kv.atlas': {
            'limit': None,
            'timeout': None,
        },
        'kv.graphics.texture': '<value is a self-reference, replaced by this string>',
        'kv.image': {
            'limit': None,
            'timeout': 60,
        },
        'kv.resourcefind': '<value is a self-reference, replaced by this string>',
        'kv.shader': {
            'limit': 1000,
            'timeout': 3600,
        },
        'kv.texture': {
            'limit': 1000,
            'timeout': 60,
        },
    }
    _objects = {
        'kv.atlas': {},
        'kv.graphics.texture': '<value is a self-reference, replaced by this string>',
        'kv.image': '<value is a self-reference, replaced by this string>',
        'kv.resourcefind': '<value is a self-reference, replaced by this string>',
        'kv.shader': '<value is a self-reference, replaced by this string>',
        'kv.texture': '<value is a self-reference, replaced by this string>',
    }
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.cache', '__doc__': 'See module documentation for more information.\\n    ', '_categories': {'kv.resourcefind': {'limit': None, 'timeout': 60}, 'kv.image': {'limit': None, 'timeout': 60}, 'kv.atlas': {'limit': None, 'timeout': None}, 'kv.texture': {'limit': 1000, 'timeout': 60}, 'kv.shader': {'limit': 1000, 'timeout': 3600}, 'kv.graphics.texture': {'limit': None, 'timeout': None}}, '_objects': {'kv.resourcefind': {}, 'kv.image': {}, 'kv.atlas': {}, 'kv.texture': {}, 'kv.shader': {}, 'kv.graphics.texture': {}}, 'register': <staticmethod(<function Cache.register at 0x00000288CBE220C0>)>, 'append': <staticmethod(<function Cache.append at 0x00000288CBE22340>)>, 'get': <staticmethod(<function Cache.get at 0x00000288CBE223E0>)>, 'get_timestamp': <staticmethod(<function Cache.get_timestamp at 0x00000288CBE22480>)>, 'get_lastaccess': <staticmethod(<function Cache.get_lastaccess at 0x00000288CBE22520>)>, 'remove': <staticmethod(<function Cache.remove at 0x00000288CBE225C0>)>, '_purge_oldest': <staticmethod(<function Cache._purge_oldest at 0x00000288CBE22660>)>, '_purge_by_timeout': <staticmethod(<function Cache._purge_by_timeout at 0x00000288CBE22700>)>, 'print_usage': <staticmethod(<function Cache.print_usage at 0x00000288CBE227A0>)>, '__dict__': <attribute '__dict__' of 'Cache' objects>, '__weakref__': <attribute '__weakref__' of 'Cache' objects>})"


class Ellipse(Rectangle):
    """
    Ellipse(*args, **kwargs)
    A 2D ellipse.
    
        :Parameters:
            `segments`: int, the default value is calculated from the range between angle.
                Define how many segments are needed for drawing the ellipse.
                The ellipse drawing will be smoother if you have many segments,
                however you can also use this property to create polygons with 3 or more sides.
            `angle_start`: float, defaults to 0.0
                Specifies the starting angle, in degrees, of the disk portion.
            `angle_end`: float, defaults to 360.0
                Specifies the ending angle, in degrees, of the disk portion.
    
        .. versionchanged:: 1.0.7
            Added angle_start and angle_end.
        
        .. versionchanged:: 2.2.0
            The default number of segments is no longer 180, it is now calculated
            according to the angle range, as this is a more efficient approach.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Ellipse.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Ellipse.__setstate_cython__(self, __pyx_state) """
        pass

    angle_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """End angle of the ellipse in degrees, defaults to 360.
        """

    angle_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Start angle of the ellipse in degrees, defaults to 0.
        """

    segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the number of segments of the ellipse.
        The ellipse drawing will be smoother if you have many segments, however
        you can also use this property to create polygons with 3 or more sides.
        Values smaller than 3 will not be represented and the number of
        segments will be automatically calculated.
        
        .. versionchanged:: 2.2.0
            The minimum number of segments allowed is 3. Smaller values will be
            ignored and the number of segments will be automatically calculated.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDAC10>'


class GraphicException(Exception):
    """ Exception raised when a graphics error is fired. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Line(__kivy_graphics_instructions.VertexInstruction):
    """
    Line(**kwargs)
    A 2d line.
    
        Drawing a line can be done easily::
    
            with self.canvas:
                Line(points=[100, 100, 200, 100, 100, 200], width=10)
    
        The line has 3 internal drawing modes that you should be aware of
        for optimal results:
    
        #. If the :attr:`width` is 1.0, then the standard GL_LINE drawing from
           OpenGL will be used. :attr:`dash_length`, :attr:`dash_offset`, and :attr:`dashes` will
           work, while properties for cap and joint have no meaning here.
        #. If the :attr:`width` is greater than 1.0, then a custom drawing method,
           based on triangulation, will be used. :attr:`dash_length`,
           :attr:`dash_offset`, and :attr:`dashes` do not work in this mode.
           Additionally, if the current color has an alpha less than 1.0, a
           stencil will be used internally to draw the line.
    
        .. image:: images/line-instruction.png
            :align: center
    
        :Parameters:
            `points`: list
                List of points in the format (x1, y1, x2, y2...)
            `dash_length`: int
                Length of a segment (if dashed), defaults to 1.
            `dash_offset`: int
                Offset between the end of a segment and the beginning of the
                next one, defaults to 0. Changing this makes it dashed.
            `dashes`: list of ints
                List of [ON length, offset, ON length, offset, ...]. E.g. ``[2,4,1,6,8,2]``
                would create a line with the first dash length 2 then an offset of 4 then
                a dash length of 1 then an offset of 6 and so on. Defaults to ``[]``.
                Changing this makes it dashed and overrides `dash_length` and `dash_offset`.
            `width`: float
                Width of the line, defaults to 1.0.
            `cap`: str, defaults to 'round'
                See :attr:`cap` for more information.
            `joint`: str, defaults to 'round'
                See :attr:`joint` for more information.
            `cap_precision`: int, defaults to 10
                See :attr:`cap_precision` for more information
            `joint_precision`: int, defaults to 10
                See :attr:`joint_precision` for more information
                See :attr:`cap_precision` for more information.
            `joint_precision`: int, defaults to 10
                See :attr:`joint_precision` for more information.
            `close`: bool, defaults to False
                If True, the line will be closed.
            `circle`: list
                If set, the :attr:`points` will be set to build a circle. See
                :attr:`circle` for more information.
            `ellipse`: list
                If set, the :attr:`points` will be set to build an ellipse. See
                :attr:`ellipse` for more information.
            `rectangle`: list
                If set, the :attr:`points` will be set to build a rectangle. See
                :attr:`rectangle` for more information.
            `bezier`: list
                If set, the :attr:`points` will be set to build a bezier line. See
                :attr:`bezier` for more information.
            `bezier_precision`: int, defaults to 180
                Precision of the Bezier drawing.
    
        .. versionchanged:: 1.0.8
            `dash_offset` and `dash_length` have been added.
    
        .. versionchanged:: 1.4.1
            `width`, `cap`, `joint`, `cap_precision`, `joint_precision`, `close`,
            `ellipse`, `rectangle` have been added.
    
        .. versionchanged:: 1.4.1
            `bezier`, `bezier_precision` have been added.
    
        .. versionchanged:: 1.11.0
            `dashes` have been added
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Line.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Line.__setstate_cython__(self, __pyx_state) """
        pass

    bezier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use this property to build a bezier line, without calculating the
        :attr:`points`. You can only set this property, not get it.

        The argument must be a tuple of 2n elements, n being the number of points.

        Usage::

            Line(bezier=(x1, y1, x2, y2, x3, y3)

        .. versionadded:: 1.4.2

        .. note:: Bezier lines calculations are inexpensive for a low number of
            points, but complexity is quadratic, so lines with a lot of points
            can be very expensive to build, use with care!
        """

    bezier_precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of iteration for drawing the bezier between 2 segments,
        defaults to 180. The bezier_precision must be at least 1.

        .. versionadded:: 1.4.2
        """

    cap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine the cap of the line, defaults to 'round'. Can be one of
        'none', 'square' or 'round'

        .. versionadded:: 1.4.1
        """

    cap_precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of iteration for drawing the "round" cap, defaults to 10.
        The cap_precision must be at least 1.

        .. versionadded:: 1.4.1
        """

    circle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use this property to build a circle, without calculating the
        :attr:`points`.

        The argument must be a tuple of (center_x, center_y, radius, angle_start,
        angle_end, segments):

        * center_x and center_y represent the center of the circle
        * radius represent the radius of the circle
        * (optional) angle_start and angle_end are in degree. The default
          value is 0 and 360.
        * (optional) segments is the precision of the ellipse. The default
          value is calculated from the range between angle.

        Note that it's up to you to :attr:`close` the circle or not.

        For example, for building a simple ellipse, in python::

            # simple circle
            Line(circle=(150, 150, 50))

            # only from 90 to 180 degrees
            Line(circle=(150, 150, 50, 90, 180))

            # only from 90 to 180 degrees, with few segments
            Line(circle=(150, 150, 50, 90, 180, 20))

        .. versionadded:: 1.4.1

        .. versionchanged:: 2.2.0
            Now you can get the circle generated through the property.

        """

    close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If True, the line will be closed by joining the two ends, according to :attr:`close_mode`.

        .. versionadded:: 1.4.1
        """

    close_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines how the ends of the line will be connected.
        Defaults to ``"straight-line"``.

        .. note::
            Support for the different closing modes depends on drawing shapes.

        Available modes:

        - ``"straight-line"`` (all drawing shapes): the ends will be closed by a straight line.
        - ``"center-connected"`` (:attr:`ellipse` specific): the ends will be closed by a line passing through the center of the ellipse.

        .. versionadded:: 2.2.0
        """

    dashes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting ``dashes``.

        List of [ON length, offset, ON length, offset, ...]. E.g. ``[2,4,1,6,8,2]``
        would create a line with the first dash length 2 then an offset of 4 then
        a dash length of 1 then an offset of 6 and so on.

        .. versionadded:: 1.11.0
        """

    dash_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the length of the dashes in the curve

        .. versionadded:: 1.0.8
        """

    dash_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the offset between the dashes in the curve

        .. versionadded:: 1.0.8
        """

    ellipse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use this property to build an ellipse, without calculating the
        :attr:`points`.

        The argument must be a tuple of (x, y, width, height, angle_start,
        angle_end, segments):

        * x and y represent the bottom left of the ellipse
        * width and height represent the size of the ellipse
        * (optional) angle_start and angle_end are in degree. The default
          value is 0 and 360.
        * (optional) segments is the precision of the ellipse. The default
          value is calculated from the range between angle. You can use this
          property to create polygons with 3 or more sides. Values smaller than
          3 will not be represented and the number of segments will be
          automatically calculated.

        Note that it's up to you to :attr:`close` or not.
        If you choose to close, use :attr:`close_mode` to define how the figure
        will be closed. Whether it will be by closed by a ``"straight-line"``
        or by ``"center-connected"``.

        For example, for building a simple ellipse, in python::

            # simple ellipse
            Line(ellipse=(0, 0, 150, 150))

            # only from 90 to 180 degrees
            Line(ellipse=(0, 0, 150, 150, 90, 180))

            # only from 90 to 180 degrees, with few segments
            Line(ellipse=(0, 0, 150, 150, 90, 180, 20))

        .. versionadded:: 1.4.1

        .. versionchanged:: 2.2.0
            Now you can get the ellipse generated through the property.

            The minimum number of segments allowed is 3. Smaller values will be
            ignored and the number of segments will be automatically calculated.
        """

    joint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine the join of the line, defaults to 'round'. Can be one of
        'none', 'round', 'bevel', 'miter'.

        .. versionadded:: 1.4.1
        """

    joint_precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of iteration for drawing the "round" joint, defaults to 10.
        The joint_precision must be at least 1.

        .. versionadded:: 1.4.1
        """

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/settings points of the line

        .. warning::

            This will always reconstruct the whole graphics from the new points
            list. It can be very CPU expensive.
        """

    rectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use this property to build a rectangle, without calculating the
        :attr:`points`.

        The argument must be a tuple of (x, y, width, height):

        * x and y represent the bottom-left position of the rectangle
        * width and height represent the size

        The line is automatically closed.

        Usage::

            Line(rectangle=(0, 0, 200, 200))

        .. versionadded:: 1.4.1

        .. versionchanged:: 2.2.0
            Now you can get the rectangle generated through the property.

        """

    rounded_rectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use this property to build a rectangle, without calculating the
        :attr:`points`.

        The argument must be a tuple of one of the following forms:

        * (x, y, width, height, corner_radius)
        * (x, y, width, height, corner_radius, resolution)
        * (x, y, width, height, corner_radius1, corner_radius2, corner_radius3, corner_radius4)
        * (x, y, width, height, corner_radius1, corner_radius2, corner_radius3, corner_radius4, resolution)

        * `x` and `y` represent the bottom-left position of the rectangle.
        * `width` and `height` represent the size.
        * `corner_radius` specifies the radius used for the rounded corners clockwise: top-left, top-right, bottom-right, bottom-left.
        * `resolution` is the number of line segment that will be used to draw the circle arc at each corner (defaults to 45).

        The line is automatically closed.

        Usage::

            Line(rounded_rectangle=(0, 0, 200, 200, 10, 20, 30, 40, 100))

        .. versionadded:: 1.9.0

        .. versionchanged:: 2.2.0
            Default value of `resolution` changed from 30 to 45.

            Now you can get the rounded rectangle generated through the property.

            The order of `corner_radius` has been changed to match the RoundedRectangle radius property (clockwise).
            It was bottom-left, bottom-right, top-right, top-left in previous versions.
            Now both are clockwise: top-left, top-right, bottom-right, bottom-left.
            To keep the corner radius order without changing the order manually, you can use python's built-in method `reversed` or `[::-1]`,
            to reverse the order of the corner radius.

        """

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine the width of the line, defaults to 1.0.

        .. versionadded:: 1.4.1
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDA970>'


class Mesh(__kivy_graphics_instructions.VertexInstruction):
    """
    Mesh(**kwargs)
    A 2d mesh.
    
        In OpenGL ES 2.0 and in our graphics implementation, you cannot have more
        than 65535 indices.
    
        A list of vertices is described as::
    
            vertices = [x1, y1, u1, v1, x2, y2, u2, v2, ...]
                        |            |  |            |
                        +---- i1 ----+  +---- i2 ----+
    
        If you want to draw a triangle, add 3 vertices. You can then make an
        indices list as follows:
    
            indices = [0, 1, 2]
    
        .. versionadded:: 1.1.0
    
        :Parameters:
            `vertices`: iterable
                List of vertices in the format (x1, y1, u1, v1, x2, y2, u2, v2...).
            `indices`: iterable
                List of indices in the format (i1, i2, i3...).
            `mode`: str
                Mode of the vbo. Check :attr:`mode` for more information. Defaults to
                'points'.
            `fmt`: list
                The format for vertices, by default, each vertex is described by 2D
                coordinates (x, y) and 2D texture coordinate (u, v).
                Each element of the list should be a tuple or list, of the form
    
                    (variable_name, size, type)
    
                which will allow mapping vertex data to the glsl instructions.
    
                    [(b'v_pos', 2, 'float'), (b'v_tc', 2, 'float'),]
    
                will allow using
    
                    attribute vec2 v_pos;
                    attribute vec2 v_tc;
    
                in glsl's vertex shader.
    
        .. versionchanged:: 1.8.1
            Before, `vertices` and `indices` would always be converted to a list,
            now, they are only converted to a list if they do not implement the
            buffer interface. So e.g. numpy arrays, python arrays etc. are used
            in place, without creating any additional copies. However, the
            buffers cannot be readonly (even though they are not changed, due to
            a cython limitation) and must be contiguous in memory.
    
        .. note::
            When passing a memoryview or a instance that implements the buffer
            interface, `vertices` should be a buffer of floats (`'f'` code in
            python array) and `indices` should be a buffer of unsigned short (`'H'`
            code in python array). Arrays in other formats will still have to be
            converted internally, negating any potential gain.
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Mesh.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Mesh.__setstate_cython__(self, __pyx_state) """
        pass

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vertex indices used to specify the order when drawing the
        mesh.
        """

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """VBO Mode used for drawing vertices/indices. Can be one of 'points',
        'line_strip', 'line_loop', 'lines', 'triangles', 'triangle_strip' or
        'triangle_fan'.
        """

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of x, y, u, v coordinates used to construct the Mesh. Right now,
        the Mesh instruction doesn't allow you to change the format of the
        vertices, which means it's only x, y + one texture coordinate.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDA910>'


class Point(__kivy_graphics_instructions.VertexInstruction):
    """
    Point(**kwargs)
    A list of 2d points. Each point is represented as a square with a
        width/height of 2 times the :attr:`pointsize`.
    
        :Parameters:
            `points`: list
                List of points in the format (x1, y1, x2, y2...), where each pair
                of coordinates specifies the center of a new point.
            `pointsize`: float, defaults to 1.
                The size of the point, measured from the center to the edge. A
                value of 1.0 therefore means the real size will be 2.0 x 2.0.
    
        .. warning::
    
            Starting from version 1.0.7, vertex instruction have a limit of 65535
            vertices (indices of vertex to be accurate).
            2 entries in the list (x, y) will be converted to 4 vertices. So the
            limit inside Point() class is 2^15-2.
    """
    def add_point(self, float_x, float_y): # real signature unknown; restored from __doc__
        """
        Point.add_point(self, float x, float y)
        Add a point to the current :attr:`points` list.
        
                If you intend to add multiple points, prefer to use this method instead
                of reassigning a new :attr:`points` list. Assigning a new :attr:`points`
                list will recalculate and reupload the whole buffer into the GPU.
                If you use add_point, it will only upload the changes.
        """
        pass

    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Point.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Point.__setstate_cython__(self, __pyx_state) """
        pass

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/settings the center points in the points list.
        Each pair of coordinates specifies the center of a new point.
        """

    pointsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting point size.
        The size is measured from the center to the edge, so a value of 1.0
        means the real size will be 2.0 x 2.0.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDAA30>'


class Quad(__kivy_graphics_instructions.VertexInstruction):
    """
    Quad(**kwargs)
    A 2d quad.
    
        :Parameters:
            `points`: list
                List of point in the format (x1, y1, x2, y2, x3, y3, x4, y4).
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Quad.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Quad.__setstate_cython__(self, __pyx_state) """
        pass

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/settings points of the quad.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDAAF0>'


class RoundedRectangle(Rectangle):
    """
    RoundedRectangle(**kwargs)
    A 2D rounded rectangle.
    
        .. versionadded:: 1.9.1
    
        :Parameters:
            `segments`: int, defaults to 10
                Define how many segments are needed for drawing the rounded corner.
                The drawing will be smoother if you have many segments.
            `radius`: list, defaults to [(10.0, 10.0), (10.0, 10.0), (10.0, 10.0), (10.0, 10.0)]
                Specifies the radii used for the rounded corners clockwise:
                top-left, top-right, bottom-right, bottom-left.
                Elements of the list can be numbers or tuples of two numbers to specify different x,y dimensions.
                One value will define all corner radii to be of this value.
                Four values will define each corner radius separately.
                Higher numbers of values will be truncated to four.
                The first value will be used for all corners if there are fewer than four values.
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ RoundedRectangle.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ RoundedRectangle.__setstate_cython__(self, __pyx_state) """
        pass

    radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Corner radii of the rounded rectangle, defaults to [10,].
        """

    segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the number of segments for each corner.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDAC70>'


class SmoothLine(Line):
    """
    SmoothLine(**kwargs)
    Experimental line using over-draw methods to get better anti-aliasing
        results. It has few drawbacks:
    
        - drawing a line with alpha will probably not have the intended result if
          the line crosses itself.
        - :attr:`~Line.cap`, :attr:`~Line.joint` and :attr:`~Line.dash` properties
          are not supported.
        - it uses a custom texture with a premultiplied alpha.
        - lines under 1px in width are not supported: they will look the same.
    
        .. warning::
    
            This is an unfinished work, experimental, and subject to crashes.
    
        .. versionadded:: 1.9.0
    """
    def premultiplied_texture(self): # real signature unknown; restored from __doc__
        """ SmoothLine.premultiplied_texture(self) """
        pass

    def _smooth_reload_observer(self, texture): # real signature unknown; restored from __doc__
        """ SmoothLine._smooth_reload_observer(self, texture) """
        pass

    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ SmoothLine.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ SmoothLine.__setstate_cython__(self, __pyx_state) """
        pass

    overdraw_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine the overdraw width of the line, defaults to 1.2.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDA9D0>'


class StripMesh(__kivy_graphics_instructions.VertexInstruction):
    """
    StripMesh(VertexFormat fmt)
    A specialized 2d mesh.
    
        (internal) Used for SVG, will be available with doc later.
    """
    def __init__(self, VertexFormat_fmt): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ StripMesh.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ StripMesh.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDA8B0>'


class Triangle(__kivy_graphics_instructions.VertexInstruction):
    """
    Triangle(**kwargs)
    A 2d triangle.
    
        :Parameters:
            `points`: list
                List of points in the format (x1, y1, x2, y2, x3, y3).
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Triangle.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Triangle.__setstate_cython__(self, __pyx_state) """
        pass

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/settings points of the triangle.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000288CBFDAA90>'


# variables with complex values

environ = None # (!) real value is "environ({'ALLUSERSPROFILE': 'C:\\\\ProgramData', 'APPDATA': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Roaming', 'COMMONPROGRAMFILES': 'C:\\\\Program Files\\\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\\\Program Files (x86)\\\\Common Files', 'COMMONPROGRAMW6432': 'C:\\\\Program Files\\\\Common Files', 'COMPUTERNAME': 'CG-WA-WS063', 'COMSPEC': 'C:\\\\Windows\\\\system32\\\\cmd.exe', 'DRIVERDATA': 'C:\\\\Windows\\\\System32\\\\Drivers\\\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\\\Users\\\\matthew.muller', 'IDEA_INITIAL_DIRECTORY': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cadds-visual-tyre-handler\\\\source', 'INCLUDE': '%MSVC_ROOT%\\\\include;%SDK_INCLUDE%\\\\ucrt;%SDK_INCLUDE%\\\\shared;%SDK_INCLUDE%\\\\um;%SDK_INCLUDE%\\\\winrt;%SDK_INCLUDE%\\\\cppwinrt', 'LIB': '%MSVC_ROOT%\\\\lib\\\\x64;%SDK_LIBS%\\\\ucrt\\\\x64;%SDK_LIBS%\\\\um\\\\x64', 'LOCALAPPDATA': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local', 'LOGONSERVER': '\\\\\\\\CG-SUS-DC1', 'MSVC_ARCH': 'x64', 'MSVC_HOST': 'Hostx64', 'MSVC_ROOT': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822', 'MSVC_VERSION': '14.37.32822', 'NINJARMMCLI': 'C:\\\\ProgramData\\\\NinjaRMMAgent\\\\ninjarmm-cli.exe', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\\\Users\\\\matthew.muller\\\\OneDrive - Cadds', 'ONEDRIVECOMMERCIAL': 'C:\\\\Users\\\\matthew.muller\\\\OneDrive - Cadds', 'OS': 'Windows_NT', 'PATH': 'C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\sdl2\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\glew\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\angle\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\sdl2\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\glew\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\angle\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Scripts;C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Windows\\\\System32\\\\OpenSSH\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Scripts\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Launcher\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Microsoft\\\\WindowsApps;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\bin;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Git\\\\cmd;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\GitHubDesktop\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cmake-3.28.0-rc3\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\go\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64\\\\ucrt;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0a', 'PROGRAMDATA': 'C:\\\\ProgramData', 'PROGRAMFILES': 'C:\\\\Program Files', 'PROGRAMFILES(X86)': 'C:\\\\Program Files (x86)', 'PROGRAMW6432': 'C:\\\\Program Files', 'PROMPT': '(app) $P$G', 'PSMODULEPATH': 'C:\\\\Program Files\\\\WindowsPowerShell\\\\Modules;C:\\\\Windows\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\Modules', 'PUBLIC': 'C:\\\\Users\\\\Public', 'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONPATH': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\JetBrains\\\\PyCharm 2023.2.4\\\\plugins\\\\python\\\\helpers', 'ROOT': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\', 'SDK_ARCH': 'x64', 'SDK_INCLUDE': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\Include\\\\10.0.22621.0', 'SDK_LIBS': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\Lib\\\\10.0.22621.0', 'SDK_VERSION': '10.0.22621.0', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\\\Windows', 'TEMP': 'C:\\\\Users\\\\MATTHE~1.MUL\\\\AppData\\\\Local\\\\Temp', 'TMP': 'C:\\\\Users\\\\MATTHE~1.MUL\\\\AppData\\\\Local\\\\Temp', 'USERDNSDOMAIN': 'CADDS.LOCAL', 'USERDOMAIN': 'CADDS', 'USERDOMAIN_ROAMINGPROFILE': 'CADDS', 'USERNAME': 'Matthew.Muller', 'USERPROFILE': 'C:\\\\Users\\\\matthew.muller', 'VCTOOLSINSTALLDIR': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\', 'VIRTUAL_ENV': 'C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6', 'WINDIR': 'C:\\\\Windows', 'ZES_ENABLE_SYSMAN': '1', '_OLD_VIRTUAL_PATH': 'C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Windows\\\\System32\\\\OpenSSH\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Scripts\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Launcher\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Microsoft\\\\WindowsApps;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\bin;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Git\\\\cmd;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\GitHubDesktop\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cmake-3.28.0-rc3\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\go\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64\\\\ucrt;', '_OLD_VIRTUAL_PROMPT': '$P$G'})"

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'Triangle',
    'Quad',
    'Rectangle',
    'RoundedRectangle',
    'BorderImage',
    'Ellipse',
    'Line',
    'Point',
    'Mesh',
    'GraphicException',
    'Bezier',
    'SmoothLine',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000288CBAB4810>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.vertex_instructions', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000288CBAB4810>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\vertex_instructions.cp311-win_amd64.pyd')"

__test__ = {}

