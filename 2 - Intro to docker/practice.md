# Part 1
## Running my first container

1. Install Docker on your local https://docs.docker.com/engine/install/
2. Run an ubuntu container and display the current unix distribution (tip: you can use [uname](https://www.cyberciti.biz/faq/find-check-unix-version-command/))
3. Try to do the same thing with another Linux distribution such as Debian or Fedora.
4. How many stopped container do you have on your machine now ? Clean up the unused containers and images.

## Running a simple web server
1. Use docker run to start an instance of NGINX on your laptop. From your browser you should be able to access the NGINX landing page at http://localhost:80.
2. Which OS base image is using NGINX ?
3. Stop the running containers and clean up the stopped containers.

### Bonus
1. Run 2 concurrent NGINX server. Both should be accessible from your web browser.
2. How many process is running inside the container ?

# Part 2

## Writing Dockerfiles

1. Fork the [simple NodeJS application](link)
2. Update the app.js file to display your own message
3. Write a Dockerfile for this application based on an ubuntu image
4. Build and run your application
5. Update the README to explain how to build and run this application

### Bonus
1. Using the documentation from the docker hub, host a static web page on an NGINX server.
