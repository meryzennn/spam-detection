document.getElementById('spamForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const message = document.getElementById('message').value;

    fetch('/check_spam', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'message': message
        })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        if (data.is_spam === 'spam') {
            resultDiv.innerHTML = '<p class="text-danger">Pesan ini adalah spam!</p>';
        } else {
            resultDiv.innerHTML = '<p class="text-success">Pesan ini bukan spam.</p>';
        }
    });
});
