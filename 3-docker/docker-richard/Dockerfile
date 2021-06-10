# we want containers
# containers are isolated processes
# to create a container, you need a container image, aka Docker image, aka image
# containers are ephemeral, created and destroyed as needed
# images are immutable, templates to make new containers
# to create an image, you build a Dockerfile.
# Dockerfiles are like recipes/instructions to build an image layer by layer
# the instructions are executed in containers of their own

# step 1 of any Dockerfile
# what is the base image for the image that will be built by this dockerfile
# you get images from docker registries where people have published them
# the default docker registry is "docker hub" hub.docker.com / docker.io

# two things we want from a base image:
# 1. as much of the dependencies of our app as possible
# 2. officially supported / well-maintained with updates

# if i picked the "3" tag, if i build this dockerfile without
# changes next month, it might pick up 3.10 if that was released

#         image name
#   |------------------------|
#                image name
#  registry   |--------------|
#   (docker.io aka    user   repos-
#    docker hub    (library  -itory  tag
#   by default)  by default)  name   (latest by default)
#   |---------|-------|------|---|

FROM docker.io/library/python:3.9
# you'd just say "python:3.9" though

# two most common commands in here
# COPY: for copying files from outside the image into the image
# RUN: for running any shell command inside the image
#    (e.g. install something with apt)

# install dependencies
# RUN apt update \
#     && apt install nano

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv venv

# THIS command executes when the image is being built
RUN venv/bin/python3 -m pip install -r requirements.txt

# don't copy unnecessary things into the image, because that might
# pollute things, make the build less repeatable
# our main tool for that is a "dockerignore" file.
# patterns matching the .dockerignore file will be ignored from the build context

# RUN python3 -m pip install -r requirements.txt
# CMD ["python3", "-m", "Hawkins_P0"]

# THIS is just metadata on the image - what command will execute to start each container
CMD ["venv/bin/python3", "-m", "Hawkins_P0"]
# you can override the CMD with a second argument to docker run
# usually we use this more awkward syntax for CMD

# the docker engine is made with a client-server architecture
# so the CLI that you type "docker" commands into
# is a separate program from all the rest (building images, running containers, etc.)
# all the rest, the server-side, is called the "Docker daemon"

# when you run "docker build", the first argument is the "build context" directory
# the first thing that happens is the build context is uploaded to the docker daemon
# we look for a Dockerfile, by default at <buildcontext>/Dockerfile, or override it with -f option
# then, we go line by line through the Dockerfile

COPY . .
