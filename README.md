Movie Collections Web Application
This Django-based web application allows users to create collections of movies they like by integrating with a third-party movie listing API. The application supports user registration with JWT authentication, CRUD operations on collections, and includes a scalable request counter middleware to monitor the number of requests served.

Features
User Registration and Authentication

Users can register using a username and password, which generates a JWT token for authentication.
All APIs except the registration API require JWT token authentication.
Movie Listing

Integrates with a third-party API to fetch a list of movies with pagination.
Users can browse movies and add them to their collections.
Collections Management

Users can create, view, update, and delete collections.
Each user can have multiple collections, and each collection can contain multiple movies.
Top 3 favorite genres of a user are calculated based on their collections.
Request Counter Middleware

A custom middleware that counts and monitors all incoming requests.
Includes API endpoints to view and reset the request count, designed to work in a concurrent and scalable environment.
