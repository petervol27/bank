# Bank Back End

This is my backend for my bank application

## Django

Using Django rest framework I have created an API that handles a custom user, accounts,loans,cards,transactions. 

### Database

Using postgresql on Render , with psycopg2 to handle the URL for the database which is inside an .env file.

### Home
The main page of the backend has a menu that shows each endpoint, most endpoints require authentication so they won't work in the backend itself , only in the front end when logged in.



