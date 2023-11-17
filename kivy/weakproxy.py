# encoding: utf-8
# module kivy.weakproxy
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\weakproxy.cp311-win_amd64.pyd
# by generator 1.147
"""
Weak Proxy
==========

In order to allow garbage collection, the weak proxy provides
`weak references <https://en.wikipedia.org/wiki/Weak_reference>`_ to objects.
It effectively enhances the
`weakref.proxy <https://docs.python.org/2/library/weakref.html#weakref.proxy>`_
by adding comparison support.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import weakref as weakref # C:\Users\matthew.muller\AppData\Local\Programs\Python\Python311\Lib\weakref.py
import operator as operator # C:\Users\matthew.muller\AppData\Local\Programs\Python\Python311\Lib\operator.py

# functions

def operator(*args, **kwargs): # real signature unknown
    """
    Operator interface.
    
    This module exports a set of functions implemented in C corresponding
    to the intrinsic operators of Python.  For example, operator.add(x, y)
    is equivalent to the expression x+y.  The function names are those
    used for special methods; variants without leading and trailing
    '__' are also provided for convenience.
    """
    pass

def __pyx_unpickle_WeakProxy(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_WeakProxy(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class WeakProxy(object):
    """
    WeakProxy(obj, destructor=None)
    Replacement for weakref.proxy to support comparisons
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __bytes__(self): # real signature unknown; restored from __doc__
        """ WeakProxy.__bytes__(self) """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __dir__(self): # real signature unknown; restored from __doc__
        """ WeakProxy.__dir__(self) """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __enter__(self): # real signature unknown; restored from __doc__
        """ WeakProxy.__enter__(self) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __exit__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """ WeakProxy.__exit__(self, *args, **kwargs) """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __ifloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//=value. """
        pass

    def __ilshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<=value. """
        pass

    def __imod__(self, *args, **kwargs): # real signature unknown
        """ Return self%=value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, obj, destructor=None): # real signature unknown; restored from __doc__
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __ipow__(self, *args, **kwargs): # real signature unknown
        """ Return self**=value. """
        pass

    def __irshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>=value. """
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __itruediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/=value. """
        pass

    def __ixor__(self, *args, **kwargs): # real signature unknown
        """ Return self^=value. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__radd__(self, other) """
        pass

    def __rand__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rand__(self, other) """
        pass

    def __rdivmod__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rdivmod__(self, other) """
        pass

    def __rdiv__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rdiv__(self, other) """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ WeakProxy.__reduce_cython__(self) """
        pass

    def __ref__(self): # real signature unknown; restored from __doc__
        """ WeakProxy.__ref__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __reversed__(self): # real signature unknown; restored from __doc__
        """ WeakProxy.__reversed__(self) """
        pass

    def __rfloordiv__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rfloordiv__(self, other) """
        pass

    def __rlshift__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rlshift__(self, other) """
        pass

    def __rmod__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rmod__(self, other) """
        pass

    def __rmul__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rmul__(self, other) """
        pass

    def __ror__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__ror__(self, other) """
        pass

    def __round__(self): # real signature unknown; restored from __doc__
        """ WeakProxy.__round__(self) """
        pass

    def __rpow__(self, other, modulo): # real signature unknown; restored from __doc__
        """ WeakProxy.__rpow__(self, other, modulo) """
        pass

    def __rrshift__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rrshift__(self, other) """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rsub__(self, other) """
        pass

    def __rtruediv__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rtruediv__(self, other) """
        pass

    def __rxor__(self, other): # real signature unknown; restored from __doc__
        """ WeakProxy.__rxor__(self, other) """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ WeakProxy.__setstate_cython__(self, __pyx_state) """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __unicode__(self): # real signature unknown; restored from __doc__
        """ WeakProxy.__unicode__(self) """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    __ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """__ref: object"""


    __class__ = type


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000264FEA07C90>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.weakproxy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000264FEA07C90>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\weakproxy.cp311-win_amd64.pyd')"

__test__ = {}

