# encoding: utf-8
# module kivy.graphics.transformation
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\transformation.cp311-win_amd64.pyd
# by generator 1.147
"""
Transformation
==============

This module contains a Matrix class used for our Graphics calculations. We
currently support:

- rotation, translation and scaling matrices
- multiplication matrix
- clip matrix (with or without perspective)
- transformation matrix for 3d touch

For more information on transformation matrices, please see the
`OpenGL Matrices Tutorial <http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/>`_.

.. versionchanged:: 1.6.0
   Added :meth:`Matrix.perspective`, :meth:`Matrix.look_at` and
   :meth:`Matrix.transpose`.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# no functions
# classes

class Matrix(object):
    """
    Matrix()
    
        Optimized matrix class for OpenGL::
    
            >>> from kivy.graphics.transformation import Matrix
            >>> m = Matrix()
            >>> print(m)
            [[ 1.000000 0.000000 0.000000 0.000000 ]
            [ 0.000000 1.000000 0.000000 0.000000 ]
            [ 0.000000 0.000000 1.000000 0.000000 ]
            [ 0.000000 0.000000 0.000000 1.000000 ]]
    
            [ 0   1   2   3]
            [ 4   5   6   7]
            [ 8   9  10  11]
            [ 12  13  14  15]
    """
    def get(self): # real signature unknown; restored from __doc__
        """
        Matrix.get(self)
        Retrieve the value of the current as a flat list.
        
                .. versionadded:: 1.9.1
        """
        pass

    def identity(self): # real signature unknown; restored from __doc__
        """
        Matrix.identity(self) -> Matrix
        Reset the matrix to the identity matrix (inplace).
        """
        return Matrix

    def inverse(self): # real signature unknown; restored from __doc__
        """
        Matrix.inverse(self) -> Matrix
        Return the inverse of the matrix as a new Matrix.
        """
        return Matrix

    def look_at(self, double_eyex, double_eyey, double_eyez, double_centerx, double_centery, double_centerz, double_upx, double_upy, double_upz): # real signature unknown; restored from __doc__
        """
        Matrix.look_at(self, double eyex, double eyey, double eyez, double centerx, double centery, double centerz, double upx, double upy, double upz)
        Returns a new lookat Matrix (similar to
                `gluLookAt <http://www.opengl.org/sdk/docs/man2/xhtml/gluLookAt.xml>`_).
        
                :Parameters:
                    `eyex`: float
                        Eyes X co-ordinate
                    `eyey`: float
                        Eyes Y co-ordinate
                    `eyez`: float
                        Eyes Z co-ordinate
                    `centerx`: float
                        The X position of the reference point
                    `centery`: float
                        The Y position of the reference point
                    `centerz`: float
                        The Z position of the reference point
                    `upx`: float
                        The X value up vector.
                    `upy`: float
                        The Y value up vector.
                    `upz`: float
                        The Z value up vector.
        
                .. versionadded:: 1.6.0
        """
        pass

    def multiply(self, mb, Matrix_ma): # real signature unknown; restored from __doc__
        """
        Matrix.multiply(mb, Matrix ma) -> Matrix
        Multiply the given matrix with self (from the left)
                i.e. we premultiply the given matrix by the current matrix and return
                the result (not inplace)::
        
                    m.multiply(n) -> n * m
        
                :Parameters:
                    `ma`: Matrix
                        The matrix to multiply by
        """
        return Matrix

    def normal_matrix(self): # real signature unknown; restored from __doc__
        """
        Matrix.normal_matrix(self) -> Matrix
        Computes the normal matrix, which is the inverse transpose
                of the top left 3x3 modelview matrix used to transform normals
                into eye/camera space.
        
                .. versionadded:: 1.6.0
        """
        return Matrix

    def perspective(self, double_fovy, double_aspect, double_zNear, double_zFar): # real signature unknown; restored from __doc__
        """
        Matrix.perspective(self, double fovy, double aspect, double zNear, double zFar) -> Matrix
        Creates a perspective matrix (inplace).
        
                :Parameters:
                    `fovy`: float
                        "Field Of View" angle
                    `aspect`: float
                        Aspect ratio
                    `zNear`: float
                        Near clipping plane
                    `zFar`: float
                        Far clippin plane
        
                .. versionadded:: 1.6.0
        """
        return Matrix

    def project(self, double_objx, double_objy, double_objz, Matrix_model, Matrix_proj, double_vx, double_vy, double_vw, double_vh): # real signature unknown; restored from __doc__
        """
        Matrix.project(self, double objx, double objy, double objz, Matrix model, Matrix proj, double vx, double vy, double vw, double vh)
        Project a point from 3d space into a 2d viewport.
        
                :Parameters:
                    `objx`: float
                        Points X co-ordinate
                    `objy`: float
                        Points Y co-ordinate
                    `objz`: float
                        Points Z co-ordinate
                    `model`: Matrix
                        The model matrix
                    `proj`: Matrix
                        The projection matrix
                    `vx`: float
                        Viewports X co-ordinate
                    `vy`: float
                        Viewports y co-ordinate
                    `vw`: float
                        Viewports width
                    `vh`: float
                        Viewports height
        
                .. versionadded:: 1.7.0
        """
        pass

    def rotate(self, double_angle, double_x, double_y, double_z): # real signature unknown; restored from __doc__
        """
        Matrix.rotate(self, double angle, double x, double y, double z) -> Matrix
        Rotate the matrix through the angle around the axis (x, y, z)
                (inplace).
        
                :Parameters:
                    `angle`: float
                        The angle through which to rotate the matrix
                    `x`: float
                        X position of the point
                    `y`: float
                        Y position of the point
                    `z`: float
                        Z position of the point
        """
        return Matrix

    def scale(self, double_x, double_y, double_z): # real signature unknown; restored from __doc__
        """
        Matrix.scale(self, double x, double y, double z) -> Matrix
        Scale the current matrix by the specified factors over
                each dimension (inplace).
        
                :Parameters:
                    `x`: float
                        The scale factor along the X axis
                    `y`: float
                        The scale factor along the Y axis
                    `z`: float
                        The scale factor along the Z axis
        """
        return Matrix

    def set(self, flat=None, array=None): # real signature unknown; restored from __doc__
        """
        Matrix.set(self, flat=None, array=None)
        Insert custom values into the matrix in a flat list format
                or 4x4 array format like below::
        
                    m.set(array=[
                        [1.0, 0.0, 0.0, 0.0],
                        [0.0, 1.0, 0.0, 0.0],
                        [0.0, 0.0, 1.0, 0.0],
                        [0.0, 0.0, 0.0, 1.0]]
                    )
        
                .. versionadded:: 1.9.0
        """
        pass

    def tolist(self): # real signature unknown; restored from __doc__
        """
        Matrix.tolist(self)
        Retrieve the value of the current matrix in numpy format.
                for example m.tolist() will return::
        
                    [[1.000000, 0.000000, 0.000000, 0.000000],
                    [0.000000, 1.000000, 0.000000, 0.000000],
                    [0.000000, 0.000000, 1.000000, 0.000000],
                    [0.000000, 0.000000, 0.000000, 1.000000]]
        
                you can use this format to plug the result straight into numpy
                in this way numpy.array(m.tolist())
        
                .. versionadded:: 1.9.0
        """
        pass

    def transform_point(self, double_x, double_y, double_z, t=None): # real signature unknown; restored from __doc__
        """
        Matrix.transform_point(self, double x, double y, double z, t=None) -> tuple
        Transforms the point by the matrix and returns the transformed point
                as a ``(x, y, z)`` tuple. If the point is a vector ``v``, the returned
                values is ``v2 = matrix * v``.
                
                If ``t`` is provided, it multiplies it with the last column of the matrix
                and returns the transformed ``(x, y, z, t)``.
        """
        return ()

    def translate(self, double_x, double_y, double_z): # real signature unknown; restored from __doc__
        """
        Matrix.translate(self, double x, double y, double z) -> Matrix
        Translate the matrix.
        
                :Parameters:
                    `x`: float
                        The translation factor along the X axis
                    `y`: float
                        The translation factor along the Y axis
                    `z`: float
                        The translation factor along the Z axis
        """
        return Matrix

    def transpose(self): # real signature unknown; restored from __doc__
        """
        Matrix.transpose(self) -> Matrix
        Return the transposed matrix as a new Matrix.
        
                .. versionadded:: 1.6.0
        """
        return Matrix

    def view_clip(self, double_left, double_right, double_bottom, double_top, double_near, double_far, int_perspective): # real signature unknown; restored from __doc__
        """
        Matrix.view_clip(self, double left, double right, double bottom, double top, double near, double far, int perspective) -> Matrix
        Create a clip matrix (inplace).
        
                :Parameters:
                    `left`: float
                        Co-ordinate
                    `right`: float
                        Co-ordinate
                    `bottom`: float
                        Co-ordinate
                    `top`: float
                        Co-ordinate
                    `near`: float
                        Co-ordinate
                    `far`: float
                        Co-ordinate
                    `perpective`: int
                        Co-ordinate
        
                .. versionchanged:: 1.6.0
                    Enable support for perspective parameter.
        """
        return Matrix

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """
        Retrieve the value at the specified index or slice
        
                .. versionadded:: 1.9.0
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Matrix.__reduce_cython__(self) """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """
        given an index and a value update the value at that location
        
                .. versionadded:: 1.9.0
        """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Matrix.__setstate_cython__(self, __pyx_state) """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x00000247078478A0>'


# variables with complex values

__all__ = (
    'Matrix',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000247078898D0>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.transformation', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000247078898D0>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\transformation.cp311-win_amd64.pyd')"

__test__ = {}

