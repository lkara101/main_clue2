// Get the select element for sorting
const sortSelect = document.getElementById("sort_by");

// Check if a previously selected option is stored in local storage
const savedSortOption = localStorage.getItem("selected_sort_option");

// If a saved sorting option is found, set it as the selected option in the dropdown
if (savedSortOption) {
    sortSelect.value = savedSortOption;
}

// Add an event listener to save the selected option when it changes
sortSelect.addEventListener("change", function() {
    localStorage.setItem("selected_sort_option", this.value);
});
