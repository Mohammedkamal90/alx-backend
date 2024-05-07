// Import necessary modules
import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

// Create a test suite for createPushNotificationsJobs function
describe('createPushNotificationsJobs', () => {
    // Define a variable to store the Kue queue
    let queue;

    // Before running the tests, set up the Kue queue and enter test mode
    before(() => {
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    // After running the tests, clear the queue and exit test mode
    after(() => {
        queue.testMode.exit();
    });

    // Test case to check error message if jobs is not an array
    it('display a error message if jobs is not an array', () => {
        // Call the function with a non-array argument
        expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
    });

    // Test case to check creation of two new jobs to the queue
    it('create two new jobs to the queue', () => {
        // Define test data (array of jobs)
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 5678 to verify your account'
            }
        ];

        // Call the function to create jobs
        createPushNotificationsJobs(jobs, queue);

        // Check if two jobs are created in the queue
        expect(queue.testMode.jobs.length).to.equal(2);
    });
});
