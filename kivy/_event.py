# encoding: utf-8
# module kivy._event
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\_event.cp311-win_amd64.pyd
# by generator 1.147
"""
Event dispatcher
================

All objects that produce events in Kivy implement the :class:`EventDispatcher`
which provides a consistent interface for registering and manipulating event
handlers.

.. versionchanged:: 1.0.9
    Property discovery and methods have been moved from the
    :class:`~kivy.uix.widget.Widget` to the :class:`EventDispatcher`.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from kivy.weakproxy import WeakProxy


# functions

def deprecated(func=None, msg=None): # reliably restored by inspect
    """
    This is a decorator which can be used to mark functions
        as deprecated. It will result in a warning being emitted the first time
        the function is used.
    """
    pass

# classes

class BoundCallback(object):
    """
    Bound callback storage.
    
        .. note::
    
            We do not call ``__init__`` on the class because we use cython's faster
            instantiation using ``__new__``.
    """
    def unbind_callback(self, *args): # real signature unknown; restored from __doc__
        """ BoundCallback.unbind_callback(self, *args) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ BoundCallback.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ BoundCallback.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002181D876F10>'


class defaultdict(dict):
    """
    defaultdict(default_factory=None, /, [...]) --> dict with default factory
    
    The default factory is called without arguments to produce
    a new value when a key is not present, in __getitem__ only.
    A defaultdict compares equal to a dict with the same items.
    All remaining arguments are treated the same as if they were
    passed to the dict constructor, including keyword arguments.
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        """ D.copy() -> a shallow copy of D. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, default_factory=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __missing__(self, key): # real signature unknown; restored from __doc__
        """
        __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
          if self.default_factory is None: raise KeyError((key,))
          self[key] = value = self.default_factory()
          return value
        """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    default_factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Factory for default value called by __missing__()."""



class ObjectWithUid(object):
    """
    (internal) This class assists in providing unique identifiers for class
        instances. It is not intended for direct usage.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ObjectWithUid.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ObjectWithUid.__setstate_cython__(self, __pyx_state) """
        pass

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class EventDispatcher(ObjectWithUid):
    """
    EventDispatcher(**kwargs)
    Generic event dispatcher interface.
    
        See the module docstring for usage.
    """
    def apply_property(self, **kwargs): # real signature unknown; restored from __doc__
        """
        EventDispatcher.apply_property(self, **kwargs)
        Adds properties at runtime to the class. The function accepts
                keyword arguments of the form `prop_name=prop`, where `prop` is a
                :class:`Property` instance and `prop_name` is the name of the attribute
                of the property.
        
                .. versionadded:: 1.9.1
        
                .. warning::
        
                    This method is not recommended for common usage because you should
                    declare the properties in your class instead of using this method.
        
                For example::
        
                    >>> print(wid.property('sticks', quiet=True))
                    None
                    >>> wid.apply_property(sticks=ObjectProperty(55, max=10))
                    >>> print(wid.property('sticks', quiet=True))
                    <kivy.properties.ObjectProperty object at 0x04303130>
        """
        pass

    def bind(self, **kwargs): # real signature unknown; restored from __doc__
        """
        EventDispatcher.bind(self, **kwargs)
        Bind an event type or a property to a callback.
        
                Usage::
        
                    # With properties
                    def my_x_callback(obj, value):
                        print('on object', obj, 'x changed to', value)
                    def my_width_callback(obj, value):
                        print('on object', obj, 'width changed to', value)
                    self.bind(x=my_x_callback, width=my_width_callback)
        
                    # With event
                    def my_press_callback(obj):
                        print('event on object', obj)
                    self.bind(on_press=my_press_callback)
        
                In general, property callbacks are called with 2 arguments (the
                object and the property's new value) and event callbacks with
                one argument (the object). The example above illustrates this.
        
                The following example demonstrates various ways of using the bind
                function in a complete application::
        
                    from kivy.uix.boxlayout import BoxLayout
                    from kivy.app import App
                    from kivy.uix.button import Button
                    from functools import partial
        
        
                    class DemoBox(BoxLayout):
                        """
                        This class demonstrates various techniques that can be used for binding to
                        events. Although parts could me made more optimal, advanced Python concepts
                        are avoided for the sake of readability and clarity.
                        """
                        def __init__(self, **kwargs):
                            super(DemoBox, self).__init__(**kwargs)
                            self.orientation = "vertical"
        
                            # We start with binding to a normal event. The only argument
                            # passed to the callback is the object which we have bound to.
                            btn = Button(text="Normal binding to event")
                            btn.bind(on_press=self.on_event)
        
                            # Next, we bind to a standard property change event. This typically
                            # passes 2 arguments: the object and the value
                            btn2 = Button(text="Normal binding to a property change")
                            btn2.bind(state=self.on_property)
        
                            # Here we use anonymous functions (a.k.a lambdas) to perform binding.
                            # Their advantage is that you can avoid declaring new functions i.e.
                            # they offer a concise way to "redirect" callbacks.
                            btn3 = Button(text="Using anonymous functions.")
                            btn3.bind(on_press=lambda x: self.on_event(None))
        
                            # You can also declare a function that accepts a variable number of
                            # positional and keyword arguments and use introspection to determine
                            # what is being passed in. This is very handy for debugging as well
                            # as function re-use. Here, we use standard event binding to a function
                            # that accepts optional positional and keyword arguments.
                            btn4 = Button(text="Use a flexible function")
                            btn4.bind(on_press=self.on_anything)
        
                            # Lastly, we show how to use partial functions. They are sometimes
                            # difficult to grasp, but provide a very flexible and powerful way to
                            # reuse functions.
                            btn5 = Button(text="Using partial functions. For hardcores.")
                            btn5.bind(on_press=partial(self.on_anything, "1", "2", monthy="python"))
        
                            for but in [btn, btn2, btn3, btn4, btn5]:
                                self.add_widget(but)
        
                        def on_event(self, obj):
                            print("Typical event from", obj)
        
                        def on_property(self, obj, value):
                            print("Typical property change from", obj, "to", value)
        
                        def on_anything(self, *args, **kwargs):
                            print('The flexible function has *args of', str(args),
                                "and **kwargs of", str(kwargs))
        
        
                    class DemoApp(App):
                        def build(self):
                            return DemoBox()
        
                    if __name__ == "__main__":
                        DemoApp().run()
        
                If a callback has already been bound to a given event or property,
                it won't be added again.
        
                When binding a method to an event or property, a
                :class:`kivy.weakmethod.WeakMethod` of the callback is saved. That is,
                rather than storing a regular reference, it stores both a weak
                reference to the instance (see Python's :class:`weakref`).
        
                This has two consequences.
        
                The first is that the binding will not prevent garbage collection of
                the method's object. The client must maintain a reference to the instance for
                the desired lifetime. The callback reference is silently removed if it
                becomes invalid.
        
                The second is that when using a decorated method e.g.::
        
                    @my_decorator
                    def callback(self, *args):
                        pass
        
                the decorator (``my_decorator`` here) must use `wraps <https://docs.python.org/3/library/functools.html#functools.wraps>`_ internally.
        """
        pass

    def create_property(self, unicode_name, value=None, default_value=True, *largs, **kwargs): # real signature unknown; restored from __doc__
        """
        EventDispatcher.create_property(self, unicode name, value=None, default_value=True, *largs, **kwargs)
        Create a new property at runtime.
        
                .. versionadded:: 1.0.9
        
                .. versionchanged:: 1.8.0
                    `value` parameter added, can be used to set the default value of the
                    property. Also, the type of the value is used to specialize the
                    created property.
        
                .. versionchanged:: 1.9.0
                    In the past, if `value` was of type `bool`, a `NumericProperty`
                    would be created, now a `BooleanProperty` is created.
        
                    Also, now and positional and keyword arguments are passed to the
                    property when created.
        
                .. versionchanged:: 2.0.0
        
                    default_value has been added.
        
                .. warning::
        
                    This function is designed for the Kivy language, don't use it in
                    your code. You should declare the property in your class instead of
                    using this method.
        
                :Parameters:
                    `name`: string
                        Name of the property
                    `value`: object, optional
                        Default value of the property. Type is also used for creating
                        more appropriate property types. Defaults to None.
                    `default_value`: bool, True by default
                        If True, `value` will be the default for the property. Otherwise,
                        the property will be initialized with the the property type's
                        normal default value, and subsequently set to ``value``.
        
                ::
        
                    >>> mywidget = Widget()
                    >>> mywidget.create_property('custom')
                    >>> mywidget.custom = True
                    >>> print(mywidget.custom)
                    True
        """
        pass

    def dispatch(self, event_type, *largs, **kwargs): # real signature unknown; restored from __doc__
        """
        EventDispatcher.dispatch(self, event_type, *largs, **kwargs)
        Dispatch an event across all the handlers added in bind/fbind().
                As soon as a handler returns True, the dispatching stops.
        
                The function collects all the positional and keyword arguments and
                passes them on to the handlers.
        
                .. note::
                    The handlers are called in reverse order than they were registered
                    with :meth:`bind`.
        
                :Parameters:
                    `event_type`: str
                        the event name to dispatch.
        
                .. versionchanged:: 1.9.0
                    Keyword arguments collection and forwarding was added. Before, only
                    positional arguments would be collected and forwarded.
        """
        pass

    def dispatch_children(self, event_type, *largs, **kwargs): # real signature unknown; restored from __doc__
        """ EventDispatcher.dispatch_children(self, event_type, *largs, **kwargs) """
        pass

    def dispatch_generic(self, event_type, *largs, **kwargs): # real signature unknown; restored from __doc__
        """ EventDispatcher.dispatch_generic(self, event_type, *largs, **kwargs) """
        pass

    def events(self): # real signature unknown; restored from __doc__
        """
        EventDispatcher.events(self)
        Return all the events in the class. Can be used for introspection.
        
                .. versionadded:: 1.8.0
        """
        pass

    def fbind(self, name, func, *largs, **kwargs): # real signature unknown; restored from __doc__
        """
        EventDispatcher.fbind(self, name, func, *largs, **kwargs)
        A method for advanced, and typically faster binding. This method is
                different than :meth:`bind` and is meant for more advanced users and
                internal usage. It can be used as long as the following points are heeded.
        
                #. As opposed to :meth:`bind`, it does not check that this function and
                   largs/kwargs has not been bound before to this name. So binding
                   the same callback multiple times will just keep adding it.
                #. Although :meth:`bind` creates a :class:`WeakMethod` of the callback when
                   binding to an event or property, this method stores the callback
                   directly, unless a keyword argument `ref` with value True is provided
                   and then a :class:`WeakMethod` is saved.
                   This is useful when there's no risk of a memory leak by storing the
                   callback directly.
                #. This method returns a unique positive number if `name` was found and
                   bound, and `0`, otherwise. It does not raise an exception, like
                   :meth:`bind` if the property `name` is not found. If not zero,
                   the uid returned is unique to this `name` and callback and can be
                   used with :meth:`unbind_uid` for unbinding.
        
        
                When binding a callback with largs and/or kwargs, :meth:`funbind`
                must be used for unbinding. If no largs and kwargs are provided,
                :meth:`unbind` may be used as well. :meth:`unbind_uid` can be used in
                either case.
        
                This method passes on any caught positional and/or keyword arguments to
                the callback, removing the need to call partial. When calling the
                callback the expended largs are passed on followed by instance/value
                (just instance for kwargs) followed by expended kwargs.
        
                Following is an example of usage similar to the example in
                :meth:`bind`::
        
                    class DemoBox(BoxLayout):
        
                        def __init__(self, **kwargs):
                            super(DemoBox, self).__init__(**kwargs)
                            self.orientation = "vertical"
        
                            btn = Button(text="Normal binding to event")
                            btn.fbind('on_press', self.on_event)
        
                            btn2 = Button(text="Normal binding to a property change")
                            btn2.fbind('state', self.on_property)
        
                            btn3 = Button(text="A: Using function with args.")
                            btn3.fbind('on_press', self.on_event_with_args, 'right',
                                           tree='birch', food='apple')
        
                            btn4 = Button(text="Unbind A.")
                            btn4.fbind('on_press', self.unbind_a, btn3)
        
                            btn5 = Button(text="Use a flexible function")
                            btn5.fbind('on_press', self.on_anything)
        
                            btn6 = Button(text="B: Using flexible functions with args. For hardcores.")
                            btn6.fbind('on_press', self.on_anything, "1", "2", monthy="python")
        
                            btn7 = Button(text="Force dispatch B with different params")
                            btn7.fbind('on_press', btn6.dispatch, 'on_press', 6, 7, monthy="other python")
        
                            for but in [btn, btn2, btn3, btn4, btn5, btn6, btn7]:
                                self.add_widget(but)
        
                        def on_event(self, obj):
                            print("Typical event from", obj)
        
                        def on_event_with_args(self, side, obj, tree=None, food=None):
                            print("Event with args", obj, side, tree, food)
        
                        def on_property(self, obj, value):
                            print("Typical property change from", obj, "to", value)
        
                        def on_anything(self, *args, **kwargs):
                            print('The flexible function has *args of', str(args),
                                "and **kwargs of", str(kwargs))
                            return True
        
                        def unbind_a(self, btn, event):
                            btn.funbind('on_press', self.on_event_with_args, 'right',
                                            tree='birch', food='apple')
        
                .. note::
        
                    Since the kv lang uses this method to bind, one has to implement
                    this method, instead of :meth:`bind` when creating a non
                    :class:`EventDispatcher` based class used with the kv lang. See
                    :class:`Observable` for an example.
        
                .. versionadded:: 1.9.0
        
                .. versionchanged:: 1.9.1
                    The `ref` keyword argument has been added.
        """
        pass

    def funbind(self, name, func, *largs, **kwargs): # real signature unknown; restored from __doc__
        """
        EventDispatcher.funbind(self, name, func, *largs, **kwargs)
        Similar to :meth:`fbind`.
        
                When unbinding, :meth:`unbind` will unbind all callbacks that match the
                callback, while this method will only unbind the first.
        
                To unbind, the same positional and keyword arguments passed to
                :meth:`fbind` must be passed on to funbind.
        
                .. note::
        
                    It is safe to use :meth:`funbind` to unbind a function bound with
                    :meth:`bind` as long as no keyword and positional arguments are
                    provided to :meth:`funbind`.
        
                .. versionadded:: 1.9.0
        """
        pass

    def getter(self, name): # real signature unknown; restored from __doc__
        """
        EventDispatcher.getter(self, name)
        Return the getter of a property.
        
                .. versionadded:: 1.0.9
        """
        pass

    def get_property_observers(self, name, args=False): # real signature unknown; restored from __doc__
        """
        EventDispatcher.get_property_observers(self, name, args=False)
         Returns a list of methods that are bound to the property/event
                passed as the *name* argument::
        
                    widget_instance.get_property_observers('on_release')
        
                :Parameters:
        
                    `name`: str
                        The name of the event or property.
                    `args`: bool
                        Whether to return the bound args. To keep compatibility,
                        only the callback functions and not their provided args will
                        be returned in the list when `args` is False.
        
                        If True, each element in the list is a 5-tuple of
                        `(callback, largs, kwargs, is_ref, uid)`, where `is_ref` indicates
                        whether `callback` is a weakref, and `uid` is the uid given by
                        :meth:`fbind`, or None if :meth:`bind` was used. Defaults to `False`.
        
                :Returns:
                    The list of bound callbacks. See `args` for details.
        
                .. versionadded:: 1.8.0
        
                .. versionchanged:: 1.9.0
                    `args` has been added.
        """
        pass

    def is_event_type(self, event_type): # real signature unknown; restored from __doc__
        """
        EventDispatcher.is_event_type(self, event_type)
        Return True if the event_type is already registered.
        
                .. versionadded:: 1.0.4
        """
        pass

    def properties(self): # real signature unknown; restored from __doc__
        """
        EventDispatcher.properties(self) -> dict
        Return all the properties in the class in a dictionary of
                key/property class. Can be used for introspection.
        
                .. versionadded:: 1.0.9
        """
        return {}

    def property(self, name, quiet=False): # real signature unknown; restored from __doc__
        """
        EventDispatcher.property(self, name, quiet=False)
        Get a property instance from the property name. If quiet is True,
                None is returned instead of raising an exception when `name` is not a
                property. Defaults to `False`.
        
                .. versionadded:: 1.0.9
        
                :return:
        
                    A :class:`~kivy.properties.Property` derived instance
                    corresponding to the name.
        
                .. versionchanged:: 1.9.0
                    quiet was added.
        """
        pass

    def register_event_type(self, event_type): # real signature unknown; restored from __doc__
        """
        EventDispatcher.register_event_type(self, event_type)
        Register an event type with the dispatcher.
        
                Registering event types allows the dispatcher to validate event handler
                names as they are attached and to search attached objects for suitable
                handlers. Each event type declaration must:
        
                    1. start with the prefix `on_`.
                    2. have a default handler in the class.
        
                Example of creating a custom event::
        
                    class MyWidget(Widget):
                        def __init__(self, **kwargs):
                            super(MyWidget, self).__init__(**kwargs)
                            self.register_event_type('on_swipe')
        
                        def on_swipe(self):
                            pass
        
                    def on_swipe_callback(*largs):
                        print('my swipe is called', largs)
                    w = MyWidget()
                    w.dispatch('on_swipe')
        """
        pass

    def setter(self, name): # real signature unknown; restored from __doc__
        """
        EventDispatcher.setter(self, name)
        Return the setter of a property. Use: instance.setter('name').
                The setter is a convenient callback function useful if you want
                to directly bind one property to another.
                It returns a partial function that will accept
                (obj, value) args and results in the property 'name' of instance
                being set to value.
        
                .. versionadded:: 1.0.9
        
                For example, to bind number2 to number1 in python you would do::
        
                    class ExampleWidget(Widget):
                        number1 = NumericProperty(None)
                        number2 = NumericProperty(None)
        
                        def __init__(self, **kwargs):
                            super(ExampleWidget, self).__init__(**kwargs)
                            self.bind(number1=self.setter('number2'))
        
                This is equivalent to kv binding::
        
                    <ExampleWidget>:
                        number2: self.number1
        """
        pass

    def unbind(self, **kwargs): # real signature unknown; restored from __doc__
        """
        EventDispatcher.unbind(self, **kwargs)
        Unbind properties from callback functions with similar usage as
                :meth:`bind`.
        
                If a callback has been bound to a given event or property multiple
                times, only the first occurrence will be unbound.
        
                .. note::
        
                    It is safe to use :meth:`unbind` on a function bound with :meth:`fbind`
                    as long as that function was originally bound without any keyword and
                    positional arguments. Otherwise, the function will fail to be unbound
                    and you should use :meth:`funbind` instead.
        """
        pass

    def unbind_uid(self, name, uid): # real signature unknown; restored from __doc__
        """
        EventDispatcher.unbind_uid(self, name, uid)
        Uses the uid returned by :meth:`fbind` to unbind the callback.
        
                This method is much more efficient than :meth:`funbind`. If `uid`
                evaluates to False (e.g. 0) a `ValueError` is raised. Also, only
                callbacks bound with :meth:`fbind` can be unbound with this method.
        
                Since each call to :meth:`fbind` will generate a unique `uid`,
                only one callback will be removed. If `uid` is not found among the
                callbacks, no error is raised.
        
                E.g.::
        
                    btn6 = Button(text="B: Using flexible functions with args. For hardcores.")
                    uid = btn6.fbind('on_press', self.on_anything, "1", "2", monthy="python")
                    if not uid:
                        raise Exception('Binding failed').
                    ...
                    btn6.unbind_uid('on_press', uid)
        
                .. versionadded:: 1.9.0
        """
        pass

    def unregister_event_type(self, event_type): # real signature unknown; restored from __doc__
        """
        EventDispatcher.unregister_event_type(self, event_type)
        Unregister an event type in the dispatcher.
        
                .. versionchanged:: 2.1.0
                    Method renamed from `unregister_event_types` to
                    `unregister_event_type`.
        """
        pass

    def unregister_event_types(*args, **kwargs): # reliably restored by inspect
        """ EventDispatcher.unregister_event_types(self, event_type) """
        pass

    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __proxy_getter(self, EventDispatcher_dstinstance, name, instance): # real signature unknown; restored from __doc__
        """ EventDispatcher.__proxy_getter(self, EventDispatcher dstinstance, name, instance) """
        pass

    def __proxy_setter(self, EventDispatcher_dstinstance, name, instance, value): # real signature unknown; restored from __doc__
        """ EventDispatcher.__proxy_setter(self, EventDispatcher dstinstance, name, instance, value) """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ EventDispatcher.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ EventDispatcher.__setstate_cython__(self, __pyx_state) """
        pass

    proxy_ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a :class:`~kivy.weakproxy.WeakProxy` reference to the
        :class:`EventDispatcher`.

        .. versionadded:: 1.9.0

        .. versionchanged:: 2.0.0

            Previously it just returned itself, now it actually returns a
            :class:`~kivy.weakproxy.WeakProxy`.
        """

    _kwargs_applied_init = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_kwargs_applied_init: set"""

    _proxy_ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_proxy_ref: object"""

    __self__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002181D7EE880>'


class EventObservers(object):
    """
    A class that stores observers as a doubly linked list. See dispatch
        for more details on locking and deletion of observers.
    
        In all instances, largs and kwargs if None or empty are all converted
        to None internally before storing or comparing.
    
        .. note::
    
            We do not call ``__init__`` on the class because we use cython's faster
            instantiation using ``__new__``.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """
        Binding/unbinding/dispatching while iterating can lead to invalid
                data.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ EventObservers.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ EventObservers.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002181D876FD0>'


class Observable(ObjectWithUid):
    """
    :class:`Observable` is a stub class defining the methods required
        for binding. :class:`EventDispatcher` is (the) one example of a class that
        implements the binding interface. See :class:`EventDispatcher` for details.
    
        .. versionadded:: 1.9.0
    """
    def bind(self, **kwargs): # real signature unknown; restored from __doc__
        """ Observable.bind(self, **kwargs) """
        pass

    def fbind(self, name, func, *largs, **kwargs): # real signature unknown; restored from __doc__
        """
        Observable.fbind(self, name, func, *largs, **kwargs)
        See :meth:`EventDispatcher.fbind`.
        
                .. note::
        
                    To keep backward compatibility with derived classes which may have
                    inherited from :class:`Observable` before, the
                    :meth:`fbind` method was added. The default implementation
                    of :meth:`fbind` is to create a partial
                    function that it passes to bind while saving the uid and largs/kwargs.
                    However, :meth:`funbind` (and :meth:`unbind_uid`) are fairly
                    inefficient since we have to first lookup this partial function
                    using the largs/kwargs or uid and then call :meth:`unbind` on
                    the returned function. It is recommended to overwrite
                    these methods in derived classes to bind directly for
                    better performance.
        
                    Similarly to :meth:`EventDispatcher.fbind`, this method returns
                    0 on failure and a positive unique uid on success. This uid can be
                    used with :meth:`unbind_uid`.
        """
        pass

    def funbind(self, name, func, *largs, **kwargs): # real signature unknown; restored from __doc__
        """
        Observable.funbind(self, name, func, *largs, **kwargs)
        See :meth:`fbind` and :meth:`EventDispatcher.funbind`.
        """
        pass

    def unbind(self, **kwargs): # real signature unknown; restored from __doc__
        """ Observable.unbind(self, **kwargs) """
        pass

    def unbind_uid(self, name, uid): # real signature unknown; restored from __doc__
        """
        Observable.unbind_uid(self, name, uid)
        See :meth:`fbind` and :meth:`EventDispatcher.unbind_uid`.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Observable.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Observable.__setstate_cython__(self, __pyx_state) """
        pass

    proxy_ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class partial(object):
    """
    partial(func, *args, **keywords) - new function with partial application
        of the given arguments and keywords.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, func, *args, **keywords): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """tuple of arguments to future partial calls"""

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """function object to use in future partial calls"""

    keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """dictionary of keyword arguments to future partial calls"""

    __vectorcalloffset__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x000002181B5BB260>, '__repr__': <slot wrapper '__repr__' of 'functools.partial' objects>, '__call__': <slot wrapper '__call__' of 'functools.partial' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'functools.partial' objects>, '__setattr__': <slot wrapper '__setattr__' of 'functools.partial' objects>, '__delattr__': <slot wrapper '__delattr__' of 'functools.partial' objects>, '__reduce__': <method '__reduce__' of 'functools.partial' objects>, '__setstate__': <method '__setstate__' of 'functools.partial' objects>, '__class_getitem__': <method '__class_getitem__' of 'functools.partial' objects>, 'func': <member 'func' of 'functools.partial' objects>, 'args': <member 'args' of 'functools.partial' objects>, 'keywords': <member 'keywords' of 'functools.partial' objects>, '__vectorcalloffset__': <member '__vectorcalloffset__' of 'functools.partial' objects>, '__dict__': <attribute '__dict__' of 'functools.partial' objects>, '__doc__': 'partial(func, *args, **keywords) - new function with partial application\\n    of the given arguments and keywords.\\n', '__module__': 'functools'})"


class string_types(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self, *args, **kwargs): # real signature unknown
        """
        Return a capitalized version of the string.
        
        More specifically, make the first character have upper case and the rest lower
        case.
        """
        pass

    def casefold(self, *args, **kwargs): # real signature unknown
        """ Return a version of the string suitable for caseless comparisons. """
        pass

    def center(self, *args, **kwargs): # real signature unknown
        """
        Return a centered string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, *args, **kwargs): # real signature unknown
        """
        Encode the string using the codec registered for encoding.
        
          encoding
            The encoding in which to encode the string.
          errors
            The error handling scheme to use for encoding errors.
            The default is 'strict' meaning that encoding errors raise a
            UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
            'xmlcharrefreplace' as well as any other name registered with
            codecs.register_error that can handle UnicodeEncodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, *args, **kwargs): # real signature unknown
        """
        Return a copy where all tab characters are expanded using spaces.
        
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alpha-numeric string, False otherwise.
        
        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        """
        pass

    def isalpha(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alphabetic string, False otherwise.
        
        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        """
        pass

    def isascii(self, *args, **kwargs): # real signature unknown
        """
        Return True if all characters in the string are ASCII, False otherwise.
        
        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.
        """
        pass

    def isdecimal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a decimal string, False otherwise.
        
        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.
        """
        pass

    def isdigit(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a digit string, False otherwise.
        
        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        """
        pass

    def isidentifier(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a valid Python identifier, False otherwise.
        
        Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
        such as "def" or "class".
        """
        pass

    def islower(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a lowercase string, False otherwise.
        
        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        """
        pass

    def isnumeric(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a numeric string, False otherwise.
        
        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
        """
        pass

    def isprintable(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is printable, False otherwise.
        
        A string is printable if all of its characters are considered printable in
        repr() or if it is empty.
        """
        pass

    def isspace(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a whitespace string, False otherwise.
        
        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
        """
        pass

    def istitle(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a title-cased string, False otherwise.
        
        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.
        """
        pass

    def isupper(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an uppercase string, False otherwise.
        
        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
        """
        pass

    def join(self, ab=None, pq=None, rs=None): # real signature unknown; restored from __doc__
        """
        Concatenate any number of strings.
        
        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.
        
        Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """
        pass

    def ljust(self, *args, **kwargs): # real signature unknown
        """
        Return a left-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def lower(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to lowercase. """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.
        """
        pass

    def removeprefix(self, *args, **kwargs): # real signature unknown
        """
        Return a str with the given prefix string removed if present.
        
        If the string starts with the prefix string, return string[len(prefix):].
        Otherwise, return a copy of the original string.
        """
        pass

    def removesuffix(self, *args, **kwargs): # real signature unknown
        """
        Return a str with the given suffix string removed if present.
        
        If the string ends with the suffix string and that suffix is not empty,
        return string[:-len(suffix)]. Otherwise, return a copy of the original
        string.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, *args, **kwargs): # real signature unknown
        """
        Return a right-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the substrings in the string, using sep as the separator string.
        
          sep
            The separator used to split the string.
        
            When set to None (the default value), will split on any whitespace
            character (including \n \r \t \f and spaces) and will discard
            empty strings from the result.
          maxsplit
            Maximum number of splits (starting from the left).
            -1 (the default value) means no limit.
        
        Splitting starts at the end of the string and works to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def split(self): # real signature unknown; restored from __doc__
        """
        Return a list of the substrings in the string, using sep as the separator string.
        
          sep
            The separator used to split the string.
        
            When set to None (the default value), will split on any whitespace
            character (including \n \r \t \f and spaces) and will discard
            empty strings from the result.
          maxsplit
            Maximum number of splits (starting from the left).
            -1 (the default value) means no limit.
        
        Note, str.split() is mainly useful for data that has been intentionally
        delimited.  With natural text that includes punctuation, consider using
        the regular expression module.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the string, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading and trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def swapcase(self, *args, **kwargs): # real signature unknown
        """ Convert uppercase characters to lowercase and lowercase characters to uppercase. """
        pass

    def title(self, *args, **kwargs): # real signature unknown
        """
        Return a version of the string where each word is titlecased.
        
        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Replace each character in the string using the given translation table.
        
          table
            Translation table, which must be a mapping of Unicode ordinals to
            Unicode ordinals, strings, or None.
        
        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """
        pass

    def upper(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to uppercase. """
        pass

    def zfill(self, *args, **kwargs): # real signature unknown
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.
        
        The string is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Return a formatted version of the string as described by format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
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

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Return the size of the string in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


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


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.weakmethod', '__doc__': 'Implementation of a\\n    `weakref <http://en.wikipedia.org/wiki/Weak_reference>`_\\n    for functions and bound methods.\\n    ', '__init__': <function WeakMethod.__init__ at 0x000002181D896660>, '__call__': <function WeakMethod.__call__ at 0x000002181D8968E0>, 'is_dead': <function WeakMethod.is_dead at 0x000002181D896980>, '__eq__': <function WeakMethod.__eq__ at 0x000002181D896A20>, '__repr__': <function WeakMethod.__repr__ at 0x000002181D896AC0>, '__dict__': <attribute '__dict__' of 'WeakMethod' objects>, '__weakref__': <attribute '__weakref__' of 'WeakMethod' objects>, '__hash__': None})"
    __hash__ = None


# variables with complex values

__all__ = (
    'EventDispatcher',
    'ObjectWithUid',
    'Observable',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002181D797C90>'

__pyx_capi__ = {
    'cache_properties_per_cls': None, # (!) real value is '<capsule object "PyObject *" at 0x000002181D7EE850>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='kivy._event', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002181D797C90>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\_event.cp311-win_amd64.pyd')"

__test__ = {
    'EventDispatcher.apply_property (line 897)': "Adds properties at runtime to the class. The function accepts\n        keyword arguments of the form `prop_name=prop`, where `prop` is a\n        :class:`Property` instance and `prop_name` is the name of the attribute\n        of the property.\n\n        .. versionadded:: 1.9.1\n\n        .. warning::\n\n            This method is not recommended for common usage because you should\n            declare the properties in your class instead of using this method.\n\n        For example::\n\n            >>> print(wid.property('sticks', quiet=True))\n            None\n            >>> wid.apply_property(sticks=ObjectProperty(55, max=10))\n            >>> print(wid.property('sticks', quiet=True))\n            <kivy.properties.ObjectProperty object at 0x04303130>\n        ",
    'EventDispatcher.create_property (line 822)': "Create a new property at runtime.\n\n        .. versionadded:: 1.0.9\n\n        .. versionchanged:: 1.8.0\n            `value` parameter added, can be used to set the default value of the\n            property. Also, the type of the value is used to specialize the\n            created property.\n\n        .. versionchanged:: 1.9.0\n            In the past, if `value` was of type `bool`, a `NumericProperty`\n            would be created, now a `BooleanProperty` is created.\n\n            Also, now and positional and keyword arguments are passed to the\n            property when created.\n\n        .. versionchanged:: 2.0.0\n\n            default_value has been added.\n\n        .. warning::\n\n            This function is designed for the Kivy language, don't use it in\n            your code. You should declare the property in your class instead of\n            using this method.\n\n        :Parameters:\n            `name`: string\n                Name of the property\n            `value`: object, optional\n                Default value of the property. Type is also used for creating\n                more appropriate property types. Defaults to None.\n            `default_value`: bool, True by default\n                If True, `value` will be the default for the property. Otherwise,\n                the property will be initialized with the the property type's\n                normal default value, and subsequently set to ``value``.\n\n        ::\n\n            >>> mywidget = Widget()\n            >>> mywidget.create_property('custom')\n            >>> mywidget.custom = True\n            >>> print(mywidget.custom)\n            True\n        ",
}

