## Backend Engineer - Technical Test

**Updates: Check the APP_README.md for how to run my solution.
### Introduction

Your goal in this task is to implement a simple back-end service for managing the blood glucose readings of diabetes patients. The service associates readings with patients using UUIDs - there is no personally-identifiable information (PII) stored in the service.

Here is a sample of some blood glucose readings (from a particular patient) that can be stored in the service.

| Reading ID                           | Patient ID                           | Value | Unit  | Recorded At               |
| ------------------------------------ | ------------------------------------ | ----- | ----- | ------------------------- |
| 1faafa60-c19a-4dd1-b5b0-e1d55f9464d4 | 22c685ae-9249-4c84-9b6e-d0e3537be66e | 5.5   | mmol/L | 2021-01-01T09:15:00+00:00 |
| 70da0f35-317c-4a1a-a549-2f8e786b7cef | 22c685ae-9249-4c84-9b6e-d0e3537be66e | 7.2   | mmol/L | 2021-01-01T12:30:00+00:00 |
| 8a041e90-6c11-4b21-b345-cddbd57b8a1b | 22c685ae-9249-4c84-9b6e-d0e3537be66e | 5.1   | mmol/L | 2021-01-01T16:45:00+00:00 |

Your task is to create a RESTful API to implement CRUD operations on this data. You should provide five endpoints:

- GET /v1/reading - Get all readings
- POST /v1/reading - Create a new reading from a JSON body
- GET /v1/reading/{reading_id} - Get a single reading by ID
- PUT /v1/reading/{reading_id} - Update a reading's details by ID
- DELETE /v1/reading/{reading_id} - Delete a reading by ID

The endpoints are described in more detail in the OpenAPI specification in `openapi.yaml`. You can copy-paste the specification into https://editor.swagger.io/ to view a user-friendly summary.

### Implementation

The service may be implemented in either Node.js or Python using a webapp framework. You may use whatever framework you like - examples of suitable frameworks include Express, Flask, and FastAPI. Refer to the provided OpenAPI specification for the desired behaviour of the webapp. Make sure there are sensible HTTP status codes in the response (as described in the OpenAPI specification).

Use a database for persistence, though the technology you use is your own choice; you may also use any publicly-available (installable through normal package managers or build systems) ORMs, etc.

### Testing

A suite of Postman tests has been provided with this task in `postman-tests.json`. This file can run using the Postman desktop app, or using the `newman` CLI tool.

Note that the tests will assume the service is available at `http://localhost:8000`, and that you have followed the API specification in `openapi.yaml`.

#### Postman desktop app
1) Install the Postman desktop app (available here: https://www.postman.com/downloads/)
2) Import the Postman collection: File -> Import -> choose `postman-tests.json`
3) Run the Postman collection: Click on the collection -> Run

#### Newman CLI tool
1) Install newman: https://github.com/postmanlabs/newman#installation (`brew install newman` or `npm install -g newman`)
2) Run Postman collection: `newman run postman-tests.json`

### Requirements

- Submit your completed solution either as a git repository (using a public repo service such as GitHub or Bitbucket), or as a zip file (making sure you include the .git directory).
- Your solution should contain instructions sufficient to allow a technical user to install and run your app (ideally a README.md including, e.g. a lockfile or requirements.txt, or any build scripts).
- The collection of Postman tests described in the [Testing](#testing) section will be run against your service to verify that it is working as expected.

### Notes and suggestions

Some advice:
- We estimate this task shouldn't take more than 2 hours. If it is taking you significantly longer than this, tidy up what you have and then submit it. This is not supposed to be a task to test your endurance; your work and thoughts will provide valuable discussion points in any interview.
- Commit early and often rather than in a single large commit; trial and error is acceptable and even encouraged as it really helps us capture your thinking.
- You will be evaluated on providing a working API as well as basic code style, simplicity, and correctness. You will not be evaluated on the API’s robustness or performance, and you do not need to worry about production server setup (i.e. a framework’s default server in debug mode is fine).

For bonus points (not required for a passing solution), you could also:
- Containerise the solution using Docker
- Demonstrate a couple of good unit tests, using mocking where appropriate
- Use a package manager to manage dependencies, e.g. poetry or pipenv
- Provide a Makefile, e.g. to run the service and/or Postman tests

...although these are likely to take longer than the two-hour estimate :)
