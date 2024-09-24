document.addEventListener("DOMContentLoaded", function() {
    // Get the modal
    var modalElement = document.getElementById('details-modal');
    var modal = new bootstrap.Modal(modalElement);

    // Get the button that opens the modal
    var btns = document.getElementsByClassName("details");

    // Get the elements to populate the modal
    var authorElement = document.getElementById("author");
    var commentElement = document.getElementById("comment");
    var basicSentimentElement = document.getElementById("basic-sentiment");
    var fineSentimentElement = document.getElementById("fine-sentiment");

    // Loop through all buttons to add event listeners
    for (var i = 0; i < btns.length; i++) {
        btns[i].onclick = function() {
            var result = this.parentElement;
            var author = result.getAttribute("data-author");
            var comment = result.getAttribute("data-comment");
            var basicSentiment = result.getAttribute("data-basic-sentiment");
            var fineSentiment = result.getAttribute("data-fine-sentiment");

            authorElement.innerText = "Author: " + author;
            commentElement.innerText = "Comment: " + comment;
            basicSentimentElement.innerText = "Basic Sentiment: " + basicSentiment;
            fineSentimentElement.innerText = "Fine-Grained Sentiment: " + fineSentiment;

            modal.show();
        }
    }
});