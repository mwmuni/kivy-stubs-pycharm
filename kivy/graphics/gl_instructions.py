# encoding: utf-8
# module kivy.graphics.gl_instructions
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\gl_instructions.cp311-win_amd64.pyd
# by generator 1.147
"""
GL instructions
===============

.. versionadded:: 1.3.0

Clearing an FBO
---------------

To clear an FBO, you can use :class:`ClearColor` and :class:`ClearBuffers`
instructions like this example::

    self.fbo = Fbo(size=self.size)
    with self.fbo:
        ClearColor(0, 0, 0, 0)
        ClearBuffers()
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import kivy.graphics.instructions as __kivy_graphics_instructions


# functions

def __pyx_unpickle_ClearBuffers(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ClearBuffers(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_ClearColor(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ClearColor(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class ClearBuffers(__kivy_graphics_instructions.Instruction):
    """
    ClearBuffers(*args, **kwargs)
     Clearbuffer Graphics Instruction.
    
        .. versionadded:: 1.3.0
    
        Clear the buffers specified by the instructions buffer mask property.
        By default, only the coloc buffer is cleared.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ClearBuffers.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ClearBuffers.__setstate_cython__(self, __pyx_state) """
        pass

    clear_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If True, the color buffer will be cleared.
        """

    clear_depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If True, the depth buffer will be cleared.
        """

    clear_stencil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If True, the stencil buffer will be cleared.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000023707BCB150>'


class ClearColor(__kivy_graphics_instructions.Instruction):
    """
    ClearColor(r, g, b, a, **kwargs)
     ClearColor Graphics Instruction.
    
        .. versionadded:: 1.3.0
    
        Sets the clear color used to clear buffers with the glClear function or
        :class:`ClearBuffers` graphics instructions.
    """
    def __init__(self, r, g, b, a, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ClearColor.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ClearColor.__setstate_cython__(self, __pyx_state) """
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

    r = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Red component, between 0 and 1.
        """

    rgb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """RGB color, a list of 3 values in 0-1 range where alpha will be 1.
        """

    rgba = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """RGBA color used for the clear color, a list of 4 values in the 0-1
        range.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000023707BCB120>'


# variables with complex values

__all__ = (
    'ClearColor',
    'ClearBuffers',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023707A2FB90>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.gl_instructions', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023707A2FB90>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\gl_instructions.cp311-win_amd64.pyd')"

__test__ = {}

