# encoding: utf-8
# module kivy.graphics.texture
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\texture.cp311-win_amd64.pyd
# by generator 1.147
"""
Texture
=======

.. versionchanged:: 1.6.0
    Added support for paletted texture on OES: 'palette4_rgb8',
    'palette4_rgba8', 'palette4_r5_g6_b5', 'palette4_rgba4', 'palette4_rgb5_a1',
    'palette8_rgb8', 'palette8_rgba8', 'palette8_r5_g6_b5', 'palette8_rgba4'
    and 'palette8_rgb5_a1'.

:class:`Texture` is a class that handles OpenGL textures. Depending on the
hardware,
some OpenGL capabilities might not be available (BGRA support, NPOT support,
etc.)

You cannot instantiate this class yourself. You must use the function
:meth:`Texture.create` to create a new texture::

    texture = Texture.create(size=(640, 480))

When you create a texture, you should be aware of the default color
and buffer format:

    - the color/pixel format (:attr:`Texture.colorfmt`) that can be one of
      'rgb', 'rgba', 'luminance', 'luminance_alpha', 'bgr' or 'bgra'.
      The default value is 'rgb'
    - the buffer format determines how a color component is stored into memory.
      This can be one of 'ubyte', 'ushort', 'uint', 'byte', 'short', 'int' or
      'float'. The default value and the most commonly used is 'ubyte'.

So, if you want to create an RGBA texture::

    texture = Texture.create(size=(640, 480), colorfmt='rgba')

You can use your texture in almost all vertex instructions with the
:attr:`kivy.graphics.VertexIntruction.texture` parameter. If you want to use
your texture in kv lang, you can save it in an
:class:`~kivy.properties.ObjectProperty` inside your widget.

.. warning::
    Using Texture before OpenGL has been initialized will lead to a crash. If
    you need to create textures before the application has started, import
    Window first: `from kivy.core.window import Window`

Blitting custom data
--------------------

You can create your own data and blit it to the texture using
:meth:`Texture.blit_buffer`.

For example, to blit immutable bytes data::

    # create a 64x64 texture, defaults to rgba / ubyte
    texture = Texture.create(size=(64, 64))

    # create 64x64 rgb tab, and fill with values from 0 to 255
    # we'll have a gradient from black to white
    size = 64 * 64 * 3
    buf = [int(x * 255 / size) for x in range(size)]

    # then, convert the array to a ubyte string
    buf = bytes(buf)

    # then blit the buffer
    texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

    # that's all ! you can use it in your graphics now :)
    # if self is a widget, you can do this
    with self.canvas:
        Rectangle(texture=texture, pos=self.pos, size=(64, 64))

Since 1.9.0, you can blit data stored in a instance that implements the python
buffer interface, or a memoryview thereof, such as numpy arrays, python
`array.array`, a `bytearray`, or a cython array. This is beneficial if you
expect to blit similar data, with perhaps a few changes in the data.

When using a bytes representation of the data, for every change you have to
regenerate the bytes instance, from perhaps a list, which is very inefficient.
When using a buffer object, you can simply edit parts of the original data.
Similarly, unless starting with a bytes object, converting to bytes requires a
full copy, however, when using a buffer instance, no memory is copied, except
to upload it to the GPU.

Continuing with the example above::

    from array import array

    size = 64 * 64 * 3
    buf = [int(x * 255 / size) for x in range(size)]
    # initialize the array with the buffer values
    arr = array('B', buf)
    # now blit the array
    texture.blit_buffer(arr, colorfmt='rgb', bufferfmt='ubyte')

    # now change some elements in the original array
    arr[24] = arr[50] = 99
    # blit again the buffer
    texture.blit_buffer(arr, colorfmt='rgb', bufferfmt='ubyte')


BGR/BGRA support
----------------

The first time you try to create a BGR or BGRA texture, we check whether
your hardware supports BGR / BGRA textures by checking the extension
'GL_EXT_bgra'.

If the extension is not found, the conversion to RGB / RGBA will be done in
software.


NPOT texture
------------

.. versionchanged:: 1.0.7

    If your hardware supports NPOT, no POT is created.

As the OpenGL documentation says, a texture must be power-of-two sized. That
means
your width and height can be one of 64, 32, 256... but not 3, 68, 42. NPOT means
non-power-of-two. OpenGL ES 2 supports NPOT textures natively but with some
drawbacks. Another type of NPOT texture is called a rectangle texture.
POT, NPOT and textures all have their own pro/cons.

================= ============= ============= =================================
    Features           POT           NPOT                Rectangle
----------------- ------------- ------------- ---------------------------------
OpenGL Target     GL_TEXTURE_2D GL_TEXTURE_2D GL_TEXTURE_RECTANGLE_(NV|ARB|EXT)
Texture coords    0-1 range     0-1 range     width-height range
Mipmapping        Supported     Partially     No
Wrap mode         Supported     Supported     No
================= ============= ============= =================================

If you create a NPOT texture, we first check whether your hardware
supports it by checking the extensions GL_ARB_texture_non_power_of_two or
OES_texture_npot. If none of these are available, we create the nearest
POT texture that can contain your NPOT texture. The :meth:`Texture.create` will
return a :class:`TextureRegion` instead.


Texture atlas
-------------

A texture atlas is a single texture that contains many images.
If you want to separate the original texture into many single ones, you don't
need to. You can get a region of the original texture. That will return the
original texture with custom texture coordinates::

    # for example, load a 128x128 image that contain 4 64x64 images
    from kivy.core.image import Image
    texture = Image('mycombinedimage.png').texture

    bottomleft = texture.get_region(0, 0, 64, 64)
    bottomright = texture.get_region(0, 64, 64, 64)
    topleft = texture.get_region(0, 64, 64, 64)
    topright = texture.get_region(64, 64, 64, 64)


.. _mipmap:

Mipmapping
----------

.. versionadded:: 1.0.7

Mipmapping is an OpenGL technique for enhancing the rendering of large textures
to small surfaces. Without mipmapping, you might see pixelation when you
render to small surfaces.
The idea is to precalculate the subtexture and apply some image filter as a
linear filter. Then, when you render a small surface, instead of using the
biggest texture, it will use a lower filtered texture. The result can look
better this way.

To make that happen, you need to specify mipmap=True when you create a
texture. Some widgets already give you the ability to create mipmapped
textures, such as the :class:`~kivy.uix.label.Label` and
:class:`~kivy.uix.image.Image`.

From the OpenGL Wiki : "So a 64x16 2D texture can have 5 mip-maps: 32x8, 16x4,
8x2, 4x1, 2x1, and 1x1". Check http://www.opengl.org/wiki/Texture for more
information.

.. note::

    As the table in previous section said, if your texture is NPOT, we
    create the nearest POT texture and generate a mipmap from it. This
    might change in the future.

Reloading the Texture
---------------------

.. versionadded:: 1.2.0

If the OpenGL context is lost, the Texture must be reloaded. Textures that have
a source are automatically reloaded but generated textures must
be reloaded by the user.

Use the :meth:`Texture.add_reload_observer` to add a reloading function that
will be automatically called when needed::

    def __init__(self, **kwargs):
        super(...).__init__(**kwargs)
        self.texture = Texture.create(size=(512, 512), colorfmt='RGB',
            bufferfmt='ubyte')
        self.texture.add_reload_observer(self.populate_texture)

        # and load the data now.
        self.cbuffer = '\x00\xf0\xff' * 512 * 512
        self.populate_texture(self.texture)

    def populate_texture(self, texture):
        texture.blit_buffer(self.cbuffer)

This way, you can use the same method for initialization and reloading.

.. note::

    For all text rendering with our core text renderer, the texture is generated
    but we already bind a method to redo the text rendering and reupload
    the text to the texture. You don't have to do anything.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\matthew.muller\AppData\Local\Programs\Python\Python311\Lib\os.py

# Variables with simple values

GLCAP_BGRA = 2
GLCAP_DXT1 = 4
GLCAP_ETC1 = 6
GLCAP_NPOT = 2
GLCAP_PVRTC = 5
GLCAP_S3TC = 3

GLCAP_UNPACK_SUBIMAGE = 7

platform = 'win'

# functions

def texture_create(size=None, colorfmt=None, bufferfmt=None, mipmap=False, callback=None, icolorfmt=None): # real signature unknown; restored from __doc__
    """
    texture_create(size=None, colorfmt=None, bufferfmt=None, mipmap=False, callback=None, icolorfmt=None)
    Create a texture based on size.
    
        :Parameters:
            `size`: tuple, defaults to (128, 128)
                Size of the texture.
            `colorfmt`: str, defaults to 'rgba'
                Color format of the texture. Can be 'rgba' or 'rgb',
                'luminance' or 'luminance_alpha'. On desktop, additional values are
                available: 'red', 'rg'.
            `icolorfmt`: str, defaults to the value of `colorfmt`
                Internal format storage of the texture. Can be 'rgba' or 'rgb',
                'luminance' or 'luminance_alpha'. On desktop, additional values are
                available: 'r8', 'rg8', 'rgba8'.
            `bufferfmt`: str, defaults to 'ubyte'
                Internal buffer format of the texture. Can be 'ubyte', 'ushort',
                'uint', 'bute', 'short', 'int' or 'float'.
            `mipmap`: bool, defaults to False
                If True, it will automatically generate the mipmap texture.
            `callback`: callable(), defaults to False
                If a function is provided, it will be called when data is
                needed in the texture.
    
        .. versionchanged:: 1.7.0
            :attr:`callback` has been added
    """
    pass

def texture_create_from_data(im, mipmap=False): # real signature unknown; restored from __doc__
    """
    texture_create_from_data(im, mipmap=False)
    Create a texture from an ImageData class.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Texture(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Texture(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_TextureRegion(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_TextureRegion(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class Texture(object):
    """
    Texture(width, height, target, texid=0, colorfmt=u'rgb', bufferfmt=u'ubyte', mipmap=False, source=None, callback=None, icolorfmt=u'rgb')
    Handle an OpenGL texture. This class can be used to create simple
        textures or complex textures based on ImageData.
    """
    def add_reload_observer(self, callback): # real signature unknown; restored from __doc__
        """
        Texture.add_reload_observer(self, callback)
        Add a callback to be called after the whole graphics context has
                been reloaded. This is where you can reupload your custom data into
                the GPU.
        
                .. versionadded:: 1.2.0
        
                :Parameters:
                    `callback`: func(context) -> return None
                        The first parameter will be the context itself.
        """
        pass

    def ask_update(self, callback): # real signature unknown; restored from __doc__
        """
        Texture.ask_update(self, callback)
        Indicate that the content of the texture should be updated and the
                callback function needs to be called when the texture will be
                used.
        """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """
        Texture.bind(self)
        Bind the texture to the current opengl state.
        """
        pass

    def blit_buffer(self, pbuffer, size=None, colorfmt=None, pos=None, bufferfmt=None, mipmap_level=0, mipmap_generation=True, int_rowlength=0): # real signature unknown; restored from __doc__
        """
        Texture.blit_buffer(self, pbuffer, size=None, colorfmt=None, pos=None, bufferfmt=None, mipmap_level=0, mipmap_generation=True, int rowlength=0)
        Blit a buffer into the texture.
        
                .. note::
        
                    Unless the canvas will be updated due to other changes,
                    :meth:`~kivy.graphics.instructions.Canvas.ask_update` should be
                    called in order to update the texture.
        
                :Parameters:
                    `pbuffer`: bytes, or a class that implements the buffer interface (including memoryview).
                        A buffer containing the image data. It can be either a bytes
                        object or a instance of a class that implements the python
                        buffer interface, e.g. `array.array`, `bytearray`, numpy arrays
                        etc. If it's not a bytes object, the underlying buffer must
                        be contiguous, have only one dimension and must not be
                        readonly, even though the data is not modified, due to a cython
                        limitation. See module description for usage details.
                    `size`: tuple, defaults to texture size
                        Size of the image (width, height)
                    `colorfmt`: str, defaults to 'rgb'
                        Image format, can be one of 'rgb', 'rgba', 'bgr', 'bgra',
                        'luminance' or 'luminance_alpha'.
                    `pos`: tuple, defaults to (0, 0)
                        Position to blit in the texture.
                    `bufferfmt`: str, defaults to 'ubyte'
                        Type of the data buffer, can be one of 'ubyte', 'ushort',
                        'uint', 'byte', 'short', 'int' or 'float'.
                    `mipmap_level`: int, defaults to 0
                        Indicate which mipmap level we are going to update.
                    `mipmap_generation`: bool, defaults to True
                        Indicate if we need to regenerate the mipmap from level 0.
        
                .. versionchanged:: 1.0.7
        
                    added `mipmap_level` and `mipmap_generation`
        
                .. versionchanged:: 1.9.0
                    `pbuffer` can now be any class instance that implements the python
                    buffer interface and / or memoryviews thereof.
        """
        pass

    def blit_data(self, im, pos=None): # real signature unknown; restored from __doc__
        """
        Texture.blit_data(self, im, pos=None)
        Replace a whole texture with image data.
        """
        pass

    def create(self, size=None, colorfmt=None, bufferfmt=None, mipmap=False, callback=None, icolorfmt=None): # real signature unknown; restored from __doc__
        """
        texture_create(size=None, colorfmt=None, bufferfmt=None, mipmap=False, callback=None, icolorfmt=None)
        Create a texture based on size.
        
            :Parameters:
                `size`: tuple, defaults to (128, 128)
                    Size of the texture.
                `colorfmt`: str, defaults to 'rgba'
                    Color format of the texture. Can be 'rgba' or 'rgb',
                    'luminance' or 'luminance_alpha'. On desktop, additional values are
                    available: 'red', 'rg'.
                `icolorfmt`: str, defaults to the value of `colorfmt`
                    Internal format storage of the texture. Can be 'rgba' or 'rgb',
                    'luminance' or 'luminance_alpha'. On desktop, additional values are
                    available: 'r8', 'rg8', 'rgba8'.
                `bufferfmt`: str, defaults to 'ubyte'
                    Internal buffer format of the texture. Can be 'ubyte', 'ushort',
                    'uint', 'bute', 'short', 'int' or 'float'.
                `mipmap`: bool, defaults to False
                    If True, it will automatically generate the mipmap texture.
                `callback`: callable(), defaults to False
                    If a function is provided, it will be called when data is
                    needed in the texture.
        
            .. versionchanged:: 1.7.0
                :attr:`callback` has been added
        """
        pass

    def create_from_data(self, im, mipmap=False): # real signature unknown; restored from __doc__
        """
        texture_create_from_data(im, mipmap=False)
        Create a texture from an ImageData class.
        """
        pass

    def flip_horizontal(self): # real signature unknown; restored from __doc__
        """
        Texture.flip_horizontal(self)
        Flip tex_coords for horizontal display.
        
                .. versionadded:: 1.9.0
        """
        pass

    def flip_vertical(self): # real signature unknown; restored from __doc__
        """
        Texture.flip_vertical(self)
        Flip tex_coords for vertical display.
        """
        pass

    def get_region(self, x, y, width, height): # real signature unknown; restored from __doc__
        """
        Texture.get_region(self, x, y, width, height)
        Return a part of the texture defined by the rectangular arguments
                (x, y, width, height). Returns a :class:`TextureRegion` instance.
        """
        pass

    def remove_reload_observer(self, callback): # real signature unknown; restored from __doc__
        """
        Texture.remove_reload_observer(self, callback)
        Remove a callback from the observer list, previously added by
                :meth:`add_reload_observer`.
        
                .. versionadded:: 1.2.0
        """
        pass

    def save(self, filename, flipped=True, fmt=None): # real signature unknown; restored from __doc__
        """
        Texture.save(self, filename, flipped=True, fmt=None)
        Save the texture content to a file. Check
                :meth:`kivy.core.image.Image.save` for more information.
        
                The flipped parameter flips the saved image vertically, and
                defaults to True.
        
                .. versionadded:: 1.7.0
        
                .. versionchanged:: 1.8.0
        
                    Parameter `flipped` added, defaults to True. All the OpenGL Texture
                    are read from bottom / left, it need to be flipped before saving.
                    If you don't want to flip the image, set flipped to False.
        
                .. versionchanged:: 1.11.0
        
                    Parameter `fmt` added, to pass the final format to the image provider.
                    Used if filename is a BytesIO
        """
        pass

    def _on_proxyimage_loaded(self, image): # real signature unknown; restored from __doc__
        """ Texture._on_proxyimage_loaded(self, image) """
        pass

    def __init__(self, width, height, target, texid=0, colorfmt=None, bufferfmt=None, mipmap=False, source=None, callback=None, icolorfmt=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Texture.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Texture.__setstate_cython__(self, __pyx_state) """
        pass

    bufferfmt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the buffer format used in this texture (readonly).

        .. versionadded:: 1.2.0
        """

    colorfmt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the color format used in this texture (readonly).

        .. versionadded:: 1.0.7
        """

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the height of the texture (readonly).
        """

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the OpenGL ID of the texture (readonly).
        """

    mag_filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set the mag filter texture. Available values:

        - linear
        - nearest

        Check the opengl documentation for more information about the behavior
        of these values :
        http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameter.xml.
        """

    min_filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set the min filter texture. Available values:

        - linear
        - nearest
        - linear_mipmap_linear
        - linear_mipmap_nearest
        - nearest_mipmap_nearest
        - nearest_mipmap_linear

        Check the opengl documentation for more information about the behavior
        of these values :
        http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameter.xml.
        """

    mipmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return True if the texture has mipmap enabled (readonly).
        """

    pixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the pixels texture, in RGBA format only, unsigned byte. The
        origin of the image is at bottom left.

        .. versionadded:: 1.7.0
        """

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the (width, height) of the texture (readonly).
        """

    target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the OpenGL target of the texture (readonly).
        """

    tex_coords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the list of tex_coords (opengl).
        """

    uvpos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set the UV position inside the texture.
        """

    uvsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set the UV size inside the texture.

        .. warning::
            The size can be negative if the texture is flipped.
        """

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the width of the texture (readonly).
        """

    wrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set the wrap texture. Available values:

        - repeat
        - mirrored_repeat
        - clamp_to_edge

        Check the opengl documentation for more information about the behavior
        of these values :
        http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameter.xml.
        """


    _sequenced_textures = {}
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002D9778F0540>'


class TextureRegion(Texture):
    """
    TextureRegion(int x, int y, int width, int height, Texture origin)
    Handle a region of a Texture class. Useful for non power-of-2
        texture handling.
    """
    def ask_update(self, callback): # real signature unknown; restored from __doc__
        """ TextureRegion.ask_update(self, callback) """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ TextureRegion.bind(self) """
        pass

    def __init__(self, int_x, int_y, int_width, int_height, Texture_origin): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ TextureRegion.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ TextureRegion.__setstate_cython__(self, __pyx_state) """
        pass

    pixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002D9778F05A0>'


class WeakMethod(object):
    """
    Implementation of a
        `weakref <http://en.wikipedia.org/wiki/Weak_reference>`_
        for functions and bound methods.
    """
    def is_dead(self): # reliably restored by inspect
        """
        Returns True if the referenced callable was a bound method and
                the instance no longer exists. Otherwise, return False.
        """
        pass

    def __call__(self): # reliably restored by inspect
        """
        Return a new bound-method like the original, or the
                original function if it was just a function or unbound
                method.
                Returns None if the original object doesn't exist.
        """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, method): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.weakmethod', '__doc__': 'Implementation of a\\n    `weakref <http://en.wikipedia.org/wiki/Weak_reference>`_\\n    for functions and bound methods.\\n    ', '__init__': <function WeakMethod.__init__ at 0x000002D977645760>, '__call__': <function WeakMethod.__call__ at 0x000002D977646C00>, 'is_dead': <function WeakMethod.is_dead at 0x000002D977646CA0>, '__eq__': <function WeakMethod.__eq__ at 0x000002D977646D40>, '__repr__': <function WeakMethod.__repr__ at 0x000002D977646DE0>, '__dict__': <attribute '__dict__' of 'WeakMethod' objects>, '__weakref__': <attribute '__weakref__' of 'WeakMethod' objects>, '__hash__': None})"
    __hash__ = None


# variables with complex values

environ = os.environ

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'Texture',
    'TextureRegion',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002D9778EB810>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.texture', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002D9778EB810>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\texture.cp311-win_amd64.pyd')"

__test__ = {}

