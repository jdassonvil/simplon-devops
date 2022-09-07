# Part 1
## Running my first container

1. Install Docker on your local machine https://docs.docker.com/engine/install/
1. Start an Ubuntu container and do the following operations:
   1. Write "Hello simplon" in a file
   1. Display the current unix distribution
   1. Install curl and run `curl https://simplon.co` 
1. How many process is running inside the container ?
1. How many stopped container do you have on your machine now ? Clean up the unused containers and images.

### Bonus
1. Try to do the same thing with the Alpine linux distribution.


## Running a simple web server
1. Use docker run to start an instance of NGINX on your laptop **in daemon mode**. From your browser you should be able to access the NGINX landing page at http://localhost:80.
2. Which OS base image is using NGINX ?
3. Stop the running containers and clean up the stopped containers.

### Bonus
1. Run 2 concurrent NGINX server. Both should be accessible from your web browser.

# Part 2

## Writing Dockerfiles

1. Fork the [simple NodeJS application](https://github.com/jdassonvil/simple-node-app)
2. Update the app.js file to display your own message
3. Write a Dockerfile for this application based on an ubuntu image
4. Run the application application
5. Update the README to explain how to build and run this application

### Bonus
1. Using the documentation from [hub.docker.com](https://hub.docker.com/_/nginx/), host a static web page on an NGINX server.
