// Add your JavaScript code here
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('patient-registration-form');
    
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        
        // Get form data and submit it to the server using AJAX or fetch API
        // Example:
        const formData = new FormData(form);
        
        fetch('/api/patients/register/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the server
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
