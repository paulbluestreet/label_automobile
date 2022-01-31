# Handed in assignment

Oh, hello to you too!
---------
Hi, I'm sure you want to test what I've done in the least effort possible, 
which is why I've written this short test-guide. Since this is my first time 
working with pyramid this assignment has cost me a bit more time than planned (>4 hours). 
Therefore I have decided to not implement any automatic test-coverage, 
for I am confident that what I've written should give a clear picture.

API-overview
--------------
The flow of this API is quite simple, you have users, products and orders.
The product basket is created by the table cart_product which links product_ids
with user_ids. The items belonging to an order can be found by looking at the
order_product table. Information regarding the order (delivery_date, user_id)
can be found in the order table.

How to test?
---------------
First alter the development.ini so the postgresql url/credentials match up
to your own postgres server and make sure that the database lamob exists.

Then run `init_mob_db development.ini &&  mock_mob_db development.ini` to
create and fill the database.

Then run the api by running `pserve development.ini`

Then you can run the following python script step by step to see the API in action!

```
import requests

url = <<fill in your api url>>

products = requests.get(f'{url}/product').json()
print(products)

# Get user_id
user_id = requests.get(f'http://127.0.0.1:7654/user/email?email=johndoe@example.com').json()['id']
print(user_id)

## Get products now in cart
init_cart = requests.get(f'http://127.0.0.1:7654/cart_product?user_id={user_id}').json()
print(init_cart)

## Add products 
# add product that is already in cart
r = requests.post(f"{url}/cart_product", json={'user_id': user_id,
                                               'product_id': init_cart[0]['product_id']})
print(r.status_code)

# check addition
print(requests.get(f'http://127.0.0.1:7654/cart_product?user_id={user_id}').json())

# Add product not already in cart
other_product_id = [x['id'] for x in products if x['name'] == 'Awesome Car Part'][0]
requests.post(f"{url}/cart_product", json={'user_id': user_id,
                                           'product_id': other_product_id})

# check addition
print(requests.get(f'http://127.0.0.1:7654/cart_product?user_id={user_id}').json())

## Time to delete stuff
r = requests.delete(f"{url}/cart_product", json={'user_id': user_id,
                                                 'product_id': other_product_id})
print(r.status_code)

# check deletion
print(requests.get(f'http://127.0.0.1:7654/cart_product?user_id={user_id}').json())

# Try to delete item not in chart
r = requests.delete(f"{url}/cart_product", json={'user_id': user_id,
                                                 'product_id': other_product_id})
print(r.status_code)
print(r.json())

## Time to place an order
r = requests.post(f"{url}/order", json={'user_id': user_id,
                                        'delivery_datetime_UTC': '2022-01-22 20:23:00'})
print(r.status_code)

# No further feedback (cause MVP), but shopping cart should now be empty
print(requests.get(f'http://127.0.0.1:7654/cart_product?user_id={user_id}').json())

# You can check the results of the order in de database by querying the order and order_product table.

```

On automatic tests
-------------------
I did not implement automatic testing because I ran out of time I had available to spent on this assignment.

Feedback on the assignment
---------------
The assignment was a fun and I like the idea of having to build a minimalistic API as a test. 
However I lost the most time trying to figure out the way pyramid works, which in my opinion should not be 
the focus of a coding assessment. Everyone can learn a framework with some time, so I think the time spent on 
testing someone should be more framework agnostic (with exceptions for frameworks that are difficult to learn).
The folder structure used as a boilerplate is also too involved for a minimalistic API test. I purposely did 
not re-use the services structure since it felt pointless and a waste of time. Perhaps this structure makes sense
for pyramid experts, but for me it didn't click.
This all sounds rather negative, but that's just because I spent a lot of time trying to explain why I think
the focus shouldn't be on a framework and what cost me the most time :). I want to stress that I do like the idea of 
building a small API and the use-cases were sensible to build with just enough challenge for the database design
to check for someones skills. Maybe just give the user-stories and allow people to use whatever framework they want? 