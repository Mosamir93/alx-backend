const redis = require('redis');
const subscriber = redis.createClient();

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
    console.log('Redis client not connected to the server:', err)
});

subscriber.subscribe('holberton school channel');
subscriber.on('message', function (channel, message) {
    console.log(message);
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    };
});
