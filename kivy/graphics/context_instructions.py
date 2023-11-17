# encoding: utf-8
# module kivy.graphics.context_instructions
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\context_instructions.cp311-win_amd64.pyd
# by generator 1.147
"""
Context instructions
====================

The context instructions represent non graphics elements such as:

* Matrix manipulations (PushMatrix, PopMatrix, Rotate, Translate, Scale,
  MatrixInstruction)
* Color manipulations (Color)
* Texture bindings (BindTexture)

.. versionchanged:: 1.0.8
    The LineWidth instruction has been removed. It wasn't working before and we
    actually have no working implementation. We need to do more experimentation
    to get it right. Check the bug
    `#207 <https://github.com/kivy/kivy/issues/207>`_ for more information.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import kivy.graphics.instructions as __kivy_graphics_instructions
import kivy._event as __kivy__event


# Variables with simple values

kivy_shader_dir = 'C:\\Users\\matthew.muller\\.virtualenvs\\app-gFbndeE6\\Lib\\site-packages\\kivy\\data\\glsl'

PY2 = False

# functions

def gl_init_resources(): # real signature unknown; restored from __doc__
    """ gl_init_resources() """
    pass

def join(path, *paths): # reliably restored by inspect
    # no doc
    pass

def resource_find(filename, use_cache=True): # reliably restored by inspect
    """
    Search for a resource in the list of paths.
        Use resource_add_path to add a custom path to the search.
        By default, results are cached for 60 seconds.
        This can be disabled using use_cache=False.
    
        .. versionchanged:: 2.1.0
            `use_cache` parameter added and made True by default.
    """
    pass

def __pyx_unpickle_ApplyContextMatrix(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ApplyContextMatrix(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_BindTexture(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_BindTexture(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_ChangeState(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ChangeState(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Color(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Color(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_LoadIdentity(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_LoadIdentity(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_MatrixInstruction(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_MatrixInstruction(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_PopMatrix(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_PopMatrix(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_PopState(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_PopState(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_PushMatrix(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_PushMatrix(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_PushState(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_PushState(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Rotate(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Rotate(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Scale(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Scale(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Transform(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Transform(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_Translate(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Translate(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_UpdateNormalMatrix(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_UpdateNormalMatrix(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class ApplyContextMatrix(__kivy_graphics_instructions.ContextInstruction):
    """
    ApplyContextMatrix(**kwargs)
    Pre-multiply the matrix at the top of the stack specified by
        `target_stack` by the matrix at the top of the 'source_stack'
    
        .. versionadded:: 1.6.0
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ApplyContextMatrix.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ApplyContextMatrix.__setstate_cython__(self, __pyx_state) """
        pass

    source_stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the matrix stack to use as a source.
        Can be 'modelview_mat', 'projection_mat' or 'frag_modelview_mat'.

        .. versionadded:: 1.6.0
        """

    target_stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the matrix stack to use as a target.
        Can be 'modelview_mat', 'projection_mat' or 'frag_modelview_mat'.

        .. versionadded:: 1.6.0
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390F30>'


class BindTexture(__kivy_graphics_instructions.ContextInstruction):
    """
    BindTexture(**kwargs)
    BindTexture Graphic instruction.
        The BindTexture Instruction will bind a texture and enable
        GL_TEXTURE_2D for subsequent drawing.
    
        :Parameters:
            `texture`: Texture
                Specifies the texture to bind to the given index.
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ BindTexture.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ BindTexture.__setstate_cython__(self, __pyx_state) """
        pass

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set/get the source (filename) to load for the texture.
        """

    texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390C90>'


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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.cache', '__doc__': 'See module documentation for more information.\\n    ', '_categories': {'kv.resourcefind': {'limit': None, 'timeout': 60}, 'kv.image': {'limit': None, 'timeout': 60}, 'kv.atlas': {'limit': None, 'timeout': None}, 'kv.texture': {'limit': 1000, 'timeout': 60}, 'kv.shader': {'limit': 1000, 'timeout': 3600}, 'kv.graphics.texture': {'limit': None, 'timeout': None}}, '_objects': {'kv.resourcefind': {}, 'kv.image': {}, 'kv.atlas': {}, 'kv.texture': {}, 'kv.shader': {}, 'kv.graphics.texture': {}}, 'register': <staticmethod(<function Cache.register at 0x0000021F27372020>)>, 'append': <staticmethod(<function Cache.append at 0x0000021F273722A0>)>, 'get': <staticmethod(<function Cache.get at 0x0000021F27372340>)>, 'get_timestamp': <staticmethod(<function Cache.get_timestamp at 0x0000021F273723E0>)>, 'get_lastaccess': <staticmethod(<function Cache.get_lastaccess at 0x0000021F27372480>)>, 'remove': <staticmethod(<function Cache.remove at 0x0000021F27372520>)>, '_purge_oldest': <staticmethod(<function Cache._purge_oldest at 0x0000021F273725C0>)>, '_purge_by_timeout': <staticmethod(<function Cache._purge_by_timeout at 0x0000021F27372660>)>, 'print_usage': <staticmethod(<function Cache.print_usage at 0x0000021F27372700>)>, '__dict__': <attribute '__dict__' of 'Cache' objects>, '__weakref__': <attribute '__weakref__' of 'Cache' objects>})"


class ChangeState(__kivy_graphics_instructions.ContextInstruction):
    """
    ChangeState(**kwargs)
    Instruction that changes the values of arbitrary states/uniforms on the
        current render context.
    
        .. versionadded:: 1.6.0
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ChangeState.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ChangeState.__setstate_cython__(self, __pyx_state) """
        pass

    changes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390D50>'


class Color(__kivy_graphics_instructions.ContextInstruction):
    """
    Color(*args, **kwargs)
    
        Instruction to set the color state for any vertices being
        drawn after it.
    
        This represents a color between 0 and 1, but is applied as a
        *multiplier* to the texture of any vertex instructions following
        it in a canvas. If no texture is set, the vertex instruction
        takes the precise color of the Color instruction.
    
        For instance, if a Rectangle has a texture with uniform color
        ``(0.5, 0.5, 0.5, 1.0)`` and the preceding Color has
        ``rgba=(1, 0.5, 2, 1)``, the actual visible color will be
        ``(0.5, 0.25, 1.0, 1.0)`` since the Color instruction is applied as
        a multiplier to every rgba component. In this case, a Color
        component outside the 0-1 range gives a visible result as the
        intensity of the blue component is doubled.
    
        To declare a Color in Python, you can do::
    
            from kivy.graphics import Color
    
            # create red v
            c = Color(1, 0, 0)
            # create blue color
            c = Color(0, 1, 0)
            # create blue color with 50% alpha
            c = Color(0, 1, 0, .5)
    
            # using hsv mode
            c = Color(0, 1, 1, mode='hsv')
            # using hsv mode + alpha
            c = Color(0, 1, 1, .2, mode='hsv')
    
        You can also set color components that are available as properties
        by passing them as keyword arguments::
    
            c = Color(b=0.5)  # sets the blue component only
    
        In kv lang you can set the color properties directly:
    
        .. code-block:: kv
    
            <Rule>:
                canvas:
                    # red color
                    Color:
                        rgb: 1, 0, 0
                    # blue color
                    Color:
                        rgb: 0, 1, 0
                    # blue color with 50% alpha
                    Color:
                        rgba: 0, 1, 0, .5
    
                    # using hsv mode
                    Color:
                        hsv: 0, 1, 1
                    # using hsv mode + alpha
                    Color:
                        hsv: 0, 1, 1
                        a: .5
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Color.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Color.__setstate_cython__(self, __pyx_state) """
        pass

    a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alpha component, between 0 and 1.
        """

    b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Blue component, between 0 and 1.
        """

    g = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Green component, between 0 and 1.
        """

    h = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Hue component, between 0 and 1.
        """

    hsv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """HSV color, list of 3 values in 0-1 range, alpha will be 1.
        """

    r = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Red component, between 0 and 1.
        """

    rgb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """RGB color, list of 3 values in 0-1 range. The alpha will be 1.
        """

    rgba = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """RGBA color, list of 4 values in 0-1 range.
        """

    s = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Saturation component, between 0 and 1.
        """

    v = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value component, between 0 and 1.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390C30>'


class Image(__kivy__event.EventDispatcher):
    """
    Load an image and store the size and texture.
    
        .. versionchanged:: 1.0.7
    
            `mipmap` attribute has been added. The `texture_mipmap` and
            `texture_rectangle` have been deleted.
    
        .. versionchanged:: 1.0.8
    
            An Image widget can change its texture. A new event 'on_texture' has
            been introduced. New methods for handling sequenced animation have been
            added.
    
        :Parameters:
            `arg`: can be a string (str), Texture, BytesIO or Image object
                A string path to the image file or data URI to be loaded; or a
                Texture object, which will be wrapped in an Image object; or a
                BytesIO object containing raw image data; or an already existing
                image object, in which case, a real copy of the given image object
                will be returned.
            `keep_data`: bool, defaults to False
                Keep the image data when the texture is created.
            `mipmap`: bool, defaults to False
                Create mipmap for the texture.
            `anim_delay`: float, defaults to .25
                Delay in seconds between each animation frame. Lower values means
                faster animation.
            `ext`: str, only with BytesIO `arg`
                File extension to use in determining how to load raw image data.
            `filename`: str, only with BytesIO `arg`
                Filename to use in the image cache for raw image data.
    """
    def anim_reset(self, allow_anim): # reliably restored by inspect
        """
        Reset an animation if available.
        
                .. versionadded:: 1.0.8
        
                :Parameters:
                    `allow_anim`: bool
                        Indicate whether the animation should restart playing or not.
        
                Usage::
        
                    # start/reset animation
                    image.anim_reset(True)
        
                    # or stop the animation
                    image.anim_reset(False)
        
                You can change the animation speed whilst it is playing::
        
                    # Set to 20 FPS
                    image.anim_delay = 1 / 20.
        """
        pass

    def load(filename, **kwargs): # reliably restored by inspect
        """
        Load an image
        
                :Parameters:
                    `filename`: str
                        Filename of the image.
                    `keep_data`: bool, defaults to False
                        Keep the image data when the texture is created.
        """
        pass

    def load_memory(self, data, ext, filename=None): # reliably restored by inspect
        """ (internal) Method to load an image from raw data. """
        pass

    def on_texture(self, *largs): # reliably restored by inspect
        """
        This event is fired when the texture reference or content has
                   changed. It is normally used for sequenced images.
        
                .. versionadded:: 1.0.8
        """
        pass

    def read_pixel(self, x, y): # reliably restored by inspect
        """
        For a given local x/y position, return the pixel color at that
                position.
        
                .. warning::
                    This function can only be used with images loaded with the
                    keep_data=True keyword. For example::
        
                        m = Image.load('image.png', keep_data=True)
                        color = m.read_pixel(150, 150)
        
                :Parameters:
                    `x`: int
                        Local x coordinate of the pixel in question.
                    `y`: int
                        Local y coordinate of the pixel in question.
        """
        pass

    def remove_from_cache(self): # reliably restored by inspect
        """
        Remove the Image from cache. This facilitates re-loading of
                images from disk in case the image content has changed.
        
                .. versionadded:: 1.3.0
        
                Usage::
        
                    im = CoreImage('1.jpg')
                    # -- do something --
                    im.remove_from_cache()
                    im = CoreImage('1.jpg')
                    # this time image will be re-loaded from disk
        """
        pass

    def save(self, filename, flipped=False, fmt=None): # reliably restored by inspect
        """
        Save image texture to file.
        
                The filename should have the '.png' extension because the texture data
                read from the GPU is in the RGBA format. '.jpg' might work but has not
                been heavily tested so some providers might break when using it.
                Any other extensions are not officially supported.
        
                The flipped parameter flips the saved image vertically, and
                defaults to False.
        
                Example::
        
                    # Save an core image object
                    from kivy.core.image import Image
                    img = Image('hello.png')
                    img.save('hello2.png')
        
                    # Save a texture
                    texture = Texture.create(...)
                    img = Image(texture)
                    img.save('hello3.png')
        
                .. versionadded:: 1.7.0
        
                .. versionchanged:: 1.8.0
                    Parameter `flipped` added to flip the image before saving, default
                    to False.
        
                .. versionchanged:: 1.11.0
                    Parameter `fmt` added to force the output format of the file
                    Filename can now be a BytesIO object.
        """
        pass

    def _anim(self, *largs): # reliably restored by inspect
        # no doc
        pass

    def _find_format_from_filename(self, filename): # reliably restored by inspect
        # no doc
        pass

    def _get_anim_delay(self): # reliably restored by inspect
        # no doc
        pass

    def _get_filename(self): # reliably restored by inspect
        # no doc
        pass

    def _get_image(self): # reliably restored by inspect
        # no doc
        pass

    def _img_iterate(self, *largs): # reliably restored by inspect
        # no doc
        pass

    def _set_anim_delay(self, x): # reliably restored by inspect
        # no doc
        pass

    def _set_filename(self, value): # reliably restored by inspect
        # no doc
        pass

    def _set_image(self, image): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, arg, **kwargs): # reliably restored by inspect
        # no doc
        pass

    anim_available = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return True if this Image instance has animation available.

        .. versionadded:: 1.0.8
        """

    anim_delay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    anim_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the index number of the image currently in the texture.

        .. versionadded:: 1.0.8
        """

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set the filename of image"""

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Image height
        """

    image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get/set the data image object"""

    nocache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicate whether the texture will not be stored in the cache or not.

        .. versionadded:: 1.6.0
        """

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Image size (width, height)
        """

    texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Texture of the image"""

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Image width
        """


    copy_attributes = (
        '_size',
        '_filename',
        '_texture',
        '_image',
        '_mipmap',
        '_nocache',
    )
    data_uri_re = re.compile('^data:image/([^;,]*)(;[^,]*)?,(.*)$')
    _anim_ev = None
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'kivy.core.image\', \'__doc__\': "Load an image and store the size and texture.\\n\\n    .. versionchanged:: 1.0.7\\n\\n        `mipmap` attribute has been added. The `texture_mipmap` and\\n        `texture_rectangle` have been deleted.\\n\\n    .. versionchanged:: 1.0.8\\n\\n        An Image widget can change its texture. A new event \'on_texture\' has\\n        been introduced. New methods for handling sequenced animation have been\\n        added.\\n\\n    :Parameters:\\n        `arg`: can be a string (str), Texture, BytesIO or Image object\\n            A string path to the image file or data URI to be loaded; or a\\n            Texture object, which will be wrapped in an Image object; or a\\n            BytesIO object containing raw image data; or an already existing\\n            image object, in which case, a real copy of the given image object\\n            will be returned.\\n        `keep_data`: bool, defaults to False\\n            Keep the image data when the texture is created.\\n        `mipmap`: bool, defaults to False\\n            Create mipmap for the texture.\\n        `anim_delay`: float, defaults to .25\\n            Delay in seconds between each animation frame. Lower values means\\n            faster animation.\\n        `ext`: str, only with BytesIO `arg`\\n            File extension to use in determining how to load raw image data.\\n        `filename`: str, only with BytesIO `arg`\\n            Filename to use in the image cache for raw image data.\\n    ", \'copy_attributes\': (\'_size\', \'_filename\', \'_texture\', \'_image\', \'_mipmap\', \'_nocache\'), \'data_uri_re\': re.compile(\'^data:image/([^;,]*)(;[^,]*)?,(.*)$\'), \'_anim_ev\': None, \'__init__\': <function Image.__init__ at 0x0000021F27400360>, \'remove_from_cache\': <function Image.remove_from_cache at 0x0000021F27400400>, \'_anim\': <function Image._anim at 0x0000021F274004A0>, \'anim_reset\': <function Image.anim_reset at 0x0000021F27400540>, \'_get_anim_delay\': <function Image._get_anim_delay at 0x0000021F274005E0>, \'_set_anim_delay\': <function Image._set_anim_delay at 0x0000021F27400680>, \'anim_delay\': <property object at 0x0000021F273DF7E0>, \'anim_available\': <property object at 0x0000021F273DF880>, \'anim_index\': <property object at 0x0000021F273DF8D0>, \'_img_iterate\': <function Image._img_iterate at 0x0000021F27400860>, \'on_texture\': <function Image.on_texture at 0x0000021F27400900>, \'load\': <staticmethod(<function Image.load at 0x0000021F274009A0>)>, \'_get_image\': <function Image._get_image at 0x0000021F27400A40>, \'_set_image\': <function Image._set_image at 0x0000021F27400AE0>, \'image\': <property object at 0x0000021F273DF920>, \'_get_filename\': <function Image._get_filename at 0x0000021F27400B80>, \'_set_filename\': <function Image._set_filename at 0x0000021F27400C20>, \'filename\': <property object at 0x0000021F273DF970>, \'load_memory\': <function Image.load_memory at 0x0000021F27400CC0>, \'size\': <property object at 0x0000021F273DF9C0>, \'width\': <property object at 0x0000021F273DFA10>, \'height\': <property object at 0x0000021F273DFA60>, \'texture\': <property object at 0x0000021F273DFAB0>, \'nocache\': <property object at 0x0000021F273DFB00>, \'save\': <function Image.save at 0x0000021F27401080>, \'_find_format_from_filename\': <function Image._find_format_from_filename at 0x0000021F27401120>, \'read_pixel\': <function Image.read_pixel at 0x0000021F274011C0>, \'__dict__\': <attribute \'__dict__\' of \'Image\' objects>})'


class LineWidth(__kivy_graphics_instructions.ContextInstruction):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390BD0>'


class LoadIdentity(__kivy_graphics_instructions.ContextInstruction):
    """
    LoadIdentity(**kwargs)
    Load the identity Matrix into the matrix stack specified by
        the instructions stack property (default='modelview_mat')
    
        .. versionadded:: 1.6.0
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ LoadIdentity.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ LoadIdentity.__setstate_cython__(self, __pyx_state) """
        pass

    stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the matrix stack to use. Can be 'modelview_mat',
        'projection_mat' or 'frag_modelview_mat'.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390E10>'


class MatrixInstruction(__kivy_graphics_instructions.ContextInstruction):
    """
    MatrixInstruction(*args, **kwargs)
    Base class for Matrix Instruction on the canvas.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ MatrixInstruction.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ MatrixInstruction.__setstate_cython__(self, __pyx_state) """
        pass

    matrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Matrix property. Matrix from the transformation module.
        Setting the matrix using this property when a change is made
        is important because it will notify the context about the update.
        """

    stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the matrix stack to use. Can be 'modelview_mat',
        'projection_mat' or 'frag_modelview_mat'.

        .. versionadded:: 1.6.0
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390FF0>'


class PopMatrix(__kivy_graphics_instructions.ContextInstruction):
    """
    PopMatrix(*args, **kwargs)
    Pop the matrix from the context's matrix stack onto the model view.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ PopMatrix.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ PopMatrix.__setstate_cython__(self, __pyx_state) """
        pass

    stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the matrix stack to use. Can be 'modelview_mat',
        'projection_mat' or 'frag_modelview_mat'.

        .. versionadded:: 1.6.0
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390ED0>'


class PopState(__kivy_graphics_instructions.ContextInstruction):
    """
    PopState(*args, **kwargs)
    Instruction that pops arbitrary states/uniforms off the context
        state stack.
    
        .. versionadded:: 1.6.0
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ PopState.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ PopState.__setstate_cython__(self, __pyx_state) """
        pass

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390DB0>'


class PushMatrix(__kivy_graphics_instructions.ContextInstruction):
    """
    PushMatrix(*args, **kwargs)
    Push the matrix onto the context's matrix stack.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ PushMatrix.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ PushMatrix.__setstate_cython__(self, __pyx_state) """
        pass

    stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of the matrix stack to use. Can be 'modelview_mat',
        'projection_mat' or 'frag_modelview_mat'.

        .. versionadded:: 1.6.0
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390E70>'


class PushState(__kivy_graphics_instructions.ContextInstruction):
    """
    PushState(*args, **kwargs)
    Instruction that pushes arbitrary states/uniforms onto the context
        state stack.
    
        .. versionadded:: 1.6.0
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ PushState.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ PushState.__setstate_cython__(self, __pyx_state) """
        pass

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390CF0>'


class Transform(MatrixInstruction):
    """
    Transform(*args, **kwargs)
    Transform class. A matrix instruction class which
        modifies the transformation matrix.
    """
    def identity(self): # real signature unknown; restored from __doc__
        """
        Transform.identity(self)
        Resets the transformation to the identity matrix.
        """
        pass

    def rotate(self, float_angle, float_ax, float_ay, float_az): # real signature unknown; restored from __doc__
        """
        Transform.rotate(self, float angle, float ax, float ay, float az)
        Rotate the transformation by matrix by *angle* degrees around the
                axis defined by the vector ax, ay, az.
        """
        pass

    def scale(self, float_s): # real signature unknown; restored from __doc__
        """
        Transform.scale(self, float s)
        Applies a uniform scaling of s to the matrix transformation.
        """
        pass

    def transform(self, Matrix_trans): # real signature unknown; restored from __doc__
        """
        Transform.transform(self, Matrix trans)
        Multiply the instructions matrix by trans.
        """
        pass

    def translate(self, float_tx, float_ty, float_tz): # real signature unknown; restored from __doc__
        """
        Transform.translate(self, float tx, float ty, float tz)
        Translate the instructions transformation by tx, ty, tz.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Transform.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Transform.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27391050>'


class Rotate(Transform):
    """
    Rotate(*args, **kwargs)
    Rotate the coordinate space by applying a rotation transformation
        on the modelview matrix. You can set the properties of the instructions
        afterwards with e.g. ::
    
            rot.angle = 90
            rot.axis = (0, 0, 1)
    """
    def set(self, float_angle, float_ax, float_ay, float_az): # real signature unknown; restored from __doc__
        """
        Rotate.set(self, float angle, float ax, float ay, float az)
        Set the angle and axis of rotation.
        
                >>> rotationobject.set(90, 0, 0, 1)
        
                .. deprecated:: 1.7.0
        
                    The set() method doesn't use the new :attr:`origin` property.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Rotate.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Rotate.__setstate_cython__(self, __pyx_state) """
        pass

    angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the angle of the rotation.
        """

    axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the axis of the rotation.

        The format of the axis is (x, y, z).
        """

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Origin of the rotation.

        .. versionadded:: 1.7.0

        The format of the origin can be either (x, y) or (x, y, z).
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F273910B0>'


class Scale(Transform):
    """
    Scale(*args, **kwargs)
    Instruction to create a non uniform scale transformation.
    
        Create using one or three arguments::
    
           Scale(s)         # scale all three axes the same
           Scale(x, y, z)   # scale the axes independently
    
        .. deprecated:: 1.6.0
            Deprecated single scale property in favor of x, y, z, xyz axis
            independent scaled factors.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Scale.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Scale.__setstate_cython__(self, __pyx_state) """
        pass

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Origin of the scale.

        .. versionadded:: 1.9.0

        The format of the origin can be either (x, y) or (x, y, z).
        """

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the scale.

        .. deprecated:: 1.6.0
            Deprecated in favor of per axis scale properties x,y,z, xyz, etc.
        """

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the scale on the X axis.

        .. versionchanged:: 1.6.0
        """

    xyz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """3 tuple scale vector in 3D in x, y, and z axis.

        .. versionchanged:: 1.6.0
        """

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the scale on the Y axis.

        .. versionchanged:: 1.6.0
        """

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the scale on Z axis.

        .. versionchanged:: 1.6.0
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27391110>'


class Translate(Transform):
    """
    Translate(*args, **kwargs)
    Instruction to create a translation of the model view coordinate space.
    
        Construct by either::
    
            Translate(x, y)         # translate in just the two axes
            Translate(x, y, z)      # translate in all three axes
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Translate.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Translate.__setstate_cython__(self, __pyx_state) """
        pass

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the translation on the X axis.
        """

    xy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """2 tuple with translation vector in 2D for x and y axis.
        """

    xyz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """3 tuple translation vector in 3D in x, y, and z axis.
        """

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the translation on the Y axis.
        """

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting the translation on the Z axis.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27391170>'


class UpdateNormalMatrix(__kivy_graphics_instructions.ContextInstruction):
    """
    Update the normal matrix 'normal_mat' based on the current
        modelview matrix. This will compute 'normal_mat' uniform as:
        `inverse( transpose( mat3(mvm) ) )`
    
        .. versionadded:: 1.6.0
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ UpdateNormalMatrix.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ UpdateNormalMatrix.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F27390F90>'


# variables with complex values

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'Color',
    'BindTexture',
    'PushMatrix',
    'PopMatrix',
    'Rotate',
    'Scale',
    'Translate',
    'MatrixInstruction',
    'gl_init_resources',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021F2738EF10>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.context_instructions', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021F2738EF10>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\context_instructions.cp311-win_amd64.pyd')"

__test__ = {
    'Rotate.set (line 686)': "Set the angle and axis of rotation.\n\n        >>> rotationobject.set(90, 0, 0, 1)\n\n        .. deprecated:: 1.7.0\n\n            The set() method doesn't use the new :attr:`origin` property.\n        ",
}

