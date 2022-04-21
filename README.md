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
