import argparse
import pandas as pd
from googleapiclient.discovery import build

API_KEY = "AIzaSyAl_KxBiOu2-7toS4yTZ7D8zCxbVC6cd4A"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def fetch_videos(genre, max_results=500):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    videos = []
    next_page_token = None

    print(f"Fetching videos for genre: {genre}")
    while len(videos) < max_results:
        request = youtube.search().list(
            q=genre,
            part="snippet",
            maxResults=min(50, max_results - len(videos)),
            type="video",
            pageToken=next_page_token
        )
        response = request.execute()
        for item in response['items']:
            videos.append(item['id']['videoId'])
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
    print(f"Found {len(videos)} videos.")
    return videos

def fetch_video_details(video_ids):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    details = []

    for i in range(0, len(video_ids), 50):  # API allows up to 50 IDs per request
        request = youtube.videos().list(
            part="snippet,statistics,contentDetails,topicDetails,recordingDetails,status",
            id=",".join(video_ids[i:i+50])
        )
        response = request.execute()
        for item in response['items']:
            captions_available = item['status'].get('caption', 'false')

            details.append({
                "Video URL": f"https://www.youtube.com/watch?v={item['id']}",
                "Title": item['snippet']['title'],
                "Description": item['snippet'].get('description', ''),
                "Channel Title": item['snippet']['channelTitle'],
                "Keyword Tags": ", ".join(item['snippet'].get('tags', [])),
                "YouTube Video Category": item['snippet'].get('categoryId', ''),
                "Topic Details": ", ".join(item.get('topicDetails', {}).get('topicCategories', [])),
                "Video Published At": item['snippet']['publishedAt'],
                "Video Duration": item['contentDetails']['duration'],
                "View Count": item['statistics'].get('viewCount', '0'),
                "Comment Count": item['statistics'].get('commentCount', '0'),
                "Captions Available": captions_available,
                "Caption Text": "Available" if captions_available == 'true' else "Not Available",
                "Location of Recording": item.get('recordingDetails', {}).get('locationDescription', 'Not Provided')
            })
    return details

def save_to_csv(data, genre):
    df = pd.DataFrame(data)
    filename = f"{genre}_videos.csv"
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube video data.")
    parser.add_argument("--genre", type=str, required=True, help="Genre for video search.")
    args = parser.parse_args()

    # Step 1: Fetch video IDs
    video_ids = fetch_videos(args.genre)

    # Step 2: Fetch video details
    video_details = fetch_video_details(video_ids)

    # Step 3: Save results to CSV
    save_to_csv(video_details, args.genre)

if __name__ == "__main__":
    main()
