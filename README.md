# flask-helloworld-docker


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
git clone https://github.com/jsdads11/flask-helloworld-docker.git
cd flask-helloworld-docker

# Building and running as a ocker container
docker build --tag flask-helloworld-docker --build-arg FLASK_DEBUG=True .
docker run --detach --name flask-app --publish 80:8080 --rm flask-helloworld-docker
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
