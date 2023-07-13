function displayUserProfile(profile) {
    var profileDiv = document.getElementById("profile");
    var html = "<p><strong>Name:</strong> " + profile.username + "</p>";
    html += "<p><strong>Bio:</strong> " + profile.biography + "</p>";
    html += "<p><strong>Followers:</strong> " + profile.follower_count + "</p>";
    profileDiv.innerHTML = html;
}

function displayThreads(threads) {
    var threadsDiv = document.getElementById("threads");
    var html = "";
    for (var i = 0; i < threads.length; i++) {
        var thread = threads[i];
        var caption = thread.thread_items[0].post.caption.text;
        var likeCount = thread.thread_items[0].post.like_count;
        html += "<div class='post'>";
        html += "<p class='caption'>" + caption + "</p>";
        html += "<p>Likes: " + likeCount + "</p>";
        html += "</div>";
    }
    threadsDiv.innerHTML = html;
}

function displayReplies(replies) {
    var repliesDiv = document.getElementById("replies");
    var html = "";
    for (var i = 0; i < replies.length; i++) {
        var reply = replies[i];
        var caption = reply.thread_items[1].post.caption.text;
        var likeCount = reply.thread_items[1].post.like_count;
        html += "<div class='post'>";
        html += "<p class='caption'>" + caption + "</p>";
        html += "<p>Likes: " + likeCount + "</p>";
        html += "</div>";
    }
    repliesDiv.innerHTML = html;
}

fetch("/data")
    .then(response => response.json())
    .then(data => {
        displayUserProfile(data.profile);
        displayThreads(data.threads);
        displayReplies(data.replies);
    })
    .catch(error => console.error(error));