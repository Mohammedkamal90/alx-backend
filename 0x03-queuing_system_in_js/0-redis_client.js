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
