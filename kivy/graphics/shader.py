# encoding: utf-8
# module kivy.graphics.shader
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\shader.cp311-win_amd64.pyd
# by generator 1.147
"""
Shader
======

The :class:`Shader` class handles the compilation of the vertex and fragment
shader as well as the creation of the program in OpenGL.

.. todo::

    Include more complete documentation about the shader.

Header inclusion
----------------

.. versionadded:: 1.0.7

When you are creating a Shader, Kivy will always include default parameters. If
you don't want to rewrite this each time you want to customize / write a new
shader, you can add the "$HEADER$" token and it will be replaced by the
corresponding shader header.

Here is the header for the fragment Shader:

.. include:: ../../kivy/data/glsl/header.fs
    :literal:

And the header for vertex Shader:

.. include:: ../../kivy/data/glsl/header.vs
    :literal:


Single file glsl shader programs
--------------------------------

.. versionadded:: 1.6.0

To simplify shader management, the vertex and fragment shaders can be loaded
automatically from a single glsl source file (plain text). The file should
contain sections identified by a line starting with '---vertex' and
'---fragment' respectively (case insensitive), e.g. ::

    // anything before a meaningful section such as this comment are ignored

    ---VERTEX SHADER--- // vertex shader starts here
    void main(){
        ...
    }

    ---FRAGMENT SHADER--- // fragment shader starts here
    void main(){
        ...
    }

The source property of the Shader should be set to the filename of a glsl
shader file (of the above format), e.g. `phong.glsl`
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\matthew.muller\AppData\Local\Programs\Python\Python311\Lib\os.py

# Variables with simple values

kivy_shader_dir = 'C:\\Users\\matthew.muller\\.virtualenvs\\app-gFbndeE6\\Lib\\site-packages\\kivy\\data\\glsl'

# functions

def join(path, *paths): # reliably restored by inspect
    # no doc
    pass

# classes

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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.cache', '__doc__': 'See module documentation for more information.\\n    ', '_categories': {'kv.resourcefind': {'limit': None, 'timeout': 60}, 'kv.image': {'limit': None, 'timeout': 60}, 'kv.atlas': {'limit': None, 'timeout': None}, 'kv.texture': {'limit': 1000, 'timeout': 60}, 'kv.shader': {'limit': 1000, 'timeout': 3600}, 'kv.graphics.texture': {'limit': None, 'timeout': None}}, '_objects': {'kv.resourcefind': {}, 'kv.image': {}, 'kv.atlas': {}, 'kv.texture': {}, 'kv.shader': {}, 'kv.graphics.texture': {}}, 'register': <staticmethod(<function Cache.register at 0x0000022BB76120C0>)>, 'append': <staticmethod(<function Cache.append at 0x0000022BB7612340>)>, 'get': <staticmethod(<function Cache.get at 0x0000022BB76123E0>)>, 'get_timestamp': <staticmethod(<function Cache.get_timestamp at 0x0000022BB7612480>)>, 'get_lastaccess': <staticmethod(<function Cache.get_lastaccess at 0x0000022BB7612520>)>, 'remove': <staticmethod(<function Cache.remove at 0x0000022BB76125C0>)>, '_purge_oldest': <staticmethod(<function Cache._purge_oldest at 0x0000022BB7612660>)>, '_purge_by_timeout': <staticmethod(<function Cache._purge_by_timeout at 0x0000022BB7612700>)>, 'print_usage': <staticmethod(<function Cache.print_usage at 0x0000022BB76127A0>)>, '__dict__': <attribute '__dict__' of 'Cache' objects>, '__weakref__': <attribute '__weakref__' of 'Cache' objects>})"


class Shader(object):
    """
    Shader(unicode vs=None, unicode fs=None, unicode source=None)
    Create a vertex or fragment shader.
    
        :Parameters:
            `vs`: string, defaults to None
                Source code for vertex shader
            `fs`: string, defaults to None
                Source code for fragment shader
    """
    def __init__(self, unicode_vs=None, unicode_fs=None, unicode_source=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Shader.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Shader.__setstate_cython__(self, __pyx_state) """
        pass

    fs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fragment shader source code.

        If you set a new fragment shader code source, it will be automatically
        compiled and will replace the current fragment shader.
        """

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """glsl  source code.

        source should be the filename of a glsl shader that contains both the
        vertex and fragment shader sourcecode, each designated by a section
        header consisting of one line starting with either "--VERTEX" or
        "--FRAGMENT" (case insensitive).

        .. versionadded:: 1.6.0
        """

    success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicate whether the shader loaded successfully and is ready for
        usage or not.
        """

    vs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vertex shader source code.

        If you set a new vertex shader code source, it will be automatically
        compiled and will replace the current vertex shader.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000022BB7599EF0>'


class ShaderSource(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ShaderSource.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ShaderSource.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000022BB759A670>'


# variables with complex values

fin = None # (!) real value is "<_io.TextIOWrapper name='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\data\\\\glsl\\\\default.fs' mode='r' encoding='cp1252'>"

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'Shader',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022BB762ABD0>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.shader', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022BB762ABD0>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\shader.cp311-win_amd64.pyd')"

__test__ = {}

