.. include:: <s5defs.txt>

Refactoring: An Introduction
============================

:Authors: Wayne Witzel III
:Date: SourceForge Cont. Ed. (2012/09/14)

..  footer:: Wayne Witzel III <wwitzel@geek.net>

The Refactoring Bible
---------------------

- Refactoring: Improving the Design of Existing Code
  (Fowler, Beck, Brant, Opdyke, Roberts)

- Use your training budget to get this book. Read it. You will be better
  programmer for it.

Terminology
-----------

- Refactoring. Modifying existing code in such a way to make it better. Better
  can have a lot of meanings and is subjective to the situation, but you know
  if you've made the code better or not.

- Smell. Any code that follows a pattern that makes it stink. We will talk
  about the most common ones from sfpy.

Common Smell: Duplicated Code
-----------------------------

- This is the worst offender and easiest to spot and usually the easiest
  to resolve. Just use Extract Method and call the new method in both places.

- Extract Method: You have code fragments that can be grouped. Turn the
  fragment in to a method whose name explains the purpose of the method.

Duplicated Code: Example
------------------------

  .. sourcecode:: python

      facet_list = [(f.name, f.count) in self._facets]
      # and in other methods ..
      facet_list = [(f.name, f.count) in self._facets]
      # and in another method .. you get the idea

      @property
      def facet_list(self):
          return [(f.name, f.count) in self._facets]

- Eventually this will help you reduce duplicated code, but be warned, this
  type of refactoring can commonly lead to Large Class (we cover that later).

Common Smell: Long Method
-------------------------

- Programs that live the best and longest lives are those with short methods.
  The longer a procedure is, the harder it is to understand and therefore
  modify.

- Extract Method, previously shown, is a great way to solve most long method
  smells.

Long Method: Example 1
----------------------

  .. sourcecode:: python

       if del_filter.facet._id in ['os', 'freshness']:
          os = g.current_os[1]
          if del_filter.value == os:
              g.session['directory_ignore_os']=True
          elif del_filter.value == 'Recently updated':
              g.session['directory_ignore_freshness'] = True

      # instead of having this inline, it gets replaced with method call

      self._update_global_filters(del_filter)

- If we do this for our logic blocks, we end up having a lot of short, self
  documented methods doing our work, which is much easier to maintain.

Common Smells: Long Method - part II
------------------------------------

- If your method has a lot of parameters and temporary values, which
  in sfpy, we tend to have a lot of, then another approach is needed.

Long Method: Example 1.1
------------------------

- Replace Temp with Query: Extract the temporary expression into a method. Now
  this information is available beyond the local scope of the method in
  question and that makes it easier to come up with cleaner code for the class

  .. sourcecode:: python

      breadcrumbs = [dict(url='/', label="Home"),
                     dict(url=self.directory_root, label="Browse")]
      return dict(breadcrumbs=breadcrumbs)

      # extract and replace, now return looks like this
      return dict(breadcrumbs=breadcrumbs())

Long Method: Example 1.2
------------------------

- Replace Parameter with Method: Remove the parameter and let the receiver
  invoke the method. The general rule here is that if a method can get a
  parameter through other means, it should.

  .. sourcecode:: python

      result = self.query(**params)
      filtered_results = self.filter(results)

      # now combine replace temp with replace parameters
      def filter(self):
          return self.query(params())
      filtered_results = filter()

Common Smell: Large Class
-------------------------

- Classes should have clear responsibilities. We find ourselves, usually in
  small doses, adding new responsbilities to existing classes that just aren't
  worth creating a whole new class for.

- End result, you have a class doing too many things. This is hard to maintain
  and leads to more errors, more developer time, and causes other smells like
  Shotgun Surgery.

- Fortunately fixing this problem is usually as easy as applying Extract Class.
  Decide how to split the class, rename old class (if needed), move any methods
  and create the link to the new class.

- Easy way to spot this smell is if you have many class variables named:
  responsibility_variable.

Large Class: Example
--------------------

  .. sourcecode:: python

      class Project(object):
          self.shortname
          self.release_metadata
          self.release_files

      # extract class

      class Release(object):
          self.metadata
          self.files

      class Project(object):
          self.shortname
          self.release = Release()


Common Smell: Shotgun Surgery
-----------------------------

- You smell this one anytime you make a change that results in you having to
  make a lot of little changes everywhere.

- This is error prone and often leads to missed code changes that come back to
  bit you in the ass.

- The good news is this is another one that is pretty easy to resolve. We can
  use Move Method and Move Field to take all the pain away.

Shotgun Surgery: Example Class
------------------------------

  .. sourcecode:: python

      class Review(object):
          self.featured =  True
          self.type = ReviewType()
          def calculate_stuff(self):
              if self.type == 'StarAndRecommended':
                  # do This
              return result
          def is_featured(self):
              return self.featured

- Here is a common example of code you will see a lof of in sfpy.

- If we want to display things differently based on information in the
  ReviewType, we should really move this to the ReviewType class.

Shotgun Surgery: Move Method Example
------------------------------------

  .. sourcecode:: python

      class ReviewType(object):
          def calculate_stuff(self):
              if self.name == 'StarAndRecommend':
                  # do Stuff
              else:
                  # do This
              return result

      class Review(object):
          def calculate_stuff(self):
              return self.type.calculate_stuff()

- We preserve the interface of Review while cleaning it up and reducing the
  the tight coupling to ReviewType.

Shotgun Surgery: Move Field Example
-----------------------------------

- We decided we also want ReviewTypes as a whole to be featured, not the
  indivual reviews themselves.

  .. sourcecode:: python

      class ReviewType(object):
          self.featured = True

      class Review(object):
          def is_featured(self):
              return self.type.featured

Stuff That Just Isn't True
--------------------------

- Refactoring makes your code slower.

- It isn't worth the time to refactor.

- Ruby is a good programming language.

Questions
---------

- That's all folks.

