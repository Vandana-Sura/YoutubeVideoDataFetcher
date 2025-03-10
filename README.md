

# **YouTube Video Data Scraper** 🎥📊  

This project fetches YouTube video data based on a given genre, extracts key metadata, and saves the results to a CSV file. It leverages the **YouTube Data API v3** to search for videos, retrieve details, and structure the information in a tabular format.

## **Features** 🚀  
✔️ Fetches up to **500 videos** per genre.  
✔️ Extracts video details such as title, description, views, comments, duration, and more.  
✔️ Saves the collected data to a **CSV file** for easy analysis.  
✔️ Uses **Google API Client** for seamless interaction with YouTube.  

## **Tech Stack** 🛠️  
- **Python 3**  
- **Google YouTube Data API v3**  
- **pandas** for data handling  
- **argparse** for command-line input  

## **Setup & Installation** ⚙️  

### **1. Clone the Repository**  
```sh
git clone https://github.com/your-username/youtube-video-scraper.git
cd youtube-video-scraper
```

### **2. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3. Set Up YouTube API Key**  
1. Get an API key from the [Google Cloud Console](https://console.cloud.google.com/).  
2. Replace `API_KEY = "XXXXXXXXXXXXXXXXX"` in `script.py` with your actual API key.  

### **4. Run the Script**  
```sh
python script.py --genre "technology"
```
This will fetch video data for the `"technology"` genre and save it as `technology_videos.csv`.

