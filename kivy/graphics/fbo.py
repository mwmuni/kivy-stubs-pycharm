# encoding: utf-8
# module kivy.graphics.fbo
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\fbo.cp311-win_amd64.pyd
# by generator 1.147
"""
Framebuffer
===========

The Fbo is like an offscreen window. You can activate the fbo for rendering into
a texture and use your fbo as a texture for other drawing.

The Fbo acts as a :class:`kivy.graphics.instructions.Canvas`.

Here is an example of using an fbo for some colored rectangles::

    from kivy.graphics import Fbo, Color, Rectangle

    class FboTest(Widget):
        def __init__(self, **kwargs):
            super(FboTest, self).__init__(**kwargs)

            # first step is to create the fbo and use the fbo texture on other
            # rectangle

            with self.canvas:
                # create the fbo
                self.fbo = Fbo(size=(256, 256))

                # show our fbo on the widget in different size
                Color(1, 1, 1)
                Rectangle(size=(32, 32), texture=self.fbo.texture)
                Rectangle(pos=(32, 0), size=(64, 64), texture=self.fbo.texture)
                Rectangle(pos=(96, 0), size=(128, 128), texture=self.fbo.texture)

            # in the second step, you can draw whatever you want on the fbo
            with self.fbo:
                Color(1, 0, 0, .8)
                Rectangle(size=(256, 64))
                Color(0, 1, 0, .8)
                Rectangle(size=(64, 256))

If you change anything in the `self.fbo` object, it will be automatically updated.
The canvas where the fbo is put will be automatically updated as well.

Reloading the FBO content
-------------------------

.. versionadded:: 1.2.0

If the OpenGL context is lost, then the FBO is lost too. You need to reupload
data on it yourself. Use the :meth:`Fbo.add_reload_observer` to add a reloading
function that will be automatically called when needed::

    def __init__(self, **kwargs):
        super(...).__init__(**kwargs)
        self.fbo = Fbo(size=(512, 512))
        self.fbo.add_reload_observer(self.populate_fbo)

        # and load the data now.
        self.populate_fbo(self.fbo)


    def populate_fbo(self, fbo):
        with fbo:
            # .. put your Color / Rectangle / ... here

This way, you could use the same method for initialization and for reloading.
But it's up to you.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from kivy.graphics.opengl import py_glReadPixels

import kivy.graphics.instructions as __kivy_graphics_instructions


# Variables with simple values

platform = 'win'

PY2 = False

# functions

def __pyx_unpickle_Fbo(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_Fbo(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class Fbo(__kivy_graphics_instructions.RenderContext):
    """
    Fbo(*args, **kwargs)
    Fbo class for wrapping the OpenGL Framebuffer extension. The Fbo support
        "with" statement.
    
        :Parameters:
            `clear_color`: tuple, defaults to (0, 0, 0, 0)
                Define the default color for clearing the framebuffer
            `size`: tuple, defaults to (1024, 1024)
                Default size of the framebuffer
            `push_viewport`: bool, defaults to True
                If True, the OpenGL viewport will be set to the framebuffer size,
                and will be automatically restored when the framebuffer released.
            `with_depthbuffer`: bool, defaults to False
                If True, the framebuffer will be allocated with a Z buffer.
            `with_stencilbuffer`: bool, defaults to False
                .. versionadded:: 1.9.0
    
                If True, the framebuffer will be allocated with a stencil buffer.
            `texture`: :class:`~kivy.graphics.texture.Texture`, defaults to None
                If None, a default texture will be created.
    
        .. note::
            Using both of ``with_stencilbuffer`` and ``with_depthbuffer`` is not
            supported in kivy 1.9.0
    """
    def add_reload_observer(self, callback): # real signature unknown; restored from __doc__
        """
        Fbo.add_reload_observer(self, callback)
        Add a callback to be called after the whole graphics context has
                been reloaded. This is where you can reupload your custom data in GPU.
        
                .. versionadded:: 1.2.0
        
                :Parameters:
                    `callback`: func(context) -> return None
                        The first parameter will be the context itself
        """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """
        Fbo.bind(self)
        Bind the FBO to the current opengl context.
                `Bind` mean that you enable the Framebuffer, and all the drawing
                operations will act inside the Framebuffer, until :meth:`release` is
                called.
        
                The bind/release operations are automatically called when you add
                graphics objects into it. If you want to manipulate a Framebuffer
                yourself, you can use it like this::
        
                    self.fbo = FBO()
                    self.fbo.bind()
                    # do any drawing command
                    self.fbo.release()
        
                    # then, your fbo texture is available at
                    print(self.fbo.texture)
        """
        pass

    def clear_buffer(self): # real signature unknown; restored from __doc__
        """
        Fbo.clear_buffer(self)
        Clear the framebuffer with the :attr:`clear_color`.
        
                You need to bind the framebuffer yourself before calling this
                method::
        
                    fbo.bind()
                    fbo.clear_buffer()
                    fbo.release()
        """
        pass

    def get_pixel_color(self, int_wx, int_wy): # real signature unknown; restored from __doc__
        """
        Fbo.get_pixel_color(self, int wx, int wy)
        Get the color of the pixel with specified window
                coordinates wx, wy. It returns result in RGBA format.
        
                .. versionadded:: 1.8.0
        """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """
        Fbo.release(self)
        Release the Framebuffer (unbind).
        """
        pass

    def remove_reload_observer(self, callback): # real signature unknown; restored from __doc__
        """
        Fbo.remove_reload_observer(self, callback)
        Remove a callback from the observer list, previously added by
                :meth:`add_reload_observer`.
        
                .. versionadded:: 1.2.0
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Fbo.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Fbo.__setstate_cython__(self, __pyx_state) """
        pass

    clear_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Clear color in (red, green, blue, alpha) format.
        """

    pixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the pixels texture, in RGBA format only, unsigned byte. The
        origin of the image is at bottom left.

        .. versionadded:: 1.7.0
        """

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size of the framebuffer, in (width, height) format.

        If you change the size, the framebuffer content will be lost.
        """

    texture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the framebuffer texture
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000015D25867120>'


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


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.weakmethod', '__doc__': 'Implementation of a\\n    `weakref <http://en.wikipedia.org/wiki/Weak_reference>`_\\n    for functions and bound methods.\\n    ', '__init__': <function WeakMethod.__init__ at 0x0000015D25585760>, '__call__': <function WeakMethod.__call__ at 0x0000015D25586C00>, 'is_dead': <function WeakMethod.is_dead at 0x0000015D25586CA0>, '__eq__': <function WeakMethod.__eq__ at 0x0000015D25586D40>, '__repr__': <function WeakMethod.__repr__ at 0x0000015D25586DE0>, '__dict__': <attribute '__dict__' of 'WeakMethod' objects>, '__weakref__': <attribute '__weakref__' of 'WeakMethod' objects>, '__hash__': None})"
    __hash__ = None


# variables with complex values

environ = None # (!) real value is "environ({'ALLUSERSPROFILE': 'C:\\\\ProgramData', 'APPDATA': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Roaming', 'COMMONPROGRAMFILES': 'C:\\\\Program Files\\\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\\\Program Files (x86)\\\\Common Files', 'COMMONPROGRAMW6432': 'C:\\\\Program Files\\\\Common Files', 'COMPUTERNAME': 'CG-WA-WS063', 'COMSPEC': 'C:\\\\Windows\\\\system32\\\\cmd.exe', 'DRIVERDATA': 'C:\\\\Windows\\\\System32\\\\Drivers\\\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\\\Users\\\\matthew.muller', 'IDEA_INITIAL_DIRECTORY': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cadds-visual-tyre-handler\\\\source', 'INCLUDE': '%MSVC_ROOT%\\\\include;%SDK_INCLUDE%\\\\ucrt;%SDK_INCLUDE%\\\\shared;%SDK_INCLUDE%\\\\um;%SDK_INCLUDE%\\\\winrt;%SDK_INCLUDE%\\\\cppwinrt', 'LIB': '%MSVC_ROOT%\\\\lib\\\\x64;%SDK_LIBS%\\\\ucrt\\\\x64;%SDK_LIBS%\\\\um\\\\x64', 'LOCALAPPDATA': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local', 'LOGONSERVER': '\\\\\\\\CG-SUS-DC1', 'MSVC_ARCH': 'x64', 'MSVC_HOST': 'Hostx64', 'MSVC_ROOT': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822', 'MSVC_VERSION': '14.37.32822', 'NINJARMMCLI': 'C:\\\\ProgramData\\\\NinjaRMMAgent\\\\ninjarmm-cli.exe', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\\\Users\\\\matthew.muller\\\\OneDrive - Cadds', 'ONEDRIVECOMMERCIAL': 'C:\\\\Users\\\\matthew.muller\\\\OneDrive - Cadds', 'OS': 'Windows_NT', 'PATH': 'C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\sdl2\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\glew\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\angle\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\sdl2\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\glew\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\angle\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Scripts;C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Windows\\\\System32\\\\OpenSSH\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Scripts\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Launcher\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Microsoft\\\\WindowsApps;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\bin;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Git\\\\cmd;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\GitHubDesktop\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cmake-3.28.0-rc3\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\go\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64\\\\ucrt;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0a', 'PROGRAMDATA': 'C:\\\\ProgramData', 'PROGRAMFILES': 'C:\\\\Program Files', 'PROGRAMFILES(X86)': 'C:\\\\Program Files (x86)', 'PROGRAMW6432': 'C:\\\\Program Files', 'PROMPT': '(app) $P$G', 'PSMODULEPATH': 'C:\\\\Program Files\\\\WindowsPowerShell\\\\Modules;C:\\\\Windows\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\Modules', 'PUBLIC': 'C:\\\\Users\\\\Public', 'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONPATH': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\JetBrains\\\\PyCharm 2023.2.4\\\\plugins\\\\python\\\\helpers', 'ROOT': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\', 'SDK_ARCH': 'x64', 'SDK_INCLUDE': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\Include\\\\10.0.22621.0', 'SDK_LIBS': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\Lib\\\\10.0.22621.0', 'SDK_VERSION': '10.0.22621.0', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\\\Windows', 'TEMP': 'C:\\\\Users\\\\MATTHE~1.MUL\\\\AppData\\\\Local\\\\Temp', 'TMP': 'C:\\\\Users\\\\MATTHE~1.MUL\\\\AppData\\\\Local\\\\Temp', 'USERDNSDOMAIN': 'CADDS.LOCAL', 'USERDOMAIN': 'CADDS', 'USERDOMAIN_ROAMINGPROFILE': 'CADDS', 'USERNAME': 'Matthew.Muller', 'USERPROFILE': 'C:\\\\Users\\\\matthew.muller', 'VCTOOLSINSTALLDIR': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\', 'VIRTUAL_ENV': 'C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6', 'WINDIR': 'C:\\\\Windows', 'ZES_ENABLE_SYSMAN': '1', '_OLD_VIRTUAL_PATH': 'C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Windows\\\\System32\\\\OpenSSH\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Scripts\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Launcher\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Microsoft\\\\WindowsApps;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\bin;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Git\\\\cmd;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\GitHubDesktop\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cmake-3.28.0-rc3\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\go\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64\\\\ucrt;', '_OLD_VIRTUAL_PROMPT': '$P$G'})"

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'Fbo',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000015D259D1010>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.fbo', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000015D259D1010>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\fbo.cp311-win_amd64.pyd')"

__test__ = {}

