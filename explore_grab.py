import requests
import re
from mash_streamurl import get_stream_url
import tkinter as tk
from tkvideo import tkvideo
# test file for cycling through livestreams of bears
# simple stress test for IP camera feed and feed switching


# grab urls from youtube playlist and append to an array
playlist_url = 'https://www.youtube.com/playlist?list=PLkAmZAcQ2jdpVJzzGLhuuKl9QO4m__VVU'

# get the url of each livestream on the playlist
def get_urls_from_playlist(playlist_url):
    r = requests.get(playlist_url)
    if r.status_code == 200:
        # Find all the video URLs in the playlist
        video_urls = re.findall(r'watch\?v=[\w-]+', r.text)
        # Construct the full video URLs
        return [f'https://www.youtube.com/{url}' for url in video_urls]
    return []

bear_url_array = get_urls_from_playlist(playlist_url)
print(bear_url_array)

# for stream_url in bear_url_array:
#     if stream_url:
#         print(f"Stream URL: {stream_url}")
#         import video_feed_test
#         video_feed_test.create_window(stream_url)
#     else:
#         print("Stream URL not found.")


root = tk.Tk()

def close_video(win):
    if win.winfo_exists():
        win.destroy()

def create_window(stream_url):
    window = tk.Toplevel()
    window.lift()

    player = tkvideo(window, loop=0)
    player.load(stream_url)
    player.pack(expand=True, fill="both")

    window.after(2000, close_video, window) # close win after 2 sec
    player.bind("<<Ended>>", lambda event: close_video(window)) # close the win if video ended

    player.play() # play the video

for stream_url in bear_url_array:
    create_window(stream_url)

root.mainloop()


# =============== #
# pass video for testing.
