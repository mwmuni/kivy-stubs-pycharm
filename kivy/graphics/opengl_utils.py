# encoding: utf-8
# module kivy.graphics.opengl_utils
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\opengl_utils.cp311-win_amd64.pyd
# by generator 1.147
"""
OpenGL utilities
================

.. versionadded:: 1.0.7
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

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

def gl_get_extensions(): # real signature unknown; restored from __doc__
    """
    gl_get_extensions() -> list
    Return a list of OpenGL extensions available. All the names in the list
        have the `GL_` stripped at the start (if it exists) and are in lowercase.
    
        >>> print(gl_get_extensions())
        ['arb_blend_func_extended', 'arb_color_buffer_float', 'arb_compatibility',
         'arb_copy_buffer'... ]
    """
    return []

def gl_get_texture_formats(): # real signature unknown; restored from __doc__
    """
    gl_get_texture_formats() -> tuple
    Return a list of texture formats recognized by kivy.
        The texture list is informative but might not been supported by your
        hardware. If you want a list of supported textures, you must filter that
        list as follows::
    
            supported_fmts = [gl_has_texture_format(x) for x in gl_get_texture_formats()]
    """
    return ()

def gl_get_version(): # real signature unknown; restored from __doc__
    """
    gl_get_version() -> tuple
    Return the (major, minor) OpenGL version, parsed from the GL_VERSION.
    
        .. versionadded:: 1.2.0
    """
    return ()

def gl_get_version_major(): # real signature unknown; restored from __doc__
    """
    gl_get_version_major() -> int
    Return the major component of the OpenGL version.
    
        .. versionadded:: 1.2.0
    """
    return 0

def gl_get_version_minor(): # real signature unknown; restored from __doc__
    """
    gl_get_version_minor() -> int
    Return the minor component of the OpenGL version.
    
        .. versionadded:: 1.2.0
    """
    return 0

def gl_has_capability(int_cap): # real signature unknown; restored from __doc__
    """
    gl_has_capability(int cap) -> int
    Return the status of a OpenGL Capability. This is a wrapper that
        auto-discovers all the capabilities that Kivy might need. The current
        capabilities tested are:
    
            - GLCAP_BGRA: Test the support of BGRA texture format
            - GLCAP_NPOT: Test the support of Non Power of Two texture
            - GLCAP_S3TC: Test the support of S3TC texture (DXT1, DXT3, DXT5)
            - GLCAP_DXT1: Test the support of DXT texture (subset of S3TC)
            - GLCAP_ETC1: Test the support of ETC1 texture
    """
    return 0

def gl_has_extension(name): # real signature unknown; restored from __doc__
    """
    gl_has_extension(name) -> int
    Check if an OpenGL extension is available. If the name starts with `GL_`,
        it will be stripped for the test and converted to lowercase.
    
            >>> gl_has_extension('NV_get_tex_image')
            False
            >>> gl_has_extension('OES_texture_npot')
            True
    """
    return 0

def gl_has_texture_conversion(fmt): # real signature unknown; restored from __doc__
    """
    gl_has_texture_conversion(fmt) -> int
    Return 1 if the texture can be converted to a native format.
    """
    return 0

def gl_has_texture_format(fmt): # real signature unknown; restored from __doc__
    """
    gl_has_texture_format(fmt) -> int
    Return whether a texture format is supported by your system, natively or
        by conversion. For example, if your card doesn't support 'bgra', we are able
        to convert to 'rgba' but only in software mode.
    """
    return 0

def gl_has_texture_native_format(fmt): # real signature unknown; restored from __doc__
    """
    gl_has_texture_native_format(fmt) -> int
    Return 1 if the texture format is handled natively.
    
        >>> gl_has_texture_format('azdmok')
        0
        >>> gl_has_texture_format('rgba')
        1
        >>> gl_has_texture_format('s3tc_dxt1')
        [INFO   ] [GL          ] S3TC texture support is available
        [INFO   ] [GL          ] DXT1 texture support is available
        1
    """
    return 0

def gl_register_get_size(int_constid, int_size): # real signature unknown; restored from __doc__
    """
    gl_register_get_size(int constid, int size)
    Register an association between an OpenGL Const used in glGet* to a number
        of elements.
    
        By example, the GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX is a special pname that
        will return the integer 1 (nvidia only).
    
            >>> GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX = 0x9047
            >>> gl_register_get_size(GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX, 1)
            >>> glGetIntegerv(GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX)[0]
            524288
    """
    pass

# no classes
# variables with complex values

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

_GL_GET_SIZE = {
    2849: 1,
    2884: 1,
    2885: 1,
    2886: 1,
    2928: 2,
    2929: 1,
    2930: 1,
    2931: 1,
    2932: 1,
    2960: 1,
    2961: 1,
    2962: 1,
    2963: 1,
    2964: 1,
    2965: 1,
    2966: 1,
    2967: 1,
    2968: 1,
    2978: 4,
    3024: 1,
    3042: 1,
    3088: 4,
    3089: 1,
    3106: 4,
    3107: 4,
    3317: 1,
    3333: 1,
    3379: 1,
    3386: 2,
    3408: 1,
    3410: 1,
    3411: 1,
    3412: 1,
    3413: 1,
    3414: 1,
    3415: 1,
    10752: 1,
    32773: 4,
    32777: 1,
    32823: 1,
    32824: 1,
    32873: 1,
    32936: 1,
    32937: 1,
    32938: 1,
    32939: 1,
    32968: 1,
    32969: 1,
    32970: 1,
    32971: 1,
    33170: 1,
    33901: 2,
    33902: 2,
    34016: 1,
    34024: 1,
    34068: 1,
    34076: 1,
    34466: 1,
    34467: 34466,
    34816: 1,
    34817: 1,
    34818: 1,
    34819: 1,
    34877: 1,
    34921: 1,
    34930: 1,
    34964: 1,
    34965: 1,
    35660: 1,
    35661: 1,
    35725: 1,
    35738: 1,
    35739: 1,
    36003: 1,
    36004: 1,
    36005: 1,
    36006: 1,
    36007: 1,
    36344: 36345,
    36345: 1,
    36346: 1,
    36347: 1,
    36348: 1,
    36349: 1,
}

__all__ = (
    'gl_get_extensions',
    'gl_has_extension',
    'gl_has_capability',
    'gl_register_get_size',
    'gl_has_texture_format',
    'gl_has_texture_conversion',
    'gl_has_texture_native_format',
    'gl_get_texture_formats',
    'gl_get_version',
    'gl_get_version_minor',
    'gl_get_version_major',
    'GLCAP_BGRA',
    'GLCAP_NPOT',
    'GLCAP_S3TC',
    'GLCAP_DXT1',
    'GLCAP_ETC1',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025FC3351650>'

__pyx_capi__ = {
    'gl_get_extensions': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x0000025FC3349EC0>'
    'gl_get_texture_formats': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x0000025FC3349F20>'
    'gl_get_version': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x0000025FC334A040>'
    'gl_get_version_major': None, # (!) real value is '<capsule object "int (int __pyx_skip_dispatch)" at 0x0000025FC334A070>'
    'gl_get_version_minor': None, # (!) real value is '<capsule object "int (int __pyx_skip_dispatch)" at 0x0000025FC334A0A0>'
    'gl_has_capability': None, # (!) real value is '<capsule object "int (int, int __pyx_skip_dispatch)" at 0x0000025FC3349FE0>'
    'gl_has_extension': None, # (!) real value is '<capsule object "int (PyObject *, int __pyx_skip_dispatch)" at 0x0000025FC3349EF0>'
    'gl_has_texture_conversion': None, # (!) real value is '<capsule object "int (PyObject *, int __pyx_skip_dispatch)" at 0x0000025FC3349F50>'
    'gl_has_texture_format': None, # (!) real value is '<capsule object "int (PyObject *, int __pyx_skip_dispatch)" at 0x0000025FC334A010>'
    'gl_has_texture_native_format': None, # (!) real value is '<capsule object "int (PyObject *, int __pyx_skip_dispatch)" at 0x0000025FC3349F80>'
    'gl_register_get_size': None, # (!) real value is '<capsule object "PyObject *(int, int, int __pyx_skip_dispatch)" at 0x0000025FC3349FB0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.opengl_utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025FC3351650>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\opengl_utils.cp311-win_amd64.pyd')"

__test__ = {
    'gl_get_extensions (line 36)': "Return a list of OpenGL extensions available. All the names in the list\n    have the `GL_` stripped at the start (if it exists) and are in lowercase.\n\n    >>> print(gl_get_extensions())\n    ['arb_blend_func_extended', 'arb_color_buffer_float', 'arb_compatibility',\n     'arb_copy_buffer'... ]\n\n    ",
    'gl_has_extension (line 54)': "Check if an OpenGL extension is available. If the name starts with `GL_`,\n    it will be stripped for the test and converted to lowercase.\n\n        >>> gl_has_extension('NV_get_tex_image')\n        False\n        >>> gl_has_extension('OES_texture_npot')\n        True\n\n    ",
    'gl_has_texture_native_format (line 192)': "Return 1 if the texture format is handled natively.\n\n    >>> gl_has_texture_format('azdmok')\n    0\n    >>> gl_has_texture_format('rgba')\n    1\n    >>> gl_has_texture_format('s3tc_dxt1')\n    [INFO   ] [GL          ] S3TC texture support is available\n    [INFO   ] [GL          ] DXT1 texture support is available\n    1\n\n    ",
    'gl_register_get_size (line 72)': 'Register an association between an OpenGL Const used in glGet* to a number\n    of elements.\n\n    By example, the GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX is a special pname that\n    will return the integer 1 (nvidia only).\n\n        >>> GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX = 0x9047\n        >>> gl_register_get_size(GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX, 1)\n        >>> glGetIntegerv(GPU_MEMORY_INFO_DEDICATED_VIDMEM_NVX)[0]\n        524288\n\n    ',
}

