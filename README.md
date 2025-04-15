# Blog DRF Project

A simple blog application built using Django and Django REST Framework (DRF) with JWT authentication.

## Features
- **JWT Authentication**: Secure login and registration using JSON Web Tokens (JWT).
- **Blog Management**: Users can create, read, update, and delete their own blog posts.
- **Commenting**: Users can add comments to blog posts.
- **Search by Author**: Users can search for blog posts by author name.

## Endpoints

### Authentication Endpoints
- **POST /api/token/**  
  Obtain a JWT token by providing your username and password.
**Request body**:
  ```json
  {
    "email": "your_username",
    "password": "your_password"
  }

- **POST /api/token/refresh/**
Refresh your JWT token by providing the refresh token.
**Request body:**
```json
{
  "refresh": "your_refresh_token"
}
````
### Account Endpoints
**POST /api/account/register/**
Register a new user account.
**Request body:**

```json
{
  "name": "your_name",
  "email": "your_email@example.com",
  "password": "new_password"
}
```

**POST /api/account/login/**
Login with email and password to get the JWT token.
**Request body:**

```json
{
  "email": "your_email@example.com",
  "password": "your_password"
}
```

# Blog Endpoints
GET /api/blog/blog/
List all blog posts.
Query parameters:

author: Filter blog posts by author name (e.g., /api/blog/?author=John).

POST /api/blog/blog/
Create a new blog post (requires JWT authentication).
**Request body:**

``` json
{
  "title": "Blog title"
}
```

GET /api/blog/blog/{id}/
Get details of a specific blog post by ID.


PUT /api/blog/blog/{id}/
Update an existing blog post (only the author can edit).
**Request body:**

```json
{
  "title": "Updated title",
  "content": "Updated content"
}
```

DELETE /api/blog/blog/{id}/
Delete a specific blog post (only the author can delete).


Comment Endpoints
POST /api/comment/blogs/{blog_id}/comments/
Add a comment to a blog post (requires JWT authentication).
**Request body:**

``` json
{
  "content": "This is a comment"
}
```

### Installation
Clone the repository:

```
git clone https://your-repository-url.git
cd your-project-folder
```

**Create a virtual environment:**
```
python -m venv env
```

**Activate the virtual environment:**

On Windows:
```
.\env\Scripts\activate
```

**Install dependencies:**
```
pip install -r requirements.txt
```

**Apply migrations:**
```
python manage.py migrate
```
**Run the server:**
```
python manage.py runserver
```
**The application will be running at http://127.0.0.1:8000/.**
