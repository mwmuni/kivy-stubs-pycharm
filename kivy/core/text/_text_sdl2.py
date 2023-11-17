# encoding: utf-8
# module kivy.core.text._text_sdl2
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\core\text\_text_sdl2.cp311-win_amd64.pyd
# by generator 1.147
"""
TODO:
    - ensure that we correctly check allocation
    - remove compat sdl usage (like SDL_SetAlpha must be replaced with sdl 1.3
      call, not 1.2)
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# Variables with simple values

PY2 = False

# functions

def _get_extents(container, text): # real signature unknown; restored from __doc__
    """ _get_extents(container, text) """
    pass

def _get_fontascent(container): # real signature unknown; restored from __doc__
    """ _get_fontascent(container) """
    pass

def _get_fontdescent(container): # real signature unknown; restored from __doc__
    """ _get_fontdescent(container) """
    pass

# classes

class ImageData(object):
    """
    Container for images and mipmap images.
        The container will always have at least the mipmap level 0.
    """
    def add_mipmap(self, level, width, height, data, rowlength): # reliably restored by inspect
        """
        Add a image for a specific mipmap level.
        
                .. versionadded:: 1.0.7
        """
        pass

    def get_mipmap(self, level): # reliably restored by inspect
        """
        Get the mipmap image at a specific level if it exists
        
                .. versionadded:: 1.0.7
        """
        pass

    def iterate_mipmaps(self): # reliably restored by inspect
        """
        Iterate over all mipmap images available.
        
                .. versionadded:: 1.0.7
        """
        pass

    def release_data(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, width, height, fmt, data, source=None, flip_vertical=True, source_image=None, rowlength=0): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Image data.
        (If the image is mipmapped, it will use the level 0)
        """

    flip_vertical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fmt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    have_mipmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Image height in pixels.
        (If the image is mipmapped, it will use the level 0)
        """

    mipmaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rowlength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Image rowlength.
        (If the image is mipmapped, it will use the level 0)

        .. versionadded:: 1.9.0
        """

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Image (width, height) in pixels.
        (If the image is mipmapped, it will use the level 0)
        """

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Image width in pixels.
        (If the image is mipmapped, it will use the level 0)
        """


    _supported_fmts = (
        'rgb',
        'bgr',
        'rgba',
        'bgra',
        'argb',
        'abgr',
        's3tc_dxt1',
        's3tc_dxt3',
        's3tc_dxt5',
        'pvrtc_rgb2',
        'pvrtc_rgb4',
        'pvrtc_rgba2',
        'pvrtc_rgba4',
        'etc1_rgb8',
    )
    __slots__ = (
        'fmt',
        'mipmaps',
        'source',
        'flip_vertical',
        'source_image',
    )


class _SurfaceContainer(object):
    """ _SurfaceContainer(w, h) """
    def get_data(self): # real signature unknown; restored from __doc__
        """ _SurfaceContainer.get_data(self) """
        pass

    def render(self, container, text, x, y): # real signature unknown; restored from __doc__
        """ _SurfaceContainer.render(self, container, text, x, y) """
        pass

    def __init__(self, w, h): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _SurfaceContainer.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _SurfaceContainer.__setstate_cython__(self, __pyx_state) """
        pass


class _TTFContainer(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ _TTFContainer.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ _TTFContainer.__setstate_cython__(self, __pyx_state) """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000011433856C10>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.core.text._text_sdl2', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000011433856C10>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\core\\\\text\\\\_text_sdl2.cp311-win_amd64.pyd')"

__test__ = {}

