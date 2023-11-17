# encoding: utf-8
# module kivy.core.audio.audio_sdl2
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\core\audio\audio_sdl2.cp311-win_amd64.pyd
# by generator 1.147
"""
SDL2 audio provider
===================

This core audio implementation require SDL_mixer library.
It might conflict with any other library that are using SDL_mixer, such as
ffmpeg-android.

Native formats:

* wav, since 1.9.0

Depending the compilation of SDL2 mixer and/or installed libraries:

* ogg since 1.9.1 (mixer needs libvorbis/libogg)
* flac since 1.9.1 (mixer needs libflac)
* mp3 since 1.9.1 (mixer needs libsmpeg/libmad; only use mad for GPL apps)
  * Since 1.10.1 + mixer 2.0.2, mpg123 can also be used
* sequenced formats since 1.9.1 (midi, mod, s3m, etc. Mixer needs
  libmodplug or libmikmod)

.. Note::

    Sequenced format support changed with mixer v2.0.2. If mixer is
    linked with one of libmodplug or libmikmod, format support for
    both libraries is assumed. This will work perfectly with formats
    supported by both libraries, but if you were to try to load an
    obscure format (like `apun` file with mikmod only), it will fail.

    * Kivy <= 1.10.0: will fail to build with mixer >= 2.0.2
      will report correct format support with < 2.0.2
    * Kivy >= 1.10.1: will build with old and new mixer, and
      will "guesstimate" sequenced format support

.. Warning::

    Sequenced formats use the SDL2 Mixer music channel, you can only play
    one at a time, and .length will be -1 if music fails to load, and 0
    if loaded successfully (we can't get duration of these formats)
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import kivy.core.audio as __kivy_core_audio
import kivy._event as __kivy__event


# no functions
# classes

class ChunkContainer(object):
    """ ChunkContainer() """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ChunkContainer.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ChunkContainer.__setstate_cython__(self, __pyx_state) """
        pass


class MusicContainer(object):
    """ MusicContainer() """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ MusicContainer.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ MusicContainer.__setstate_cython__(self, __pyx_state) """
        pass


class Sound(__kivy__event.EventDispatcher):
    """
    Represents a sound to play. This class is abstract, and cannot be used
        directly.
    
        Use SoundLoader to load a sound.
    
        :Events:
            `on_play`: None
                Fired when the sound is played.
            `on_stop`: None
                Fired when the sound is stopped.
    """
    def get_pos(self): # reliably restored by inspect
        """
        Returns the current position of the audio file.
                Returns 0 if not playing.
        
                .. versionadded:: 1.4.1
        """
        pass

    def load(self): # reliably restored by inspect
        """ Load the file into memory. """
        pass

    def on_play(self): # reliably restored by inspect
        # no doc
        pass

    def on_source(self, instance, filename): # reliably restored by inspect
        # no doc
        pass

    def on_stop(self): # reliably restored by inspect
        # no doc
        pass

    def play(self): # reliably restored by inspect
        """ Play the file. """
        pass

    def seek(self, position): # reliably restored by inspect
        """
        Go to the <position> (in seconds).
        
                .. note::
                    Most sound providers cannot seek when the audio is stopped.
                    Play then seek.
        """
        pass

    def stop(self): # reliably restored by inspect
        """ Stop playback. """
        pass

    def unload(self): # reliably restored by inspect
        """ Unload the file from memory. """
        pass

    def _get_filename(self): # reliably restored by inspect
        # no doc
        pass

    def _get_length(self): # reliably restored by inspect
        # no doc
        pass

    def _get_status(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get length of the sound (in seconds)."""


    filename = None # (!) real value is '<AliasProperty name=filename>'
    loop = None # (!) real value is '<BooleanProperty name=loop>'
    pitch = None # (!) real value is '<BoundedNumericProperty name=pitch>'
    source = None # (!) real value is '<StringProperty name=source>'
    state = None # (!) real value is '<OptionProperty name=state>'
    status = None # (!) real value is '<AliasProperty name=status>'
    volume = None # (!) real value is '<NumericProperty name=volume>'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.core.audio', '__doc__': 'Represents a sound to play. This class is abstract, and cannot be used\\n    directly.\\n\\n    Use SoundLoader to load a sound.\\n\\n    :Events:\\n        `on_play`: None\\n            Fired when the sound is played.\\n        `on_stop`: None\\n            Fired when the sound is stopped.\\n    ', 'source': <StringProperty name=source>, 'volume': <NumericProperty name=volume>, 'pitch': <BoundedNumericProperty name=pitch>, 'state': <OptionProperty name=state>, 'loop': <BooleanProperty name=loop>, '_get_status': <function Sound._get_status at 0x000001B78DBF3600>, 'status': <AliasProperty name=status>, '_get_filename': <function Sound._get_filename at 0x000001B78DBF36A0>, 'filename': <AliasProperty name=filename>, '__events__': ('on_play', 'on_stop'), 'on_source': <function Sound.on_source at 0x000001B78DBF3740>, 'get_pos': <function Sound.get_pos at 0x000001B78DBF37E0>, '_get_length': <function Sound._get_length at 0x000001B78DBF3880>, 'length': <property object at 0x000001B78DBE7C90>, 'load': <function Sound.load at 0x000001B78DBF39C0>, 'unload': <function Sound.unload at 0x000001B78DBF3A60>, 'play': <function Sound.play at 0x000001B78DBF3B00>, 'stop': <function Sound.stop at 0x000001B78DBF3BA0>, 'seek': <function Sound.seek at 0x000001B78DBF3C40>, 'on_play': <function Sound.on_play at 0x000001B78DBF3CE0>, 'on_stop': <function Sound.on_stop at 0x000001B78DBF3D80>, '__dict__': <attribute '__dict__' of 'Sound' objects>})"
    __events__ = (
        'on_play',
        'on_stop',
    )


class MusicSDL2(__kivy_core_audio.Sound):
    # no doc
    def extensions(self): # real signature unknown; restored from __doc__
        """ MusicSDL2.extensions() """
        pass

    def load(self): # real signature unknown; restored from __doc__
        """ MusicSDL2.load(self) """
        pass

    def on_volume(self, instance, volume): # real signature unknown; restored from __doc__
        """ MusicSDL2.on_volume(self, instance, volume) """
        pass

    def play(self): # real signature unknown; restored from __doc__
        """ MusicSDL2.play(self) """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ MusicSDL2.stop(self) """
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ MusicSDL2.unload(self) """
        pass

    def _check_play(self, dt): # real signature unknown; restored from __doc__
        """ MusicSDL2._check_play(self, dt) """
        pass

    def _get_length(self): # real signature unknown; restored from __doc__
        """ MusicSDL2._get_length(self) """
        pass

    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        """ MusicSDL2.__init__(self, **kwargs) """
        pass


class SoundLoader(object):
    """ Load a sound, using the best loader for the given file type. """
    def load(filename): # reliably restored by inspect
        """ Load a sound, and return a Sound() instance. """
        pass

    def register(classobj): # reliably restored by inspect
        """ Register a new class to load the sound. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _classes = [
        None, # (!) forward: SoundSDL2, real value is "<class 'kivy.core.audio.audio_sdl2.SoundSDL2'>"
        MusicSDL2,
    ]
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.core.audio', '__doc__': 'Load a sound, using the best loader for the given file type.\\n    ', '_classes': [<class 'kivy.core.audio.audio_sdl2.SoundSDL2'>, <class 'kivy.core.audio.audio_sdl2.MusicSDL2'>], 'register': <staticmethod(<function SoundLoader.register at 0x000001B78D9F7E20>)>, 'load': <staticmethod(<function SoundLoader.load at 0x000001B78DBF3560>)>, '__dict__': <attribute '__dict__' of 'SoundLoader' objects>, '__weakref__': <attribute '__weakref__' of 'SoundLoader' objects>})"


class SoundSDL2(__kivy_core_audio.Sound):
    # no doc
    def extensions(self): # real signature unknown; restored from __doc__
        """ SoundSDL2.extensions() """
        pass

    def load(self): # real signature unknown; restored from __doc__
        """ SoundSDL2.load(self) """
        pass

    def on_pitch(self, instance, value): # real signature unknown; restored from __doc__
        """ SoundSDL2.on_pitch(self, instance, value) """
        pass

    def on_volume(self, instance, volume): # real signature unknown; restored from __doc__
        """ SoundSDL2.on_volume(self, instance, volume) """
        pass

    def play(self): # real signature unknown; restored from __doc__
        """ SoundSDL2.play(self) """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ SoundSDL2.stop(self) """
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ SoundSDL2.unload(self) """
        pass

    def _check_play(self, dt): # real signature unknown; restored from __doc__
        """ SoundSDL2._check_play(self, dt) """
        pass

    def _get_length(self): # real signature unknown; restored from __doc__
        """ SoundSDL2._get_length(self) """
        pass

    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        """ SoundSDL2.__init__(self, **kwargs) """
        pass


# variables with complex values

Clock = None # (!) real value is '<kivy.clock.ClockBase object at 0x000001B78D985C80>'

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'SoundSDL2',
    'MusicSDL2',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B78DBEBED0>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.core.audio.audio_sdl2', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B78DBEBED0>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\core\\\\audio\\\\audio_sdl2.cp311-win_amd64.pyd')"

__test__ = {}

