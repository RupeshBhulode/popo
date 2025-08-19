from fastapi import APIRouter, HTTPException
from .models import VideoRequest
from .scraper import scrape_video_data
from .firebase_db import videos_collection  # Firestore
from google.cloud.firestore_v1 import DocumentReference

router = APIRouter()

# SCRAPE + SAVE
@router.post("/scrape-video")
def scrape_video(data: VideoRequest):
    video_data = scrape_video_data(data.url)
    if not video_data:
        raise HTTPException(status_code=400, detail="Could not scrape video")
    
    # Add to Firestore
    doc_ref = videos_collection.add(video_data)
    video_data["id"] = doc_ref[1].id
    return video_data

# READ all videos
@router.get("/videos")
def get_videos():
    videos = videos_collection.stream()
    video_list = []
    for doc in videos:
        data = doc.to_dict()
        data["id"] = doc.id
        video_list.append(data)
    return video_list

# DELETE by ID
@router.delete("/videos/{video_id}")
def delete_video(video_id: str):
    doc_ref = videos_collection.document(video_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Video not found")
    doc_ref.delete()
    return {"message": "Video deleted successfully"}
