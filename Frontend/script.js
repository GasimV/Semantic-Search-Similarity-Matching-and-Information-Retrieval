document.addEventListener('DOMContentLoaded', function() {
  // Toggle like/dislike
  var radios = document.querySelectorAll('input[type="radio"]');
  radios.forEach(function(radio) {
    radio.addEventListener('change', function(event) {
      alert('You selected ' + event.target.value);
    });
  });

  // Search form submission handling
  var searchForm = document.getElementById('searchForm');
  searchForm.addEventListener('submit', function(event) {
    event.preventDefault();
    var searchValue = document.getElementById('search').value;
    alert('Search for: ' + searchValue);
    // Typically, you would make an AJAX request here
  });

  // Feedback form handling
  const feedbackForm = document.getElementById('feedbackForm');
  const submitButton = document.getElementById('submitForm');
  const evaluationRadios = document.getElementsByName('evaluation');

  feedbackForm.addEventListener('input', function() {
    let isFeedbackFilled = document.getElementById('feedback').value.trim() !== '';
    let isEvaluationSelected = Array.from(evaluationRadios).some(radio => radio.checked);
    submitButton.disabled = !(isFeedbackFilled && isEvaluationSelected);
  });
});