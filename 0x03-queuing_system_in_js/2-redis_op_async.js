const redis = require('redis');
const { promisify } = require('util');
import { createClient } from "redis";

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err)
});

async function connectToRedis() {
    await client.connect();
}

const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
    await client.set(schoolName, value, redis.print);
};

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.log(err);
    }
};

connectToRedis();
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
