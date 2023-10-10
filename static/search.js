// Get the input element for the search string
const searchInput = document.getElementById("search_string");

// Check if a previously entered search string is stored in local storage
const savedSearchString = localStorage.getItem("search_string");

// If a saved search string is found, set it as the value of the input field
if (savedSearchString) {
    searchInput.value = savedSearchString;
}

// Add an event listener to save the entered search string when it changes
searchInput.addEventListener("input", function() {
    localStorage.setItem("search_string", this.value);
});
