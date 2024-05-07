// Import necessary modules
import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
function sendNotification(phoneNumber, message, job, done) {
    // Track progress of the job
    job.progress(0, 100);

    // Check if phoneNumber is blacklisted
    if (blacklistedNumbers.includes(phoneNumber)) {
        // Fail the job if phoneNumber is blacklisted
        job.fail(new Error(`Phone number ${phoneNumber} is blacklisted`));
        done();
    } else {
        // Update progress of the job
        job.progress(50, 100);
        
        // Log sending notification
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

        // Complete the job
        done();
    }
}

// Create a job queue with Kue
const queue = kue.createQueue({ concurrent: 2, prefix: 'q' });

// Process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
    // Get job data
    const { phoneNumber, message } = job.data;

    // Call sendNotification function
    sendNotification(phoneNumber, message, job, done);
});
