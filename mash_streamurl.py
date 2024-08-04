import yt_dlp

def get_stream_url(youtube_video_id):
    url = f"https://youtu.be/hdt1aldxafk?si=kW7iy0GEy57qIIED"
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'simulate': True,
        'dump_json': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])
        if formats:
            # Prefer the first format that is not a dash (adaptive streaming)
            for f in formats:
                if f.get('protocol') == 'https':
                    return f.get('url')
        return None

if __name__ == '__main__':
    youtube_video_id = 'YOUR_LIVESTREAM_VIDEO_ID'  # Replace with the actual YouTube livestream ID
    stream_url = get_stream_url(youtube_video_id)
    if stream_url:
        print(f"Stream URL: {stream_url}")
    else:
        print("Stream URL not found.")
