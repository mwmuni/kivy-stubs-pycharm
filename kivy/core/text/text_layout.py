# encoding: utf-8
# module kivy.core.text.text_layout
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\core\text\text_layout.cp311-win_amd64.pyd
# by generator 1.147
"""
Text layout
============

An internal module for laying out text according to options and constraints.
This is not part of the API and may change at any time.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def layout_text(text, list_lines, tuple_size, tuple_text_size, dict_options, get_extents, int_append_down, int_complete): # real signature unknown; restored from __doc__
    """
    layout_text(text, list lines, tuple size, tuple text_size, dict options, get_extents, int append_down, int complete)
     Lays out text into a series of :class:`LayoutWord` and
        :class:`LayoutLine` instances according to the options specified.
    
        The function is designed to be called many times, each time new text is
        appended to the last line (or first line if appending upwards), unless a
        newline is present in the text. Each text appended is described by its own
        options which can change between successive calls. If the text is
        constrained, we stop as soon as the constraint is reached.
    
        :Parameters:
            `text`: string or bytes
                the text to be broken down into lines. If lines is not empty,
                the text is added to the last line (or first line if `append_down`
                is False) until a newline is reached which creates a new line in
                `lines`. See :class:`LayoutLine`.
            `lines`: list
                a list of :class:`LayoutLine` instances, each describing a line of
                the text. Calls to :func:`layout_text` append or create
                new :class:`LayoutLine` instances in `lines`.
            `size`: 2-tuple of ints
                the size of the laid out text so far. Upon first call it should
                probably be (0, 0), afterwards it should be the (w, h) returned
                by this function in a previous call. When size reaches the
                constraining size, `text_size`, we stop adding lines and return
                True for the clipped parameter. size includes the x and y padding.
            `text_size`: 2-tuple of ints or None.
                the size constraint on the laid out text. If either element is
                None, the text is not constrained in that dimension. For example,
                (None, 200) will constrain the height, including padding to 200,
                while the width is unconstrained. The first line, and the first
                character of a line is always returned, even if it exceeds the
                constraint. The value be changed between different calls.
            `options`: dict
                the label options of this `text`. The options are saved with each
                word allowing different words to have different options from
                successive calls.
    
                Note, `options` must include a `space_width` key with a value
                indicating the width of a space for that set of options.
            `get_extents`: callable
                a function called with a string, which returns a tuple containing
                the width, height of the string.
            `append_down`: bool
                Whether successive calls to the function appends lines before or
                after the existing lines. If True, they are appended to the last
                line and below it. If False, it's appended at the first line and
                above. For example, if False, everything after the last
                newline in `text` is appended to the first line in lines.
                Everything before the last newline is inserted at the start of
                lines in same order as text; that is we do not invert the line
                order.
    
                This allows laying out from top to bottom until the constrained is
                reached, or from bottom to top until the constrained is reached.
            `complete`: bool
                whether this text complete lines. It use is that normally is
                strip in `options` is True, all leading and trailing spaces
                are removed from each line except from the last line (or first
                line if `append_down` is False) which only removes leading spaces.
                That's because further text can still be appended to the last line
                so we cannot strip them. If `complete` is True, it indicates no
                further text is coming and all lines will be stripped.
    
                The function can also be called with `text` set to the empty string
                and `complete` set to True in order for the last (first) line to
                be stripped.
    
        :returns:
            3-tuple, (w, h, clipped).
            w and h is the width and height of the text in lines so far and
            includes padding. This can be larger than `text_size`, e.g. if not even
            a single fitted, the first line would still be returned.
            `clipped` is True if not all the text has been added to lines because
            w, h reached the constrained size.
    
        Following is a simple example with no padding and no stripping::
    
            >>> from kivy.core.text import Label
            >>> from kivy.core.text.text_layout import layout_text
    
            >>> l = Label()
            >>> lines = []
            >>> # layout text with width constraint by 50, but no height constraint
            >>> w, h, clipped = layout_text('heres some text\nah, another line',
            ... lines, (0, 0), (50, None), l.options, l.get_cached_extents(), True,
            ... False)
            >>> w, h, clipped
            (46, 90, False)
            # now add text from bottom up, and constrain width only be 100
            >>> w, h, clipped = layout_text('\nyay, more text\n', lines, (w, h),
            ... (100, None), l.options, l.get_cached_extents(), False, True)
            >>> w, h, clipped
            (77, 120, 0)
            >>> for line in lines:
            ...     print('line w: {}, line h: {}'.format(line.w, line.h))
            ...     for word in line.words:
            ...         print('w: {}, h: {}, text: {}'.format(word.lw, word.lh,
            ...         [word.text]))
            line w: 0, line h: 15
            line w: 77, line h: 15
            w: 77, h: 15, text: ['yay, more text']
            line w: 31, line h: 15
            w: 31, h: 15, text: ['heres']
            line w: 34, line h: 15
            w: 34, h: 15, text: [' some']
            line w: 24, line h: 15
            w: 24, h: 15, text: [' text']
            line w: 17, line h: 15
            w: 17, h: 15, text: ['ah,']
            line w: 46, line h: 15
            w: 46, h: 15, text: [' another']
            line w: 23, line h: 15
            w: 23, h: 15, text: [' line']
    """
    pass

# classes

class LayoutLine(object):
    """
    Formally describes a line of text. A line of text is composed of many
        :class:`LayoutWord` instances, each with it's own text, size and options.
    
        A :class:`LayoutLine` instance does not always imply that the words
        contained in the line ended with a newline. That is only the case if
        :attr:`is_last_line` is True. For example a single real line of text can
        be split across multiple :class:`LayoutLine` instances if the whole line
        doesn't fit in the constrained width.
    
        :Parameters:
            `x`: int
                the location in a texture from where the left side of this line is
                began drawn.
            `y`: int
                the location in a texture from where the bottom of this line is
                drawn.
            `w`: int
                the width of the line. This is the sum of the individual widths
                of its :class:`LayoutWord` instances. Does not include any padding.
            `h`: int
                the height of the line. This is the maximum of the individual
                heights of its :class:`LayoutWord` instances multiplied by the
                `line_height` of these instance. So this is larger then the word
                height.
            `is_last_line`: bool
                whether this line was the last line in a paragraph. When True, it
                implies that the line was followed by a newline. Newlines should
                not be included in the text of words, but is implicit by setting
                this to True.
            `line_wrap`: bool
                whether this line is continued from a previous line which didn't
                fit into a constrained width and was therefore split across
                multiple :class:`LayoutLine` instances. `line_wrap` can be True
                or False independently of `is_last_line`.
            `words`: python list
                a list that contains only :class:`LayoutWord` instances describing
                the text of the line.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ LayoutLine.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ LayoutLine.__setstate_cython__(self, __pyx_state) """
        pass

    h = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """h: 'int'"""

    is_last_line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """is_last_line: 'int'"""

    line_wrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """line_wrap: 'int'"""

    w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """w: 'int'"""

    words = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """words: list"""

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """x: 'int'"""

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """y: 'int'"""



class LayoutWord(object):
    """
    Formally describes a word contained in a line. The name word simply
        means a chunk of text and can be used to describe any text.
    
        A word has some width, height and is rendered according to options saved
        in :attr:`options`. See :class:`LayoutLine` for its usage.
    
        :Parameters:
            `options`: dict
                the label options dictionary for this word.
            `lw`: int
                the width of the text in pixels.
            `lh`: int
                the height of the text in pixels.
            `text`: string
                the text of the word.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ LayoutWord.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ LayoutWord.__setstate_cython__(self, __pyx_state) """
        pass

    lh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """lh: 'int'"""

    lw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """lw: 'int'"""

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """options: dict"""

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """text: object"""



# variables with complex values

__all__ = (
    'layout_text',
    'LayoutWord',
    'LayoutLine',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000229FABD4DD0>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.core.text.text_layout', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000229FABD4DD0>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\core\\\\text\\\\text_layout.cp311-win_amd64.pyd')"

__test__ = {
    'layout_text (line 270)': " Lays out text into a series of :class:`LayoutWord` and\n    :class:`LayoutLine` instances according to the options specified.\n\n    The function is designed to be called many times, each time new text is\n    appended to the last line (or first line if appending upwards), unless a\n    newline is present in the text. Each text appended is described by its own\n    options which can change between successive calls. If the text is\n    constrained, we stop as soon as the constraint is reached.\n\n    :Parameters:\n        `text`: string or bytes\n            the text to be broken down into lines. If lines is not empty,\n            the text is added to the last line (or first line if `append_down`\n            is False) until a newline is reached which creates a new line in\n            `lines`. See :class:`LayoutLine`.\n        `lines`: list\n            a list of :class:`LayoutLine` instances, each describing a line of\n            the text. Calls to :func:`layout_text` append or create\n            new :class:`LayoutLine` instances in `lines`.\n        `size`: 2-tuple of ints\n            the size of the laid out text so far. Upon first call it should\n            probably be (0, 0), afterwards it should be the (w, h) returned\n            by this function in a previous call. When size reaches the\n            constraining size, `text_size`, we stop adding lines and return\n            True for the clipped parameter. size includes the x and y padding.\n        `text_size`: 2-tuple of ints or None.\n            the size constraint on the laid out text. If either element is\n            None, the text is not constrained in that dimension. For example,\n            (None, 200) will constrain the height, including padding to 200,\n            while the width is unconstrained. The first line, and the first\n            character of a line is always returned, even if it exceeds the\n            constraint. The value be changed between different calls.\n        `options`: dict\n            the label options of this `text`. The options are saved with each\n            word allowing different words to have different options from\n            successive calls.\n\n            Note, `options` must include a `space_width` key with a value\n            indicating the width of a space for that set of options.\n        `get_extents`: callable\n            a function called with a string, which returns a tuple containing\n            the width, height of the string.\n        `append_down`: bool\n            Whether successive calls to the function appends lines before or\n            after the existing lines. If True, they are appended to the last\n            line and below it. If False, it's appended at the first line and\n            above. For example, if False, everything after the last\n            newline in `text` is appended to the first line in lines.\n            Everything before the last newline is inserted at the start of\n            lines in same order as text; that is we do not invert the line\n            order.\n\n            This allows laying out from top to bottom until the constrained is\n            reached, or from bottom to top until the constrained is reached.\n        `complete`: bool\n            whether this text complete lines. It use is that normally is\n            strip in `options` is True, all leading and trailing spaces\n            are removed from each line except from the last line (or first\n            line if `append_down` is False) which only removes leading spaces.\n            That's because further text can still be appended to the last line\n            so we cannot strip them. If `complete` is True, it indicates no\n            further text is coming and all lines will be stripped.\n\n            The function can also be called with `text` set to the empty string\n            and `complete` set to True in order for the last (first) line to\n            be stripped.\n\n    :returns:\n        3-tuple, (w, h, clipped).\n        w and h is the width and height of the text in lines so far and\n        includes padding. This can be larger than `text_size`, e.g. if not even\n        a single fitted, the first line would still be returned.\n        `clipped` is True if not all the text has been added to lines because\n        w, h reached the constrained size.\n\n    Following is a simple example with no padding and no stripping::\n\n        >>> from kivy.core.text import Label\n        >>> from kivy.core.text.text_layout import layout_text\n\n        >>> l = Label()\n        >>> lines = []\n        >>> # layout text with width constraint by 50, but no height constraint\n        >>> w, h, clipped = layout_text('heres some text\\nah, another line',\n        ... lines, (0, 0), (50, None), l.options, l.get_cached_extents(), True,\n        ... False)\n        >>> w, h, clipped\n        (46, 90, False)\n        # now add text from bottom up, and constrain width only be 100\n        >>> w, h, clipped = layout_text('\\nyay, more text\\n', lines, (w, h),\n        ... (100, None), l.options, l.get_cached_extents(), False, True)\n        >>> w, h, clipped\n        (77, 120, 0)\n        >>> for line in lines:\n        ...     print('line w: {}, line h: {}'.format(line.w, line.h))\n        ...     for word in line.words:\n        ...         print('w: {}, h: {}, text: {}'.format(word.lw, word.lh,\n        ...         [word.text]))\n        line w: 0, line h: 15\n        line w: 77, line h: 15\n        w: 77, h: 15, text: ['yay, more text']\n        line w: 31, line h: 15\n        w: 31, h: 15, text: ['heres']\n        line w: 34, line h: 15\n        w: 34, h: 15, text: [' some']\n        line w: 24, line h: 15\n        w: 24, h: 15, text: [' text']\n        line w: 17, line h: 15\n        w: 17, h: 15, text: ['ah,']\n        line w: 46, line h: 15\n        w: 46, h: 15, text: [' another']\n        line w: 23, line h: 15\n        w: 23, h: 15, text: [' line']\n    ",
}

