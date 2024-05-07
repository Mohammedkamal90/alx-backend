// Import necessary modules
import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Promisify the get and set functions of the client
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

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

// Function to set a new school value in Redis
async function setNewSchool(schoolName, value) {
    await setAsync(schoolName, value);
    console.log(`Value for ${schoolName} set to ${value}`);
}

// Function to display the value for a school key using async/await
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.error(`Error getting value for ${schoolName}: ${err}`);
    }
}

// Call the functions as per requirements
async function main() {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
}

main();
