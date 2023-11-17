# encoding: utf-8
# module kivy.properties
# from C:\Users\matthew.muller\.virtualenvs\app-gFbndeE6\Lib\site-packages\kivy\properties.cp311-win_amd64.pyd
# by generator 1.147
"""
Properties
==========

The *Properties* classes are used when you create an
:class:`~kivy.event.EventDispatcher`.

.. warning::
        Kivy's Properties are **not to be confused** with Python's
        properties (i.e. the ``@property`` decorator and the <property> type).

Kivy's property classes support:

    Value Checking / Validation
        When you assign a new value to a property, the value is checked against
        validation constraints. For
        example, validation for an :class:`OptionProperty` will make sure that
        the value is in a predefined list of possibilities. Validation for a
        :class:`NumericProperty` will check that your value is a numeric type.
        This prevents many errors early on.

    Observer Pattern
        You can specify what should happen when a property's value changes.
        You can bind your own function as a callback to changes of a
        :class:`Property`. If, for example, you want a piece of code to be
        called when a widget's :class:`~kivy.uix.widget.Widget.pos` property
        changes, you can :class:`~kivy.event.EventDispatcher.bind` a function
        to it.

    Better Memory Management
        The same instance of a property is shared across multiple widget
        instances.

Comparison Python vs. Kivy
--------------------------

Basic example
~~~~~~~~~~~~~

Let's compare Python and Kivy properties by creating a Python class with 'a'
as a float property::

    class MyClass(object):
        def __init__(self, a=1.0):
            super(MyClass, self).__init__()
            self.a = a

With Kivy, you can do::

    class MyClass(EventDispatcher):
        a = NumericProperty(1.0)


Depth being tracked
~~~~~~~~~~~~~~~~~~~

Only the "top level" of a nested object is being tracked. For example::

    my_list_prop = ListProperty([1, {'hi': 0}])
    # Changing a top level element will trigger all `on_my_list_prop` callbacks
    my_list_prop[0] = 4
    # Changing a deeper element will be ignored by all `on_my_list_prop` callbacks
    my_list_prop[1]['hi'] = 4

The same holds true for all container-type kivy properties.

Value checking
~~~~~~~~~~~~~~

If you wanted to add a check for a minimum / maximum value allowed for a
property, here is a possible implementation in Python::

    class MyClass(object):
        def __init__(self, a=1):
            super(MyClass, self).__init__()
            self.a_min = 0
            self.a_max = 100
            self.a = a

        def _get_a(self):
            return self._a
        def _set_a(self, value):
            if value < self.a_min or value > self.a_max:
                raise ValueError('a out of bounds')
            self._a = value
        a = property(_get_a, _set_a)

The disadvantage is you have to do that work yourself. And it becomes
laborious and complex if you have many properties.
With Kivy, you can simplify the process::

    class MyClass(EventDispatcher):
        a = BoundedNumericProperty(1, min=0, max=100)

That's all!


Error Handling
~~~~~~~~~~~~~~

If setting a value would otherwise raise a ValueError, you have two options to
handle the error gracefully within the property. The first option is to use an
errorvalue parameter. An errorvalue is a substitute for the invalid value::

    # simply returns 0 if the value exceeds the bounds
    bnp = BoundedNumericProperty(0, min=-500, max=500, errorvalue=0)

The second option in to use an errorhandler parameter. An errorhandler is a
callable (single argument function or lambda) which can return a valid
substitute::

    # returns the boundary value when exceeded
    bnp = BoundedNumericProperty(0, min=-500, max=500,
        errorhandler=lambda x: 500 if x > 500 else -500)

Keyword arguments and __init__()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When working with inheritance, namely with the `__init__()` of an object that
inherits from :class:`~kivy.event.EventDispatcher` e.g. a
:class:`~kivy.uix.widget.Widget`, the properties protect
you from a Python 3 object error. This error occurs when passing kwargs to the
`object` instance through a `super()` call::

    class MyClass(EventDispatcher):
        def __init__(self, **kwargs):
            super(MyClass, self).__init__(**kwargs)
            self.my_string = kwargs.get('my_string')

    print(MyClass(my_string='value').my_string)

While this error is silenced in Python 2, it will stop the application
in Python 3 with::

    TypeError: object.__init__() takes no parameters

Logically, to fix that you'd either put `my_string` directly in the
`__init__()` definition as a required argument or as an optional keyword
argument with a default value i.e.::

    class MyClass(EventDispatcher):
        def __init__(self, my_string, **kwargs):
            super(MyClass, self).__init__(**kwargs)
            self.my_string = my_string

or::

    class MyClass(EventDispatcher):
        def __init__(self, my_string='default', **kwargs):
            super(MyClass, self).__init__(**kwargs)
            self.my_string = my_string

Alternatively, you could pop the key-value pair from the `kwargs` dictionary
before calling `super()`::

    class MyClass(EventDispatcher):
        def __init__(self, **kwargs):
            self.my_string = kwargs.pop('my_string')
            super(MyClass, self).__init__(**kwargs)

Kivy properties are more flexible and do the required `kwargs.pop()`
in the background automatically (within the `super()` call
to :class:`~kivy.event.EventDispatcher`) to prevent this distraction::

    class MyClass(EventDispatcher):
        my_string = StringProperty('default')
        def __init__(self, **kwargs):
            super(MyClass, self).__init__(**kwargs)

    print(MyClass(my_string='value').my_string)

Conclusion
~~~~~~~~~~

Kivy properties are easier to use than the standard ones. See the next chapter
for examples of how to use them :)


Observe Property changes
------------------------

As we said in the beginning, Kivy's Properties implement the `Observer pattern
<http://en.wikipedia.org/wiki/Observer_pattern>`_. That means you can
:meth:`~kivy.event.EventDispatcher.bind` to a property and have your own
function called when the value changes.

There are multiple ways to observe the changes.

Observe using bind()
~~~~~~~~~~~~~~~~~~~~

You can observe a property change by using the bind() method outside of the
class::

    class MyClass(EventDispatcher):
        a = NumericProperty(1)

    def callback(instance, value):
        print('My callback is call from', instance)
        print('and the a value changed to', value)

    ins = MyClass()
    ins.bind(a=callback)

    # At this point, any change to the a property will call your callback.
    ins.a = 5    # callback called
    ins.a = 5    # callback not called, because the value did not change
    ins.a = -1   # callback called

.. note::

    Property objects live at the class level and manage the values attached
    to instances. Re-assigning at class level will remove the Property. For
    example, continuing with the code above, `MyClass.a = 5` replaces
    the property object with a simple int.


Observe using 'on_<propname>'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you defined the class yourself, you can use the 'on_<propname>' callback::

    class MyClass(EventDispatcher):
        a = NumericProperty(1)

        def on_a(self, instance, value):
            print('My property a changed to', value)

.. warning::

    Be careful with 'on_<propname>'. If you are creating such a callback on a
    property you are inheriting, you must not forget to call the superclass
    function too.

Binding to properties of properties.
------------------------------------

When binding to a property of a property, for example binding to a numeric
property of an object saved in a object property, updating the object property
to point to a new object will not re-bind the numeric property to the
new object. For example:

.. code-block:: kv

    <MyWidget>:
        Label:
            id: first
            text: 'First label'
        Label:
            id: second
            text: 'Second label'
        Button:
            label: first
            text: self.label.text
            on_press: self.label = second

When clicking on the button, although the label object property has changed
to the second widget, the button text will not change because it is bound to
the text property of the first label directly.

In `1.9.0`, the ``rebind`` option has been introduced that will allow the
automatic updating of the ``text`` when ``label`` is changed, provided it
was enabled. See :class:`ObjectProperty`.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from kivy._metrics import dpi2px

import configparser as __configparser


# functions

def get_color_from_hex(s): # reliably restored by inspect
    """
    Transform a hex string color to a kivy
        :class:`~kivy.graphics.Color`.
    """
    pass

# classes

class Property(object):
    """
    Property(defaultvalue, **kw)
    Base class for building more complex properties.
    
        This class handles all the basic setters and getters, None type handling,
        the observer list and storage initialisation. This class should not be
        directly instantiated.
    
        By default, a :class:`Property` always takes a default value::
    
            class MyObject(Widget):
    
                hello = Property('Hello world')
    
        The default value must be a value that agrees with the Property type. For
        example, you can't set a list to a :class:`StringProperty` because the
        StringProperty will check the default value.
    
        None is a special case: you can set the default value of a Property to
        None, but you can't set None to a property afterward.  If you really want
        to do that, you must declare the Property with `allownone=True`::
    
            class MyObject(Widget):
    
                hello = ObjectProperty(None, allownone=True)
    
            # then later
            a = MyObject()
            a.hello = 'bleh' # working
            a.hello = None # working too, because allownone is True.
    
        :Parameters:
            `default`:
                Specifies the default value for the property.
            `\*\*kwargs`:
                If the parameters include `errorhandler`, this should be a callable
                which must take a single argument and return a valid substitute
                value.
    
                If the parameters include `errorvalue`, this should be an object.
                If set, it will replace an invalid property value (overrides
                errorhandler).
    
                If the parameters include `force_dispatch`, it should be a boolean.
                If True, no value comparison will be done, so the property event
                will be dispatched even if the new value matches the old value (by
                default identical values are not dispatched to avoid infinite
                recursion in two-way binds). Be careful, this is for advanced use only.
    
                `comparator`: callable or None
                    When not None, it's called with two values to be compared.
                    The function returns whether they are considered the same.
    
                `deprecated`: bool
                    When True, a warning will be logged if the property is accessed
                    or set. Defaults to False.
    
        .. versionchanged:: 1.4.2
            Parameters errorhandler and errorvalue added
    
        .. versionchanged:: 1.9.0
            Parameter force_dispatch added
    
        .. versionchanged:: 1.11.0
            Parameter deprecated added
    """
    def bind(self, EventDispatcher_obj, observer): # real signature unknown; restored from __doc__
        """
        Property.bind(self, EventDispatcher obj, observer)
        Add a new observer to be called only when the value is changed.
        """
        pass

    def dispatch(self, EventDispatcher_obj): # real signature unknown; restored from __doc__
        """
        Property.dispatch(self, EventDispatcher obj)
        Dispatch the value change to all observers.
        
                .. versionchanged:: 1.1.0
                    The method is now accessible from Python.
        
                This can be used to force the dispatch of the property, even if the
                value didn't change::
        
                    button = Button()
                    # get the Property class instance
                    prop = button.property('text')
                    # dispatch this property on the button instance
                    prop.dispatch(button)
        """
        pass

    def fbind(self, EventDispatcher_obj, observer, int_ref, tuple_largs=(), dict_kwargs={}): # real signature unknown; restored from __doc__
        """
        Property.fbind(self, EventDispatcher obj, observer, int ref, tuple largs=(), dict kwargs={})
        Similar to bind, except it doesn't check if the observer already
                exists. It also expands and forwards largs and kwargs to the callback.
                funbind or unbind_uid should be called when unbinding.
                It returns a unique positive uid to be used with unbind_uid.
        """
        pass

    def funbind(self, EventDispatcher_obj, observer, tuple_largs=(), dict_kwargs={}): # real signature unknown; restored from __doc__
        """
        Property.funbind(self, EventDispatcher obj, observer, tuple largs=(), dict kwargs={})
        Remove the observer from our widget observer list bound with
                fbind. It removes the first match it finds, as opposed to unbind
                which searches for all matches.
        """
        pass

    def get(self, EventDispatcher_obj): # real signature unknown; restored from __doc__
        """
        Property.get(self, EventDispatcher obj)
        Return the value of the property.
        """
        pass

    def link(self, EventDispatcher_obj, unicode_name): # real signature unknown; restored from __doc__
        """
        Property.link(self, EventDispatcher obj, unicode name) -> PropertyStorage
        Link the instance with its real name.
        
                .. warning::
        
                    Internal usage only.
        
                When a widget is defined and uses a :class:`Property` class, the
                creation of the property object happens, but the instance doesn't know
                anything about its name in the widget class::
        
                    class MyWidget(Widget):
                        uid = NumericProperty(0)
        
                In this example, the uid will be a NumericProperty() instance, but the
                property instance doesn't know its name. That's why :meth:`link` is
                used in `Widget.__new__`. The link function is also used to create the
                storage space of the property for this specific widget instance.
        """
        return PropertyStorage

    def link_deps(self, EventDispatcher_obj, unicode_name): # real signature unknown; restored from __doc__
        """ Property.link_deps(self, EventDispatcher obj, unicode name) """
        pass

    def link_eagerly(self, EventDispatcher_obj): # real signature unknown; restored from __doc__
        """ Property.link_eagerly(self, EventDispatcher obj) -> PropertyStorage """
        return PropertyStorage

    def set(self, EventDispatcher_obj, value): # real signature unknown; restored from __doc__
        """
        Property.set(self, EventDispatcher obj, value)
        Set a new value for the property.
        """
        pass

    def set_name(self, EventDispatcher_obj, unicode_name): # real signature unknown; restored from __doc__
        """ Property.set_name(self, EventDispatcher obj, unicode name) """
        pass

    def unbind(self, EventDispatcher_obj, observer, int_stop_on_first=0): # real signature unknown; restored from __doc__
        """
        Property.unbind(self, EventDispatcher obj, observer, int stop_on_first=0)
        Remove the observer from our widget observer list.
        """
        pass

    def unbind_uid(self, EventDispatcher_obj, uid): # real signature unknown; restored from __doc__
        """
        Property.unbind_uid(self, EventDispatcher obj, uid)
        Remove the observer from our widget observer list bound with
                fbind using the uid.
        """
        pass

    def __delete__(self, *args, **kwargs): # real signature unknown
        """ Delete an attribute of instance. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, defaultvalue, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Property.__reduce_cython__(self) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Property.__setstate_cython__(self, __pyx_state) """
        pass

    def __set_name__(self, owner, name): # real signature unknown; restored from __doc__
        """ Property.__set_name__(self, owner, name) """
        pass

    def __set__(self, *args, **kwargs): # real signature unknown
        """ Set an attribute of instance to value. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    defaultvalue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """defaultvalue: object"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E6F40>'


class AliasProperty(Property):
    """
    AliasProperty(getter, setter=None, rebind=False, watch_before_use=True, **kwargs)
    Create a property with a custom getter and setter.
    
        If you don't find a Property class that fits to your needs, you can make
        your own by creating custom Python getter and setter methods.
    
        Example from kivy/uix/widget.py where `x` and `width` are instances of
        :class:`NumericProperty`::
    
            def get_right(self):
                return self.x + self.width
            def set_right(self, value):
                self.x = value - self.width
            right = AliasProperty(get_right, set_right, bind=['x', 'width'])
    
        If `x` were a non Kivy property then you have to return `True` from setter
        to dispatch new value of `right`::
    
            def set_right(self, value):
                self.x = value - self.width
                return True
    
        Usually `bind` list should contain all Kivy properties used in getter
        method. If you return `True` it will cause a dispatch which one should do
        when the property value has changed, but keep in mind that the property
        could already have dispatched the changed value if a kivy property the
        alias property is bound was set in the setter, causing a second dispatch
        if the setter returns `True`.
    
        If you want to cache the value returned by getter then pass `cache=True`.
        This way getter will only be called if new value is set or one of the
        binded properties changes. In both cases new value of alias property will
        be cached again.
    
        To make property readonly pass `None` as setter. This way `AttributeError`
        will be raised on every set attempt::
    
            right = AliasProperty(get_right, None, bind=['x', 'width'], cache=True)
    
        :Parameters:
            `getter`: function
                Function to use as a property getter.
            `setter`: function
                Function to use as a property setter. Callbacks bound to the
                alias property won't be called when the property is set (e.g.
                `right = 10`), unless the setter returns `True`.
            `bind`: list/tuple
                Properties to observe for changes as property name strings.
                Changing values of this properties will dispatch value of the
                alias property.
            `cache`: boolean
                If `True`, the value will be cached until one of the binded
                elements changes or if setter returns `True`.
            `rebind`: bool, defaults to `False`
                See :class:`ObjectProperty` for details.
            `watch_before_use`: bool, defaults to ``True``
                Whether the ``bind`` properties are tracked (bound) before this
                property is used in any way.
    
                By default, the getter is called if the ``bind`` properties update
                or if the property value (unless cached) is read. As an
                optimization to speed up widget creation, when ``watch_before_use``
                is False, we only track the bound properties once this property is
                used in any way (i.e. it is bound, it was set/read, etc).
    
                The property value read/set/bound will be correct as expected in
                both cases. The difference is only that when ``False``, any side
                effects from the ``getter`` would not occur until this property is
                interacted with in any way because the ``getter`` won't be called
                early.
    
        .. versionchanged:: 1.9.0
            `rebind` has been introduced.
    
        .. versionchanged:: 1.4.0
            Parameter `cache` added.
    """
    def get(self, EventDispatcher_obj): # real signature unknown; restored from __doc__
        """ AliasProperty.get(self, EventDispatcher obj) """
        pass

    def link_deps(self, EventDispatcher_obj, unicode_name): # real signature unknown; restored from __doc__
        """ AliasProperty.link_deps(self, EventDispatcher obj, unicode name) """
        pass

    def link_eagerly(self, EventDispatcher_obj): # real signature unknown; restored from __doc__
        """ AliasProperty.link_eagerly(self, EventDispatcher obj) -> PropertyStorage """
        return PropertyStorage

    def set(self, EventDispatcher_obj, value): # real signature unknown; restored from __doc__
        """ AliasProperty.set(self, EventDispatcher obj, value) """
        pass

    def trigger_change(self, EventDispatcher_obj, value): # real signature unknown; restored from __doc__
        """ AliasProperty.trigger_change(self, EventDispatcher obj, value) """
        pass

    def __init__(self, getter, setter=None, rebind=False, watch_before_use=True, **kwargs): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __read_only(self, _obj, _value): # real signature unknown; restored from __doc__
        """ AliasProperty.__read_only(self, _obj, _value) """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ AliasProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ AliasProperty.__setstate_cython__(self, __pyx_state) """
        pass

    rebind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """rebind: 'int'"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E7D80>'


class PropertyStorage(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class AliasPropertyStorage(PropertyStorage):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class BooleanProperty(Property):
    """
    BooleanProperty(defaultvalue=True, **kw)
    Property that represents only a boolean value.
    
        :Parameters:
            `defaultvalue`: boolean
                Specifies the default value of the property.
    """
    def __init__(self, defaultvalue=True, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ BooleanProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ BooleanProperty.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E6D90>'


class BoundedNumericProperty(Property):
    """
    BoundedNumericProperty(*largs, **kw)
    Property that represents a numeric value within a minimum bound and/or
        maximum bound -- within a numeric range.
    
        :Parameters:
            `default`: numeric
                Specifies the default value of the property.
            `\*\*kwargs`: a list of keyword arguments
                If a `min` parameter is included, this specifies the minimum
                numeric value that will be accepted.
                If a `max` parameter is included, this specifies the maximum
                numeric value that will be accepted.
    """
    def get_max(self, EventDispatcher_obj): # real signature unknown; restored from __doc__
        """
        BoundedNumericProperty.get_max(self, EventDispatcher obj)
        Return the maximum value acceptable for the BoundedNumericProperty
                in `obj`. Return None if no maximum value is set. Check
                :attr:`get_min` for a usage example.
        
                .. versionadded:: 1.1.0
        """
        pass

    def get_min(self, EventDispatcher_obj): # real signature unknown; restored from __doc__
        """
        BoundedNumericProperty.get_min(self, EventDispatcher obj)
        Return the minimum value acceptable for the BoundedNumericProperty
                in `obj`. Return None if no minimum value is set::
        
                    class MyWidget(Widget):
                        number = BoundedNumericProperty(0, min=-5, max=5)
        
                    widget = MyWidget()
                    print(widget.property('number').get_min(widget))
                    # will output -5
        
                .. versionadded:: 1.1.0
        """
        pass

    def set_max(self, EventDispatcher_obj, value): # real signature unknown; restored from __doc__
        """
        BoundedNumericProperty.set_max(self, EventDispatcher obj, value)
        Change the maximum value acceptable for the BoundedNumericProperty,
                only for the `obj` instance. Set to None if you want to disable it.
                Check :attr:`set_min` for a usage example.
        
                .. warning::
        
                    Changing the bounds doesn't revalidate the current value.
        
                .. versionadded:: 1.1.0
        """
        pass

    def set_min(self, EventDispatcher_obj, value): # real signature unknown; restored from __doc__
        """
        BoundedNumericProperty.set_min(self, EventDispatcher obj, value)
        Change the minimum value acceptable for the BoundedNumericProperty,
                only for the `obj` instance. Set to None if you want to disable it::
        
                    class MyWidget(Widget):
                        number = BoundedNumericProperty(0, min=-5, max=5)
        
                    widget = MyWidget()
                    # change the minimum to -10
                    widget.property('number').set_min(widget, -10)
                    # or disable the minimum check
                    widget.property('number').set_min(widget, None)
        
                .. warning::
        
                    Changing the bounds doesn't revalidate the current value.
        
                .. versionadded:: 1.1.0
        """
        pass

    def __init__(self, *largs, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ BoundedNumericProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ BoundedNumericProperty.__setstate_cython__(self, __pyx_state) """
        pass

    bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return min/max of the value.

        .. versionadded:: 1.0.9
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E6E50>'


class BoundedNumericPropertyStorage(PropertyStorage):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ColorProperty(Property):
    """
    ColorProperty(defaultvalue=0, **kw)
    Property that represents a color. The assignment can take either:
    
        - a collection of 3 or 4 float values between 0-1 (kivy default)
        - a string in the format #rrggbb or #rrggbbaa
        - a string representing color name (eg. 'red', 'yellow', 'green')
    
        Object :obj:`~kivy.utils.colormap` is used to retrieve color from color
        name and names definitions can be found at this
        `link <https://www.w3.org/TR/SVG11/types.html#ColorKeywords>`_. Color can
        be assigned in different formats, but it will be returned as
        :class:`~kivy.properties.ObservableList` of 4 float elements with values
        between 0-1.
    
        :Parameters:
            `defaultvalue`: list or string, defaults to [1.0, 1.0, 1.0, 1.0]
                Specifies the default value of the property.
    
        .. versionadded:: 1.10.0
    
        .. versionchanged:: 2.0.0
            Color value will be dispatched when set through indexing or slicing,
            but when setting with slice you must ensure that slice has 4 components
            with float values between 0-1.
            Assingning color name as value is now supported.
            Value `None` is allowed as default value for property.
    """
    def __init__(self, defaultvalue=0, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ColorProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ColorProperty.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E77E0>'


class ConfigParser(__configparser.RawConfigParser, object):
    """
    Enhanced ConfigParser class that supports the addition of default
        sections and default values.
    
        By default, the kivy ConfigParser instance, :attr:`~kivy.config.Config`,
        is named `'kivy'` and the ConfigParser instance used by the
        :meth:`App.build_settings <~kivy.app.App.build_settings>` method is named
        `'app'`.
    
        :Parameters:
            `name`: string
                The name of the instance. See :attr:`name`. Defaults to `''`.
    
        .. versionchanged:: 1.9.0
            Each ConfigParser can now be :attr:`named <name>`. You can get the
            ConfigParser associated with a name using :meth:`get_configparser`.
            In addition, you can now control the config values with
            :class:`~kivy.properties.ConfigParserProperty`.
    
        .. versionadded:: 1.0.7
    """
    def adddefaultsection(self, section): # reliably restored by inspect
        """ Add a section if the section is missing. """
        pass

    def add_callback(self, callback, section=None, key=None): # reliably restored by inspect
        """
        Add a callback to be called when a specific section or key has
                changed. If you don't specify a section or key, it will call the
                callback for all section/key changes.
        
                Callbacks will receive 3 arguments: the section, key and value.
        
                .. versionadded:: 1.4.1
        """
        pass

    def get(self, section, option, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def getdefault(self, section, option, defaultvalue): # reliably restored by inspect
        """
        Get the value of an option in the specified section. If not found,
                it will return the default value.
        """
        pass

    def getdefaultint(self, section, option, defaultvalue): # reliably restored by inspect
        """
        Get the value of an option in the specified section. If not found,
                it will return the default value. The value will always be
                returned as an integer.
        
                .. versionadded:: 1.6.0
        """
        pass

    def get_configparser(name): # reliably restored by inspect
        """
        Returns the :class:`ConfigParser` instance whose name is `name`, or
                None if not found.
        
                :Parameters:
                    `name`: string
                        The name of the :class:`ConfigParser` instance to return.
        """
        pass

    def read(self, filename): # reliably restored by inspect
        """
        Read only one filename. In contrast to the original ConfigParser of
                Python, this one is able to read only one file at a time. The last
                read file will be used for the :meth:`write` method.
        
                .. versionchanged:: 1.9.0
                    :meth:`read` now calls the callbacks if read changed any values.
        """
        pass

    def remove_callback(self, callback, section=None, key=None): # reliably restored by inspect
        """
        Removes a callback added with :meth:`add_callback`.
                :meth:`remove_callback` must be called with the same parameters as
                :meth:`add_callback`.
        
                Raises a `ValueError` if not found.
        
                .. versionadded:: 1.9.0
        """
        pass

    def set(self, section, option, value): # reliably restored by inspect
        """
        Functions similarly to PythonConfigParser's set method, except that
                the value is implicitly converted to a string.
        """
        pass

    def setall(self, section, keyvalues): # reliably restored by inspect
        """
        Sets multiple key-value pairs in a section. keyvalues should be a
                dictionary containing the key-value pairs to be set.
        """
        pass

    def setdefault(self, section, option, value): # reliably restored by inspect
        """ Set the default value for an option in the specified section. """
        pass

    def setdefaults(self, section, keyvalues): # reliably restored by inspect
        """
        Set multiple key-value defaults in a section. keyvalues should be
                a dictionary containing the new key-value defaults.
        """
        pass

    def update_config(self, filename, overwrite=False): # reliably restored by inspect
        """
        Upgrade the configuration based on a new default config file.
                Overwrite any existing values if overwrite is True.
        """
        pass

    def write(self): # reliably restored by inspect
        """
        Write the configuration to the last file opened using the
                :meth:`read` method.
        
                Return True if the write finished successfully, False otherwise.
        """
        pass

    def _do_callbacks(self, section, key, value): # reliably restored by inspect
        # no doc
        pass

    def _register_named_property(name, widget_ref, *largs): # reliably restored by inspect
        """
        Called by the ConfigParserProperty to register a property which
                was created with a config name instead of a config object.
        
                When a ConfigParser with this name is later created, the properties
                are then notified that this parser now exists so they can use it.
                If the parser already exists, the property is notified here. See
                :meth:`~kivy.properties.ConfigParserProperty.set_config`.
        
                :Parameters:
                    `name`: a non-empty string
                        The name of the ConfigParser that is associated with the
                        property. See :attr:`name`.
                    `widget_ref`: 2-tuple.
                        The first element is a reference to the widget containing the
                        property, the second element is the name of the property. E.g.:
        
                            class House(Widget):
                                address = ConfigParserProperty('', 'info', 'street',
                                    'directory')
        
                        Then, the first element is a ref to a House instance, and the
                        second is `'address'`.
        """
        pass

    def __init__(self, name=None, **kwargs): # reliably restored by inspect
        # no doc
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ The name associated with this ConfigParser instance, if not `''`.
        Defaults to `''`. It can be safely changed dynamically or set to `''`.

        When a ConfigParser is given a name, that config object can be
        retrieved using :meth:`get_configparser`. In addition, that config
        instance can also be used with a
        :class:`~kivy.properties.ConfigParserProperty` instance that set its
        `config` value to this name.

        Setting more than one ConfigParser with the same name will raise a
        `ValueError`.
        """


    _abc_impl = None # (!) real value is '<_abc._abc_data object at 0x0000021F770D26C0>'
    _name = ''
    _named_configs = {
        'kivy': (
            None, # (!) real value is "<weakref at 0x0000021F770BE430; to 'ConfigParser' at 0x0000021F770D3090>"
            [],
        ),
    }
    __abstractmethods__ = frozenset()


class ConfigParserProperty(Property):
    """
    ConfigParserProperty(defaultvalue, section, key, config, **kw)
     Property that allows one to bind to changes in the configuration values
        of a :class:`~kivy.config.ConfigParser` as well as to bind the ConfigParser
        values to other properties.
    
        A ConfigParser is composed of sections, where each section has a number of
        keys and values associated with these keys. ConfigParserProperty lets
        you automatically listen to and change the values of specified keys based
        on other kivy properties.
    
        For example, say we want to have a TextInput automatically write
        its value, represented as an int, in the `info` section of a ConfigParser.
        Also, the textinputs should update its values from the ConfigParser's
        fields. Finally, their values should be displayed in a label. In py::
    
            class Info(Label):
    
                number = ConfigParserProperty(0, 'info', 'number', 'example',
                                              val_type=int, errorvalue=41)
    
                def __init__(self, **kw):
                    super(Info, self).__init__(**kw)
                    config = ConfigParser(name='example')
    
        The above code creates a property that is connected to the `number` key in
        the `info` section of the ConfigParser named `example`. Initially, this
        ConfigParser doesn't exist. Then, in `__init__`, a ConfigParser is created
        with name `example`, which is then automatically linked with this property.
        then in kv:
    
        .. code-block:: kv
    
            BoxLayout:
                TextInput:
                    id: number
                    text: str(info.number)
                Info:
                    id: info
                    number: number.text
                    text: 'Number: {}'.format(self.number)
    
        You'll notice that we have to do `text: str(info.number)`, this is because
        the value of this property is always an int, because we specified `int` as
        the `val_type`. However, we can assign anything to the property, e.g.
        `number: number.text` which assigns a string, because it is instantly
        converted with the `val_type` callback.
    
        .. note::
    
            If a file has been opened for this ConfigParser using
            :meth:`~kivy.config.ConfigParser.read`, then
            :meth:`~kivy.config.ConfigParser.write` will be called every property
            change, keeping the file updated.
    
        .. warning::
    
            It is recommend that the config parser object be assigned to the
            property after the kv tree has been constructed (e.g. schedule on next
            frame from init). This is because the kv tree and its properties, when
            constructed, are evaluated on its own order, therefore, any initial
            values in the parser might be overwritten by objects it's bound to.
            So in the example above, the TextInput might be initially empty,
            and if `number: number.text` is evaluated before
            `text: str(info.number)`, the config value will be overwritten with the
            (empty) text value.
    
        :Parameters:
            `default`: object type
                Specifies the default value for the key. If the parser associated
                with this property doesn't have this section or key, it'll be
                created with the current value, which is the default value
                initially.
            `section`: string type
                The section in the ConfigParser where the key / value will be
                written. Must be provided. If the section doesn't exist, it'll be
                created.
            `key`: string type
                The key in section `section` where the value will be written to.
                Must be provided. If the key doesn't exist, it'll be created and
                the current value written to it, otherwise its value will be used.
            `config`: string or :class:`~kivy.config.ConfigParser` instance.
                The ConfigParser instance to associate with this property if
                not None. If it's a string, the ConfigParser instance whose
                :attr:`~kivy.config.ConfigParser.name` is the value of `config`
                will be used. If no such parser exists yet, whenever a ConfigParser
                with this name is created, it will automatically be linked to this
                property.
    
                Whenever a ConfigParser becomes linked with a property, if the
                section or key doesn't exist, the current property value will be
                used to create that key, otherwise, the existing key value will be
                used for the property value; overwriting its current value. You can
                change the ConfigParser associated with this property if a string
                was used here, by changing the
                :attr:`~kivy.config.ConfigParser.name` of an existing or new
                ConfigParser instance. Or through :meth:`set_config`.
            `\*\*kwargs`: a list of keyword arguments
                `val_type`: a callable object
                    The key values are saved in the ConfigParser as strings. When
                    the ConfigParser value is read internally and assigned to the
                    property or when the user changes the property value directly,
                    if `val_type` is not None, it will be called with the new value
                    as input and it should return the value converted to the proper
                    type accepted ny this property. For example, if the property
                    represent ints, `val_type` can simply be `int`.
    
                    If the `val_type` callback raises a `ValueError`, `errorvalue`
                    or `errorhandler` will be used if provided. Tip: the
                    `getboolean` function of the ConfigParser might also be useful
                    here to convert to a boolean type.
                `verify`: a callable object
                    Can be used to restrict the allowable values of the property.
                    For every value assigned to the property, if this is specified,
                    `verify` is called with the new value, and if it returns `True`
                    the value is accepted, otherwise, `errorvalue` or
                    `errorhandler` will be used if provided or a `ValueError` is
                    raised.
    
        .. versionadded:: 1.9.0
    """
    def link_deps(self, EventDispatcher_obj, unicode_name): # real signature unknown; restored from __doc__
        """ ConfigParserProperty.link_deps(self, EventDispatcher obj, unicode name) """
        pass

    def set(self, EventDispatcher_obj, value): # real signature unknown; restored from __doc__
        """ ConfigParserProperty.set(self, EventDispatcher obj, value) """
        pass

    def set_config(self, config): # real signature unknown; restored from __doc__
        """
        ConfigParserProperty.set_config(self, config)
         Sets the ConfigParser object to be used by this property. Normally,
                the ConfigParser is set when initializing the Property using the
                `config` parameter.
        
                :Parameters:
                    `config`: A :class:`~kivy.config.ConfigParser` instance.
                        The instance to use for listening to and saving property value
                        changes. If None, it disconnects the currently used
                        `ConfigParser`.
        
                ::
        
                    class MyWidget(Widget):
                        username = ConfigParserProperty('', 'info', 'name', None)
        
                    widget = MyWidget()
                    widget.property('username').set_config(ConfigParser())
        """
        pass

    def _edit_setting(self, section, key, value): # real signature unknown; restored from __doc__
        """ ConfigParserProperty._edit_setting(self, section, key, value) """
        pass

    def __init__(self, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ConfigParserProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ConfigParserProperty.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E7780>'


class DictProperty(Property):
    """
    DictProperty(defaultvalue=0, rebind=False, **kw)
    Property that represents a dict.
    
        :Parameters:
            `defaultvalue`: dict, defaults to {}
                Specifies the default value of the property.
            `rebind`: bool, defaults to False
                See :class:`ObjectProperty` for details.
    
        .. versionchanged:: 1.9.0
            `rebind` has been introduced.
    
        .. warning::
    
            Similar to :class:`ListProperty`, when assigning a dict to a
            :class:`DictProperty`, the dict stored in the property is a shallow copy of the
            dict and not the original dict. See :class:`ListProperty` for details.
    """
    def link(self, EventDispatcher_obj, unicode_name): # real signature unknown; restored from __doc__
        """ DictProperty.link(self, EventDispatcher obj, unicode name) -> PropertyStorage """
        return PropertyStorage

    def set(self, EventDispatcher_obj, value): # real signature unknown; restored from __doc__
        """ DictProperty.set(self, EventDispatcher obj, value) """
        pass

    def __init__(self, defaultvalue=0, rebind=False, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ DictProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ DictProperty.__setstate_cython__(self, __pyx_state) """
        pass

    rebind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """rebind: 'int'"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E6CD0>'


class ListProperty(Property):
    """
    ListProperty(defaultvalue=0, **kw)
    Property that represents a list.
    
        :Parameters:
            `defaultvalue`: list, defaults to []
                Specifies the default value of the property.
    
        .. warning::
    
            When assigning a list to a :class:`ListProperty`, the list stored in
            the property is a shallow copy of the list and not the original list. This can
            be demonstrated with the following example::
    
                >>> class MyWidget(Widget):
                >>>     my_list = ListProperty([])
    
                >>> widget = MyWidget()
                >>> my_list = [1, 5, {'hi': 'hello'}]
                >>> widget.my_list = my_list
                >>> print(my_list is widget.my_list)
                False
                >>> my_list.append(10)
                >>> print(my_list, widget.my_list)
                [1, 5, {'hi': 'hello'}, 10] [1, 5, {'hi': 'hello'}]
    
            However, changes to nested levels will affect the property as well,
            since the property uses a shallow copy of my_list.
    
                >>> my_list[2]['hi'] = 'bye'
                >>> print(my_list, widget.my_list)
                [1, 5, {'hi': 'bye'}, 10] [1, 5, {'hi': 'bye'}]
    """
    def link(self, EventDispatcher_obj, unicode_name): # real signature unknown; restored from __doc__
        """ ListProperty.link(self, EventDispatcher obj, unicode name) -> PropertyStorage """
        return PropertyStorage

    def set(self, EventDispatcher_obj, value): # real signature unknown; restored from __doc__
        """ ListProperty.set(self, EventDispatcher obj, value) """
        pass

    def __init__(self, defaultvalue=0, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ListProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ListProperty.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E6C70>'


class NumericProperty(Property):
    """
    NumericProperty(defaultvalue=0, **kw)
    Property that represents a numeric value.
    
        It only accepts the int or float numeric data type or a string that can be
        converted to a number as shown below. For other numeric types use ObjectProperty
        or use errorhandler to convert it to an int/float.
    
        It does not support numpy numbers so they must be manually converted to int/float.
        E.g. ``widget.num = np.arange(4)[0]`` will raise an exception. Numpy arrays are not
        supported at all, even by ObjectProperty because their comparison does not return
        a bool. But if you must use a Kivy property, use a ObjectProperty with ``comparator``
        set to ``np.array_equal``. E.g.::
    
            >>> class A(EventDispatcher):
            ...     data = ObjectProperty(comparator=np.array_equal)
            >>> a = A()
            >>> a.bind(data=print)
            >>> a.data = np.arange(2)
            <__main__.A object at 0x000001C839B50208> [0 1]
            >>> a.data = np.arange(3)
            <__main__.A object at 0x000001C839B50208> [0 1 2]
    
        :Parameters:
            `defaultvalue`: int or float, defaults to 0
                Specifies the default value of the property.
    
        >>> wid = Widget()
        >>> wid.x = 42
        >>> print(wid.x)
        42
        >>> wid.x = "plop"
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
           File "properties.pyx", line 93, in kivy.properties.Property.__set__
           File "properties.pyx", line 111, in kivy.properties.Property.set
           File "properties.pyx", line 159, in kivy.properties.NumericProperty.check
         ValueError: NumericProperty accept only int/float
    
        .. versionchanged:: 1.4.1
            NumericProperty can now accept custom text and tuple value to indicate a
            type, like "in", "pt", "px", "cm", "mm", in the format: '10pt' or (10,
            'pt').
    """
    def get_format(self, EventDispatcher_obj): # real signature unknown; restored from __doc__
        """
        NumericProperty.get_format(self, EventDispatcher obj)
        
                Return the format used for Numeric calculation. Default is px (mean
                the value have not been changed at all). Otherwise, it can be one of
                'in', 'pt', 'cm', 'mm'.
        """
        pass

    def _dpi_callback(self, obj, _obj, _value): # real signature unknown; restored from __doc__
        """ NumericProperty._dpi_callback(self, obj, _obj, _value) """
        pass

    def __init__(self, defaultvalue=0, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ NumericProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ NumericProperty.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E70F0>'


class NumericPropertyStorage(PropertyStorage):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ObjectProperty(Property):
    """
    ObjectProperty(defaultvalue=None, rebind=False, **kw)
    Property that represents a Python object.
    
        :Parameters:
            `defaultvalue`: object type
                Specifies the default value of the property.
            `rebind`: bool, defaults to False
                Whether kv rules using this object as an intermediate attribute
                in a kv rule, will update the bound property when this object
                changes.
    
                That is the standard behavior is that if there's a kv rule
                ``text: self.a.b.c.d``, where ``a``, ``b``, and ``c`` are
                properties with ``rebind`` ``False`` and ``d`` is a
                :class:`StringProperty`. Then when the rule is applied, ``text``
                becomes bound only to ``d``. If ``a``, ``b``, or ``c`` change,
                ``text`` still remains bound to ``d``. Furthermore, if any of them
                were ``None`` when the rule was initially evaluated, e.g. ``b`` was
                ``None``; then ``text`` is bound to ``b`` and will not become bound
                to ``d`` even when ``b`` is changed to not be ``None``.
    
                By setting ``rebind`` to ``True``, however, the rule will be
                re-evaluated and all the properties rebound when that intermediate
                property changes. E.g. in the example above, whenever ``b`` changes
                or becomes not ``None`` if it was ``None`` before, ``text`` is
                evaluated again and becomes rebound to ``d``. The overall result is
                that ``text`` is now bound to all the properties among ``a``,
                ``b``, or ``c`` that have ``rebind`` set to ``True``.
            `\*\*kwargs`: a list of keyword arguments
                `baseclass`
                    If kwargs includes a `baseclass` argument, this value will be
                    used for validation: `isinstance(value, kwargs['baseclass'])`.
    
        .. warning::
    
            To mark the property as changed, you must reassign a new python object.
    
        .. versionchanged:: 1.9.0
            `rebind` has been introduced.
    
        .. versionchanged:: 1.7.0
    
            `baseclass` parameter added.
    """
    def __init__(self, defaultvalue=None, rebind=False, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ObjectProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ObjectProperty.__setstate_cython__(self, __pyx_state) """
        pass

    rebind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """rebind: 'int'"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E6D30>'


class ObservableDict(dict):
    # no doc
    def clear(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableDict.clear(self, *largs) """
        pass

    def pop(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableDict.pop(self, *largs) """
        pass

    def popitem(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableDict.popitem(self, *largs) """
        pass

    def remove(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableDict.remove(self, *largs) """
        pass

    def setdefault(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableDict.setdefault(self, *largs) """
        pass

    def update(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableDict.update(self, *largs) """
        pass

    def _weak_return(self, item): # real signature unknown; restored from __doc__
        """ ObservableDict._weak_return(self, item) """
        pass

    def __delitem__(self, key): # real signature unknown; restored from __doc__
        """ ObservableDict.__delitem__(self, key) """
        pass

    def __getattr__(self, attr): # real signature unknown; restored from __doc__
        """ ObservableDict.__getattr__(self, attr) """
        pass

    def __init__(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableDict.__init__(self, *largs) """
        pass

    def __setattr__(self, attr, value): # real signature unknown; restored from __doc__
        """ ObservableDict.__setattr__(self, attr, value) """
        pass

    def __setitem__(self, key, value): # real signature unknown; restored from __doc__
        """ ObservableDict.__setitem__(self, key, value) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.properties', '__init__': <cyfunction ObservableDict.__init__ at 0x0000021F77384860>, '_weak_return': <cyfunction ObservableDict._weak_return at 0x0000021F77384930>, '__getattr__': <cyfunction ObservableDict.__getattr__ at 0x0000021F77384A00>, '__setattr__': <cyfunction ObservableDict.__setattr__ at 0x0000021F77384AD0>, '__setitem__': <cyfunction ObservableDict.__setitem__ at 0x0000021F77384C70>, '__delitem__': <cyfunction ObservableDict.__delitem__ at 0x0000021F77384D40>, 'clear': <cyfunction ObservableDict.clear at 0x0000021F77384E10>, 'remove': <cyfunction ObservableDict.remove at 0x0000021F77384EE0>, 'pop': <cyfunction ObservableDict.pop at 0x0000021F77384FB0>, 'popitem': <cyfunction ObservableDict.popitem at 0x0000021F77384BA0>, 'setdefault': <cyfunction ObservableDict.setdefault at 0x0000021F77385080>, 'update': <cyfunction ObservableDict.update at 0x0000021F77385150>, '__dict__': <attribute '__dict__' of 'ObservableDict' objects>, '__weakref__': <attribute '__weakref__' of 'ObservableDict' objects>, '__doc__': None})"


class ObservableList(list):
    # no doc
    def append(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableList.append(self, *largs) """
        pass

    def extend(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableList.extend(self, *largs) """
        pass

    def insert(self, i, x): # real signature unknown; restored from __doc__
        """ ObservableList.insert(self, i, x) """
        pass

    def pop(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableList.pop(self, *largs) """
        pass

    def remove(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableList.remove(self, *largs) """
        pass

    def reverse(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableList.reverse(self, *largs) """
        pass

    def sort(self, *largs, **kwargs): # real signature unknown; restored from __doc__
        """ ObservableList.sort(self, *largs, **kwargs) """
        pass

    def __delitem__(self, key): # real signature unknown; restored from __doc__
        """ ObservableList.__delitem__(self, key) """
        pass

    def __delslice__(self, b, c): # real signature unknown; restored from __doc__
        """ ObservableList.__delslice__(self, b, c) """
        pass

    def __iadd__(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableList.__iadd__(self, *largs) """
        pass

    def __imul__(self, b): # real signature unknown; restored from __doc__
        """ ObservableList.__imul__(self, b) """
        pass

    def __init__(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableList.__init__(self, *largs) """
        pass

    def __setitem__(self, key, value): # real signature unknown; restored from __doc__
        """ ObservableList.__setitem__(self, key, value) """
        pass

    def __setslice__(self, b, c, v): # real signature unknown; restored from __doc__
        """ ObservableList.__setslice__(self, b, c, v) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.properties', '__init__': <cyfunction ObservableList.__init__ at 0x0000021F771342B0>, '__setitem__': <cyfunction ObservableList.__setitem__ at 0x0000021F77134380>, '__delitem__': <cyfunction ObservableList.__delitem__ at 0x0000021F772EA9B0>, '__setslice__': <cyfunction ObservableList.__setslice__ at 0x0000021F772EAA80>, '__delslice__': <cyfunction ObservableList.__delslice__ at 0x0000021F772EB5E0>, '__iadd__': <cyfunction ObservableList.__iadd__ at 0x0000021F773841E0>, '__imul__': <cyfunction ObservableList.__imul__ at 0x0000021F773842B0>, 'append': <cyfunction ObservableList.append at 0x0000021F77384380>, 'remove': <cyfunction ObservableList.remove at 0x0000021F77384450>, 'insert': <cyfunction ObservableList.insert at 0x0000021F772EAB50>, 'pop': <cyfunction ObservableList.pop at 0x0000021F77384520>, 'extend': <cyfunction ObservableList.extend at 0x0000021F773845F0>, 'sort': <cyfunction ObservableList.sort at 0x0000021F773846C0>, 'reverse': <cyfunction ObservableList.reverse at 0x0000021F77384790>, '__dict__': <attribute '__dict__' of 'ObservableList' objects>, '__weakref__': <attribute '__weakref__' of 'ObservableList' objects>, '__doc__': None})"


class ObservableReferenceList(ObservableList):
    # no doc
    def __init__(self, *largs): # real signature unknown; restored from __doc__
        """ ObservableList.__init__(self, *largs) """
        pass

    def __setitem__(self, key, value, update_properties=True): # real signature unknown; restored from __doc__
        """ ObservableReferenceList.__setitem__(self, key, value, update_properties=True) """
        pass

    def __setslice__(self, start, stop, value, update_properties=True): # real signature unknown; restored from __doc__
        """ ObservableReferenceList.__setslice__(self, start, stop, value, update_properties=True) """
        pass


class OptionProperty(Property):
    """
    OptionProperty(*largs, **kw)
    Property that represents a string from a predefined list of valid
        options.
    
        If the string set in the property is not in the list of valid options
        (passed at property creation time), a ValueError exception will be raised.
    
        :Parameters:
            `default`: any valid type in the list of options
                Specifies the default value of the property.
            `\*\*kwargs`: a list of keyword arguments
                Should include an `options` parameter specifying a list (not tuple)
                of valid options.
    
        For example::
    
            class MyWidget(Widget):
                state = OptionProperty("None", options=["On", "Off", "None"])
    """
    def __init__(self, *largs, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ OptionProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ OptionProperty.__setstate_cython__(self, __pyx_state) """
        pass

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the options available.

        .. versionadded:: 1.0.9
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E6EE0>'


class OptionPropertyStorage(PropertyStorage):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


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


    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x0000021F74D2C3D0>, '__repr__': <slot wrapper '__repr__' of 'functools.partial' objects>, '__call__': <slot wrapper '__call__' of 'functools.partial' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'functools.partial' objects>, '__setattr__': <slot wrapper '__setattr__' of 'functools.partial' objects>, '__delattr__': <slot wrapper '__delattr__' of 'functools.partial' objects>, '__reduce__': <method '__reduce__' of 'functools.partial' objects>, '__setstate__': <method '__setstate__' of 'functools.partial' objects>, '__class_getitem__': <method '__class_getitem__' of 'functools.partial' objects>, 'func': <member 'func' of 'functools.partial' objects>, 'args': <member 'args' of 'functools.partial' objects>, 'keywords': <member 'keywords' of 'functools.partial' objects>, '__vectorcalloffset__': <member '__vectorcalloffset__' of 'functools.partial' objects>, '__dict__': <attribute '__dict__' of 'functools.partial' objects>, '__doc__': 'partial(func, *args, **keywords) - new function with partial application\\n    of the given arguments and keywords.\\n', '__module__': 'functools'})"


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



class ReferenceListProperty(Property):
    """
    ReferenceListProperty(*largs, **kw)
    Property that allows the creation of a tuple of other properties.
    
        For example, if `x` and `y` are :class:`NumericProperty`\s, we can create a
        :class:`ReferenceListProperty` for the `pos`. If you change the value of
        `pos`, it will automatically change the values of `x` and `y` accordingly.
        If you read the value of `pos`, it will return a tuple with the values of
        `x` and `y`.
    
        For example::
    
            class MyWidget(EventDispatcher):
                x = NumericProperty(0)
                y = NumericProperty(0)
                pos = ReferenceListProperty(x, y)
    """
    def get(self, EventDispatcher_obj): # real signature unknown; restored from __doc__
        """ ReferenceListProperty.get(self, EventDispatcher obj) """
        pass

    def link(self, EventDispatcher_obj, unicode_name): # real signature unknown; restored from __doc__
        """ ReferenceListProperty.link(self, EventDispatcher obj, unicode name) -> PropertyStorage """
        return PropertyStorage

    def link_deps(self, EventDispatcher_obj, unicode_name): # real signature unknown; restored from __doc__
        """ ReferenceListProperty.link_deps(self, EventDispatcher obj, unicode name) """
        pass

    def set(self, EventDispatcher_obj, _value): # real signature unknown; restored from __doc__
        """ ReferenceListProperty.set(self, EventDispatcher obj, _value) """
        pass

    def setitem(self, EventDispatcher_obj, key, value): # real signature unknown; restored from __doc__
        """ ReferenceListProperty.setitem(self, EventDispatcher obj, key, value) """
        pass

    def trigger_change(self, EventDispatcher_obj, value): # real signature unknown; restored from __doc__
        """ ReferenceListProperty.trigger_change(self, EventDispatcher obj, value) """
        pass

    def __init__(self, *largs, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ ReferenceListProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ ReferenceListProperty.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E7960>'


class ReferenceListPropertyStorage(PropertyStorage):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class StringProperty(Property):
    """
    StringProperty(defaultvalue=u'', **kw)
    Property that represents a string value.
    
        :Parameters:
            `defaultvalue`: string, defaults to ''
                Specifies the default value of the property.
    """
    def __init__(self, defaultvalue=None, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ StringProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ StringProperty.__setstate_cython__(self, __pyx_state) """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E7510>'


class VariableListProperty(Property):
    """
    VariableListProperty(defaultvalue=None, length=4, **kw)
    A ListProperty that allows you to work with a variable amount of
        list items and to expand them to the desired list size.
    
        For example, GridLayout's padding used to just accept one numeric value
        which was applied equally to the left, top, right and bottom of the
        GridLayout. Now padding can be given one, two or four values, which are
        expanded into a length four list [left, top, right, bottom] and stored
        in the property.
    
        :Parameters:
            `default`: a default list of values
                Specifies the default values for the list.
            `length`: int, one of 2 or 4.
                Specifies the length of the final list. The `default` list will
                be expanded to match a list of this length.
            `\*\*kwargs`: a list of keyword arguments
                Not currently used.
    
        Keeping in mind that the `default` list is expanded to a list of length 4,
        here are some examples of how VariableListProperty is handled.
    
        - VariableListProperty([1]) represents [1, 1, 1, 1].
        - VariableListProperty([1, 2]) represents [1, 2, 1, 2].
        - VariableListProperty(['1px', (2, 'px'), 3, 4.0]) represents [1, 2, 3, 4.0].
        - VariableListProperty(5) represents [5, 5, 5, 5].
        - VariableListProperty(3, length=2) represents [3, 3].
    
        .. versionadded:: 1.7.0
    """
    def link(self, EventDispatcher_obj, unicode_name): # real signature unknown; restored from __doc__
        """ VariableListProperty.link(self, EventDispatcher obj, unicode name) -> PropertyStorage """
        return PropertyStorage

    def _dpi_callback(self, obj, _obj, _value): # real signature unknown; restored from __doc__
        """ VariableListProperty._dpi_callback(self, obj, _obj, _value) """
        pass

    def __init__(self, defaultvalue=None, length=4, **kw): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ VariableListProperty.__reduce_cython__(self) """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ VariableListProperty.__setstate_cython__(self, __pyx_state) """
        pass

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """length: 'int'"""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000021F770E7E10>'


class VariableListPropertyStorage(PropertyStorage):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
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


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'kivy.weakmethod', '__doc__': 'Implementation of a\\n    `weakref <http://en.wikipedia.org/wiki/Weak_reference>`_\\n    for functions and bound methods.\\n    ', '__init__': <function WeakMethod.__init__ at 0x0000021F77105440>, '__call__': <function WeakMethod.__call__ at 0x0000021F77105800>, 'is_dead': <function WeakMethod.is_dead at 0x0000021F771058A0>, '__eq__': <function WeakMethod.__eq__ at 0x0000021F77105940>, '__repr__': <function WeakMethod.__repr__ at 0x0000021F771059E0>, '__dict__': <attribute '__dict__' of 'WeakMethod' objects>, '__weakref__': <attribute '__weakref__' of 'WeakMethod' objects>, '__hash__': None})"
    __hash__ = None


# variables with complex values

Clock = None # (!) real value is '<kivy.clock.ClockBase object at 0x0000021F770D5860>'

colormap = {
    'aliceblue': [
        0.9411764705882353,
        0.9725490196078431,
        1.0,
        1.0,
    ],
    'antiquewhite': [
        0.9803921568627451,
        0.9215686274509803,
        0.8431372549019608,
        1.0,
    ],
    'aqua': [
        0.0,
        1.0,
        1.0,
        1.0,
    ],
    'aquamarine': [
        0.4980392156862745,
        1.0,
        0.8313725490196079,
        1.0,
    ],
    'azure': [
        0.9411764705882353,
        1.0,
        1.0,
        1.0,
    ],
    'beige': [
        0.9607843137254902,
        0.9607843137254902,
        0.8627450980392157,
        1.0,
    ],
    'bisque': [
        1.0,
        0.8941176470588236,
        0.7686274509803922,
        1.0,
    ],
    'black': [
        0.0,
        0.0,
        0.0,
        1.0,
    ],
    'blanchedalmond': [
        1.0,
        0.9215686274509803,
        0.803921568627451,
        1.0,
    ],
    'blue': [
        0.0,
        0.0,
        1.0,
        1.0,
    ],
    'blueviolet': [
        0.5411764705882353,
        0.16862745098039217,
        0.8862745098039215,
        1.0,
    ],
    'brown': [
        0.6470588235294118,
        0.16470588235294117,
        0.16470588235294117,
        1.0,
    ],
    'burlywood': [
        0.8705882352941177,
        0.7215686274509804,
        0.5294117647058824,
        1.0,
    ],
    'cadetblue': [
        0.37254901960784315,
        0.6196078431372549,
        0.6274509803921569,
        1.0,
    ],
    'chartreuse': [
        0.4980392156862745,
        1.0,
        0.0,
        1.0,
    ],
    'chocolate': [
        0.8235294117647058,
        0.4117647058823529,
        0.11764705882352941,
        1.0,
    ],
    'coral': [
        1.0,
        0.4980392156862745,
        0.3137254901960784,
        1.0,
    ],
    'cornflowerblue': [
        0.39215686274509803,
        0.5843137254901961,
        0.9294117647058824,
        1.0,
    ],
    'cornsilk': [
        1.0,
        0.9725490196078431,
        0.8627450980392157,
        1.0,
    ],
    'crimson': [
        0.8627450980392157,
        0.0784313725490196,
        0.23529411764705882,
        1.0,
    ],
    'cyan': '<value is a self-reference, replaced by this string>',
    'darkblue': [
        0.0,
        0.0,
        0.5450980392156862,
        1.0,
    ],
    'darkcyan': [
        0.0,
        0.5450980392156862,
        0.5450980392156862,
        1.0,
    ],
    'darkgoldenrod': [
        0.7215686274509804,
        0.5254901960784314,
        0.043137254901960784,
        1.0,
    ],
    'darkgray': [
        0.6627450980392157,
        0.6627450980392157,
        0.6627450980392157,
        1.0,
    ],
    'darkgreen': [
        0.0,
        0.39215686274509803,
        0.0,
        1.0,
    ],
    'darkgrey': '<value is a self-reference, replaced by this string>',
    'darkkhaki': [
        0.7411764705882353,
        0.7176470588235294,
        0.4196078431372549,
        1.0,
    ],
    'darkmagenta': [
        0.5450980392156862,
        0.0,
        0.5450980392156862,
        1.0,
    ],
    'darkolivegreen': [
        0.3333333333333333,
        0.4196078431372549,
        0.1843137254901961,
        1.0,
    ],
    'darkorange': [
        1.0,
        0.5490196078431373,
        0.0,
        1.0,
    ],
    'darkorchid': [
        0.6,
        0.19607843137254902,
        0.8,
        1.0,
    ],
    'darkred': [
        0.5450980392156862,
        0.0,
        0.0,
        1.0,
    ],
    'darksalmon': [
        0.9137254901960784,
        0.5882352941176471,
        0.47843137254901963,
        1.0,
    ],
    'darkseagreen': [
        0.5607843137254902,
        0.7372549019607844,
        0.5607843137254902,
        1.0,
    ],
    'darkslateblue': [
        0.2823529411764706,
        0.23921568627450981,
        0.5450980392156862,
        1.0,
    ],
    'darkslategray': [
        0.1843137254901961,
        0.30980392156862746,
        0.30980392156862746,
        1.0,
    ],
    'darkslategrey': '<value is a self-reference, replaced by this string>',
    'darkturquoise': [
        0.0,
        0.807843137254902,
        0.8196078431372549,
        1.0,
    ],
    'darkviolet': [
        0.5803921568627451,
        0.0,
        0.8274509803921568,
        1.0,
    ],
    'deeppink': [
        1.0,
        0.0784313725490196,
        0.5764705882352941,
        1.0,
    ],
    'deepskyblue': [
        0.0,
        0.7490196078431373,
        1.0,
        1.0,
    ],
    'dimgray': [
        0.4117647058823529,
        0.4117647058823529,
        0.4117647058823529,
        1.0,
    ],
    'dimgrey': '<value is a self-reference, replaced by this string>',
    'dodgerblue': [
        0.11764705882352941,
        0.5647058823529412,
        1.0,
        1.0,
    ],
    'firebrick': [
        0.6980392156862745,
        0.13333333333333333,
        0.13333333333333333,
        1.0,
    ],
    'floralwhite': [
        1.0,
        0.9803921568627451,
        0.9411764705882353,
        1.0,
    ],
    'forestgreen': [
        0.13333333333333333,
        0.5450980392156862,
        0.13333333333333333,
        1.0,
    ],
    'fuchsia': [
        1.0,
        0.0,
        1.0,
        1.0,
    ],
    'gainsboro': [
        0.8627450980392157,
        0.8627450980392157,
        0.8627450980392157,
        1.0,
    ],
    'ghostwhite': [
        0.9725490196078431,
        0.9725490196078431,
        1.0,
        1.0,
    ],
    'gold': [
        1.0,
        0.8431372549019608,
        0.0,
        1.0,
    ],
    'goldenrod': [
        0.8549019607843137,
        0.6470588235294118,
        0.12549019607843137,
        1.0,
    ],
    'gray': [
        0.5019607843137255,
        0.5019607843137255,
        0.5019607843137255,
        1.0,
    ],
    'green': [
        0.0,
        0.5019607843137255,
        0.0,
        1.0,
    ],
    'greenyellow': [
        0.6784313725490196,
        1.0,
        0.1843137254901961,
        1.0,
    ],
    'grey': '<value is a self-reference, replaced by this string>',
    'honeydew': [
        0.9411764705882353,
        1.0,
        0.9411764705882353,
        1.0,
    ],
    'hotpink': [
        1.0,
        0.4117647058823529,
        0.7058823529411765,
        1.0,
    ],
    'indianred': [
        0.803921568627451,
        0.3607843137254902,
        0.3607843137254902,
        1.0,
    ],
    'indigo': [
        0.29411764705882354,
        0.0,
        0.5098039215686274,
        1.0,
    ],
    'ivory': [
        1.0,
        1.0,
        0.9411764705882353,
        1.0,
    ],
    'khaki': [
        0.9411764705882353,
        0.9019607843137255,
        0.5490196078431373,
        1.0,
    ],
    'lavender': [
        0.9019607843137255,
        0.9019607843137255,
        0.9803921568627451,
        1.0,
    ],
    'lavenderblush': [
        1.0,
        0.9411764705882353,
        0.9607843137254902,
        1.0,
    ],
    'lawngreen': [
        0.48627450980392156,
        0.9882352941176471,
        0.0,
        1.0,
    ],
    'lemonchiffon': [
        1.0,
        0.9803921568627451,
        0.803921568627451,
        1.0,
    ],
    'lightblue': [
        0.6784313725490196,
        0.8470588235294118,
        0.9019607843137255,
        1.0,
    ],
    'lightcoral': [
        0.9411764705882353,
        0.5019607843137255,
        0.5019607843137255,
        1.0,
    ],
    'lightcyan': [
        0.8784313725490196,
        1.0,
        1.0,
        1.0,
    ],
    'lightgoldenrodyellow': [
        0.9803921568627451,
        0.9803921568627451,
        0.8235294117647058,
        1.0,
    ],
    'lightgray': [
        0.8274509803921568,
        0.8274509803921568,
        0.8274509803921568,
        1.0,
    ],
    'lightgreen': [
        0.5647058823529412,
        0.9333333333333333,
        0.5647058823529412,
        1.0,
    ],
    'lightgrey': '<value is a self-reference, replaced by this string>',
    'lightpink': [
        1.0,
        0.7137254901960784,
        0.7568627450980392,
        1.0,
    ],
    'lightsalmon': [
        1.0,
        0.6274509803921569,
        0.47843137254901963,
        1.0,
    ],
    'lightseagreen': [
        0.12549019607843137,
        0.6980392156862745,
        0.6666666666666666,
        1.0,
    ],
    'lightskyblue': [
        0.5294117647058824,
        0.807843137254902,
        0.9803921568627451,
        1.0,
    ],
    'lightslategray': [
        0.4666666666666667,
        0.5333333333333333,
        0.6,
        1.0,
    ],
    'lightslategrey': '<value is a self-reference, replaced by this string>',
    'lightsteelblue': [
        0.6901960784313725,
        0.7686274509803922,
        0.8705882352941177,
        1.0,
    ],
    'lightyellow': [
        1.0,
        1.0,
        0.8784313725490196,
        1.0,
    ],
    'lime': [
        0.0,
        1.0,
        0.0,
        1.0,
    ],
    'limegreen': [
        0.19607843137254902,
        0.803921568627451,
        0.19607843137254902,
        1.0,
    ],
    'linen': [
        0.9803921568627451,
        0.9411764705882353,
        0.9019607843137255,
        1.0,
    ],
    'magenta': '<value is a self-reference, replaced by this string>',
    'maroon': [
        0.5019607843137255,
        0.0,
        0.0,
        1.0,
    ],
    'mediumaquamarine': [
        0.4,
        0.803921568627451,
        0.6666666666666666,
        1.0,
    ],
    'mediumblue': [
        0.0,
        0.0,
        0.803921568627451,
        1.0,
    ],
    'mediumorchid': [
        0.7294117647058823,
        0.3333333333333333,
        0.8274509803921568,
        1.0,
    ],
    'mediumpurple': [
        0.5764705882352941,
        0.4392156862745098,
        0.8588235294117647,
        1.0,
    ],
    'mediumseagreen': [
        0.23529411764705882,
        0.7019607843137254,
        0.44313725490196076,
        1.0,
    ],
    'mediumslateblue': [
        0.4823529411764706,
        0.40784313725490196,
        0.9333333333333333,
        1.0,
    ],
    'mediumspringgreen': [
        0.0,
        0.9803921568627451,
        0.6039215686274509,
        1.0,
    ],
    'mediumturquoise': [
        0.2823529411764706,
        0.8196078431372549,
        0.8,
        1.0,
    ],
    'mediumvioletred': [
        0.7803921568627451,
        0.08235294117647059,
        0.5215686274509804,
        1.0,
    ],
    'midnightblue': [
        0.09803921568627451,
        0.09803921568627451,
        0.4392156862745098,
        1.0,
    ],
    'mintcream': [
        0.9607843137254902,
        1.0,
        0.9803921568627451,
        1.0,
    ],
    'mistyrose': [
        1.0,
        0.8941176470588236,
        0.8823529411764706,
        1.0,
    ],
    'moccasin': [
        1.0,
        0.8941176470588236,
        0.7098039215686275,
        1.0,
    ],
    'navajowhite': [
        1.0,
        0.8705882352941177,
        0.6784313725490196,
        1.0,
    ],
    'navy': [
        0.0,
        0.0,
        0.5019607843137255,
        1.0,
    ],
    'oldlace': [
        0.9921568627450981,
        0.9607843137254902,
        0.9019607843137255,
        1.0,
    ],
    'olive': [
        0.5019607843137255,
        0.5019607843137255,
        0.0,
        1.0,
    ],
    'olivedrab': [
        0.4196078431372549,
        0.5568627450980392,
        0.13725490196078433,
        1.0,
    ],
    'orange': [
        1.0,
        0.6470588235294118,
        0.0,
        1.0,
    ],
    'orangered': [
        1.0,
        0.27058823529411763,
        0.0,
        1.0,
    ],
    'orchid': [
        0.8549019607843137,
        0.4392156862745098,
        0.8392156862745098,
        1.0,
    ],
    'palegoldenrod': [
        0.9333333333333333,
        0.9098039215686274,
        0.6666666666666666,
        1.0,
    ],
    'palegreen': [
        0.596078431372549,
        0.984313725490196,
        0.596078431372549,
        1.0,
    ],
    'paleturquoise': [
        0.6862745098039216,
        0.9333333333333333,
        0.9333333333333333,
        1.0,
    ],
    'palevioletred': [
        0.8588235294117647,
        0.4392156862745098,
        0.5764705882352941,
        1.0,
    ],
    'papayawhip': [
        1.0,
        0.9372549019607843,
        0.8352941176470589,
        1.0,
    ],
    'peachpuff': [
        1.0,
        0.8549019607843137,
        0.7254901960784313,
        1.0,
    ],
    'peru': [
        0.803921568627451,
        0.5215686274509804,
        0.24705882352941178,
        1.0,
    ],
    'pink': [
        1.0,
        0.7529411764705882,
        0.796078431372549,
        1.0,
    ],
    'plum': [
        0.8666666666666667,
        0.6274509803921569,
        0.8666666666666667,
        1.0,
    ],
    'powderblue': [
        0.6901960784313725,
        0.8784313725490196,
        0.9019607843137255,
        1.0,
    ],
    'purple': [
        0.5019607843137255,
        0.0,
        0.5019607843137255,
        1.0,
    ],
    'red': [
        1.0,
        0.0,
        0.0,
        1.0,
    ],
    'rosybrown': [
        0.7372549019607844,
        0.5607843137254902,
        0.5607843137254902,
        1.0,
    ],
    'royalblue': [
        0.2549019607843137,
        0.4117647058823529,
        0.8823529411764706,
        1.0,
    ],
    'saddlebrown': [
        0.5450980392156862,
        0.27058823529411763,
        0.07450980392156863,
        1.0,
    ],
    'salmon': [
        0.9803921568627451,
        0.5019607843137255,
        0.4470588235294118,
        1.0,
    ],
    'sandybrown': [
        0.9568627450980393,
        0.6431372549019608,
        0.3764705882352941,
        1.0,
    ],
    'seagreen': [
        0.1803921568627451,
        0.5450980392156862,
        0.3411764705882353,
        1.0,
    ],
    'seashell': [
        1.0,
        0.9607843137254902,
        0.9333333333333333,
        1.0,
    ],
    'sienna': [
        0.6274509803921569,
        0.3215686274509804,
        0.17647058823529413,
        1.0,
    ],
    'silver': [
        0.7529411764705882,
        0.7529411764705882,
        0.7529411764705882,
        1.0,
    ],
    'skyblue': [
        0.5294117647058824,
        0.807843137254902,
        0.9215686274509803,
        1.0,
    ],
    'slateblue': [
        0.41568627450980394,
        0.35294117647058826,
        0.803921568627451,
        1.0,
    ],
    'slategray': [
        0.4392156862745098,
        0.5019607843137255,
        0.5647058823529412,
        1.0,
    ],
    'slategrey': '<value is a self-reference, replaced by this string>',
    'snow': [
        1.0,
        0.9803921568627451,
        0.9803921568627451,
        1.0,
    ],
    'springgreen': [
        0.0,
        1.0,
        0.4980392156862745,
        1.0,
    ],
    'steelblue': [
        0.27450980392156865,
        0.5098039215686274,
        0.7058823529411765,
        1.0,
    ],
    'tan': [
        0.8235294117647058,
        0.7058823529411765,
        0.5490196078431373,
        1.0,
    ],
    'teal': [
        0.0,
        0.5019607843137255,
        0.5019607843137255,
        1.0,
    ],
    'thistle': [
        0.8470588235294118,
        0.7490196078431373,
        0.8470588235294118,
        1.0,
    ],
    'tomato': [
        1.0,
        0.38823529411764707,
        0.2784313725490196,
        1.0,
    ],
    'turquoise': [
        0.25098039215686274,
        0.8784313725490196,
        0.8156862745098039,
        1.0,
    ],
    'violet': [
        0.9333333333333333,
        0.5098039215686274,
        0.9333333333333333,
        1.0,
    ],
    'wheat': [
        0.9607843137254902,
        0.8705882352941177,
        0.7019607843137254,
        1.0,
    ],
    'white': [
        1.0,
        1.0,
        1.0,
        1.0,
    ],
    'whitesmoke': [
        0.9607843137254902,
        0.9607843137254902,
        0.9607843137254902,
        1.0,
    ],
    'yellow': [
        1.0,
        1.0,
        0.0,
        1.0,
    ],
    'yellowgreen': [
        0.6039215686274509,
        0.803921568627451,
        0.19607843137254902,
        1.0,
    ],
}

Logger = None # (!) real value is '<Logger kivy (DEBUG)>'

NUMERIC_FORMATS = (
    'in',
    'px',
    'dp',
    'sp',
    'pt',
    'cm',
    'mm',
)

__all__ = (
    'Property',
    'NumericProperty',
    'StringProperty',
    'ListProperty',
    'ObjectProperty',
    'BooleanProperty',
    'BoundedNumericProperty',
    'OptionProperty',
    'ReferenceListProperty',
    'AliasProperty',
    'DictProperty',
    'VariableListProperty',
    'ConfigParserProperty',
    'ColorProperty',
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021F77007C90>'

__spec__ = None # (!) real value is "ModuleSpec(name='kivy.properties', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021F77007C90>, origin='C:\\\\Users\\\\matthew.muller\\\\.virtualenvs\\\\app-gFbndeE6\\\\Lib\\\\site-packages\\\\kivy\\\\properties.cp311-win_amd64.pyd')"

__test__ = {}

