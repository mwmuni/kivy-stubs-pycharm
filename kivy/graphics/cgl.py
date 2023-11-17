# encoding: utf-8
# module kivy.graphics.cgl
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\graphics\cgl.cp311-win_amd64.pyd
# by generator 1.147
"""
CGL: standard C interface for OpenGL
====================================

Kivy uses OpenGL and therefore requires a backend that provides it.
The backend used is controlled through the ``USE_OPENGL_MOCK`` and ``USE_SDL2``
compile-time variables and through the ``KIVY_GL_BACKEND`` runtime
environmental variable.

Currently, OpenGL is used through direct linking (gl/glew), sdl2,
or by mocking it. Setting ``USE_OPENGL_MOCK`` disables gl/glew.
Similarly, setting ``USE_SDL2`` to ``0`` will disable sdl2. Mocking
is always available.

At runtime the following backends are available and can be set using
``KIVY_GL_BACKEND``:

* ``gl`` -- Available on unix (the default backend). Unavailable when
  ``USE_OPENGL_MOCK=0``. Requires gl be installed.
* ``glew`` -- Available on Windows (the default backend). Unavailable when
  ``USE_OPENGL_MOCK=0``. Requires glew be installed.
* ``sdl2`` -- Available on Windows/unix (the default when gl/glew is disabled).
  Unavailable when ``USE_SDL2=0``. Requires ``kivy_deps.sdl2`` be installed.
* ``angle_sdl2`` -- Available on Windows with Python 3.5+.
  Unavailable when ``USE_SDL2=0``. Requires ``kivy_deps.sdl2`` and
  ``kivy_deps.angle`` be installed.
* ``mock`` -- Always available. Doesn't actually do anything.


Additionally, the following environmental runtime variables control the graphics
system:

* ``KIVY_GL_DEBUG`` -- Logs al gl calls when ``1``.
* ``KIVY_GRAPHICS`` -- Forces OpenGL ES2 when it is ``gles``. OpenGL ES2 is always
  used on the android, ios, rpi, and mali OSs.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import importlib as importlib # C:\Users\matthew.muller\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py
from _thread import get_ident


# Variables with simple values

platform = 'win32'

# functions

def cgl_get_backend_name(allowed=[], ignored=[]): # real signature unknown; restored from __doc__
    """ cgl_get_backend_name(allowed=[], ignored=[]) """
    pass

def cgl_get_initialized_backend_name(): # real signature unknown; restored from __doc__
    """ cgl_get_initialized_backend_name() """
    pass

def cgl_init(allowed=[], ignored=[]): # real signature unknown; restored from __doc__
    """ cgl_init(allowed=[], ignored=[]) """
    pass

def _update_verify_gl_main_thread(*args): # real signature unknown; restored from __doc__
    """ _update_verify_gl_main_thread(*args) """
    pass

# no classes
# variables with complex values

Config = None # (!) real value is '<kivy.config.ConfigParser object at 0x000001F9D37731D0>'

environ = None # (!) real value is "environ({'ALLUSERSPROFILE': 'C:\\\\ProgramData', 'APPDATA': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Roaming', 'COMMONPROGRAMFILES': 'C:\\\\Program Files\\\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\\\Program Files (x86)\\\\Common Files', 'COMMONPROGRAMW6432': 'C:\\\\Program Files\\\\Common Files', 'COMPUTERNAME': 'CG-WA-WS063', 'COMSPEC': 'C:\\\\Windows\\\\system32\\\\cmd.exe', 'DRIVERDATA': 'C:\\\\Windows\\\\System32\\\\Drivers\\\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\\\Users\\\\matthew.muller', 'IDEA_INITIAL_DIRECTORY': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cadds-visual-tyre-handler\\\\source', 'INCLUDE': '%MSVC_ROOT%\\\\include;%SDK_INCLUDE%\\\\ucrt;%SDK_INCLUDE%\\\\shared;%SDK_INCLUDE%\\\\um;%SDK_INCLUDE%\\\\winrt;%SDK_INCLUDE%\\\\cppwinrt', 'LIB': '%MSVC_ROOT%\\\\lib\\\\x64;%SDK_LIBS%\\\\ucrt\\\\x64;%SDK_LIBS%\\\\um\\\\x64', 'LOCALAPPDATA': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local', 'LOGONSERVER': '\\\\\\\\CG-SUS-DC1', 'MSVC_ARCH': 'x64', 'MSVC_HOST': 'Hostx64', 'MSVC_ROOT': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822', 'MSVC_VERSION': '14.37.32822', 'NINJARMMCLI': 'C:\\\\ProgramData\\\\NinjaRMMAgent\\\\ninjarmm-cli.exe', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\\\Users\\\\matthew.muller\\\\OneDrive - Cadds', 'ONEDRIVECOMMERCIAL': 'C:\\\\Users\\\\matthew.muller\\\\OneDrive - Cadds', 'OS': 'Windows_NT', 'PATH': 'C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\sdl2\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\glew\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\angle\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\sdl2\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\glew\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\share\\\\angle\\\\bin;C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Scripts;C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Windows\\\\System32\\\\OpenSSH\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Scripts\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Launcher\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Microsoft\\\\WindowsApps;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\bin;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Git\\\\cmd;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\GitHubDesktop\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cmake-3.28.0-rc3\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\go\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64\\\\ucrt;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0a', 'PROGRAMDATA': 'C:\\\\ProgramData', 'PROGRAMFILES': 'C:\\\\Program Files', 'PROGRAMFILES(X86)': 'C:\\\\Program Files (x86)', 'PROGRAMW6432': 'C:\\\\Program Files', 'PROMPT': '(app) $P$G', 'PSMODULEPATH': 'C:\\\\Program Files\\\\WindowsPowerShell\\\\Modules;C:\\\\Windows\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\Modules', 'PUBLIC': 'C:\\\\Users\\\\Public', 'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONPATH': 'C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\JetBrains\\\\PyCharm 2023.2.4\\\\plugins\\\\python\\\\helpers', 'ROOT': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\', 'SDK_ARCH': 'x64', 'SDK_INCLUDE': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\Include\\\\10.0.22621.0', 'SDK_LIBS': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\Lib\\\\10.0.22621.0', 'SDK_VERSION': '10.0.22621.0', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\\\Windows', 'TEMP': 'C:\\\\Users\\\\MATTHE~1.MUL\\\\AppData\\\\Local\\\\Temp', 'TMP': 'C:\\\\Users\\\\MATTHE~1.MUL\\\\AppData\\\\Local\\\\Temp', 'USERDNSDOMAIN': 'CADDS.LOCAL', 'USERDOMAIN': 'CADDS', 'USERDOMAIN_ROAMINGPROFILE': 'CADDS', 'USERNAME': 'Matthew.Muller', 'USERPROFILE': 'C:\\\\Users\\\\matthew.muller', 'VCTOOLSINSTALLDIR': 'C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\', 'VIRTUAL_ENV': 'C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6', 'WINDIR': 'C:\\\\Windows', 'ZES_ENABLE_SYSMAN': '1', '_OLD_VIRTUAL_PATH': 'C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Windows\\\\System32\\\\OpenSSH\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Scripts\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Launcher\\\\;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Microsoft\\\\WindowsApps;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\bin;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\Programs\\\\Git\\\\cmd;C:\\\\Users\\\\matthew.muller\\\\AppData\\\\Local\\\\GitHubDesktop\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\cmake-3.28.0-rc3\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\go\\\\bin;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\VC\\\\Tools\\\\MSVC\\\\14.37.32822\\\\bin\\\\Hostx64\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64;C:\\\\Users\\\\matthew.muller\\\\Downloads\\\\msvc\\\\msvc\\\\Windows Kits\\\\10\\\\bin\\\\10.0.22621.0\\\\x64\\\\ucrt;', '_OLD_VIRTUAL_PROMPT': '$P$G'})"

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F9D39FFE90>'

__pyx_capi__ = {
    'cgl': None, # (!) real value is '<capsule object "__pyx_t_4kivy_8graphics_3cgl_GLES2_Context *" at 0x000001F9D39EBED0>'
    'cgl_get_backend_name': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch, struct __pyx_opt_args_4kivy_8graphics_3cgl_cgl_get_backend_name *__pyx_optional_args)" at 0x000001F9D39EBDB0>'
    'cgl_get_context': None, # (!) real value is '<capsule object "__pyx_t_4kivy_8graphics_3cgl_GLES2_Context *(void)" at 0x000001F9D39EBE10>'
    'cgl_get_initialized_backend_name': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch)" at 0x000001F9D39EBD80>'
    'cgl_init': None, # (!) real value is '<capsule object "PyObject *(int __pyx_skip_dispatch, struct __pyx_opt_args_4kivy_8graphics_3cgl_cgl_init *__pyx_optional_args)" at 0x000001F9D39EBF00>'
    'cgl_set_context': None, # (!) real value is '<capsule object "void (__pyx_t_4kivy_8graphics_3cgl_GLES2_Context *)" at 0x000001F9D39EBDE0>'
    'initialized_tid': None, # (!) real value is '<capsule object "unsigned long" at 0x000001F9D39EBE70>'
    'kivy_opengl_es2': None, # (!) real value is '<capsule object "int" at 0x000001F9D39EBF30>'
    'pi': None, # (!) real value is '<capsule object "double" at 0x000001F9D39EBEA0>'
    'verify_gl_main_thread': None, # (!) real value is '<capsule object "int" at 0x000001F9D39EBE40>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.graphics.cgl', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F9D39FFE90>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\graphics\\\\cgl.cp311-win_amd64.pyd')"

__test__ = {}

