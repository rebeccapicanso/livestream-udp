import tkinter as tk
from tkvideo import tkvideo

root = tk.Tk()

def close_video(win):
    if win.winfo_exists():
        win.destroy()

def create_window(stream_url):
    window = tk.Toplevel()
    window.lift()

    player = tkvideo.TkinterVideo(window, loop=0)
    player.load(stream_url)
    player.pack(expand=True, fill="both")

    window.after(2000, close_video, window) # close win after 2 sec
    player.bind("<<Ended>>", lambda event: close_video(window)) # close the win if video ended

    player.play() # play the video

tk.Button(root, text="Show Video", command=create_window).pack()
root.mainloop()
