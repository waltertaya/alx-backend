# 0x03. Queuing System in JS

This project focuses on building a queuing system in JavaScript using various tools and technologies, including Redis, Node.js, Express, and Kue. The tasks involve setting up a Redis server, interacting with it using Node.js, handling asynchronous operations, and implementing a queue system with Kue.

## Resources
To complete this project, the following resources are recommended:
- [Redis quick start](https://redis.io/topics/quickstart)
- [Redis client interface](https://github.com/NodeRedis/node-redis)
- [Redis client for Node JS](https://github.com/NodeRedis/node-redis)
- [Kue (deprecated but still used in the industry)](https://github.com/Automattic/kue)

## Learning Objectives
By the end of this project, you should be able to:
- Run a Redis server on your machine.
- Perform basic operations with Redis using a client.
- Use Redis with Node.js for basic operations.
- Store hash values in Redis.
- Handle asynchronous operations with Redis.
- Use Kue as a queuing system.
- Build a basic Express app interacting with a Redis server and queue.

## Requirements
- All code will be executed on Ubuntu 18.04, Node 12.x, and Redis 5.0.7.
- All files should end with a new line.
- A `README.md` file is mandatory.
- All code should use the `.js` extension.

## Tasks

### 0. Install a Redis Instance
- **Objective:** Download, extract, compile, and start a Redis server.
- **File:** `dump.rdb`

### 1. Node Redis Client
- **Objective:** Connect to a Redis server using Node.js and log connection status.
- **File:** `0-redis_client.js`

### 2. Node Redis Client and Basic Operations
- **Objective:** Set and get values in Redis using a Node.js client.
- **File:** `1-redis_op.js`

### 3. Node Redis Client and Async Operations
- **Objective:** Use `promisify` to handle async/await operations with Redis.
- **File:** `2-redis_op_async.js`

### 4. Node Redis Client and Advanced Operations
- **Objective:** Store and retrieve hash values in Redis.
- **File:** `4-redis_advanced_op.js`

### 5. Node Redis Client Publisher and Subscriber
- **Objective:** Implement a basic publish/subscribe system with Redis.
- **Files:** `5-subscriber.js`, `5-publisher.js`

### 6. Create the Job Creator
- **Objective:** Create a Kue job and handle job events.
- **File:** `6-job_creator.js`

### 7. Create the Job Processor
- **Objective:** Process jobs from a queue using Kue.
- **File:** `6-job_processor.js`

### 8. Track Progress and Errors with Kue: Create the Job Creator
- **Objective:** Track job progress and handle errors in Kue.
- **File:** `7-job_creator.js`

## Usage
To set up the environment, install the required packages by running:
```bash
$ npm install
```

For each task, execute the corresponding script with:
```bash
$ npm run dev <script_name.js>
```

## Repository
- **GitHub repository:** `alx-backend`
- **Directory:** `0x03-queuing_system_in_js`

## Notes
- Ensure that the Redis server is running before executing any scripts.
- Follow the instructions in each task to achieve the desired functionality.

## Author

- [waltertaya](https://www.github.com/waltertaya)
