# encoding: utf-8
# module kivy.graphics.vbo
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\vbo.cp311-win_amd64.pyd
# by generator 1.147
"""
Vertex Buffer
=============

The :class:`VBO` class handles the creation and updating of Vertex Buffer
Objects in OpenGL.

.. versionadded:: 1.6.0
    VertexFormat class added. VertexFormat is used to describe the layout
    of the vertex data stored in vertex arrays/vbo's. The default vertex format
    is:
        VertexFormat(('vPosition', 2, 'float'), ('vTexCoords0', 2, 'float'))

.. versionchanged:: 1.6.0
    VBO now no longer has a fixed vertex format. If no VertexFormat is given
    at initialization, the default vertex format is used.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\matthew.muller\AppData\Local\Programs\Python\Python311\Lib\os.py

# functions

def __pyx_unpickle_VertexBatch(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_VertexBatch(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class VBO(object):
    """
    VBO(VertexFormat vertex_format=None)
    
        .. versionchanged:: 1.6.0
            VBO now no longer has a fixed vertex format. If no VertexFormat is given
            at initialization, the default vertex format is used.
    """
    def __init__(self, VertexFormat_vertex_format=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ VBO.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ VBO.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002480277BB40>'


class VertexBatch(object):
    """ VertexBatch(**kwargs) """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ VertexBatch.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ VertexBatch.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002480277BB70>'


# variables with complex values

environ = os.environ

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'VBO',
    'VertexBatch',
    'VertexFormat',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000248027B8910>'

__pyx_capi__ = {
    'default_vertex': None, # (!) real value is '<capsule object "struct __pyx_obj_4kivy_8graphics_6vertex_VertexFormat *" at 0x000002480277BAE0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.vbo', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000248027B8910>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\vbo.cp311-win_amd64.pyd')"

__test__ = {}

