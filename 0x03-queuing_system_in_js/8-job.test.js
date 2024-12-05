import createPushNotificationsJobs from './8-job.js';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
    before(() => {
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
    });

    after(() => {
        queue.testMode.exit();
    });

    it('display an error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
    });

    it('create two new jobs to the queue', () => {
        const jobs = [
            { phoneNumber: '4153518780', message: 'This is the code 1234' },
            { phoneNumber: '4153518781', message: 'This is the code 5678' },
        ];

        createPushNotificationsJobs(jobs, queue);
        const jobsInQueue = queue.testMode.jobs;

        expect(jobsInQueue).to.have.lengthOf(2);

        jobsInQueue.forEach((job, index) => {
            expect(job.type).to.equal('push_notification_code_3');
            expect(job.data).to.deep.equal(jobs[index]);
        });
    });
});
