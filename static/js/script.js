// JavaScript for RecipeHub

// Function to toggle visibility of recipe details
function toggleRecipeDetails(recipeId) {
    var details = document.getElementById('recipe-details-' + recipeId);
    details.classList.toggle('hidden');
}

// Function to handle rating submission
function submitRating(recipeId) {
    var ratingValue = document.getElementById('rating-value-' + recipeId).value;
    // Perform AJAX request to submit rating to the server
    fetch('/recipe/' + recipeId + '/rate', {
        method: 'POST',
        body: JSON.stringify({ value: ratingValue }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to submit rating');
        }
        return response.json();
    })
    .then(data => {
        console.log('Rating submitted successfully:', data);
        // Update UI to reflect rating submission
        // For example, display a success message or update the rating display
    })
    .catch(error => {
        console.error('Error submitting rating:', error);
        // Handle error, display error message to user, etc.
    });
}

// Function to handle comment submission
function submitComment(recipeId) {
    var commentContent = document.getElementById('comment-content-' + recipeId).value;
    // Perform AJAX request to submit comment to the server
    fetch('/recipe/' + recipeId + '/comments', {
        method: 'POST',
        body: JSON.stringify({ content: commentContent }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to submit comment');
        }
        return response.json();
    })
    .then(data => {
        console.log('Comment submitted successfully:', data);
        // Update UI to reflect comment submission
        // For example, display a success message or update the comment display
    })
    .catch(error => {
        console.error('Error submitting comment:', error);
        // Handle error, display error message to user, etc.
    });
}
