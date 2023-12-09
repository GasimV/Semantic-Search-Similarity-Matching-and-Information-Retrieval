
// Example JavaScript to toggle like/dislike
document.addEventListener('DOMContentLoaded', function() {
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
    // Here you would typically make an AJAX request to your server or perform some other action
  });
});
