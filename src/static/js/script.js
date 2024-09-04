document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("analyzeForm");
  const input = document.getElementById("url");
  const clearButton = document.getElementById("clear-button");

  form.addEventListener("submit", (event) => {
    if (!input.value) {
      event.preventDefault();
    }
  });

  input.addEventListener("input", function () {
    if (input.value.length > 0) {
      clearButton.style.display = "block";
    } else {
      clearButton.style.display = "none";
    }
  });

  clearButton.addEventListener("click", function () {
    input.value = "";
    clearButton.style.display = "none";
    input.blur();
  });
});
