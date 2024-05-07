// Import necessary modules
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});

// Close the connection when the script exits
process.on('SIGINT', () => {
    client.quit();
});

// Function to create and store a hash in Redis
function createHash() {
    client.hset('HolbertonSchools', 'Portland', 50, redis.print);
    client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
    client.hset('HolbertonSchools', 'New York', 20, redis.print);
    client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
    client.hset('HolbertonSchools', 'Cali', 40, redis.print);
    client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

// Function to display the hash stored in Redis
function displayHash() {
    client.hgetall('HolbertonSchools', (err, reply) => {
        if (err) {
            console.error(`Error getting hash from Redis: ${err}`);
        } else {
            console.log(reply);
        }
    });
}

// Call the functions as per requirements
createHash();
setTimeout(displayHash, 1000); // Adding a timeout to ensure the hash is stored before displaying it
