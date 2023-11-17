# encoding: utf-8
# module kivy.graphics.stencil_instructions
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\stencil_instructions.cp311-win_amd64.pyd
# by generator 1.147
"""
Stencil instructions
====================

.. versionadded:: 1.0.4

.. versionchanged:: 1.3.0
    The stencil operation has been updated to resolve some issues that appeared
    when nested. You **must** now have a StencilUnUse and repeat the same
    operation as you did after StencilPush.

Stencil instructions permit you to draw and use the current drawing as a mask.
They don't give as much control as pure OpenGL, but you can still do fancy
things!

The stencil buffer can be controlled using these 3 instructions:

    - :class:`StencilPush`: push a new stencil layer.
      Any drawing that happens after this will be used as a mask.
    - :class:`StencilUse` : now draw the next instructions and use the stencil
      for masking them.
    - :class:`StencilUnUse` : stop using the stencil i.e. remove the mask and
      draw normally.
    - :class:`StencilPop` : pop the current stencil layer.


You should always respect this scheme:

.. code-block:: kv

    StencilPush

    # PHASE 1: put any drawing instructions to use as a mask here.

    StencilUse

    # PHASE 2: all the drawing here will be automatically clipped by the
    # mask created in PHASE 1.

    StencilUnUse

    # PHASE 3: put the same drawing instruction here as you did in PHASE 1

    StencilPop

    # PHASE 4: the stencil is now removed from the stack and unloaded.


Limitations
-----------

- Drawing in PHASE 1 and PHASE 3 must not collide or you
  will get unexpected results
- The stencil is activated as soon as you perform a StencilPush
- The stencil is deactivated as soon as you've correctly popped all the stencil
  layers
- You must not play with stencils yourself between a StencilPush / StencilPop
- You can push another stencil after a StencilUse / before the StencilPop
- You can push up to 128 layers of stencils (8 for kivy < 1.3.0)


Example of stencil usage
------------------------

Here is an example, in kv style::

    StencilPush

    # create a rectangular mask with a pos of (100, 100) and a (100, 100) size.
    Rectangle:
        pos: 100, 100
        size: 100, 100

    StencilUse

    # we want to show a big green rectangle, however, the previous stencil
    # mask will crop us :)
    Color:
        rgb: 0, 1, 0
    Rectangle:
        size: 900, 900

    StencilUnUse

    # you must redraw the stencil mask to remove it
    Rectangle:
        pos: 100, 100
        size: 100, 100

    StencilPop
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # C:\Users\matthew.muller\AppData\Local\Programs\Python\Python311\Lib\os.py
import kivy.graphics.instructions as __kivy_graphics_instructions


# Variables with simple values

PY2 = False

# functions

def __pyx_unpickle_StencilPop(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_StencilPop(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_StencilPush(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_StencilPush(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_StencilUnUse(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_StencilUnUse(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_StencilUse(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_StencilUse(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class StencilPop(__kivy_graphics_instructions.Instruction):
    """ Pop the stencil stack. See the module documentation for more information. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ StencilPop.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ StencilPop.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000024B1BC78450>'


class StencilPush(__kivy_graphics_instructions.Instruction):
    """
    Push the stencil stack. See the module documentation for more
        information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ StencilPush.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ StencilPush.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000024B1BC78420>'


class StencilUnUse(__kivy_graphics_instructions.Instruction):
    """ Use current stencil buffer to unset the mask. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ StencilUnUse.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ StencilUnUse.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000024B1BC784B0>'


class StencilUse(__kivy_graphics_instructions.Instruction):
    """
    StencilUse(**kwargs)
    Use current stencil buffer as a mask. Check the module documentation for
        more information.
    """
    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ StencilUse.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ StencilUse.__setstate_cython__(self, __pyx_state) """
        pass

    func_op = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine the stencil operation to use for glStencilFunc(). Can be
        one of 'never', 'less', 'equal', 'lequal', 'greater', 'notequal',
        'gequal' or 'always'.

        By default, the operator is set to 'equal'.

        .. versionadded:: 1.5.0
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000024B1BC78480>'


# variables with complex values

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'StencilPush',
    'StencilPop',
    'StencilUse',
    'StencilUnUse',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024B1BC82010>'

__pyx_capi__ = {
    'get_stencil_state': None, # (!) real value is '<capsule object "PyObject *(void)" at 0x0000024B1BC78360>'
    'reset_stencil_state': None, # (!) real value is '<capsule object "void (void)" at 0x0000024B1BC78270>'
    'restore_stencil_state': None, # (!) real value is '<capsule object "void (PyObject *)" at 0x0000024B1BC78390>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.stencil_instructions', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024B1BC82010>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\stencil_instructions.cp311-win_amd64.pyd')"

__test__ = {}

