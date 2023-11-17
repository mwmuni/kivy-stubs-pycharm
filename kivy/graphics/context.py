# encoding: utf-8
# module kivy.graphics.context
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\context.cp311-win_amd64.pyd
# by generator 1.147
"""
Context management
==================

.. versionadded:: 1.2.0

This class manages a registry of all created graphics instructions. It has
the ability to flush and delete them.

You can read more about Kivy graphics contexts in the :doc:`api-kivy.graphics`
module documentation. These are based on
`OpenGL graphics contexts <http://www.opengl.org/wiki/OpenGL_Context>`_.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import gc as gc # <module 'gc' (built-in)>
from time import time


# functions

def get_context(): # real signature unknown; restored from __doc__
    """ get_context() -> Context """
    return Context

def __pyx_unpickle_Context(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Context(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class Cache(object):
    """ See module documentation for more information. """
    def append(category, key, obj, timeout=None): # reliably restored by inspect
        """
        Add a new object to the cache.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `key`: str
                        Unique identifier of the object to store.
                    `obj`: object
                        Object to store in cache.
                    `timeout`: double (optional)
                        Time after which to delete the object if it has not been used.
                        If None, no timeout is applied.
        
                :raises:
                    `ValueError`: If `None` is used as `key`.
        
                .. versionchanged:: 2.0.0
                    Raises `ValueError` if `None` is used as `key`.
        """
        pass

    def get(category, key, default=None): # reliably restored by inspect
        """
        Get a object from the cache.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `key`: str
                        Unique identifier of the object in the store.
                    `default`: anything, defaults to None
                        Default value to be returned if the key is not found.
        """
        pass

    def get_lastaccess(category, key, default=None): # reliably restored by inspect
        """
        Get the objects last access time in the cache.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `key`: str
                        Unique identifier of the object in the store.
                    `default`: anything, defaults to None
                        Default value to be returned if the key is not found.
        """
        pass

    def get_timestamp(category, key, default=None): # reliably restored by inspect
        """
        Get the object timestamp in the cache.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `key`: str
                        Unique identifier of the object in the store.
                    `default`: anything, defaults to None
                        Default value to be returned if the key is not found.
        """
        pass

    def print_usage(): # reliably restored by inspect
        """ Print the cache usage to the console. """
        pass

    def register(category, limit=None, timeout=None): # reliably restored by inspect
        """
        Register a new category in the cache with the specified limit.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `limit`: int (optional)
                        Maximum number of objects allowed in the cache.
                        If None, no limit is applied.
                    `timeout`: double (optional)
                        Time after which to delete the object if it has not been used.
                        If None, no timeout is applied.
        """
        pass

    def remove(category, key=None): # reliably restored by inspect
        """
        Purge the cache.
        
                :Parameters:
                    `category`: str
                        Identifier of the category.
                    `key`: str (optional)
                        Unique identifier of the object in the store. If this
                        argument is not supplied, the entire category will be purged.
        """
        pass

    def _purge_by_timeout(dt): # reliably restored by inspect
        # no doc
        pass

    def _purge_oldest(category, maxpurge=1): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _categories = {
        'kv.atlas': {
            'limit': None,
            'timeout': None,
        },
        'kv.graphics.texture': '<value is a self-reference, replaced by this string>',
        'kv.image': {
            'limit': None,
            'timeout': 60,
        },
        'kv.resourcefind': '<value is a self-reference, replaced by this string>',
        'kv.shader': {
            'limit': 1000,
            'timeout': 3600,
        },
        'kv.texture': {
            'limit': 1000,
            'timeout': 60,
        },
    }
    _objects = {
        'kv.atlas': {},
        'kv.graphics.texture': '<value is a self-reference, replaced by this string>',
        'kv.image': '<value is a self-reference, replaced by this string>',
        'kv.resourcefind': '<value is a self-reference, replaced by this string>',
        'kv.shader': '<value is a self-reference, replaced by this string>',
        'kv.texture': '<value is a self-reference, replaced by this string>',
    }
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.cache', '__doc__': 'See module documentation for more information.\\n    ', '_categories': {'kv.resourcefind': {'limit': None, 'timeout': 60}, 'kv.image': {'limit': None, 'timeout': 60}, 'kv.atlas': {'limit': None, 'timeout': None}, 'kv.texture': {'limit': 1000, 'timeout': 60}, 'kv.shader': {'limit': 1000, 'timeout': 3600}, 'kv.graphics.texture': {'limit': None, 'timeout': None}}, '_objects': {'kv.resourcefind': {}, 'kv.image': {}, 'kv.atlas': {}, 'kv.texture': {}, 'kv.shader': {}, 'kv.graphics.texture': {}}, 'register': <staticmethod(<function Cache.register at 0x0000024E5A0E2160>)>, 'append': <staticmethod(<function Cache.append at 0x0000024E5A0E23E0>)>, 'get': <staticmethod(<function Cache.get at 0x0000024E5A0E2480>)>, 'get_timestamp': <staticmethod(<function Cache.get_timestamp at 0x0000024E5A0E2520>)>, 'get_lastaccess': <staticmethod(<function Cache.get_lastaccess at 0x0000024E5A0E25C0>)>, 'remove': <staticmethod(<function Cache.remove at 0x0000024E5A0E2660>)>, '_purge_oldest': <staticmethod(<function Cache._purge_oldest at 0x0000024E5A0E2700>)>, '_purge_by_timeout': <staticmethod(<function Cache._purge_by_timeout at 0x0000024E5A0E27A0>)>, 'print_usage': <staticmethod(<function Cache.print_usage at 0x0000024E5A0E2840>)>, '__dict__': <attribute '__dict__' of 'Cache' objects>, '__weakref__': <attribute '__weakref__' of 'Cache' objects>})"


class Context(object):
    """
    Context()
    
        The Context class manages groups of graphics instructions. It can also be used to manage
        observer callbacks. See :meth:`add_reload_observer` and :meth:`remove_reload_observer`
        for more information.
    """
    def add_reload_observer(self, callback, before=False): # real signature unknown; restored from __doc__
        """
        Context.add_reload_observer(self, callback, before=False)
        (internal) Add a callback to be called after the whole graphics context has
                been reloaded. This is where you can reupload your custom data into the
                GPU.
        
                :Parameters:
                    `callback`: func(context) -> return None
                        The first parameter will be the context itself
                    `before`: boolean, defaults to False
                        If True, the callback will be executed before all the
                        reloading processes. Use it if you want to clear your cache for
                        example.
        
                .. versionchanged:: 1.4.0
                    `before` parameter added.
        """
        pass

    def flag_update_canvas(self): # real signature unknown; restored from __doc__
        """ Context.flag_update_canvas(self) """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ Context.flush(self) -> void """
        pass

    def gl_dealloc(self, *largs): # real signature unknown; restored from __doc__
        """ Context.gl_dealloc(self, *largs) """
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ Context.reload(self) """
        pass

    def remove_reload_observer(self, callback, before=False): # real signature unknown; restored from __doc__
        """
        Context.remove_reload_observer(self, callback, before=False)
        (internal) Remove a callback from the observer list previously added by
                :meth:`add_reload_observer`.
        """
        pass

    def trigger_gl_dealloc(self): # real signature unknown; restored from __doc__
        """ Context.trigger_gl_dealloc(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Context.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Context.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000024E5A298330>'


class ref(object):
    # no doc
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __callback__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class WeakMethod(object):
    """
    Implementation of a
        `weakref <http://en.wikipedia.org/wiki/Weak_reference>`_
        for functions and bound methods.
    """
    def is_dead(self): # reliably restored by inspect
        """
        Returns True if the referenced callable was a bound method and
                the instance no longer exists. Otherwise, return False.
        """
        pass

    def __call__(self): # reliably restored by inspect
        """
        Return a new bound-method like the original, or the
                original function if it was just a function or unbound
                method.
                Returns None if the original object doesn't exist.
        """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, method): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.weakmethod', '__doc__': 'Implementation of a\\n    `weakref <http://en.wikipedia.org/wiki/Weak_reference>`_\\n    for functions and bound methods.\\n    ', '__init__': <function WeakMethod.__init__ at 0x0000024E59E55760>, '__call__': <function WeakMethod.__call__ at 0x0000024E59E56C00>, 'is_dead': <function WeakMethod.is_dead at 0x0000024E59E56CA0>, '__eq__': <function WeakMethod.__eq__ at 0x0000024E59E56D40>, '__repr__': <function WeakMethod.__repr__ at 0x0000024E59E56DE0>, '__dict__': <attribute '__dict__' of 'WeakMethod' objects>, '__weakref__': <attribute '__weakref__' of 'WeakMethod' objects>, '__hash__': None})"
    __hash__ = None


# variables with complex values

Clock = None # (!) real value is '<kivy.clock.ClockBase object at 0x0000024E59E25A70>'

environ = None # (!) real value is "environ({'ALLUSERSPROFILE': 'C:\\\\ProgramData', 'APPDATA': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Roaming', 'COMMONPROGRAMFILES': 'C:\\\\Program Files\\\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\\\Program Files (x86)\\\\Common Files', 'COMMONPROGRAMW6432': 'C:\\\\Program Files\\\\Common Files', 'COMPUTERNAME': 'CG-WA-WS063', 'COMSPEC': 'C:\\\\Windows\\\\system32\\\\cmd.exe', 'DRIVERDATA': 'C:\\\\Windows\\\\System32\\\\Drivers\\\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\\\Users\\\\matthew.muller', 'IDEA_INITIAL_DIRECTORY': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cadds-visual-tyre-handler\\\\source', 'INCLUDE': '%MSVC_ROOT%\\\\include;%SDK_INCLUDE%\\\\ucrt;%SDK_INCLUDE%\\\\shared;%SDK_INCLUDE%\\\\um;%SDK_INCLUDE%\\\\winrt;%SDK_INCLUDE%\\\\cppwinrt', 'LIB': '%MSVC_ROOT%\\\\lib\\\\x64;%SDK_LIBS%\\\\ucrt\\\\x64;%SDK_LIBS%\\\\um\\\\x64', 'LOCALAPPDATA': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local', 'LOGONSERVER': '\\\\\\\\CG-SUS-DC1', 'MSVC_ARCH': 'x64', 'MSVC_HOST': 'Hostx64', 'MSVC_ROOT': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822', 'MSVC_VERSION': '14.37.32822', 'NINJARMMCLI': 'C:\\\\ProgramData\\\\NinjaRMMAgent\\\\ninjarmm-cli.exe', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\\\Users\\\\matthew.muller\\\\OneDrive - Cadds', 'ONEDRIVECOMMERCIAL': 'C:\\\\Users\\\\matthew.muller\\\\OneDrive - Cadds', 'OS': 'Windows_NT', 'PATH': 'C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\sdl2\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\glew\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\angle\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\sdl2\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\glew\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\angle\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Scripts;C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Windows\\\\System32\\\\OpenSSH\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Scripts\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Launcher\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Microsoft\\\\WindowsApps;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\bin;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Git\\\\cmd;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\GitHubDesktop\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cmake-3.28.0-rc3\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\go\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64\\\\ucrt;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0a', 'PROGRAMDATA': 'C:\\\\ProgramData', 'PROGRAMFILES': 'C:\\\\Program Files', 'PROGRAMFILES(X86)': 'C:\\\\Program Files (x86)', 'PROGRAMW6432': 'C:\\\\Program Files', 'PROMPT': '(app) $P$G', 'PSMODULEPATH': 'C:\\\\Program Files\\\\WindowsPowerShell\\\\Modules;C:\\\\Windows\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\Modules', 'PUBLIC': 'C:\\\\Users\\\\Public', 'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONPATH': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\JetBrains\\\\PyCharm 2023.2.4\\\\plugins\\\\python\\\\helpers', 'ROOT': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\', 'SDK_ARCH': 'x64', 'SDK_INCLUDE': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\Include\\\\10.0.22621.0', 'SDK_LIBS': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\Lib\\\\10.0.22621.0', 'SDK_VERSION': '10.0.22621.0', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\\\Windows', 'TEMP': 'C:\\\\Users\\\\MATTHE~1.MUL\\\\AppData\\\\Local\\\\Temp', 'TMP': 'C:\\\\Users\\\\MATTHE~1.MUL\\\\AppData\\\\Local\\\\Temp', 'USERDNSDOMAIN': 'CADDS.LOCAL', 'USERDOMAIN': 'CADDS', 'USERDOMAIN_ROAMINGPROFILE': 'CADDS', 'USERNAME': 'Matthew.Muller', 'USERPROFILE': 'C:\\\\Users\\\\matthew.muller', 'VCTOOLSINSTALLDIR': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\', 'VIRTUAL_ENV': 'C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6', 'WINDIR': 'C:\\\\Windows', 'ZES_ENABLE_SYSMAN': '1', '_OLD_VIRTUAL_PATH': 'C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Windows\\\\System32\\\\OpenSSH\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Scripts\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Launcher\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Microsoft\\\\WindowsApps;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\bin;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Git\\\\cmd;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\GitHubDesktop\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cmake-3.28.0-rc3\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\go\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64\\\\ucrt;', '_OLD_VIRTUAL_PROMPT': '$P$G'})"

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'Context',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024E5A2A18D0>'

__pyx_capi__ = {
    'get_context': None, # (!) real value is '<capsule object "struct __pyx_obj_4kivy_8graphics_7context_Context *(int __pyx_skip_dispatch)" at 0x0000024E5A298240>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.context', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024E5A2A18D0>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\context.cp311-win_amd64.pyd')"

__test__ = {}

