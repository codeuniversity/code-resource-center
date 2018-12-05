# Django Design Principles 📐📏

## ➡️ Loose coupling and tight cohesion

![Cohesion](https://drive.google.com/uc?export=view&id=1akH6ytCH4pcvuo1a74hYE2uZP6HHUnoD)

_extracted from: \[_[https://www.coursera.org/lecture/object-oriented-design/1-3-1-coupling-and-cohesion-q8wGt](https://www.coursera.org/lecture/object-oriented-design/1-3-1-coupling-and-cohesion-q8wGt)_\]_

**One of the core features of Django's stack is loose coupling and tight cohesion, following Encapsulation principles.**

In Computer Science, coupling is related to the degree of interdependence that exists between software modules and how closely they are connected to each other.

Tight coupling means the modules are deeply connected and interdependent. This is considered bad design, like a puzzle system. Loose coupling, means the components know little or only enough about each other when absolutely necessary and yet can work well together, like a lego system.

Cohesion is related to the interdependency within the module, amongst its elements, forming a single cohesive unit.

Quoted from "Boulder Patterns Group Minutes Old"

> the correct terminology is "tight internal cohesion" and "loose external coupling". This basically means that each method in a class should have one task and the class as a whole should have one major responsibility \(tight internal cohesion\) and that other classes should not depend on the inner workings of this class but should be designed to the "interface" of the class \(loose external coupling\). See a recent post by AlanShalloway on this: \[[http://groups.yahoo.com/group/dpexplained/message/108](http://groups.yahoo.com/group/dpexplained/message/108)\]

More on that topic can be found at: \[[http://wiki.c2.com/?CouplingAndCohesion](http://wiki.c2.com/?CouplingAndCohesion)\]

**An example of loose coupling and tight cohesion in Django is that the template system doesn't know about Web requests, the database layer knows nothing about how the data will be displayed and the view system allows for any template system a programmer uses.**

If one wants to use the REST framework approach, that is possible and the view can be handled by another application written in React or Vue, for example.

This allows Django to be flexible, reusable and maintainable. Keeping modules simple is fundamental. \(KISS\)

## ➡️ Don’t repeat yourself \(DRY\)

Django follows the DRY principle, making it easy to avoid repeating code, since modules are reusable and not bloated, as previously stated.

The framework deduces as much as possible from as little as possible.

## ➡️ Explicit is better than implicit

According to Python's core principles stated in PEP 20, Django shouldn’t do too much “magic.” Magic would be everything done for you under the hood. Magic should only be used if there is a good reason for it. Django's documentation is clear and it is very easy to customize it.

## ➡️ Models

Models in Django include all relevant domain logic, encapsulating every aspect of an “object,” following Martin Fowler’s Active Record design pattern.

## ➡️ Database application

Django's ORM allows for SQL statements to be quickly executed. Joins are done automatically. Objects access related objects systemwide.

Yet, if you're not a fan of magic you have the option to use raw SQL if you want. It is easy to write custom SQL queries. :\)

## ➡️ URL Design

URLs are flexible. Any design is allowed.

Django does a very good jog when it comes to definitive URLs.

> Technically, foo.com/bar and foo.com/bar/ are two different URLs, and search-engine robots \(and some Web traffic-analyzing tools\) would treat them as separate pages. Django should make an effort to “normalize” URLs so that search-engine robots don’t get confused.

This is why the APPEND\_SLASH setting is set to True as default.

## ➡️ Template System

_More information can be found at \[_[https://docs.djangoproject.com/en/2.1/misc/design-philosophies/](https://docs.djangoproject.com/en/2.1/misc/design-philosophies/)_\]_

