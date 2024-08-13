const token = 'YOUR_PERSONAL_ACCESS_TOKEN';
const repoOwner = 'CodingKilling';
const repoName = 'voting_func';

function handleVote(voteOption) {
    const issueTitle = 'New Vote';
    const issueBody = `Voted for: ${voteOption}`;

    const apiUrl = `https://api.github.com/repos/${repoOwner}/${repoName}/issues`;

    const data = {
        title: issueTitle,
        body: issueBody
    };

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            Authorization: `token ${token}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Issue created:', data);
        alert('Vote recorded successfully!');
    })
    .catch(error => {
        console.error('Error creating issue:', error);
        alert('Failed to record vote. Please try again.');
    });
}

document.getElementById('voteButton').addEventListener('click', function() {
    const selectedOption = document.querySelector('input[name="vote"]:checked').value;
    handleVote(selectedOption);
});
