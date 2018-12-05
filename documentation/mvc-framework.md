---
description: Pattern used by Django
---

# MVC Pattern

## Model View Controller Design Pattern

![image](https://drive.google.com/uc?export=view&id=1PawxfzI7exIjT3uKSYNxrD-ZzdjdK9Kq)

_extracted from \[_[_https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction_](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction)_\]_

Django uses the MVC pattern. It is a widely adopted pattern for user interface, such as Code Resource Center. It has a layered architecture, following the principle of Least Knowledge.

![](../.gitbook/assets/screen-shot-2018-12-05-at-12.59.08-pm.png)

extracted from [https://www.coursera.org/learn/design-patterns/lecture/hvINx/2-3-1-mvc-pattern](https://www.coursera.org/learn/design-patterns/lecture/hvINx/2-3-1-mvc-pattern)

It relies heavily on the Separation of Concerns principle. The Model corresponds to Entity Objects,  a View corresponds to the Boundary Object that deals with users and Controller corresponds to the Control objects that receives events and coordinates actions.

**Notice:** 

* The View is an Observer of the Model. Model will "tell" View when a change has occurred and the view will update itself;
* The Model exists on its own. It doesn't rely on a View or Controller to exist;
* A View is the Observer \(subscriber\) and the Model is an Observable;
* The Controller is the "middleman".  It receives orders from the user and works with the Model based on those requests, and then delivers back to the frontend;
* They are loosely coupled.
* M\(Data Layer\) , V\(Presentation Layer\) C\(Logic Layer\) - Layered Architecture - Model at the bottom, Controller in the middle, and View at the top. The Controller talks with both the View and the Model. But the model interacts only with its adjacent layer, which is the Controller. Same thing goes for the View, which only interacts with the adjacent layer, the Controller.

Django uses this pattern, which follows the Separation of Concerns principle, making the software modular and loosely coupled. 

**Observation:**   Why not choosing Observational, Creational or Structural Design patterns instead? Simply because we chose Django as a Framework. As beginners, we thought it would be safer to have some decisions made on our behalf. Once we advance our knowledge we might use other patterns depending on our use case. But we believe MVC frameworks fits perfectly for the Code Resource Center since it relies on a constant interaction with users. 

\*\*\*\*

