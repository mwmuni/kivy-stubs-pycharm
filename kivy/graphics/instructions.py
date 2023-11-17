# encoding: utf-8
# module kivy.graphics.instructions
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\instructions.cp311-win_amd64.pyd
# by generator 1.147
"""
Canvas
======

The :class:`Canvas` is the root object used for drawing by a
:class:`~kivy.uix.widget.Widget`. Check the class documentation for more
information about the usage of Canvas.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from _thread import get_ident

from _weakref import proxy

import kivy._event as __kivy__event


# Variables with simple values

kivy_shader_dir = 'C:\\Users\\matthew.muller\\.virtualenvs\\app-gFbndeE6\\Lib\\site-packages\\kivy\\data\\glsl'

PY2 = False

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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.cache', '__doc__': 'See module documentation for more information.\\n    ', '_categories': {'kv.resourcefind': {'limit': None, 'timeout': 60}, 'kv.image': {'limit': None, 'timeout': 60}, 'kv.atlas': {'limit': None, 'timeout': None}, 'kv.texture': {'limit': 1000, 'timeout': 60}, 'kv.shader': {'limit': 1000, 'timeout': 3600}, 'kv.graphics.texture': {'limit': None, 'timeout': None}}, '_objects': {'kv.resourcefind': {}, 'kv.image': {}, 'kv.atlas': {}, 'kv.texture': {}, 'kv.shader': {}, 'kv.graphics.texture': {}}, 'register': <staticmethod(<function Cache.register at 0x000001FD792E2020>)>, 'append': <staticmethod(<function Cache.append at 0x000001FD792E22A0>)>, 'get': <staticmethod(<function Cache.get at 0x000001FD792E2340>)>, 'get_timestamp': <staticmethod(<function Cache.get_timestamp at 0x000001FD792E23E0>)>, 'get_lastaccess': <staticmethod(<function Cache.get_lastaccess at 0x000001FD792E2480>)>, 'remove': <staticmethod(<function Cache.remove at 0x000001FD792E2520>)>, '_purge_oldest': <staticmethod(<function Cache._purge_oldest at 0x000001FD792E25C0>)>, '_purge_by_timeout': <staticmethod(<function Cache._purge_by_timeout at 0x000001FD792E2660>)>, 'print_usage': <staticmethod(<function Cache.print_usage at 0x000001FD792E2700>)>, '__dict__': <attribute '__dict__' of 'Cache' objects>, '__weakref__': <attribute '__weakref__' of 'Cache' objects>})"


class Instruction(__kivy__event.ObjectWithUid):
    """
    Instruction(**kwargs)
    Represents the smallest instruction available. This class is for internal
        usage only, don't use it directly.
    """
    def flag_data_update(self): # real signature unknown; restored from __doc__
        """ Instruction.flag_data_update(self) """
        pass

    def flag_update(self, int_do_parent=1): # real signature unknown; restored from __doc__
        """ Instruction.flag_update(self, int do_parent=1) """
        pass

    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Instruction.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Instruction.__setstate_cython__(self, __pyx_state) """
        pass

    group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group: unicode"""

    needs_redraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proxy_ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return a proxy reference to the Instruction i.e. without creating a
        reference of the widget. See `weakref.proxy
        <http://docs.python.org/2/library/weakref.html?highlight=proxy#weakref.proxy>`_
        for more information.

        .. versionadded:: 1.7.2
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FD792B7810>'


class Callback(Instruction):
    """
    Callback(callback=None, **kwargs)
    .. versionadded:: 1.0.4
    
        A Callback is an instruction that will be called when the drawing
        operation is performed. When adding instructions to a canvas, you can do
        this::
    
            with self.canvas:
                Color(1, 1, 1)
                Rectangle(pos=self.pos, size=self.size)
                Callback(self.my_callback)
    
        The definition of the callback must be::
    
            def my_callback(self, instr):
                print('I have been called!')
    
        .. warning::
    
            Note that if you perform many and/or costly calls to callbacks, you
            might potentially slow down the rendering performance significantly.
    
        The updating of your canvas does not occur until something new happens.
        From your callback, you can ask for an update::
    
            with self.canvas:
                self.cb = Callback(self.my_callback)
            # then later in the code
            self.cb.ask_update()
    
        If you use the Callback class to call rendering methods of another
        toolkit, you will have issues with the OpenGL context. The OpenGL state may
        have been manipulated by the other toolkit, and as soon as program flow
        returns to Kivy, it will just break. You can have glitches, crashes, black
        holes might occur, etc.
        To avoid that, you can activate the :attr:`reset_context` option. It will
        reset the OpenGL context state to make Kivy's rendering correct after the
        call to your callback.
    
        .. warning::
    
            The :attr:`reset_context` is not a full OpenGL reset. If you have issues
            regarding that, please contact us.
    """
    def ask_update(self): # real signature unknown; restored from __doc__
        """
        Callback.ask_update(self)
        Inform the parent canvas that we'd like it to update on the next
                frame. This is useful when you need to trigger a redraw due to some
                value having changed for example.
        
                .. versionadded:: 1.0.4
        """
        pass

    def __init__(self, callback=None, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Callback.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Callback.__setstate_cython__(self, __pyx_state) """
        pass

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting/setting func.
        """

    reset_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set this to True if you want to reset the OpenGL context for Kivy
        after the callback has been called.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FD792B7FC0>'


class InstructionGroup(Instruction):
    """
    InstructionGroup(**kwargs)
    
        Group of :class:`Instruction`. Allows for the adding and removing
        of graphics instructions. It can be used directly as follows::
    
            blue = InstructionGroup()
            blue.add(Color(0, 0, 1, 0.2))
            blue.add(Rectangle(pos=self.pos, size=(100, 100)))
    
            green = InstructionGroup()
            green.add(Color(0, 1, 0, 0.4))
            green.add(Rectangle(pos=(100, 100), size=(100, 100)))
    
            # Here, self should be a Widget or subclass
            [self.canvas.add(group) for group in [blue, green]]
    """
    def add(self, Instruction_c): # real signature unknown; restored from __doc__
        """
        InstructionGroup.add(self, Instruction c)
        Add a new :class:`Instruction` to our list.
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        InstructionGroup.clear(self)
        Remove all the :class:`Instructions <Instruction>`.
        """
        pass

    def get_group(self, unicode_groupname): # real signature unknown; restored from __doc__
        """
        InstructionGroup.get_group(self, unicode groupname)
        Return an iterable for all the :class:`Instructions <Instruction>`
                with a specific group name.
        """
        pass

    def indexof(self, Instruction_c): # real signature unknown; restored from __doc__
        """ InstructionGroup.indexof(self, Instruction c) """
        pass

    def insert(self, int_index, Instruction_c): # real signature unknown; restored from __doc__
        """
        InstructionGroup.insert(self, int index, Instruction c)
        Insert a new :class:`Instruction` into our list at index.
        """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ InstructionGroup.length(self) """
        pass

    def remove(self, Instruction_c): # real signature unknown; restored from __doc__
        """
        InstructionGroup.remove(self, Instruction c)
        Remove an existing :class:`Instruction` from our list.
        """
        pass

    def remove_group(self, unicode_groupname): # real signature unknown; restored from __doc__
        """
        InstructionGroup.remove_group(self, unicode groupname)
        Remove all :class:`Instructions <Instruction>` with a specific group
                name.
        """
        pass

    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ InstructionGroup.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ InstructionGroup.__setstate_cython__(self, __pyx_state) """
        pass

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """children: list"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FD792B7B70>'


class CanvasBase(InstructionGroup):
    """
    CanvasBase provides the context manager methods for the
        :class:`Canvas`.
    """
    def __enter__(self): # real signature unknown; restored from __doc__
        """ CanvasBase.__enter__(self) """
        pass

    def __exit__(self, *largs): # real signature unknown; restored from __doc__
        """ CanvasBase.__exit__(self, *largs) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ CanvasBase.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ CanvasBase.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FD792B7C30>'


class Canvas(CanvasBase):
    """
    Canvas(**kwargs)
    The important Canvas class. Use this class to add graphics or context
        instructions that you want to be used for drawing.
    
        .. note::
    
            The Canvas supports Python's ``with`` statement and its enter & exit
            semantics.
    
        Usage of a canvas without the ``with`` statement::
    
            self.canvas.add(Color(1., 1., 0))
            self.canvas.add(Rectangle(size=(50, 50)))
    
        Usage of a canvas with Python's ``with`` statement::
    
            with self.canvas:
                Color(1., 1., 0)
                Rectangle(size=(50, 50))
    """
    def add(self, Instruction_c): # real signature unknown; restored from __doc__
        """
        Canvas.add(self, Instruction c)
        Append an :class:`Instruction` to our list. If the canvas contains
                an `after` group, then this instruction is inserted just before the
                after group, which remains last. This is different from how
                :meth:`insert` works, which can insert anywhere.
        """
        pass

    def ask_update(self): # real signature unknown; restored from __doc__
        """
        Canvas.ask_update(self)
        Inform the canvas that we'd like it to update on the next frame.
                This is useful when you need to trigger a redraw due to some value
                having changed for example.
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        Canvas.clear(self)
        Clears every :class:`Instruction` in the canvas, leaving it clean.
        """
        pass

    def draw(self): # real signature unknown; restored from __doc__
        """
        Canvas.draw(self)
        Apply the instruction to our window.
        """
        pass

    def remove(self, Instruction_c): # real signature unknown; restored from __doc__
        """ Canvas.remove(self, Instruction c) """
        pass

    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Canvas.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Canvas.__setstate_cython__(self, __pyx_state) """
        pass

    after = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting the 'after' group.
        """

    before = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property for getting the 'before' group.
        """

    has_after = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to see if the :attr:`after` group has already been created.

        .. versionadded:: 1.7.0
        """

    has_before = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to see if the :attr:`before` group has already been created.

        .. versionadded:: 1.7.0
        """

    opacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property to get/set the opacity value of the canvas.

        .. versionadded:: 1.4.1

        The opacity attribute controls the opacity of the canvas and its
        children.  Be careful, it's a cumulative attribute: the value is
        multiplied to the current global opacity and the result is applied to
        the current context color.

        For example: if your parent has an opacity of 0.5 and a child has an
        opacity of 0.2, the real opacity of the child will be 0.5 * 0.2 = 0.1.

        Then, the opacity is applied on the shader as::

            frag_color = color * vec4(1.0, 1.0, 1.0, opacity);

        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FD792B7C60>'


class ContextInstruction(Instruction):
    """
    ContextInstruction(**kwargs)
    The ContextInstruction class is the base for the creation of instructions
        that don't have a direct visual representation, but instead modify the
        current Canvas' state, e.g. texture binding, setting color parameters,
        matrix manipulation and so on.
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ContextInstruction.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ContextInstruction.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FD792B7840>'


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
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'kivy.core.image\', \'__doc__\': "Load an image and store the size and texture.\\n\\n    .. versionchanged:: 1.0.7\\n\\n        `mipmap` attribute has been added. The `texture_mipmap` and\\n        `texture_rectangle` have been deleted.\\n\\n    .. versionchanged:: 1.0.8\\n\\n        An Image widget can change its texture. A new event \'on_texture\' has\\n        been introduced. New methods for handling sequenced animation have been\\n        added.\\n\\n    :Parameters:\\n        `arg`: can be a string (str), Texture, BytesIO or Image object\\n            A string path to the image file or data URI to be loaded; or a\\n            Texture object, which will be wrapped in an Image object; or a\\n            BytesIO object containing raw image data; or an already existing\\n            image object, in which case, a real copy of the given image object\\n            will be returned.\\n        `keep_data`: bool, defaults to False\\n            Keep the image data when the texture is created.\\n        `mipmap`: bool, defaults to False\\n            Create mipmap for the texture.\\n        `anim_delay`: float, defaults to .25\\n            Delay in seconds between each animation frame. Lower values means\\n            faster animation.\\n        `ext`: str, only with BytesIO `arg`\\n            File extension to use in determining how to load raw image data.\\n        `filename`: str, only with BytesIO `arg`\\n            Filename to use in the image cache for raw image data.\\n    ", \'copy_attributes\': (\'_size\', \'_filename\', \'_texture\', \'_image\', \'_mipmap\', \'_nocache\'), \'data_uri_re\': re.compile(\'^data:image/([^;,]*)(;[^,]*)?,(.*)$\'), \'_anim_ev\': None, \'__init__\': <function Image.__init__ at 0x000001FD79370360>, \'remove_from_cache\': <function Image.remove_from_cache at 0x000001FD79370400>, \'_anim\': <function Image._anim at 0x000001FD793704A0>, \'anim_reset\': <function Image.anim_reset at 0x000001FD79370540>, \'_get_anim_delay\': <function Image._get_anim_delay at 0x000001FD793705E0>, \'_set_anim_delay\': <function Image._set_anim_delay at 0x000001FD79370680>, \'anim_delay\': <property object at 0x000001FD7934F5B0>, \'anim_available\': <property object at 0x000001FD7934F650>, \'anim_index\': <property object at 0x000001FD7934F6A0>, \'_img_iterate\': <function Image._img_iterate at 0x000001FD79370860>, \'on_texture\': <function Image.on_texture at 0x000001FD79370900>, \'load\': <staticmethod(<function Image.load at 0x000001FD793709A0>)>, \'_get_image\': <function Image._get_image at 0x000001FD79370A40>, \'_set_image\': <function Image._set_image at 0x000001FD79370AE0>, \'image\': <property object at 0x000001FD7934F6F0>, \'_get_filename\': <function Image._get_filename at 0x000001FD79370B80>, \'_set_filename\': <function Image._set_filename at 0x000001FD79370C20>, \'filename\': <property object at 0x000001FD7934F740>, \'load_memory\': <function Image.load_memory at 0x000001FD79370CC0>, \'size\': <property object at 0x000001FD7934F790>, \'width\': <property object at 0x000001FD7934F7E0>, \'height\': <property object at 0x000001FD7934F830>, \'texture\': <property object at 0x000001FD7934F880>, \'nocache\': <property object at 0x000001FD7934F8D0>, \'save\': <function Image.save at 0x000001FD79371080>, \'_find_format_from_filename\': <function Image._find_format_from_filename at 0x000001FD79371120>, \'read_pixel\': <function Image.read_pixel at 0x000001FD793711C0>, \'__dict__\': <attribute \'__dict__\' of \'Image\' objects>})'


class RenderContext(Canvas):
    """
    RenderContext(*args, **kwargs)
    The render context stores all the necessary information for drawing, i.e.:
    
        - The vertex shader
        - The fragment shader
        - The default texture
        - The state stack (color, texture, matrix...)
    """
    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ RenderContext.__reduce_cython__(self) """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ RenderContext.__setstate_cython__(self, __pyx_state) """
        pass

    shader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the shader attached to the render context.
        """

    use_parent_frag_modelview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If True, the parent fragment modelview matrix will be used.

        .. versionadded:: 1.10.1

            rc = RenderContext(use_parent_frag_modelview=True)
        """

    use_parent_modelview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If True, the parent modelview matrix will be used.

        .. versionadded:: 1.7.0

        Before::

            rc['modelview_mat'] = Window.render_context['modelview_mat']

        Now::

            rc = RenderContext(use_parent_modelview=True)
        """

    use_parent_projection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If True, the parent projection matrix will be used.

        .. versionadded:: 1.7.0

        Before::

            rc['projection_mat'] = Window.render_context['projection_mat']

        Now::

            rc = RenderContext(use_parent_projection=True)
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FD792B7C90>'


class VertexInstruction(Instruction):
    """
    VertexInstruction(**kwargs)
    The VertexInstruction class is the base for all graphics instructions
        that have a direct visual representation on the canvas, such as Rectangles,
        Triangles, Lines, Ellipse and so on.
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ VertexInstruction.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ VertexInstruction.__setstate_cython__(self, __pyx_state) """
        pass

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property represents the filename to load the texture from.
        If you want to use an image as source, do it like this::

            with self.canvas:
                Rectangle(source='mylogo.png', pos=self.pos, size=self.size)

        Here's the equivalent in Kivy language:

        .. code-block:: kv

            <MyWidget>:
                canvas:
                    Rectangle:
                        source: 'mylogo.png'
                        pos: self.pos
                        size: self.size

        .. note::

            The filename will be searched for using the
            :func:`kivy.resources.resource_find` function.

        """

    texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property that represents the texture used for drawing this
        Instruction. You can set a new texture like this::

            from kivy.core.image import Image

            texture = Image('logo.png').texture
            with self.canvas:
                Rectangle(texture=texture, pos=self.pos, size=self.size)

        Usually, you will use the :attr:`source` attribute instead of the
        texture.
        """

    tex_coords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This property represents the texture coordinates used for drawing the
        vertex instruction. The value must be a list of 8 values.

        A texture coordinate has a position (u, v), and a size (w, h). The size
        can be negative, and would represent the 'flipped' texture. By default,
        the tex_coords are::

            [u, v, u + w, v, u + w, v + h, u, v + h]

        You can pass your own texture coordinates if you want to achieve fancy
        effects.

        .. warning::

            The default values just mentioned can be negative. Depending
            on the image and label providers, the coordinates are flipped
            vertically because of the order in which the image is internally
            stored. Instead of flipping the image data, we are just flipping
            the texture coordinates to be faster.

        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001FD792B7C00>'


# variables with complex values

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'Instruction',
    'InstructionGroup',
    'ContextInstruction',
    'VertexInstruction',
    'Canvas',
    'CanvasBase',
    'RenderContext',
    'Callback',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FD78FD49D0>'

__pyx_capi__ = {
    'getActiveCanvas': None, # (!) real value is '<capsule object "struct __pyx_obj_4kivy_8graphics_12instructions_CanvasBase *(void)" at 0x000001FD79087090>'
    'getActiveContext': None, # (!) real value is '<capsule object "struct __pyx_obj_4kivy_8graphics_12instructions_RenderContext *(void)" at 0x000001FD790870C0>'
    'reset_gl_context': None, # (!) real value is '<capsule object "void (void)" at 0x000001FD79087000>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.instructions', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001FD78FD49D0>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\instructions.cp311-win_amd64.pyd')"

__test__ = {}

