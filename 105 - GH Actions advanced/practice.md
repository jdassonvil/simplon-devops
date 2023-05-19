# Part 2
## Continuous delivery

Update the Github actions configuration to add a release stage with the following specs:

- Publish a new docker image to hub.docker.com for each new commit **on the main branch**
- Image should be available with a different version tag for each commit
- Latest release should be available using the `latest` tag
- Dockerhub token must be kept secret
