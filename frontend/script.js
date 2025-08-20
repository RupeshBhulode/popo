const API_URL = "https://popo-1.onrender.com"; // FastAPI backend

// Fetch and display videos
async function loadVideos() {
  const res = await fetch(`${API_URL}/videos`);
  const videos = await res.json();

  const videoList = document.getElementById("videoList");
  videoList.innerHTML = "";

  videos.forEach(video => {
    const card = document.createElement("div");
    card.className = "video-card";

    card.innerHTML = `
      <img src="${video.thumbnail}" alt="thumbnail">
      <h3>${video.title}</h3>
      <a href="${video.url}" target="_blank">Watch Video</a>
      <button class="delete-btn" onclick="deleteVideo('${video.id}')">Delete</button>
    `;

    videoList.appendChild(card);
  });
}

// Add a new video
async function addVideo() {
  const url = document.getElementById("videoUrl").value;
  if (!url) return alert("Enter a URL!");

  // POST to the new route /scrape-video
  await fetch(`${API_URL}/scrape-video`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url })
  });

  document.getElementById("videoUrl").value = "";
  loadVideos();
}

// Delete a video
async function deleteVideo(id) {
  await fetch(`${API_URL}/videos/${id}`, { method: "DELETE" });
  loadVideos();
}

// Load videos on page load
loadVideos();
