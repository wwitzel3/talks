.. include <s5defs.txt>

Let's Get Functional
====================

:Authors: Wayne Witzel III
:Date: SourceForge Cont. Ed. (2013/04/11)

.. footer:: Wayne Witzel III <wwitzel@slashdotmedia.com>

What Is Functional Programming?
-------------------------------

- Evaluation centric

- Avoiding state, mutables, and side-effects

- Orgins: lambda calculus

- Popularized by Lisp, Erland, Scheme

Neat, so what?
--------------

- State can be messy. Using some functional programming techniques we can clean up 
  parts of our code.

- Mixing imparative styles with functional styles can result in cleaner and easier to understand code.

- Using closures to create function generators is a great way to clean up the common pattern where we
  create a method that takes in a configuration value, but that value is fixed at startup.

Closures, function generator
----------------------------

- Simple Example

  .. sourcecode:: python

      def func1(i):
          def func2():
              return i+5
          return func2

      >>> f = func1(10)
      >>> f()
      >>> 15

Real example, kind of
---------------------

- Example, didn't have time to find good one.

  .. sourcecode:: python

      def gen_configtree(settings):
        def _configtree():
            return initialize_configtree(**settings)
        return _configtree

      # do this once
      init_configtree = gen_configtree(settings)
      # use this many places
      configtree = init_configtree()

Better than a global
--------------------

- Since the closure itself doesn't maintain state, you can always just generate a new configtree
  with different settings if you need to.

- No need to import or pass around the settings. You can generate your instance and call it when needed.

- The code still has side effects but using functional techniques we can create a cleaner abstraction.

I got nothing
-------------

- I rushed this, so I don't have anything else to say.

- Questions?
