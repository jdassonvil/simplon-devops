# Part 1
## docker-compose

The objective of this exercise is to create a fully self served docker-compose environment for the simple-node-app.

1. Checkout the latest version of the [simple-node-app](https://github.com/jdassonvil/simple-node-app)
1. Using the documentation from the [docker hub](https://hub.docker.com/_/postgres) start a postgres container exposed to your localhost
1. Create the `messages` table as described in the [simple-node-app](https://github.com/jdassonvil/simple-node-app)
1. Test that the simple-node-app works well and can display the messages you have inserted in the database
1. Using the documentation from the [docker hub](https://hub.docker.com/_/postgres) create an init script to initialize the database with values
1. Create a `docker-compose.yml` that contains the simple-node-app and the database
