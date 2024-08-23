document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    
    if (form) {
        form.addEventListener('submit', function (event) {
            const description = document.querySelector('textarea[name="description"]');
            const fileInput = document.querySelector('input[type="file"]');
            const maxFileSize = 5 * 1024 * 1024; // 5MB

            if (!description.value.trim()) {
                alert('Description cannot be empty.');
                event.preventDefault();
                return false;
            }

            if (fileInput && fileInput.files[0] && fileInput.files[0].size > maxFileSize) {
                alert('File size cannot exceed 5MB.');
                event.preventDefault();
                return false;
            }
        });
    }
});
