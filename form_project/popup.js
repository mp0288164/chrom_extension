document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('fillFormBtn').addEventListener('click', function () {
        var fileInput = document.getElementById('pdfFile');
        var file = fileInput.files[0];
        if (file) {
            var formData = new FormData();
            formData.append('pdf', file);
            
            // Send PDF file to backend for processing
            fetch('http://localhost:8000/fill_form/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log('Form filled successfully:', data);
                alert('Form filled successfully!');
            })
            .catch(error => {
                console.error('Error filling form:', error);
                alert('Error filling form. Please try again.');
            });
        } else {
            alert('Please select a PDF file.');
        }
    });
});
