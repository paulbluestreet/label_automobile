# Assignment

Oh, hello!
---------
First of all, awesome that you want to join our team! We already know that you're a cool
person, but now we just want to know if you're a cool coder as well! To that end we've set 
up a basic exercise for you to complete.

Our tech stack
--------------
Before we start off, let me elaborate about our tech stack. For most projects, we use the following technologies:
* Python (3.4+, preferably 3.6) for rapid development
* PostgreSQL database, because it adheres more closely to the SQL standard than MySQL: https://www.postgresql.org/
* Python Pyramid framework, because it has less vendor lock-in than Django, and the basic stack is leaner and meaner
* SQLAlchemy as database ORM, because not writing your own SQL statements is faster and more secure (ORM takes care of not allowing SQL Injection etc)

The premise
-----------
A company specialised in car parts wants to modernise their company, and start selling their parts online.
Being the pro car salesmen that they are, they decided to develop the front-end via another agency. They entrust
the back-end to none other than Label A.

After a research Sprint 0, we've defined the following user stories on top of our backlog:
* As a company, I want all my products in a database, so I can offer them via our new platform to customers
* As a client, I want to add a product to my shopping cart, so I can order it at a later stage
* As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need
* As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car
* As a client, I want to select a delivery date and time, so I will be there to receive the order
* As a client, I want to see an overview of all the products, so I can choose which product I want
* As a client, I want to view the details of a product, so I can see if the product satisfies my needs

The actual exercise
-------------------
Develop an API (built on top of this skeleton) according to the user stories defined above.
You should not spend more than 8 hours on this exercise, to put on your MVP glasses and prioritise according to what you think the product should minimally entail.

We can make the following assumptions:
* We don't have to worry about the front-end, but should think of a data format a JavaScript application can handle
* We don't need to worry about the payment of the order. Who needs money anyway?

How to score bonus points (ergo: we really advise you to tackle it this way):
* Implement a RESTful API
* Use PostgreSQL, we've already configured the ORM for you!
* Read the Pyramid documentation, especially how it works with SQLAlchemy
* Document how we can set up and instantiate the project, so we can easily test it functionally

If you have any questions, feel free to contact us! Any feedback on this exercise is always welcome!!!