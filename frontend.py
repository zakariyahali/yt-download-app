from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup

# Import the backend downloader
from backend import Youtubedownloader 

# Import tkinter for the file dialog
import tkinter as tk
from tkinter import filedialog

class DownloaderGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Dropdown for selecting the download type
        self.spinner = Spinner(
            text='Select Download Type',
            values=('Download Video', 'Download Playlist', 'Download Video as Audio', 'Download Playlist as MP3'),
            size_hint=(1, 0.1)
        )
        self.add_widget(self.spinner)

        # Text input for the URL
        self.url_input = TextInput(
            size_hint=(1, 0.2),
            multiline=False,
            hint_text='Enter YouTube URL here'
        )
        self.add_widget(self.url_input)

        # Text input for the save path
        self.path_input = TextInput(
            size_hint=(1, 0.15),
            multiline=False,
            hint_text='Enter save path here',
            readonly=True  # Make the text input read-only
        )
        self.add_widget(self.path_input)

        # Button to open the file dialog
        self.path_button = Button(
            text='Browse',
            size_hint=(1, 0.1)
        )
        self.path_button.bind(on_press=self.open_file_dialog)
        self.add_widget(self.path_button)

        # Download button
        self.download_button = Button(
            text='Download',
            size_hint=(1, 0.1)
        )
        self.download_button.bind(on_press=self.start_download)
        self.add_widget(self.download_button)

        # Label for showing messages
        self.message_label = Label(size_hint=(1, 0.1))
        self.add_widget(self.message_label)

    def open_file_dialog(self, instance):
        root = tk.Tk()
        root.withdraw()  # Use to hide tkinter window

        dir_path = filedialog.askdirectory()
        if dir_path:
            self.path_input.text = dir_path

    def start_download(self, instance):
        print("Download button pressed")  # Debug print
        download_type = self.spinner.text
        url = self.url_input.text.strip()
        save_path = self.path_input.text.strip()

        if not url:
            self.message_label.text = 'Please enter a valid URL.'
            return

        if not save_path:
            self.message_label.text = 'You must choose a file path for your download.'
            return

        downloader = Youtubedownloader()  # Assuming no args are needed for initialization

        try:
            if download_type == 'Download Video':
                downloader.download_single_video(url, save_path)
            elif download_type == 'Download Playlist':
                downloader.download_playlist(url, save_path)
            elif download_type == 'Download Video as Audio':
                downloader.download_video_as_audio(url, save_path)
            elif download_type == 'Download Playlist as MP3':
                downloader.download_playlist_as_mp3(url, save_path)

            self.message_label.text = 'Download started! Check your downloads folder.'
        except Exception as e:
            self.message_label.text = f'Error: {str(e)}'
            print("Error details:", str(e))  # Print more detailed error information for debugging

class YoutubeDownloaderApp(App):
    def build(self):
        return DownloaderGUI()

if __name__ == '__main__':
    YoutubeDownloaderApp().run()