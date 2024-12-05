const redis = require('redis');
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


async function setNewSchool(schoolName, value) {
    await client.set(schoolName, value, redis.print);
};

async function displaySchoolValue(schoolName) {
    await client.get(schoolName, (err, reply) => {
        if (err) throw err;
        console.log(reply)
    })
};

connectToRedis();
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
