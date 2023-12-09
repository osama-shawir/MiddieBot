document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();

    fetch('/generate', {
        method: 'POST',
        body: new FormData(event.target)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = data.message;
    });
});