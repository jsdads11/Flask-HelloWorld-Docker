# flask-init-mini
This project is a boilerplate for future Flask applications.
The steps below can be executed on any unix-like system.
## Setup SSH key

**This step is an option and can be omitted.**
Create ssh key and add it to GitHub's [SSH keys](https://github.com/settings/keys) settings.
```bash
ssh-keygen
cat ~/.ssh/id_rsa.pub
```



## Installation
```bash
# Cloning the source code
git clone https://github.com/ldynia/flask-init-mini.git
cd flask-init-mini
# Building and running docker container
docker build --tag flask-mini --build-arg FLASK_DEBUG=True .
docker run --detach --name flask-a
pp --publish 80:8080 --rm flask-mini
docker ps



```
## API
```bash
curl "http://localhost"; echo
```
## Testing
Unit test
```bash
docker exec flask-app pytest
```
Code coverage
```bash
docker exec flask-app coverage run -m pytest
docker exec flask-app coverage report
```
Stop container
```bash
docker stop flask-app
```

Contents

# API Styles Fundamentals
If you only have a hammer, everything begins to look like a nail, but sticking with a single API style is limiting. Nowadays, a service or microservice has several APIs, and they must all be well-defined. You’ll examine the best types of APIs for your use cases as well as the design decisions you must make for RESTful APIs, GraphQL APIs, Websockets API, gRPC API, and messaging protocols. You’ll learn how to design a variety of APIs, recognize the trade-offs among them, and understand where to use each one for the best communication among applications. 
Search for a live event about API Styles Fundamentals at [learning.oreilly.com](https://learning.oreilly.com/live-events/api-styles-fundamentals/0636920078591/)
## Table of Contents
1. [Slides](slides/API_Styles_Fundamentals.pdf)
1. [Snippets](docs/snippets.md)
1. [Resources](docs/resources.md)
1. [Q&A](docs/q&a.md)
1. [Feedback](docs/feedback.md)
## Metadata
Published on 17th March 2024

