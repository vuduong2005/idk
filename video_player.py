import tkinter as tk
from tkinter import ttk
from create_video_list import CreateVideo
from check_videos import CheckVideos
from update_videos import UpdateVideo
import font_manager as font

class MainApp:
    def __init__(self, root):
        self.root = root
        root.geometry("1200x600")
        root.title("Video Library")

        # Configure fonts
        font.configure()

        # Create notebook (tabs) and frames
        self.tab_control = ttk.Notebook(root)
        self.tab_control.pack(expand=1, fill="both")

        # Create tabs
        self.create_video_tab = ttk.Frame(self.tab_control)
        self.check_videos_tab = ttk.Frame(self.tab_control)
        self.update_video_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.create_video_tab, text="Create Video")
        self.tab_control.add(self.check_videos_tab, text="Check Videos")
        self.tab_control.add(self.update_video_tab, text="Update Video")

        # Initialize frames for each tab
        self.create_video_app = CreateVideo(self.create_video_tab)
        self.check_videos_app = CheckVideos(self.check_videos_tab)
        self.update_video_app = UpdateVideo(self.update_video_tab)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
    
