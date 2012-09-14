.. include:: <s5defs.txt>

Building the PyCon 5K: Open Race Tracking
=========================================

:Authors: Wayne Witzel III
:Date: PyCarolinas - 10/20/2012

..  footer:: Wayne Witzel III

What We Have
------------

- Bad Perl hacker until Python.  Came to Python via Zope in 1999.  Worked at
  Digital Creations (aka Zope Corporation) until 2003.  Now a consultant with
  Agendaless Consulting.

- Primary author of: Pyramid web framework, Supervisor UNIX process control
  system, Deform form system, Repoze collection of middleware, and other
  unmentionables.  Contributor to Zope, WebOb, and other OSS projects.

How We Did It
-------------

- If you follow these guidelines, your library will be useful for other
  people in both the scenarios you expect and in ones you don't.

- The importance of these guidelines increases along with the number of users
  whom will depend upon your library.  The more people whom use your library,
  the more likely it is that some of them will try to use your library in
  unexpected ways.  Ex: someone will want to create two separate applications
  that use your library in the same process.

Prototyping
-----------

- Library authors sometimes do the wrong things for the right reasons.

- Incorrect assumptions of how people will need to use the library they're
  developing.

- Optimistic perception of what tradeoffs are acceptable for the sake of
  convenience.

- Skewed perception of "cleanliness".

Coding
------

- Library: maintains none or little of its own state, no or few callbacks.

- Framework: no or little state, but lots of callbacks.  Some frameworks
  mutate or require global state (IMO inappropriately).  A web framework
  instance is often fed to a global mainloop, but that doesn't mean it should
  use globals with abandon.  Even then if the framework doesn't use global
  state, with a little care, two framework instances can live in the same
  process.

- Application: maintains lots of state, can use global state with abandon.

Integration
-----------

- The assumption: "clean" == "is maximally convenient for the case I presume
  this code is going to be used in"

- The reality:  "clean" == "maximally understandable; without surprises or
  exceptions".

- The fewer limiting assumptions made by the library, the fewer surprises it
  will have and the more understandable it will be.

- Ex: thread-local state management doesn't work in async systems without
  magical intervention.

What We Learned
---------------

- During this talk, I call out antipattern examples from actual projects
  (including my own).

- If I use code from one of your projects as an antipattern example, it
  doesn't mean I don't like you.

- This talk is impossible to give without showing negative examples.  I'm
  lazy and the best negative examples are those that already exist.

What We Need
------------

- Avoid the mutation of global (module-level) state when your library is
  imported.  

- Avoid requiring that other people mutate global state to use your library.
  Ex: telling people to set an environment variable or call a function
  which mutates global state to use your library

- If your library mutates global state when it's imported or you tell people
  to mutate global state to use it, it's not really a library, it's kinda
  more like an application.

Demo
----

- An import of another module or global.

- Assignment of a variable name in the module to some constant value.

- The addition of a function via a def statement.

- The addition of a class via a class statement.

- Control flow which may handles conditionals for platform-specific handling
  or failure handling of the above.

- Anything else will usually end in tears.


