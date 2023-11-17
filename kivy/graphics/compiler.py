# encoding: utf-8
# module kivy.graphics.compiler
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\compiler.cp311-win_amd64.pyd
# by generator 1.147
"""
Graphics compiler
=================

Before rendering an :class:`~kivy.graphics.instructions.InstructionGroup`, we
compile the group in order to reduce the number of instructions executed
at rendering time.

Reducing the context instructions
---------------------------------

Imagine that you have a scheme like this::

    Color(1, 1, 1)
    Rectangle(source='button.png', pos=(0, 0), size=(20, 20))
    Color(1, 1, 1)
    Rectangle(source='button.png', pos=(10, 10), size=(20, 20))
    Color(1, 1, 1)
    Rectangle(source='button.png', pos=(10, 20), size=(20, 20))

The real instructions seen by the graphics canvas would be::

    Color: change 'color' context to 1, 1, 1
    BindTexture: change 'texture0' to `button.png texture`
    Rectangle: push vertices (x1, y1...) to vbo & draw
    Color: change 'color' context to 1, 1, 1
    BindTexture: change 'texture0' to `button.png texture`
    Rectangle: push vertices (x1, y1...) to vbo & draw
    Color: change 'color' context to 1, 1, 1
    BindTexture: change 'texture0' to `button.png texture`
    Rectangle: push vertices (x1, y1...) to vbo & draw

Only the first :class:`~kivy.graphics.context_instructions.Color` and
:class:`~kivy.graphics.context_instructions.BindTexture` are useful and really
change the context. We can reduce them to::

    Color: change 'color' context to 1, 1, 1
    BindTexture: change 'texture0' to `button.png texture`
    Rectangle: push vertices (x1, y1...) to vbo & draw
    Rectangle: push vertices (x1, y1...) to vbo & draw
    Rectangle: push vertices (x1, y1...) to vbo & draw

This is what the compiler does in the first place, by flagging all the unused
instruction with GI_IGNORE flag. As soon as a Color content changes, the whole
InstructionGroup will be recompiled and a previously unused Color might be
used for the next compilation.


Note to any Kivy contributor / internal developer:

- All context instructions are checked to see if they change anything in the
  cache.
- We must ensure that a context instruction is needed for our current Canvas.
- We must ensure that we don't depend of any other canvas.
- We must reset our cache if one of our children is another instruction group
  because we don't know whether it might do weird things or not.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def __pyx_unpickle_GraphicsCompiler(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_GraphicsCompiler(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class GraphicsCompiler(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ GraphicsCompiler.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ GraphicsCompiler.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000018F0BC3BA20>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000018F0BC79690>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.compiler', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000018F0BC79690>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\compiler.cp311-win_amd64.pyd')"

__test__ = {}

