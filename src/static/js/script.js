document.getElementById('analyzeForm').addEventListener('submit', function(event) {
    var urlInput = document.getElementById('url').value;

    if (!urlInput) {
        event.preventDefault();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('url');
    const clearButton = document.getElementById('clear-button');

    input.addEventListener('input', function() {
        if (input.value.length > 0) {
            clearButton.style.display = 'block';
        } else {
            clearButton.style.display = 'none';
        }
    });

    clearButton.addEventListener('click', function() {
        input.value = '';
        clearButton.style.display = 'none';
    })
});