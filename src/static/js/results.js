document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.result-box').forEach(function(box) {
        const shortComment = box.querySelector('.short-comment');
        const fullComment = box.querySelector('.full-comment');
        const toggleButton = box.querySelector('.toggle-comment');

        // Check if elements exist before accessing their properties
        if (shortComment && fullComment && toggleButton) {
            if (fullComment.textContent.trim().length <= 100) {
                shortComment.classList.add('d-none');
                fullComment.classList.remove('d-none');
                toggleButton.classList.add('d-none');
            } else {
                toggleButton.addEventListener('click', function() {
                    if (fullComment.classList.contains('d-none')) {
                        fullComment.classList.remove('d-none');
                        shortComment.classList.add('d-none');
                        this.textContent = 'Read less';
                    } else {
                        fullComment.classList.add('d-none');
                        shortComment.classList.remove('d-none');
                        this.textContent = 'Read more';
                    }
                });
            }
        }
    });
});