# Part 1
## Networking

1. Start a mongo database using docker in daemon monde. What is its IP address ? How can you reach it ?
1. From the mongo container run the command `mongosh` to open a shell to the mongo database.
1. In the shell the following instructions to add some data to the database:

```
use simplon
db.messages.insertOne({"message": "Hello it's <your name>"});
```

4. Get the new version of the simple node app. Don't forget to checkout the README.
5. Start the application <ins>locally without docker</ins> and connect it to the database.
6. Make sure `curl http://localhost:3000` still works
7. Stop and clean up all the containers

### Bonus
1. Update the Dockerfile and make sure the application can still be started
1. Run both applications in containers

# Part 2
### Volumes

1. Checkout the [documentation](https://hub.docker.com/_/mongo) to understand how volumes should be configured for mongodb
1. Use a named volume to persist the mongo data
1. Mount the volume in another container to inspect the content of the data directory
