# Maxcraft Product API

**Alex Greenberg**

- **The Maxcraft Product API will help deliver the breadth of products availabe at Maxcraft, inc. These products have a type, size, image and price associated with them. Full CRUD will be available via routes below**

**https://github.com/a1g23/maxcraft_backend**

Deployed Backend: https://maxcraft-backend.onrender.com/products/


## List of Dependencies

- django
- django-environ
- dj-database-url
- djangorestframework
- psycopg2-binary

## Backend Route Map

| Route Name | Endpoint | Method | Description |
|------------|----------|--------|-------------|
| Product Index | /products    | GET    | JSON of all products |
| Create Product | /products   | POST    | Adds JSON of new product from FormBody |
| Update Product | /products/:id   | PUT    | Updates JSON of updated product from FormBody  |
| Remove Product | /products/:id   | DELETE    | Deletes JSON of the product from the DB |
| Show Product | /products/:id    | GET    | JSON of specified product |


## ERD (Entity Relationship Diagram)

![ERD](./Screenshot%202024-03-30%20at%2010.42.53 AM.png)