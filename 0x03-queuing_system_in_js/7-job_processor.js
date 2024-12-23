const kue = require('kue');
const queue = kue.createQueue();

const blacklisted = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);

    if (blacklisted.includes(phoneNumber)) {
        
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    } else {
        job.progress(50, 100);
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
        job.progress(100, 100);
        done();
    };
};

queue.process('push_notification_code_2', 2, function(job, done) {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
