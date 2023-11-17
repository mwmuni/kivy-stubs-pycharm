# encoding: utf-8
# module kivy.graphics.opengl
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\opengl.cp311-win_amd64.pyd
# by generator 1.147
"""
OpenGL
======

This module is a Python wrapper for OpenGL commands.

.. warning::

    Not every OpenGL command has been wrapped and because we are using the C
    binding for higher performance, and you should rather stick to the Kivy
    Graphics API. By using OpenGL commands directly, you might change
    the OpenGL context and introduce inconsistency between the Kivy state and
    the OpenGL state.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# Variables with simple values

GL_ACTIVE_ATTRIBUTES = 35721

GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 35722

GL_ACTIVE_TEXTURE = 34016
GL_ACTIVE_UNIFORMS = 35718

GL_ACTIVE_UNIFORM_MAX_LENGTH = 35719

GL_ALIASED_LINE_WIDTH_RANGE = 33902

GL_ALIASED_POINT_SIZE_RANGE = 33901

GL_ALPHA = 6406

GL_ALPHA_BITS = 3413

GL_ALWAYS = 519

GL_ARRAY_BUFFER = 34962

GL_ARRAY_BUFFER_BINDING = 34964

GL_ATTACHED_SHADERS = 35717

GL_BACK = 1029
GL_BLEND = 3042

GL_BLEND_COLOR = 32773

GL_BLEND_DST_ALPHA = 32970
GL_BLEND_DST_RGB = 32968

GL_BLEND_EQUATION = 32777

GL_BLEND_EQUATION_ALPHA = 34877
GL_BLEND_EQUATION_RGB = 32777

GL_BLEND_SRC_ALPHA = 32971
GL_BLEND_SRC_RGB = 32969

GL_BLUE_BITS = 3412

GL_BOOL = 35670

GL_BOOL_VEC2 = 35671
GL_BOOL_VEC3 = 35672
GL_BOOL_VEC4 = 35673

GL_BUFFER_SIZE = 34660
GL_BUFFER_USAGE = 34661

GL_BYTE = 5120
GL_CCW = 2305

GL_CLAMP_TO_EDGE = 33071

GL_COLOR_ATTACHMENT0 = 36064

GL_COLOR_BUFFER_BIT = 16384

GL_COLOR_CLEAR_VALUE = 3106

GL_COLOR_WRITEMASK = 3107

GL_COMPILE_STATUS = 35713

GL_COMPRESSED_TEXTURE_FORMATS = 34467

GL_CULL_FACE = 2884

GL_CULL_FACE_MODE = 2885

GL_CURRENT_PROGRAM = 35725

GL_CURRENT_VERTEX_ATTRIB = 34342

GL_CW = 2304
GL_DECR = 7683

GL_DECR_WRAP = 34056

GL_DELETE_STATUS = 35712

GL_DEPTH_ATTACHMENT = 36096
GL_DEPTH_BITS = 3414

GL_DEPTH_BUFFER_BIT = 256

GL_DEPTH_CLEAR_VALUE = 2931

GL_DEPTH_COMPONENT = 6402
GL_DEPTH_COMPONENT16 = 33189
GL_DEPTH_FUNC = 2932
GL_DEPTH_RANGE = 2928
GL_DEPTH_TEST = 2929
GL_DEPTH_WRITEMASK = 2930

GL_DITHER = 3024

GL_DONT_CARE = 4352

GL_DST_ALPHA = 772
GL_DST_COLOR = 774

GL_DYNAMIC_DRAW = 35048

GL_ELEMENT_ARRAY_BUFFER = 34963

GL_ELEMENT_ARRAY_BUFFER_BINDING = 34965

GL_EQUAL = 514
GL_EXTENSIONS = 7939
GL_FALSE = 0
GL_FASTEST = 4353
GL_FLOAT = 5126

GL_FLOAT_MAT2 = 35674
GL_FLOAT_MAT3 = 35675
GL_FLOAT_MAT4 = 35676
GL_FLOAT_VEC2 = 35664
GL_FLOAT_VEC3 = 35665
GL_FLOAT_VEC4 = 35666

GL_FRAGMENT_SHADER = 35632

GL_FRAMEBUFFER = 36160

GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 36049
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 36048

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 36051

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 36050

GL_FRAMEBUFFER_BINDING = 36006
GL_FRAMEBUFFER_COMPLETE = 36053

GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 36054
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 36057

GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 36055

GL_FRAMEBUFFER_UNSUPPORTED = 36061

GL_FRONT = 1028

GL_FRONT_AND_BACK = 1032

GL_FRONT_FACE = 2886

GL_FUNC_ADD = 32774

GL_FUNC_REVERSE_SUBTRACT = 32779

GL_FUNC_SUBTRACT = 32778

GL_GENERATE_MIPMAP_HINT = 33170

GL_GEQUAL = 518
GL_GREATER = 516

GL_GREEN_BITS = 3411

GL_INCR = 7682

GL_INCR_WRAP = 34055

GL_INFO_LOG_LENGTH = 35716

GL_INT = 5124

GL_INT_VEC2 = 35667
GL_INT_VEC3 = 35668
GL_INT_VEC4 = 35669

GL_INVALID_ENUM = 1280

GL_INVALID_FRAMEBUFFER_OPERATION = 1286

GL_INVALID_OPERATION = 1282
GL_INVALID_VALUE = 1281

GL_INVERT = 5386
GL_KEEP = 7680
GL_LEQUAL = 515
GL_LESS = 513
GL_LINEAR = 9729

GL_LINEAR_MIPMAP_LINEAR = 9987
GL_LINEAR_MIPMAP_NEAREST = 9985

GL_LINES = 1

GL_LINE_LOOP = 2
GL_LINE_STRIP = 3
GL_LINE_WIDTH = 2849

GL_LINK_STATUS = 35714

GL_LUMINANCE = 6409

GL_LUMINANCE_ALPHA = 6410

GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 35661

GL_MAX_CUBE_MAP_TEXTURE_SIZE = 34076

GL_MAX_RENDERBUFFER_SIZE = 34024

GL_MAX_TEXTURE_IMAGE_UNITS = 34930

GL_MAX_TEXTURE_SIZE = 3379

GL_MAX_VERTEX_ATTRIBS = 34921

GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 35660

GL_MAX_VIEWPORT_DIMS = 3386

GL_MIRRORED_REPEAT = 33648

GL_NEAREST = 9728

GL_NEAREST_MIPMAP_LINEAR = 9986
GL_NEAREST_MIPMAP_NEAREST = 9984

GL_NEVER = 512
GL_NICEST = 4354
GL_NONE = 0
GL_NOTEQUAL = 517

GL_NO_ERROR = 0

GL_NUM_COMPRESSED_TEXTURE_FORMATS = 34466

GL_ONE = 1

GL_ONE_MINUS_DST_ALPHA = 773
GL_ONE_MINUS_DST_COLOR = 775

GL_ONE_MINUS_SRC_ALPHA = 771
GL_ONE_MINUS_SRC_COLOR = 769

GL_OUT_OF_MEMORY = 1285

GL_PACK_ALIGNMENT = 3333

GL_POINTS = 0

GL_POLYGON_OFFSET_FACTOR = 32824
GL_POLYGON_OFFSET_FILL = 32823
GL_POLYGON_OFFSET_UNITS = 10752

GL_RED_BITS = 3410

GL_RENDERBUFFER = 36161

GL_RENDERBUFFER_ALPHA_SIZE = 36179

GL_RENDERBUFFER_BINDING = 36007

GL_RENDERBUFFER_BLUE_SIZE = 36178

GL_RENDERBUFFER_DEPTH_SIZE = 36180

GL_RENDERBUFFER_GREEN_SIZE = 36177

GL_RENDERBUFFER_HEIGHT = 36163

GL_RENDERBUFFER_INTERNAL_FORMAT = 36164

GL_RENDERBUFFER_RED_SIZE = 36176

GL_RENDERBUFFER_STENCIL_SIZE = 36181

GL_RENDERBUFFER_WIDTH = 36162

GL_RENDERER = 7937
GL_REPEAT = 10497
GL_REPLACE = 7681
GL_RGB = 6407
GL_RGB565 = 36194

GL_RGB5_A1 = 32855

GL_RGBA = 6408
GL_RGBA4 = 32854

GL_SAMPLER_2D = 35678
GL_SAMPLER_CUBE = 35680

GL_SAMPLES = 32937

GL_SAMPLE_ALPHA_TO_COVERAGE = 32926

GL_SAMPLE_BUFFERS = 32936
GL_SAMPLE_COVERAGE = 32928

GL_SAMPLE_COVERAGE_INVERT = 32939
GL_SAMPLE_COVERAGE_VALUE = 32938

GL_SCISSOR_BOX = 3088
GL_SCISSOR_TEST = 3089

GL_SHADER_BINARY_FORMATS = 36344

GL_SHADER_SOURCE_LENGTH = 35720

GL_SHADER_TYPE = 35663

GL_SHADING_LANGUAGE_VERSION = 35724

GL_SHORT = 5122

GL_SRC_ALPHA = 770

GL_SRC_ALPHA_SATURATE = 776

GL_SRC_COLOR = 768

GL_STATIC_DRAW = 35044

GL_STENCIL_ATTACHMENT = 36128

GL_STENCIL_BACK_FAIL = 34817
GL_STENCIL_BACK_FUNC = 34816

GL_STENCIL_BACK_PASS_DEPTH_FAIL = 34818
GL_STENCIL_BACK_PASS_DEPTH_PASS = 34819

GL_STENCIL_BACK_REF = 36003

GL_STENCIL_BACK_VALUE_MASK = 36004

GL_STENCIL_BACK_WRITEMASK = 36005

GL_STENCIL_BITS = 3415

GL_STENCIL_BUFFER_BIT = 1024

GL_STENCIL_CLEAR_VALUE = 2961

GL_STENCIL_FAIL = 2964
GL_STENCIL_FUNC = 2962
GL_STENCIL_INDEX8 = 36168

GL_STENCIL_PASS_DEPTH_FAIL = 2965
GL_STENCIL_PASS_DEPTH_PASS = 2966

GL_STENCIL_REF = 2967
GL_STENCIL_TEST = 2960

GL_STENCIL_VALUE_MASK = 2963

GL_STENCIL_WRITEMASK = 2968

GL_STREAM_DRAW = 35040

GL_SUBPIXEL_BITS = 3408

GL_TEXTURE = 5890
GL_TEXTURE0 = 33984
GL_TEXTURE1 = 33985
GL_TEXTURE10 = 33994
GL_TEXTURE11 = 33995
GL_TEXTURE12 = 33996
GL_TEXTURE13 = 33997
GL_TEXTURE14 = 33998
GL_TEXTURE15 = 33999
GL_TEXTURE16 = 34000
GL_TEXTURE17 = 34001
GL_TEXTURE18 = 34002
GL_TEXTURE19 = 34003
GL_TEXTURE2 = 33986
GL_TEXTURE20 = 34004
GL_TEXTURE21 = 34005
GL_TEXTURE22 = 34006
GL_TEXTURE23 = 34007
GL_TEXTURE24 = 34008
GL_TEXTURE25 = 34009
GL_TEXTURE26 = 34010
GL_TEXTURE27 = 34011
GL_TEXTURE28 = 34012
GL_TEXTURE29 = 34013
GL_TEXTURE3 = 33987
GL_TEXTURE30 = 34014
GL_TEXTURE31 = 34015
GL_TEXTURE4 = 33988
GL_TEXTURE5 = 33989
GL_TEXTURE6 = 33990
GL_TEXTURE7 = 33991
GL_TEXTURE8 = 33992
GL_TEXTURE9 = 33993

GL_TEXTURE_2D = 3553

GL_TEXTURE_BINDING_2D = 32873

GL_TEXTURE_BINDING_CUBE_MAP = 34068

GL_TEXTURE_CUBE_MAP = 34067

GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 34070
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 34072
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 34074

GL_TEXTURE_CUBE_MAP_POSITIVE_X = 34069
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 34071
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 34073

GL_TEXTURE_MAG_FILTER = 10240

GL_TEXTURE_MIN_FILTER = 10241

GL_TEXTURE_WRAP_S = 10242
GL_TEXTURE_WRAP_T = 10243

GL_TRIANGLES = 4

GL_TRIANGLE_FAN = 6
GL_TRIANGLE_STRIP = 5

GL_TRUE = 1

GL_UNPACK_ALIGNMENT = 3317

GL_UNSIGNED_BYTE = 5121
GL_UNSIGNED_INT = 5125
GL_UNSIGNED_SHORT = 5123

GL_UNSIGNED_SHORT_4_4_4_4 = 32819

GL_UNSIGNED_SHORT_5_5_5_1 = 32820

GL_UNSIGNED_SHORT_5_6_5 = 33635

GL_VALIDATE_STATUS = 35715

GL_VENDOR = 7936
GL_VERSION = 7938

GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 34975

GL_VERTEX_ATTRIB_ARRAY_ENABLED = 34338
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 34922
GL_VERTEX_ATTRIB_ARRAY_POINTER = 34373
GL_VERTEX_ATTRIB_ARRAY_SIZE = 34339
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 34340
GL_VERTEX_ATTRIB_ARRAY_TYPE = 34341

GL_VERTEX_SHADER = 35633

GL_VIEWPORT = 2978
GL_ZERO = 0

# functions

def glActiveTexture(GLenum_texture): # real signature unknown; restored from __doc__
    """
    glActiveTexture(GLenum texture)
    See: `glActiveTexture() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glActiveTexture.xml>`_
    """
    pass

def glAttachShader(GLuint_program, GLuint_shader): # real signature unknown; restored from __doc__
    """
    glAttachShader(GLuint program, GLuint shader)
    See: `glAttachShader() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glAttachShader.xml>`_
    """
    pass

def glBindAttribLocation(GLuint_program, GLuint_index, bytes_name): # real signature unknown; restored from __doc__
    """
    glBindAttribLocation(GLuint program, GLuint index, bytes name)
    See: `glBindAttribLocation() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBindAttribLocation.xml>`_
    """
    pass

def glBindBuffer(GLenum_target, GLuint_buffer): # real signature unknown; restored from __doc__
    """
    glBindBuffer(GLenum target, GLuint buffer)
    See: `glBindBuffer() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBindBuffer.xml>`_
    """
    pass

def glBindFramebuffer(GLenum_target, GLuint_framebuffer): # real signature unknown; restored from __doc__
    """
    glBindFramebuffer(GLenum target, GLuint framebuffer)
    See: `glBindFramebuffer() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBindFramebuffer.xml>`_
    """
    pass

def glBindRenderbuffer(GLenum_target, GLuint_renderbuffer): # real signature unknown; restored from __doc__
    """
    glBindRenderbuffer(GLenum target, GLuint renderbuffer)
    See: `glBindRenderbuffer() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBindRenderbuffer.xml>`_
    """
    pass

def glBindTexture(GLenum_target, GLuint_texture): # real signature unknown; restored from __doc__
    """
    glBindTexture(GLenum target, GLuint texture)
    See: `glBindTexture() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBindTexture.xml>`_
    """
    pass

def glBlendColor(GLclampf_red, GLclampf_green, GLclampf_blue, GLclampf_alpha): # real signature unknown; restored from __doc__
    """
    glBlendColor(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)
    See: `glBlendColor() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBlendColor.xml>`_
    """
    pass

def glBlendEquation(GLenum_mode): # real signature unknown; restored from __doc__
    """
    glBlendEquation(GLenum mode)
    See: `glBlendEquation() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBlendEquation.xml>`_
    """
    pass

def glBlendEquationSeparate(GLenum_modeRGB, GLenum_modeAlpha): # real signature unknown; restored from __doc__
    """
    glBlendEquationSeparate(GLenum modeRGB, GLenum modeAlpha)
    See: `glBlendEquationSeparate() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBlendEquationSeparate.xml>`_
    """
    pass

def glBlendFunc(GLenum_sfactor, GLenum_dfactor): # real signature unknown; restored from __doc__
    """
    glBlendFunc(GLenum sfactor, GLenum dfactor)
    See: `glBlendFunc() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBlendFunc.xml>`_
    """
    pass

def glBlendFuncSeparate(GLenum_srcRGB, GLenum_dstRGB, GLenum_srcAlpha, GLenum_dstAlpha): # real signature unknown; restored from __doc__
    """
    glBlendFuncSeparate(GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
    See: `glBlendFuncSeparate() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBlendFuncSeparate.xml>`_
    """
    pass

def glBufferData(GLenum_target, GLsizeiptr_size, bytes_data, GLenum_usage): # real signature unknown; restored from __doc__
    """
    glBufferData(GLenum target, GLsizeiptr size, bytes data, GLenum usage)
    See: `glBufferData() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBufferData.xml>`_
    """
    pass

def glBufferSubData(GLenum_target, GLintptr_offset, GLsizeiptr_size, bytes_data): # real signature unknown; restored from __doc__
    """
    glBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, bytes data)
    See: `glBufferSubData() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glBufferSubData.xml>`_
    """
    pass

def glCheckFramebufferStatus(GLenum_target): # real signature unknown; restored from __doc__
    """
    glCheckFramebufferStatus(GLenum target)
    See: `glCheckFramebufferStatus() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCheckFramebufferStatus.xml>`_
    """
    pass

def glClear(GLbitfield_mask): # real signature unknown; restored from __doc__
    """
    glClear(GLbitfield mask)
    See: `glClear() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glClear.xml>`_
    """
    pass

def glClearColor(GLclampf_red, GLclampf_green, GLclampf_blue, GLclampf_alpha): # real signature unknown; restored from __doc__
    """
    glClearColor(GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha)
    See: `glClearColor() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glClearColor.xml>`_
    """
    pass

def glClearStencil(GLint_s): # real signature unknown; restored from __doc__
    """
    glClearStencil(GLint s)
    See: `glClearStencil() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glClearStencil.xml>`_
    """
    pass

def glColorMask(GLboolean_red, GLboolean_green, GLboolean_blue, GLboolean_alpha): # real signature unknown; restored from __doc__
    """
    glColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha)
    See: `glColorMask() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glColorMask.xml>`_
    """
    pass

def glCompileShader(GLuint_shader): # real signature unknown; restored from __doc__
    """
    glCompileShader(GLuint shader)
    See: `glCompileShader() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCompileShader.xml>`_
    """
    pass

def glCompressedTexImage2D(GLenum_target, GLint_level, GLenum_internalformat, GLsizei_width, GLsizei_height, GLint_border, GLsizei_imageSize, bytes_data): # real signature unknown; restored from __doc__
    """
    glCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, bytes data)
    See: `glCompressedTexImage2D() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCompressedTexImage2D.xml>`_
    """
    pass

def glCompressedTexSubImage2D(GLenum_target, GLint_level, GLint_xoffset, GLint_yoffset, GLsizei_width, GLsizei_height, GLenum_format, GLsizei_imageSize, bytes_data): # real signature unknown; restored from __doc__
    """
    glCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, bytes data)
    See: `glCompressedTexSubImage2D() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCompressedTexSubImage2D.xml>`_
    """
    pass

def glCopyTexImage2D(GLenum_target, GLint_level, GLenum_internalformat, GLint_x, GLint_y, GLsizei_width, GLsizei_height, GLint_border): # real signature unknown; restored from __doc__
    """
    glCopyTexImage2D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border)
    See: `glCopyTexImage2D() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCopyTexImage2D.xml>`_
    """
    pass

def glCopyTexSubImage2D(GLenum_target, GLint_level, GLint_xoffset, GLint_yoffset, GLint_x, GLint_y, GLsizei_width, GLsizei_height): # real signature unknown; restored from __doc__
    """
    glCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
    See: `glCopyTexSubImage2D() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCopyTexSubImage2D.xml>`_
    """
    pass

def glCreateProgram(): # real signature unknown; restored from __doc__
    """
    glCreateProgram()
    See: `glCreateProgram() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCreateProgram.xml>`_
    """
    pass

def glCreateShader(GLenum_type): # real signature unknown; restored from __doc__
    """
    glCreateShader(GLenum type)
    See: `glCreateShader() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCreateShader.xml>`_
    """
    pass

def glCullFace(GLenum_mode): # real signature unknown; restored from __doc__
    """
    glCullFace(GLenum mode)
    See: `glCullFace() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glCullFace.xml>`_
    """
    pass

def glDeleteBuffers(GLsizei_n, bytes_buffers): # real signature unknown; restored from __doc__
    """
    glDeleteBuffers(GLsizei n, bytes buffers)
    See: `glDeleteBuffers() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteBuffers.xml>`_
    """
    pass

def glDeleteFramebuffers(GLsizei_n, bytes_framebuffers): # real signature unknown; restored from __doc__
    """
    glDeleteFramebuffers(GLsizei n, bytes framebuffers)
    See: `glDeleteFramebuffers() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteFramebuffers.xml>`_
    """
    pass

def glDeleteProgram(GLuint_program): # real signature unknown; restored from __doc__
    """
    glDeleteProgram(GLuint program)
    See: `glDeleteProgram() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteProgram.xml>`_
    """
    pass

def glDeleteRenderbuffers(GLsizei_n, bytes_renderbuffers): # real signature unknown; restored from __doc__
    """
    glDeleteRenderbuffers(GLsizei n, bytes renderbuffers)
    See: `glDeleteRenderbuffers() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteRenderbuffers.xml>`_
    """
    pass

def glDeleteShader(GLuint_shader): # real signature unknown; restored from __doc__
    """
    glDeleteShader(GLuint shader)
    See: `glDeleteShader() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteShader.xml>`_
    """
    pass

def glDeleteTextures(GLsizei_n, bytes_textures): # real signature unknown; restored from __doc__
    """
    glDeleteTextures(GLsizei n, bytes textures)
    See: `glDeleteTextures() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDeleteTextures.xml>`_
    """
    pass

def glDepthFunc(GLenum_func): # real signature unknown; restored from __doc__
    """
    glDepthFunc(GLenum func)
    See: `glDepthFunc() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDepthFunc.xml>`_
    """
    pass

def glDepthMask(GLboolean_flag): # real signature unknown; restored from __doc__
    """
    glDepthMask(GLboolean flag)
    See: `glDepthMask() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDepthMask.xml>`_
    """
    pass

def glDetachShader(GLuint_program, GLuint_shader): # real signature unknown; restored from __doc__
    """
    glDetachShader(GLuint program, GLuint shader)
    See: `glDetachShader() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDetachShader.xml>`_
    """
    pass

def glDisable(GLenum_cap): # real signature unknown; restored from __doc__
    """
    glDisable(GLenum cap)
    See: `glDisable() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDisable.xml>`_
    """
    pass

def glDisableVertexAttribArray(GLuint_index): # real signature unknown; restored from __doc__
    """
    glDisableVertexAttribArray(GLuint index)
    See: `glDisableVertexAttribArray() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDisableVertexAttribArray.xml>`_
    """
    pass

def glDrawArrays(GLenum_mode, GLint_first, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glDrawArrays(GLenum mode, GLint first, GLsizei count)
    See: `glDrawArrays() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDrawArrays.xml>`_
    """
    pass

def glDrawElements(GLenum_mode, GLsizei_count, GLenum_type, indices): # real signature unknown; restored from __doc__
    """
    glDrawElements(GLenum mode, GLsizei count, GLenum type, indices)
    See: `glDrawElements() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glDrawElements.xml>`_
    """
    pass

def glEnable(GLenum_cap): # real signature unknown; restored from __doc__
    """
    glEnable(GLenum cap)
    See: `glEnable() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glEnable.xml>`_
    """
    pass

def glEnableVertexAttribArray(GLuint_index): # real signature unknown; restored from __doc__
    """
    glEnableVertexAttribArray(GLuint index)
    See: `glEnableVertexAttribArray() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glEnableVertexAttribArray.xml>`_
    """
    pass

def glFinish(): # real signature unknown; restored from __doc__
    """
    glFinish()
    See: `glFinish() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glFinish.xml>`_
    """
    pass

def glFlush(): # real signature unknown; restored from __doc__
    """
    glFlush()
    See: `glFlush() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glFlush.xml>`_
    """
    pass

def glFramebufferRenderbuffer(GLenum_target, GLenum_attachment, GLenum_renderbuffertarget, GLuint_renderbuffer): # real signature unknown; restored from __doc__
    """
    glFramebufferRenderbuffer(GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
    See: `glFramebufferRenderbuffer() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glFramebufferRenderbuffer.xml>`_
    """
    pass

def glFramebufferTexture2D(GLenum_target, GLenum_attachment, GLenum_textarget, GLuint_texture, GLint_level): # real signature unknown; restored from __doc__
    """
    glFramebufferTexture2D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level)
    See: `glFramebufferTexture2D() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glFramebufferTexture2D.xml>`_
    """
    pass

def glFrontFace(GLenum_mode): # real signature unknown; restored from __doc__
    """
    glFrontFace(GLenum mode)
    See: `glFrontFace() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glFrontFace.xml>`_
    """
    pass

def glGenBuffers(GLsizei_n): # real signature unknown; restored from __doc__
    """
    glGenBuffers(GLsizei n)
    See: `glGenBuffers() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGenBuffers.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGenerateMipmap(GLenum_target): # real signature unknown; restored from __doc__
    """
    glGenerateMipmap(GLenum target)
    See: `glGenerateMipmap() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGenerateMipmap.xml>`_
    """
    pass

def glGenFramebuffers(GLsizei_n): # real signature unknown; restored from __doc__
    """
    glGenFramebuffers(GLsizei n)
    See: `glGenFramebuffers() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGenFramebuffers.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGenRenderbuffers(GLsizei_n): # real signature unknown; restored from __doc__
    """
    glGenRenderbuffers(GLsizei n)
    See: `glGenRenderbuffers() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGenRenderbuffers.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGenTextures(GLsizei_n): # real signature unknown; restored from __doc__
    """
    glGenTextures(GLsizei n)
    See: `glGenTextures() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGenTextures.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetActiveAttrib(GLuint_program, GLuint_index): # real signature unknown; restored from __doc__
    """
    glGetActiveAttrib(GLuint program, GLuint index)
    See: `glGetActiveAttrib() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetActiveAttrib.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetActiveUniform(GLuint_program, GLuint_index): # real signature unknown; restored from __doc__
    """
    glGetActiveUniform(GLuint program, GLuint index)
    See: `glGetActiveUniform() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetActiveUniform.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetAttachedShaders(GLuint_program, GLsizei_maxcount): # real signature unknown; restored from __doc__
    """
    glGetAttachedShaders(GLuint program, GLsizei maxcount)
    See: `glGetAttachedShaders() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetAttachedShaders.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetAttribLocation(GLuint_program, bytes_name): # real signature unknown; restored from __doc__
    """
    glGetAttribLocation(GLuint program, bytes name)
    See: `glGetAttribLocation() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetAttribLocation.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetBooleanv(GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetBooleanv(GLenum pname)
    See: `glGetBooleanv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetBooleanv.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetBufferParameteriv(GLenum_target, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetBufferParameteriv(GLenum target, GLenum pname)
    See: `glGetBufferParameteriv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetBufferParameteriv.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetError(): # real signature unknown; restored from __doc__
    """
    glGetError()
    See: `glGetError() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetError.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetFloatv(GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetFloatv(GLenum pname)
    See: `glGetFloatv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetFloatv.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetFramebufferAttachmentParameteriv(GLenum_target, GLenum_attachment, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetFramebufferAttachmentParameteriv(GLenum target, GLenum attachment, GLenum pname)
    See: `glGetFramebufferAttachmentParameteriv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetFramebufferAttachmentParameteriv.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetIntegerv(GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetIntegerv(GLenum pname)
    See: `glGetIntegerv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetIntegerv.xml>`_
    
        Unlike the C specification, the value(s) will be the result of the call
    """
    pass

def glGetProgramInfoLog(GLuint_program, GLsizei_bufsize): # real signature unknown; restored from __doc__
    """
    glGetProgramInfoLog(GLuint program, GLsizei bufsize)
    See: `glGetProgramInfoLog() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetProgramInfoLog.xml>`_
    
        Unlike the C specification, the source code will be returned as a string.
    """
    pass

def glGetProgramiv(GLuint_program, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetProgramiv(GLuint program, GLenum pname)
    See: `glGetProgramiv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetProgramiv.xml>`_
    
        Unlike the C specification, the value(s) will be the result of the call
    """
    pass

def glGetRenderbufferParameteriv(GLenum_target, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetRenderbufferParameteriv(GLenum target, GLenum pname)
    See: `glGetRenderbufferParameteriv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetRenderbufferParameteriv.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetShaderInfoLog(GLuint_shader, GLsizei_bufsize): # real signature unknown; restored from __doc__
    """
    glGetShaderInfoLog(GLuint shader, GLsizei bufsize)
    See: `glGetShaderInfoLog() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetShaderInfoLog.xml>`_
    
        Unlike the C specification, the source code will be returned as a string.
    """
    pass

def glGetShaderiv(GLuint_shader, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetShaderiv(GLuint shader, GLenum pname)
    See: `glGetShaderiv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetShaderiv.xml>`_
    
        Unlike the C specification, the value will be the result of call.
    """
    pass

def glGetShaderPrecisionFormat(GLenum_shadertype, GLenum_precisiontype): # real signature unknown; restored from __doc__
    """
    glGetShaderPrecisionFormat(GLenum shadertype, GLenum precisiontype)
    See: `glGetShaderPrecisionFormat() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetShaderPrecisionFormat.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glGetShaderSource(GLuint_shader): # real signature unknown; restored from __doc__
    """
    glGetShaderSource(GLuint shader)
    See: `glGetShaderSource() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetShaderSource.xml>`_
    
        Unlike the C specification, the source code will be returned as a string.
    """
    pass

def glGetString(GLenum_name): # real signature unknown; restored from __doc__
    """
    glGetString(GLenum name)
    See: `glGetString() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetString.xml>`_
    
        Unlike the C specification, the value will be returned as a string.
    """
    pass

def glGetTexParameterfv(GLenum_target, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetTexParameterfv(GLenum target, GLenum pname)
    See: `glGetTexParameterfv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetTexParameterfv.xml>`_
    """
    pass

def glGetTexParameteriv(GLenum_target, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetTexParameteriv(GLenum target, GLenum pname)
    See: `glGetTexParameteriv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetTexParameteriv.xml>`_
    """
    pass

def glGetUniformfv(GLuint_program, GLint_location): # real signature unknown; restored from __doc__
    """
    glGetUniformfv(GLuint program, GLint location)
    See: `glGetUniformfv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetUniformfv.xml>`_
    """
    pass

def glGetUniformiv(GLuint_program, GLint_location): # real signature unknown; restored from __doc__
    """
    glGetUniformiv(GLuint program, GLint location)
    See: `glGetUniformiv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetUniformiv.xml>`_
    """
    pass

def glGetUniformLocation(GLuint_program, bytes_name): # real signature unknown; restored from __doc__
    """
    glGetUniformLocation(GLuint program, bytes name)
    See: `glGetUniformLocation() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetUniformLocation.xml>`_
    """
    pass

def glGetVertexAttribfv(GLuint_index, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetVertexAttribfv(GLuint index, GLenum pname)
    See: `glGetVertexAttribfv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetVertexAttribfv.xml>`_
    """
    pass

def glGetVertexAttribiv(GLuint_index, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetVertexAttribiv(GLuint index, GLenum pname)
    See: `glGetVertexAttribiv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetVertexAttribiv.xml>`_
    """
    pass

def glGetVertexAttribPointerv(GLuint_index, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glGetVertexAttribPointerv(GLuint index, GLenum pname)
    See: `glGetVertexAttribPointerv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glGetVertexAttribPointerv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glHint(GLenum_target, GLenum_mode): # real signature unknown; restored from __doc__
    """
    glHint(GLenum target, GLenum mode)
    See: `glHint() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glHint.xml>`_
    """
    pass

def glIsBuffer(GLuint_buffer): # real signature unknown; restored from __doc__
    """
    glIsBuffer(GLuint buffer)
    See: `glIsBuffer() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsBuffer.xml>`_
    """
    pass

def glIsEnabled(GLenum_cap): # real signature unknown; restored from __doc__
    """
    glIsEnabled(GLenum cap)
    See: `glIsEnabled() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsEnabled.xml>`_
    """
    pass

def glIsFramebuffer(GLuint_framebuffer): # real signature unknown; restored from __doc__
    """
    glIsFramebuffer(GLuint framebuffer)
    See: `glIsFramebuffer() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsFramebuffer.xml>`_
    """
    pass

def glIsProgram(GLuint_program): # real signature unknown; restored from __doc__
    """
    glIsProgram(GLuint program)
    See: `glIsProgram() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsProgram.xml>`_
    """
    pass

def glIsRenderbuffer(GLuint_renderbuffer): # real signature unknown; restored from __doc__
    """
    glIsRenderbuffer(GLuint renderbuffer)
    See: `glIsRenderbuffer() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsRenderbuffer.xml>`_
    """
    pass

def glIsShader(GLuint_shader): # real signature unknown; restored from __doc__
    """
    glIsShader(GLuint shader)
    See: `glIsShader() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsShader.xml>`_
    """
    pass

def glIsTexture(GLuint_texture): # real signature unknown; restored from __doc__
    """
    glIsTexture(GLuint texture)
    See: `glIsTexture() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glIsTexture.xml>`_
    """
    pass

def glLineWidth(GLfloat_width): # real signature unknown; restored from __doc__
    """
    glLineWidth(GLfloat width)
    See: `glLineWidth() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glLineWidth.xml>`_
    """
    pass

def glLinkProgram(GLuint_program): # real signature unknown; restored from __doc__
    """
    glLinkProgram(GLuint program)
    See: `glLinkProgram() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glLinkProgram.xml>`_
    """
    pass

def glPixelStorei(GLenum_pname, GLint_param): # real signature unknown; restored from __doc__
    """
    glPixelStorei(GLenum pname, GLint param)
    See: `glPixelStorei() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glPixelStorei.xml>`_
    """
    pass

def glPolygonOffset(GLfloat_factor, GLfloat_units): # real signature unknown; restored from __doc__
    """
    glPolygonOffset(GLfloat factor, GLfloat units)
    See: `glPolygonOffset() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glPolygonOffset.xml>`_
    """
    pass

def glReadPixels(GLint_x, GLint_y, GLsizei_width, GLsizei_height, GLenum_format, GLenum_type): # real signature unknown; restored from __doc__
    """
    glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type)
    See: `glReadPixels() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glReadPixels.xml>`_
    
        We support only GL_RGB/GL_RGBA as a format and GL_UNSIGNED_BYTE as a
        type.
    """
    pass

def glReleaseShaderCompiler(): # real signature unknown; restored from __doc__
    """
    glReleaseShaderCompiler()
    See: `glReleaseShaderCompiler() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glReleaseShaderCompiler.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glRenderbufferStorage(GLenum_target, GLenum_internalformat, GLsizei_width, GLsizei_height): # real signature unknown; restored from __doc__
    """
    glRenderbufferStorage(GLenum target, GLenum internalformat, GLsizei width, GLsizei height)
    See: `glRenderbufferStorage() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glRenderbufferStorage.xml>`_
    """
    pass

def glSampleCoverage(GLclampf_value, GLboolean_invert): # real signature unknown; restored from __doc__
    """
    glSampleCoverage(GLclampf value, GLboolean invert)
    See: `glSampleCoverage() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glSampleCoverage.xml>`_
    """
    pass

def glScissor(GLint_x, GLint_y, GLsizei_width, GLsizei_height): # real signature unknown; restored from __doc__
    """
    glScissor(GLint x, GLint y, GLsizei width, GLsizei height)
    See: `glScissor() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glScissor.xml>`_
    """
    pass

def glShaderBinary(): # real signature unknown; restored from __doc__
    """
    glShaderBinary()
    See: `glShaderBinary() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glShaderBinary.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glShaderSource(GLuint_shader, bytes_source): # real signature unknown; restored from __doc__
    """
    glShaderSource(GLuint shader, bytes source)
    See: `glShaderSource() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glShaderSource.xml>`_
    """
    pass

def glStencilFunc(GLenum_func, GLint_ref, GLuint_mask): # real signature unknown; restored from __doc__
    """
    glStencilFunc(GLenum func, GLint ref, GLuint mask)
    See: `glStencilFunc() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilFunc.xml>`_
    """
    pass

def glStencilFuncSeparate(GLenum_face, GLenum_func, GLint_ref, GLuint_mask): # real signature unknown; restored from __doc__
    """
    glStencilFuncSeparate(GLenum face, GLenum func, GLint ref, GLuint mask)
    See: `glStencilFuncSeparate() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilFuncSeparate.xml>`_
    """
    pass

def glStencilMask(GLuint_mask): # real signature unknown; restored from __doc__
    """
    glStencilMask(GLuint mask)
    See: `glStencilMask() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilMask.xml>`_
    """
    pass

def glStencilMaskSeparate(GLenum_face, GLuint_mask): # real signature unknown; restored from __doc__
    """
    glStencilMaskSeparate(GLenum face, GLuint mask)
    See: `glStencilMaskSeparate() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilMaskSeparate.xml>`_
    """
    pass

def glStencilOp(GLenum_fail, GLenum_zfail, GLenum_zpass): # real signature unknown; restored from __doc__
    """
    glStencilOp(GLenum fail, GLenum zfail, GLenum zpass)
    See: `glStencilOp() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilOp.xml>`_
    """
    pass

def glStencilOpSeparate(GLenum_face, GLenum_fail, GLenum_zfail, GLenum_zpass): # real signature unknown; restored from __doc__
    """
    glStencilOpSeparate(GLenum face, GLenum fail, GLenum zfail, GLenum zpass)
    See: `glStencilOpSeparate() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glStencilOpSeparate.xml>`_
    """
    pass

def glTexImage2D(GLenum_target, GLint_level, GLint_internalformat, GLsizei_width, GLsizei_height, GLint_border, GLenum_format, GLenum_type, bytes_pixels): # real signature unknown; restored from __doc__
    """
    glTexImage2D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, bytes pixels)
    See: `glTexImage2D() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexImage2D.xml>`_
    """
    pass

def glTexParameterf(GLenum_target, GLenum_pname, GLfloat_param): # real signature unknown; restored from __doc__
    """
    glTexParameterf(GLenum target, GLenum pname, GLfloat param)
    See: `glTexParameterf() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameterf.xml>`_
    """
    pass

def glTexParameterfv(GLenum_target, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glTexParameterfv(GLenum target, GLenum pname)
    See: `glTexParameterfv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameterfv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glTexParameteri(GLenum_target, GLenum_pname, GLint_param): # real signature unknown; restored from __doc__
    """
    glTexParameteri(GLenum target, GLenum pname, GLint param)
    See: `glTexParameteri() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameteri.xml>`_
    """
    pass

def glTexParameteriv(GLenum_target, GLenum_pname): # real signature unknown; restored from __doc__
    """
    glTexParameteriv(GLenum target, GLenum pname)
    See: `glTexParameteriv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexParameteriv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glTexSubImage2D(GLenum_target, GLint_level, GLint_xoffset, GLint_yoffset, GLsizei_width, GLsizei_height, GLenum_format, GLenum_type, bytes_pixels): # real signature unknown; restored from __doc__
    """
    glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, bytes pixels)
    See: `glTexSubImage2D() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glTexSubImage2D.xml>`_
    """
    pass

def glUniform1f(GLint_location, GLfloat_x): # real signature unknown; restored from __doc__
    """
    glUniform1f(GLint location, GLfloat x)
    See: `glUniform1f() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform1f.xml>`_
    """
    pass

def glUniform1fv(GLint_location, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glUniform1fv(GLint location, GLsizei count)
    See: `glUniform1fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform1fv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniform1i(GLint_location, GLint_x): # real signature unknown; restored from __doc__
    """
    glUniform1i(GLint location, GLint x)
    See: `glUniform1i() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform1i.xml>`_
    """
    pass

def glUniform1iv(GLint_location, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glUniform1iv(GLint location, GLsizei count)
    See: `glUniform1iv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform1iv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniform2f(GLint_location, GLfloat_x, GLfloat_y): # real signature unknown; restored from __doc__
    """
    glUniform2f(GLint location, GLfloat x, GLfloat y)
    See: `glUniform2f() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform2f.xml>`_
    """
    pass

def glUniform2fv(GLint_location, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glUniform2fv(GLint location, GLsizei count)
    See: `glUniform2fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform2fv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniform2i(GLint_location, GLint_x, GLint_y): # real signature unknown; restored from __doc__
    """
    glUniform2i(GLint location, GLint x, GLint y)
    See: `glUniform2i() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform2i.xml>`_
    """
    pass

def glUniform2iv(GLint_location, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glUniform2iv(GLint location, GLsizei count)
    See: `glUniform2iv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform2iv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniform3f(GLint_location, GLfloat_x, GLfloat_y, GLfloat_z): # real signature unknown; restored from __doc__
    """
    glUniform3f(GLint location, GLfloat x, GLfloat y, GLfloat z)
    See: `glUniform3f() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform3f.xml>`_
    """
    pass

def glUniform3fv(GLint_location, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glUniform3fv(GLint location, GLsizei count)
    See: `glUniform3fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform3fv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniform3i(GLint_location, GLint_x, GLint_y, GLint_z): # real signature unknown; restored from __doc__
    """
    glUniform3i(GLint location, GLint x, GLint y, GLint z)
    See: `glUniform3i() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform3i.xml>`_
    """
    pass

def glUniform3iv(GLint_location, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glUniform3iv(GLint location, GLsizei count)
    See: `glUniform3iv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform3iv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniform4f(GLint_location, GLfloat_x, GLfloat_y, GLfloat_z, GLfloat_w): # real signature unknown; restored from __doc__
    """
    glUniform4f(GLint location, GLfloat x, GLfloat y, GLfloat z, GLfloat w)
    See: `glUniform4f() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform4f.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniform4fv(GLint_location, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glUniform4fv(GLint location, GLsizei count)
    See: `glUniform4fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform4fv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniform4i(GLint_location, GLint_x, GLint_y, GLint_z, GLint_w): # real signature unknown; restored from __doc__
    """
    glUniform4i(GLint location, GLint x, GLint y, GLint z, GLint w)
    See: `glUniform4i() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform4i.xml>`_
    """
    pass

def glUniform4iv(GLint_location, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glUniform4iv(GLint location, GLsizei count)
    See: `glUniform4iv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniform4iv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniformMatrix2fv(GLint_location, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glUniformMatrix2fv(GLint location, GLsizei count)
    See: `glUniformMatrix2fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniformMatrix2fv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniformMatrix3fv(GLint_location, GLsizei_count): # real signature unknown; restored from __doc__
    """
    glUniformMatrix3fv(GLint location, GLsizei count)
    See: `glUniformMatrix3fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniformMatrix3fv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glUniformMatrix4fv(GLint_location, GLsizei_count, GLboolean_transpose, bytes_value): # real signature unknown; restored from __doc__
    """
    glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, bytes value)
    See: `glUniformMatrix4fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUniformMatrix4fv.xml>`_
    """
    pass

def glUseProgram(GLuint_program): # real signature unknown; restored from __doc__
    """
    glUseProgram(GLuint program)
    See: `glUseProgram() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glUseProgram.xml>`_
    """
    pass

def glValidateProgram(GLuint_program): # real signature unknown; restored from __doc__
    """
    glValidateProgram(GLuint program)
    See: `glValidateProgram() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glValidateProgram.xml>`_
    """
    pass

def glVertexAttrib1f(GLuint_indx, GLfloat_x): # real signature unknown; restored from __doc__
    """
    glVertexAttrib1f(GLuint indx, GLfloat x)
    See: `glVertexAttrib1f() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib1f.xml>`_
    """
    pass

def glVertexAttrib1fv(GLuint_indx, list_values): # real signature unknown; restored from __doc__
    """
    glVertexAttrib1fv(GLuint indx, list values)
    See: `glVertexAttrib1fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib1fv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glVertexAttrib2f(GLuint_indx, GLfloat_x, GLfloat_y): # real signature unknown; restored from __doc__
    """
    glVertexAttrib2f(GLuint indx, GLfloat x, GLfloat y)
    See: `glVertexAttrib2f() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib2f.xml>`_
    """
    pass

def glVertexAttrib2fv(GLuint_indx, list_values): # real signature unknown; restored from __doc__
    """
    glVertexAttrib2fv(GLuint indx, list values)
    See: `glVertexAttrib2fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib2fv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glVertexAttrib3f(GLuint_indx, GLfloat_x, GLfloat_y, GLfloat_z): # real signature unknown; restored from __doc__
    """
    glVertexAttrib3f(GLuint indx, GLfloat x, GLfloat y, GLfloat z)
    See: `glVertexAttrib3f() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib3f.xml>`_
    """
    pass

def glVertexAttrib3fv(GLuint_indx, list_values): # real signature unknown; restored from __doc__
    """
    glVertexAttrib3fv(GLuint indx, list values)
    See: `glVertexAttrib3fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib3fv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glVertexAttrib4f(GLuint_indx, GLfloat_x, GLfloat_y, GLfloat_z, GLfloat_w): # real signature unknown; restored from __doc__
    """
    glVertexAttrib4f(GLuint indx, GLfloat x, GLfloat y, GLfloat z, GLfloat w)
    See: `glVertexAttrib4f() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib4f.xml>`_
    """
    pass

def glVertexAttrib4fv(GLuint_indx, list_values): # real signature unknown; restored from __doc__
    """
    glVertexAttrib4fv(GLuint indx, list values)
    See: `glVertexAttrib4fv() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttrib4fv.xml>`_
    
        .. warning:: Not implemented yet.
    """
    pass

def glVertexAttribPointer(GLuint_index, GLint_size, GLenum_type, GLboolean_normalized, GLsizei_stride, data): # real signature unknown; restored from __doc__
    """
    glVertexAttribPointer(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, data)
    See: `glVertexAttribPointer() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glVertexAttribPointer.xml>`_
    """
    pass

def glViewport(GLint_x, GLint_y, GLsizei_width, GLsizei_height): # real signature unknown; restored from __doc__
    """
    glViewport(GLint x, GLint y, GLsizei width, GLsizei height)
    See: `glViewport() on Kronos website
        <http://www.khronos.org/opengles/sdk/docs/man/xhtml/glViewport.xml>`_
    """
    pass

def gl_init_symbols(allowed=[], ignored=[]): # real signature unknown; restored from __doc__
    """ gl_init_symbols(allowed=[], ignored=[]) """
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

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021F28DA3590>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.opengl', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021F28DA3590>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\opengl.cp311-win_amd64.pyd')"

__test__ = {}

