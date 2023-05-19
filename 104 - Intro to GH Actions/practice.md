# Part 1
## Simple CI workflow

Create a CI workflow for the the [simple-node-app](https://github.com/jdassonvil/simple-node-app) or another nodeJS repository of yours.

This workflow should at least run the following steps:

- Check the code format using [prettier](https://prettier.io/)
- Run the unit tests using `npm test`
- Run the [ES lint](https://eslint.org/) linter
- Check for outdated dependencies using [npm-check-updates](https://www.npmjs.com/package/npm-check-updates)
- Check for known vulnerabilities using `npm audit`



Bonus:

- Run a test that start the docker-compose and test that app work properly
