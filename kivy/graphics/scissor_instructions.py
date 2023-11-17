# encoding: utf-8
# module kivy.graphics.scissor_instructions
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\scissor_instructions.cp311-win_amd64.pyd
# by generator 1.147
"""
Scissor Instructions
====================

.. versionadded:: 1.9.1


Scissor instructions clip your drawing area into a rectangular region.

- :class:`ScissorPush`: Begins clipping, sets the bounds of the clip space
- :class:`ScissorPop`: Ends clipping

The area provided to clip is in screenspace pixels and must be provided as
integer values not floats.

The following code will draw a circle on top of our widget while clipping
the circle so it does not expand beyond the widget borders.

.. code-block:: python

    with self.canvas.after:
        #If our widget is inside another widget that modified the coordinates
        #spacing (such as ScrollView) we will want to convert to Window coords
        x,y = self.to_window(*self.pos)
        width, height = self.size
        #We must convert from the possible float values provided by kivy
        #widgets to an integer screenspace, in python3 round returns an int so
        #the int cast will be unnecessary.
        ScissorPush(x=int(round(x)), y=int(round(y)),
            width=int(round(width)), height=int(round(height)))
        Color(rgba=(1., 0., 0., .5))
        Ellipse(size=(width*2., height*2.),
            pos=self.center)
        ScissorPop()
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import kivy.graphics.instructions as __kivy_graphics_instructions


# functions

def __pyx_unpickle_Rect(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Rect(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_ScissorPop(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ScissorPop(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_ScissorPush(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ScissorPush(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_ScissorStack(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ScissorStack(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class Rect(object):
    """
    Rect(int x, int y, int width, int height)
    Rect class used internally by ScissorStack and ScissorPush to determine
        correct clipping area.
    """
    def intersect(self, Rect_other): # real signature unknown; restored from __doc__
        """ Rect.intersect(self, Rect other) """
        pass

    def __init__(self, int_x, int_y, int_width, int_height): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Rect.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Rect.__setstate_cython__(self, __pyx_state) """
        pass


class ScissorPop(__kivy_graphics_instructions.Instruction):
    """
    Pop the scissor stack. Call after ScissorPush, once you have completed
        the drawing you wish to be clipped.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ScissorPop.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ScissorPop.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000020E29CFB330>'


class ScissorPush(__kivy_graphics_instructions.Instruction):
    """
    ScissorPush(**kwargs)
    Push the scissor stack. Provide kwargs of 'x', 'y', 'width', 'height'
        to control the area and position of the scissoring region. Defaults to
        0, 0, 100, 100
    
        Scissor works by clipping all drawing outside of a rectangle starting at
        int x, int y position and having sides of int width by int height in Window
        space coordinates
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ScissorPush.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ScissorPush.__setstate_cython__(self, __pyx_state) """
        pass

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000020E29CFB2A0>'


class ScissorStack(object):
    """
    ScissorStack()
    Class used internally to keep track of the current state of
        glScissors regions. Do not instantiate, prefer to inspect the module's
        scissor_stack.
    """
    def pop(self): # real signature unknown; restored from __doc__
        """ ScissorStack.pop(self) """
        pass

    def push(self, element): # real signature unknown; restored from __doc__
        """ ScissorStack.push(self, element) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ScissorStack.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ScissorStack.__setstate_cython__(self, __pyx_state) """
        pass

    back = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    empty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

scissor_stack = None # (!) real value is '<kivy.graphics.scissor_instructions.ScissorStack object at 0x0000020E29CFB3A0>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020E29D21350>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.scissor_instructions', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000020E29D21350>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\scissor_instructions.cp311-win_amd64.pyd')"

__test__ = {}

