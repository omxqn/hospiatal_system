// registration.js

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('patient-registration-form');
    
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Perform client-side validation (e.g., check for valid inputs)
        const firstName = document.getElementById('first-name').value;
        const lastName = document.getElementById('last-name').value;
        const dob = document.getElementById('dob').value;

        if (firstName.trim() === '' || lastName.trim() === '' || dob.trim() === '') {
            alert('Please fill out all fields.');
            return;
        }

        // If validation passes, submit the form to the server
        form.submit();
    });
});
