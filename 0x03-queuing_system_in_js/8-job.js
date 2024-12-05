export default function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData);

        job
            .on('complete', () => {
                console.log(`Notification job ${job.id || 'test'} completed`);
            })
            .on('failed', (err) => {
                console.log(`Notification job ${job.id || 'test'} failed: ${err}`);
            })
            .on('progress', (progress) => {
                console.log(`Notification job ${job.id || 'test'} ${progress}% complete`);
            });

        job.save((err) => {
            if (!err) console.log(`Notification job created: ${job.id || 'test'}`);
        });
    });
}
