# API Documentation

This project provides a simple API for managing posts and comments.

## Endpoints

### Post Endpoints

- `GET /posts/`  
  **Description**: Retrieve a list of all posts.

- `POST /posts/`  
  **Description**: Create a new post.

- `GET /post/<uuid:pk>/`  
  **Description**: Retrieve a specific post by its unique ID (`pk`).

### Comment Endpoints

- `GET /comments/`  
  **Description**: Retrieve a list of all comments.

- `POST /comments/`  
  **Description**: Create a new comment.

- `GET /comment/<uuid:pk>/`  
  **Description**: Retrieve a specific comment by its unique ID (`pk`).

## Example Responses

- **Post Detail**: Includes post data along with comments associated with the post.



### Fetch 3 random comments: 
You can Find the Answer in the ```backend_repo\apps\demo\serializers.py```