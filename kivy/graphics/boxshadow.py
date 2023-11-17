# encoding: utf-8
# module kivy.graphics.boxshadow
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\boxshadow.cp311-win_amd64.pyd
# by generator 1.147
"""
BoxShadow
=========

.. versionadded:: 2.2.0


BoxShadow is a graphical instruction used to add a shadow effect to an element.

Its behavior is similar to the concept of a CSS3 box-shadow.

.. image:: images/boxshadow.png
    :align: center

The BoxShadow declaration must occur inside a :class:`~kivy.graphics.instructions.Canvas` statement. It works
similarly to other graphical instructions such as :class:`~kivy.graphics.vertex_instructions.Rectangle`,
:class:`~kivy.graphics.vertex_instructions.RoundedRectangle`, etc.

.. note::

    Although the ``BoxShadow`` graphical instruction has a visually similar behavior to box-shadow (CSS), the hierarchy
    of the drawing layer of ``BoxShadow`` in relation to the target element must be defined following the same layer
    hierarchy rules as when declaring other canvas instructions.
    
    |

    For more details, refer to the :attr:`~kivy.graphics.boxshadow.BoxShadow.inset` mode.

.. _example:

Example:
--------

    .. image:: images/boxshadow_demo.gif
        :align: center

    .. code-block:: kv

        <MyWidget>:
            Button:
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                size_hint: None, None
                size: 200, 150
                background_down: self.background_normal
                canvas.before:
                    Color:
                        rgba: 0, 0, 1, 0.85
                    BoxShadow:
                        pos: self.pos
                        size: self.size
                        offset: 0, -10
                        spread_radius: -20, -20
                        border_radius: 10, 10, 10, 10
                        blur_radius: 80 if self.state == "normal" else 50
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from kivy.graphics.gl_instructions import ClearBuffers, ClearColor

from kivy.graphics.vertex_instructions import Rectangle, RoundedRectangle

import kivy.graphics.fbo as __kivy_graphics_fbo


# functions

def __pyx_unpickle_BoxShadow(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_BoxShadow(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class BoxShadow(__kivy_graphics_fbo.Fbo):
    """
    BoxShadow(*args, **kwargs)
    A box shadow effect.
    
        .. versionadded:: 2.2.0
    
        :Parameters:
    
            `inset`: bool, defaults to ``False``.
                Defines whether the shadow is drawn from the inside out or from the
                outline to the inside of the ``BoxShadow`` instruction.
            `size`: list | tuple, defaults to ``(100.0, 100.0)``.
                Define the raw size of the shadow, that is, you should not take into account
                changes in the value of :attr:`blur_radius` and :attr:`spread_radius`
                properties when setting this parameter.
            `pos`: list | tuple, defaults to ``(0.0, 0.0)``.
                Define the raw position of the shadow, that is, you should not take into account
                changes in the value of the :attr:`offset` property when setting this parameter.
            `offset`: list | tuple, defaults to ``(0.0, 0.0)``.
                Specifies shadow offsets in `(horizontal, vertical)` format. 
                Positive values for the offset indicate that the shadow should move to the right and/or top.
                The negative ones indicate that the shadow should move to the left and/or down.
            `blur_radius`: float, defaults to ``15.0``.
                Define the shadow blur radius. Controls shadow expansion and softness.
            `spread_radius`: list | tuple, defaults to ``(0.0, 0.0)``.
                Define the shrink/expansion of the shadow.
            `border_radius`: list | tuple, defaults to ``(0.0, 0.0, 0.0, 0.0)``.
                Specifies the radii used for the rounded corners clockwise:
                top-left, top-right, bottom-right, bottom-left.
    """
    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ BoxShadow.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ BoxShadow.__setstate_cython__(self, __pyx_state) """
        pass

    blur_radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Define the shadow blur radius. Controls shadow expansion and softness.

        Defaults to ``15.0``.

        In the images below, the start and end positions of the shadow blur
        effect length are indicated.
        The transition between color and transparency is seamless, and although
        the shadow appears to end before before the dotted rectangle, its end
        is made to be as smooth as possible.

        - :attr:`inset` **OFF**:
            .. image:: images/boxshadow_blur_radius.svg
                :align: center
        
        | 

        - :attr:`inset` **ON**:
            .. image:: images/boxshadow_blur_radius_inset.svg
                :align: center
        
        | 

        .. note::
            In some cases (**if this is not your intention**), placing an element
            above the shadow (before the blur radius ends) will result in a unwanted
            cropping/overlay behavior rather than continuity, breaking the
            shadow's soft ending, as shown in the image below.

            | 

            .. image:: images/boxshadow_common_mistake_1.svg
                :align: center

        """

    border_radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies the radii used for the rounded corners clockwise:
        top-left, top-right, bottom-right, bottom-left.

        Defaults to ``(0.0, 0.0, 0.0, 0.0)``.

        - :attr:`inset` **OFF**:
            .. image:: images/boxshadow_border_radius.svg
                :align: center
        
        | 

        - :attr:`inset` **ON**:
            .. image:: images/boxshadow_border_radius_inset.svg
                :align: center

        """

    inset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Defines whether the shadow is drawn from the inside out or from the outline to the inside of the ``BoxShadow`` instruction.

        Defaults to ``False``.

        .. note::
            | 

            Although the inset mode determines the drawing behavior of the shadow, the position of the ``BoxShadow``
            instruction in the ``canvas`` hierarchy depends on the other graphic instructions present in the
            :class:`~kivy.graphics.instructions.Canvas` instruction tree.

            | 

            In other words, if the **target** is in the ``canvas`` layer and you want to use the default ``inset = False``
            mode to create an elevation effect, you must declare the ``BoxShadow`` instruction in ``canvas.before`` layer.

            | 

            .. image:: images/boxshadow_example_1.png
                :align: center
                :width: 300px

            .. code-block:: kv

                <MyWidget@Widget>:
                    size_hint: None, None
                    size: 100, 100
                    pos: 100, 100

                    canvas.before:
                        # BoxShadow statements
                        Color:
                            rgba: 0, 0, 0, 0.65
                        BoxShadow:
                            pos: self.pos
                            size: self.size
                            offset: 0, -10
                            blur_radius: 25
                            spread_radius: -10, -10
                            border_radius: 10, 10, 10, 10
                    
                    canvas:
                        # target element statements
                        Color:
                            rgba: 1, 1, 1, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
            
            | 

            Or, if the target is in the ``canvas`` layer and you want to use the ``inset = True`` mode to create an
            insertion effect, you must declare the ``BoxShadow`` instruction in the ``canvas`` layer, immediately after
            the **target** ``canvas`` declaration, or declare it in ``canvas.after``.

            | 

            .. image:: images/boxshadow_example_2.png
                :align: center
                :width: 300px

            .. code-block:: kv

                <MyWidget@Widget>:
                    size_hint: None, None
                    size: 100, 100
                    pos: 100, 100

                    canvas:
                        # target element statements
                        Color:
                            rgba: 1, 1, 1, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size

                        # BoxShadow statements
                        Color:
                            rgba: 0, 0, 0, 0.65
                        BoxShadow:
                            inset: True
                            pos: self.pos
                            size: self.size
                            offset: 0, -10
                            blur_radius: 25
                            spread_radius: -10, -10
                            border_radius: 10, 10, 10, 10

            | 

            **In summary:**

                - Elevation effect - ``inset = False``: the ``BoxShadow`` instruction needs to be drawn **before** the target element.

                - Insertion effect - ``inset = True``: the ``BoxShadow`` instruction needs to be drawn **after** the target element.

            | 

            In general, ``BoxShadow`` is more flexible than box-shadow (CSS) because the ``inset = False`` and
            ``inset = True`` modes do not limit the drawing of the shadow below and above the target element,
            respectively. Actually, you can define any hierarchy you want in the :class:`~kivy.graphics.instructions.Canvas`
            declaration tree, to create more complex effects that go beyond common shadow effects.

        **Modes:**

            - ``False`` (default) - The shadow is drawn inside out the ``BoxShadow`` instruction, creating a raised effect.
            
            - ``True`` - The shadow is drawn from the outline to the inside of the ``BoxShadow`` instruction, creating a inset effect.

        .. image:: images/boxshadow_inset.svg
            :align: center

        """

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies shadow offsets in `[horizontal, vertical]` format. 
        Positive values for the offset indicate that the shadow should move to
        the right and/or top.
        The negative ones indicate that the shadow should move to the left
        and/or down.

        Defaults to ``(0.0, 0.0)``.

        For this property to work as expected, it is indicated that the value
        of :attr:`pos` coincides with the position of the target element of the
        shadow, as in the example below:

        - :attr:`inset` **OFF**:
            .. image:: images/boxshadow_offset.svg
                :align: center
        
        | 

        - :attr:`inset` **ON**:
            .. image:: images/boxshadow_offset_inset.svg
                :align: center

        """

    pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Define the raw position of the shadow, that is, you should not take
        into account changes in the value of the :attr:`offset` property when
        setting this property.

        - :attr:`inset` **OFF**:
            Returns the adjusted position of the shadow according to the
            adjusted :attr:`size` of the shadow and :attr:`offset` property.

        - :attr:`inset` **ON**:
            Returns the raw position (the same as specified).

        Defaults to ``(0.0, 0.0)``.

        .. note::

            It is recommended that this property matches the raw position of
            the shadow target element. To manipulate horizontal and vertical
            offset, use :attr:`offset` instead.

        """

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Define the raw size of the shadow, that is, you should not take into
        account changes in the value of :attr:`blur_radius` and :attr:`spread_radius` properties.

        - :attr:`inset` **OFF**:
            Returns the adjusted size of the shadow according to the
            :attr:`blur_radius` and :attr:`spread_radius` properties.

        - :attr:`inset` **ON**:
            Returns the raw size (the same as specified).

        Defaults to ``(100.0, 100.0)``.

        .. note::

            It is recommended that this property matches the raw size of
            the shadow target element. To control the shrink/expansion of
            the shadow's raw :attr:`size`, use :attr:`spread_radius` instead.

        """

    spread_radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Define the shrink/expansion of the shadow in `[horizontal, vertical]` format.

        Defaults to ``(0.0, 0.0)``.

        This property is especially useful for cases where you want to achieve
        a softer shadow around the element, by setting negative values for
        :attr:`spread_radius` and a larger value for :attr:`blur_radius` as
        in the :ref:`example <example>`.

        - :attr:`inset` **OFF**:
            In the image below, the target element has a raw size of ``200 x 150px``.
            Positive changes to the :attr:`spread_radius` values will cause the raw
            :attr:`size` of the shadow to increase, while negative values will cause
            the shadow to shrink.

            .. image:: images/boxshadow_spread_radius.svg
                :align: center

        | 

        - :attr:`inset` **ON**:
            Positive values will cause the shadow to grow into the bounding box,
            while negative values will cause the shadow to shrink.

            .. image:: images/boxshadow_spread_radius_inset.svg
                :align: center

        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000019CAA19B0C0>'


# variables with complex values

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'BoxShadow',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019CAA1DC7D0>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.boxshadow', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000019CAA1DC7D0>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\boxshadow.cp311-win_amd64.pyd')"

__test__ = {}

