# encoding: utf-8
# module kivy._clock
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\_clock.cp311-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from _thread import Lock


# functions

def RLock(*args, **kwargs): # reliably restored by inspect
    """
    Factory function that returns a new reentrant lock.
    
        A reentrant lock must be released by the thread that acquired it. Once a
        thread has acquired a reentrant lock, the same thread may acquire it again
        without blocking; the thread must release it once for each time it has
        acquired it.
    """
    pass

def __pyx_unpickle_ClockEvent(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_ClockEvent(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

def __pyx_unpickle_FreeClockEvent(__pyx_type, long___pyx_checksum, __pyx_state): # real signature unknown; restored from __doc__
    """ __pyx_unpickle_FreeClockEvent(__pyx_type, long __pyx_checksum, __pyx_state) """
    pass

# classes

class ClockEvent(object):
    """
    ClockEvent(CyClockBase clock, int loop, callback, double timeout, double starttime, cid=None, int trigger=False, clock_ended_callback=None, release_ref=True, **kwargs)
     A class that describes a callback scheduled with kivy's :attr:`Clock`.
        This class is never created by the user; instead, kivy creates and returns
        an instance of this class when scheduling a callback.
    
        An event can be triggered (scheduled) by calling it. If it's already
        scheduled, nothing will happen, otherwise it'll be scheduled. E.g.::
    
            event = Clock.schedule_once(my_callback, .5)
            event()  # nothing will happen since it's already scheduled.
            event.cancel()  # cancel it
            event()  # now it's scheduled again.
    """
    def cancel(self): # real signature unknown; restored from __doc__
        """
        ClockEvent.cancel(self)
         Cancels the callback if it was scheduled to be called. If not
                scheduled, nothing happens.
        """
        pass

    def get_callback(self): # real signature unknown; restored from __doc__
        """
        ClockEvent.get_callback(self)
        Returns the callback associated with the event. Callbacks get stored
                with a indirect ref so that it doesn't keep objects alive. If the callback
                is dead, None is returned.
        """
        pass

    def get_clock_ended_callback(self): # real signature unknown; restored from __doc__
        """
        ClockEvent.get_clock_ended_callback(self)
        Returns the clock_ended_callback associated with the event.
                Callbacks get stored with a indirect ref so that it doesn't keep
                objects alive. If the callback is dead or wasn't provided,
                None is returned.
        """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """
        ClockEvent.release(self)
        (internal method) Converts the callback into a indirect ref.
        """
        pass

    def tick(self, double_curtime): # real signature unknown; restored from __doc__
        """
        ClockEvent.tick(self, double curtime)
        (internal method) Processes the event for the kivy thread.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """
        Schedules the callback associated with this instance.
                If the callback is already scheduled, it will not be scheduled again.
        """
        pass

    def __init__(self, CyClockBase_clock, int_loop, callback, double_timeout, double_starttime, cid=None, int_trigger=False, clock_ended_callback=None, release_ref=True, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ClockEvent.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ClockEvent.__setstate_cython__(self, __pyx_state) """
        pass

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """callback: object"""

    cid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """cid: object"""

    clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """clock: kivy._clock.CyClockBase
The :class:`CyClockBase` instance associated with the event.
    """

    clock_ended_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """clock_ended_callback: object
A Optional callback for this event, which if provided is called by the clock
    when the clock is stopped and the event was not ticked.
    """

    is_triggered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns whether the event is scheduled to have its callback executed by
        the kivy thread.
        """

    loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """loop: 'int'
Whether this event repeats at intervals of :attr:`timeout`.
    """

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """next: kivy._clock.ClockEvent
The next :class:`ClockEvent` in order they were scheduled.
    """

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """prev: kivy._clock.ClockEvent
The previous :class:`ClockEvent` in order they were scheduled.
    """

    release_ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """release_ref: 'int'
If True, the event should never release the reference to the callbacks.
    If False, a weakref may be created instead.
    """

    timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """timeout: 'double'
The duration after scheduling when the callback should be executed.
    """

    weak_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """weak_callback: object"""

    weak_clock_ended_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """weak_clock_ended_callback: object"""

    _del_queue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_del_queue: list"""

    _dt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_dt: 'double'"""

    _last_dt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_last_dt: 'double'"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A7C1AFE8B0>'


class ClockNotRunningError(RuntimeError):
    """
    Raised by the kivy Clock when scheduling an event if the
        Kivy Clock has already finished (:class:`~CyClockBase.stop_clock` was
        called).
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class CyClockBase(object):
    """
    CyClockBase(**kwargs)
    The base clock object with event support.
    """
    def create_lifecycle_aware_trigger(self, callback, clock_ended_callback, timeout=0, interval=False, release_ref=True): # real signature unknown; restored from __doc__
        """
        CyClockBase.create_lifecycle_aware_trigger(self, callback, clock_ended_callback, timeout=0, interval=False, release_ref=True) -> ClockEvent
        Create a Trigger event similarly to :meth:`create_trigger`, but the event
                is sensitive to the clock's state.
        
                If this event is triggered after the clock has stopped (:meth:`stop_clock`), then a
                :class:`ClockNotRunningError` will be raised. If the error is not raised,
                then either ``callback`` or ``clock_ended_callback`` will be
                called. ``callback`` will be called when the event
                is normally executed. If the clock is stopped before it can be executed,
                provided the app exited normally without crashing and the event wasn't manually
                canceled, and the callbacks are not garbage collected then
                ``clock_ended_callback`` will be called instead when the clock is stopped.
        
                :Parameters:
        
                    `callback`: callable
                        The callback to execute from kivy. It takes a single parameter - the
                        current elapsed kivy time.
                    `clock_ended_callback`: callable
                        A callback that will be called if the clock is stopped
                        while the event is still scheduled to be called. The callback takes
                        a single parameter - the event object. When the event is successfully
                        scheduled, if the app exited normally and the event wasn't canceled,
                        and the callbacks are not garbage collected - it is guaranteed that
                        either ``callback`` or ``clock_ended_callback`` would have been called.
                    `timeout`: float
                        How long to wait before calling the callback.
                    `interval`: bool
                        Whether the callback should be called once (False) or repeatedly
                        with a period of ``timeout`` (True) like :meth:`schedule_interval`.
                    `release_ref`: bool
                        If True, the default, then if ``callback`` or ``clock_ended_callback``
                        is a class method and the object has no references to it, then
                        the object may be garbage collected and the callbacks won't be called.
                        If False, the clock keeps a reference to the object preventing it
                        from being garbage collected - so it will be called.
        
                :returns:
        
                    A :class:`ClockEvent` instance. To schedule the callback of this
                    instance, you can call it.
        
                .. versionadded:: 2.0.0
        """
        return ClockEvent

    def create_trigger(self, callback, timeout=0, interval=False, release_ref=True): # real signature unknown; restored from __doc__
        """
        CyClockBase.create_trigger(self, callback, timeout=0, interval=False, release_ref=True) -> ClockEvent
        Create a Trigger event. It is thread safe but not ``__del__`` or
                ``__dealloc__`` safe (see :meth:`schedule_del_safe`).
                Check module documentation for more information.
        
                To cancel the event before it is executed, call :meth:`ClockEvent.cancel`
                on the returned event.
                To schedule it again, simply call the event (``event()``) and it'll be safely
                rescheduled if it isn't already scheduled.
        
                :Parameters:
        
                    `callback`: callable
                        The callback to execute from kivy. It takes a single parameter - the
                        current elapsed kivy time.
                    `timeout`: float
                        How long to wait before calling the callback.
                    `interval`: bool
                        Whether the callback should be called once (False) or repeatedly
                        with a period of ``timeout`` (True) like :meth:`schedule_interval`.
                    `release_ref`: bool
                        If True, the default, then if ``callback``
                        is a class method and the object has no references to it, then
                        the object may be garbage collected and the callbacks won't be called.
                        If False, the clock keeps a reference to the object preventing it
                        from being garbage collected - so it will be called.
        
                :returns:
        
                    A :class:`ClockEvent` instance. To schedule the callback of this
                    instance, you can call it.
        
                .. versionadded:: 1.0.5
        
                .. versionchanged:: 1.10.0
        
                    ``interval`` has been added.
        
                .. versionchanged:: 2.0.0
        
                    ``release_ref`` has been added.
        """
        return ClockEvent

    def get_before_frame_events(self): # real signature unknown; restored from __doc__
        """
        CyClockBase.get_before_frame_events(self)
        Returns the list of :class:`ClockEvent` instances that are scheduled
                to be called before the next frame (``-1`` timeout).
        
                .. versionadded:: 2.1.0
        """
        pass

    def get_events(self): # real signature unknown; restored from __doc__
        """
        CyClockBase.get_events(self)
        Returns the list of :class:`ClockEvent` instances currently scheduled.
        """
        pass

    def get_min_timeout(self): # real signature unknown; restored from __doc__
        """
        CyClockBase.get_min_timeout(self)
        Returns the remaining time since the start of the current frame
                for the event with the smallest timeout.
        """
        pass

    def get_resolution(self): # real signature unknown; restored from __doc__
        """
        CyClockBase.get_resolution(self)
        Returns the minimum resolution the clock has. It's a function of
                :attr:`clock_resolution` and ``maxfps`` provided at the config.
        """
        pass

    def handle_exception(self, e): # real signature unknown; restored from __doc__
        """
        CyClockBase.handle_exception(self, e)
        Provides an opportunity to handle an event's exception.
        
                If desired, the exception is handled, otherwise it should be raised
                again. By default it is raised again.
        
                :param e: The exception to be handled.
        
                .. versionadded:: 2.0.0
        """
        pass

    def on_schedule(self, event): # real signature unknown; restored from __doc__
        """
        CyClockBase.on_schedule(self, event)
        Function that is called internally every time an event is triggered
                for this clock. It takes the event as a parameter.
        
                The order of ``on_schedule`` calls are not guaranteed to be in the same
                order that the events are scheduled. Similarly, it is possible that the
                event being scheduled was canceled before this is called on the event.
                That's because :meth:`on_schedule` may be called from different threads.
        """
        pass

    def schedule_del_safe(self, callback): # real signature unknown; restored from __doc__
        """
        CyClockBase.schedule_del_safe(self, callback)
        Schedule a callback that is thread safe and ``__del__`` or
                ``__dealloc__`` safe.
        
                It's unsafe to call various kinds of code from ``__del__`` or
                ``__dealloc__`` methods because they can be executed at any time. Most
                Kivy's Clock methods are unsafe to call the Clock from these methods. Instead,
                use this method, which is thread safe and ``__del__`` or ``__dealloc__``
                safe, to schedule the callback in the kivy thread. It'll be executed
                in order after the normal events are processed.
        
                :Parameters:
        
                    `callback`: Callable
                        The callback the execute from kivy. It takes no parameters and
                        cannot be canceled.
        
                .. versionadded:: 1.11.0
        """
        pass

    def schedule_interval(self, callback, timeout): # real signature unknown; restored from __doc__
        """
        CyClockBase.schedule_interval(self, callback, timeout) -> ClockEvent
        Schedule an event to be called every <timeout> seconds.
                See :meth:`create_trigger` for advanced scheduling and more details.
        
                To cancel the event before it is executed, call :meth:`ClockEvent.cancel`
                on the returned event.
                If the callback is a class method, a weakref to the object is created and it
                may be garbage collected if there's no other reference to the object.
        
                :returns:
        
                    A :class:`ClockEvent` instance. As opposed to
                    :meth:`create_trigger` which only creates the trigger event, this
                    method also schedules it.
        """
        return ClockEvent

    def schedule_lifecycle_aware_del_safe(self, callback, clock_ended_callback): # real signature unknown; restored from __doc__
        """
        CyClockBase.schedule_lifecycle_aware_del_safe(self, callback, clock_ended_callback)
        Schedule a callback that is thread safe and ``__del__`` or
                ``__dealloc__`` safe similarly to :meth:`schedule_del_safe`, but the callback
                is sensitive to the clock's state.
        
                If this event is triggered after the clock has stopped (:meth:`stop_clock`), then a
                :class:`ClockNotRunningError` will be raised. If the error is not raised,
                then either ``callback`` or ``clock_ended_callback`` will be
                called. ``callback`` will be called when the callback
                is normally executed. If the clock is stopped before it can be executed,
                provided the app exited normally without crashing then
                ``clock_ended_callback`` will be called instead when the clock is stopped.
        
                :Parameters:
        
                    `callback`: Callable
                        The callback the execute from kivy. It takes no parameters and
                        cannot be canceled.
                    `clock_ended_callback`: callable
                        A callback that will be called if the clock is stopped
                        while the callback is still scheduled to be called. The callback takes
                        a single parameter - the callback. If the
                        app exited normally, it is guaranteed that either ``callback``
                        or ``clock_ended_callback`` would have been called.
        
                .. versionadded:: 2.0.0
        """
        pass

    def schedule_once(self, callback, timeout=0): # real signature unknown; restored from __doc__
        """
        CyClockBase.schedule_once(self, callback, timeout=0) -> ClockEvent
        Schedule an event in <timeout> seconds. If <timeout> is unspecified
                or 0, the callback will be called after the next frame is rendered.
                See :meth:`create_trigger` for advanced scheduling and more details.
        
                To cancel the event before it is executed, call :meth:`ClockEvent.cancel`
                on the returned event.
                If the callback is a class method, a weakref to the object is created and it
                may be garbage collected if there's no other reference to the object.
        
                :returns:
        
                    A :class:`ClockEvent` instance. As opposed to
                    :meth:`create_trigger` which only creates the trigger event, this
                    method also schedules it.
        
                .. versionchanged:: 1.0.5
                    If the timeout is -1, the callback will be called before the next
                    frame (at :meth:`tick_draw`).
        """
        return ClockEvent

    def start_clock(self): # real signature unknown; restored from __doc__
        """
        CyClockBase.start_clock(self)
        Must be called to start the clock.
        
                Once :meth:`stop_clock` is called, it cannot be started again.
        """
        pass

    def stop_clock(self): # real signature unknown; restored from __doc__
        """
        CyClockBase.stop_clock(self)
        Stops the clock and cleans up.
        
                This must be called to process the lifecycle_aware callbacks etc.
        """
        pass

    def unschedule(self, callback, all=True): # real signature unknown; restored from __doc__
        """
        CyClockBase.unschedule(self, callback, all=True)
        Remove a previously scheduled event.
        
                An :class:`ClockEvent` can also be canceled directly by calling
                :meth:`ClockEvent.cancel`.
        
                :parameters:
        
                    `callback`: :class:`ClockEvent` or a callable.
                        If it's a :class:`ClockEvent` instance, then the callback
                        associated with this event will be canceled if it is
                        scheduled.
        
                        If it's a callable, then the callable will be unscheduled if it
                        was scheduled.
        
                        .. warning::
        
                            Passing the callback function rather than the returned
                            :class:`ClockEvent` will result in a significantly slower
                            unscheduling.
                    `all`: bool
                        If True and if `callback` is a callable, all instances of this
                        callable will be unscheduled (i.e. if this callable was
                        scheduled multiple times). Defaults to `True`.
        
                .. versionchanged:: 1.9.0
                    The all parameter was added. Before, it behaved as if `all` was
                    `True`.
        """
        pass

    def _process_clock_ended_callbacks(self): # real signature unknown; restored from __doc__
        """ CyClockBase._process_clock_ended_callbacks(self) """
        pass

    def _process_clock_ended_del_safe_events(self): # real signature unknown; restored from __doc__
        """ CyClockBase._process_clock_ended_del_safe_events(self) """
        pass

    def _process_del_safe_events(self): # real signature unknown; restored from __doc__
        """ CyClockBase._process_del_safe_events(self) """
        pass

    def _process_events(self): # real signature unknown; restored from __doc__
        """ CyClockBase._process_events(self) """
        pass

    def _process_events_before_frame(self): # real signature unknown; restored from __doc__
        """ CyClockBase._process_events_before_frame(self) """
        pass

    def _release_references(self): # real signature unknown; restored from __doc__
        """ CyClockBase._release_references(self) """
        pass

    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ CyClockBase.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ CyClockBase.__setstate_cython__(self, __pyx_state) """
        pass

    clock_resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """clock_resolution: 'double'
If the remaining time until the event timeout is less than :attr:`clock_resolution`,
    the clock will execute the callback even if it hasn't exactly timed out.

    If -1, the default, the resolution will be computed from config's ``maxfps``.
    Otherwise, the provided value is used. Defaults to -1.
    """

    has_ended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """has_ended: 'int'"""

    has_started = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """has_started: 'int'"""

    max_iteration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """max_iteration: 'int'
The maximum number of callback iterations at the end of the frame, before the next
    frame. If more iterations occur, a warning is issued.
    """

    _cap_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_cap_event: kivy._clock.ClockEvent
The cap event is the last event in the chain for each frame.
    For a particular frame, events may be added dynamically after this event,
    and the current frame should not process them.

    Similarly to :attr:`_next_event`,
    when canceling the :attr:`_cap_event`, :attr:`_cap_event` is shifted to the
    one previous to it.
    """

    _del_safe_done = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_del_safe_done: 'int'"""

    _del_safe_lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_del_safe_lock: object"""

    _last_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_last_event: kivy._clock.ClockEvent
The last event in the chain. New events are added after this. Can be None.
    """

    _last_tick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_last_tick: 'double'"""

    _lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_lock: object"""

    _lock_acquire = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_lock_acquire: object"""

    _lock_release = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_lock_release: object"""

    _max_fps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_max_fps: 'double'"""

    _next_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_next_event: kivy._clock.ClockEvent
During frame processing when we service the events, this points to the next
    event that will be processed. After ticking an event, we continue with
    :attr:`_next_event`.

    If a event that is canceled is the :attr:`_next_event`, :attr:`_next_event`
    is shifted to point to the after after this, or None if it's at the end of the
    chain.
    """

    _root_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_root_event: kivy._clock.ClockEvent
The first event in the chain. Can be None.
    """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A7C1B86F70>'


class CyClockBaseFree(CyClockBase):
    """
    A clock class that supports scheduling free events in addition to normal
        events.
    
        Each of the :meth:`~CyClockBase.create_trigger`,
        :meth:`~CyClockBase.schedule_once`, and :meth:`~CyClockBase.schedule_interval`
        methods, which create a normal event, have a corresponding method
        for creating a free event.
    """
    def create_lifecycle_aware_trigger(self, callback, clock_ended_callback, timeout=0, interval=False, release_ref=True): # real signature unknown; restored from __doc__
        """ CyClockBaseFree.create_lifecycle_aware_trigger(self, callback, clock_ended_callback, timeout=0, interval=False, release_ref=True) -> FreeClockEvent """
        return FreeClockEvent

    def create_lifecycle_aware_trigger_free(self, callback, clock_ended_callback, timeout=0, interval=False, release_ref=True): # real signature unknown; restored from __doc__
        """
        CyClockBaseFree.create_lifecycle_aware_trigger_free(self, callback, clock_ended_callback, timeout=0, interval=False, release_ref=True) -> FreeClockEvent
        Similar to :meth:`~CyClockBase.create_lifecycle_aware_trigger`, but instead creates
                a free event.
        """
        return FreeClockEvent

    def create_trigger(self, callback, timeout=0, interval=False, release_ref=True): # real signature unknown; restored from __doc__
        """ CyClockBaseFree.create_trigger(self, callback, timeout=0, interval=False, release_ref=True) -> FreeClockEvent """
        return FreeClockEvent

    def create_trigger_free(self, callback, timeout=0, interval=False, release_ref=True): # real signature unknown; restored from __doc__
        """
        CyClockBaseFree.create_trigger_free(self, callback, timeout=0, interval=False, release_ref=True) -> FreeClockEvent
        Similar to :meth:`~CyClockBase.create_trigger`, but instead creates
                a free event.
        """
        return FreeClockEvent

    def get_min_free_timeout(self): # real signature unknown; restored from __doc__
        """
        CyClockBaseFree.get_min_free_timeout(self)
        Returns the remaining time since the start of the current frame
                for the *free* event with the smallest timeout.
        """
        pass

    def schedule_interval(self, callback, timeout): # real signature unknown; restored from __doc__
        """ CyClockBaseFree.schedule_interval(self, callback, timeout) -> FreeClockEvent """
        return FreeClockEvent

    def schedule_interval_free(self, callback, timeout): # real signature unknown; restored from __doc__
        """
        CyClockBaseFree.schedule_interval_free(self, callback, timeout) -> FreeClockEvent
        Similar to :meth:`~CyClockBase.schedule_interval`, but instead creates
                a free event.
        """
        return FreeClockEvent

    def schedule_once(self, callback, timeout=0): # real signature unknown; restored from __doc__
        """ CyClockBaseFree.schedule_once(self, callback, timeout=0) -> FreeClockEvent """
        return FreeClockEvent

    def schedule_once_free(self, callback, timeout=0): # real signature unknown; restored from __doc__
        """
        CyClockBaseFree.schedule_once_free(self, callback, timeout=0) -> FreeClockEvent
        Similar to :meth:`~CyClockBase.schedule_once`, but instead creates
                a free event.
        """
        return FreeClockEvent

    def _process_free_events(self, double_last_tick): # real signature unknown; restored from __doc__
        """ CyClockBaseFree._process_free_events(self, double last_tick) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ CyClockBaseFree.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ CyClockBaseFree.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A7C1B86F10>'


class FreeClockEvent(ClockEvent):
    """
    FreeClockEvent(free, *largs, **kwargs)
    The event returned by the ``Clock.XXX_free`` methods of
        :class:`CyClockBaseFree`. It stores whether the event was scheduled as a
        free event.
    """
    def __init__(self, free, *largs, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ FreeClockEvent.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ FreeClockEvent.__setstate_cython__(self, __pyx_state) """
        pass

    free = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """free: 'int'
Whether this event was scheduled as a free event.
    """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A7C1AFE880>'


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


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.weakmethod', '__doc__': 'Implementation of a\\n    `weakref <http://en.wikipedia.org/wiki/Weak_reference>`_\\n    for functions and bound methods.\\n    ', '__init__': <function WeakMethod.__init__ at 0x000001A7C1BA5260>, '__call__': <function WeakMethod.__call__ at 0x000001A7C1BA54E0>, 'is_dead': <function WeakMethod.is_dead at 0x000001A7C1BA5580>, '__eq__': <function WeakMethod.__eq__ at 0x000001A7C1BA5620>, '__repr__': <function WeakMethod.__repr__ at 0x000001A7C1BA56C0>, '__dict__': <attribute '__dict__' of 'WeakMethod' objects>, '__weakref__': <attribute '__weakref__' of 'WeakMethod' objects>, '__hash__': None})"
    __hash__ = None


# variables with complex values

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

__all__ = (
    'ClockNotRunningError',
    'ClockEvent',
    'CyClockBase',
    'FreeClockEvent',
    'CyClockBaseFree',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A7C1AA7C90>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy._clock', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A7C1AA7C90>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\_clock.cp311-win_amd64.pyd')"

__test__ = {}

