from moviepy.editor import *
from pytube import Playlist, YouTube
import os

class Youtubedownloader:

    def download_single_video(self, url, save_path):
        # Try to execute the download process
        try:
            # URL of the YouTube video
            yt = YouTube(url)  # Create a YouTube object

            # Select the highest resolution
            stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
            print("Video Title:", yt.title)

            # Set the save path and filename
            filename = yt.title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace('&', '_').replace('%', '_').replace('#', '_').replace('{', '_').replace('}', '_').replace('[', '_').replace(']', '_').replace('=', '_').replace('+', '_').replace('-', '_').replace('--', '_').replace(';', '_').replace('!', '_').replace('@', '_').replace('$', '_').replace('^', '_').replace('`', '_').replace('~', '_').replace(',', '_').replace('.', '_').replace(' ', '_')

            # Download with specified filename
            stream.download(output_path=save_path, filename=filename)
            print(f'Download completed! Video saved as -> {filename} in {save_path}')

        except Exception as e:
            print(f"An error occurred: {e}")

        ####################################################################################
        ####################################################################################
        ########  renaming the file to add the .mp4 extension
        new_extension = '.mp4'
        directory = save_path
        old_name = filename

        sepaa = '/'

        # # locate the file 
        full_path = directory +sepaa +old_name
        # Check if the file exists
        if not os.path.exists(full_path):
            print(f"The file {old_name} does not exist.")


        # declare new name (just adding the .mp4 onto the file)
        new_full_path = directory + sepaa + old_name + new_extension


        # # Rename the file
        os.rename(full_path, new_full_path)
        print(f"File renamed to: {new_full_path}")
        ####################################################################################
        ####################################################################################

    def download_playlist(self, url, save_path):
        # Create a Playlist object
        p = Playlist(url)

        # Loop through all videos in the playlist
        for video_url in p.video_urls:
            print(f'Downloading video: {video_url}')
            yt = YouTube(video_url)
            
            # Get the highest resolution MP4 stream available
            stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
            # Download the video in MP4 format
            filename = yt.title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace('&', '_').replace('%', '_').replace('#', '_').replace('{', '_').replace('}', '_').replace('[', '_').replace(']', '_').replace('=', '_').replace('+', '_').replace('-', '_').replace('--', '_').replace(';', '_').replace('!', '_').replace('@', '_').replace('$', '_').replace('^', '_').replace('`', '_').replace('~', '_').replace(',', '_').replace('.', '_').replace(' ', '_')
            stream.download(output_path=save_path, filename=filename)
     
            print(f'Downloaded: {yt.title}')



            new_extension = '.mp4'
            directory = save_path
            old_name = filename

            sepaa = '/'

            # # locate the file 
            full_path = directory +sepaa +old_name
            # Check if the file exists
            if not os.path.exists(full_path):
                print(f"The file {old_name} does not exist.")


            # declare new name (just adding the .mp4 onto the file)
            new_full_path = directory + sepaa + old_name + new_extension


            # # Rename the file
            os.rename(full_path, new_full_path)
            print(f"File renamed to: {new_full_path}")


        print("All videos downloaded in MP4 format!")

    def download_video_as_audio(self, url, save_path):
        try:
            print("Accessing YouTube URL...")
            yt = YouTube(url)
            print("Downloading audio from:", yt.title)
            
            # Select the audio stream
            audio_stream = yt.streams.filter(only_audio=True).first()
            if not audio_stream:
                print("No audio stream found")
                return
            
            # Download the audio stream
            output_file = audio_stream.download(output_path=save_path)
            print("Downloaded audio file:", output_file)
            
            # Convert the audio file to MP3 using moviepy
            new_file = os.path.splitext(output_file)[0] + '.mp3'
            print("Converting file to MP3...")
            audio_clip = AudioFileClip(output_file)
            audio_clip.write_audiofile(new_file, codec='mp3')
            audio_clip.close()
            
            # Remove the original download (optional)
            os.remove(output_file)
            print("Conversion complete. Saved as:", new_file)
            
        except Exception as e:
            print(f"An error occurred: {e}")

    def download_playlist_as_mp3(self,url, save_path):
        try:
            # Initialize Playlist
            p = Playlist(url)
            print(f"Downloading playlist: {p.title}")

            # Process each video in the playlist
            for video_url in p.video_urls:
                yt = YouTube(video_url)
                print(f"Downloading audio from: {yt.title}")

                # Select the best audio stream
                audio_stream = yt.streams.filter(only_audio=True).first()
                if audio_stream is None:
                    print("No audio stream found")
                    continue

                # Download the audio stream
                output_file = audio_stream.download(output_path=save_path)
                print("Downloaded audio file:", output_file)

                # Convert the audio file to MP3 using moviepy
                new_file = os.path.splitext(output_file)[0] + '.mp3'
                print("Converting file to MP3...")
                audio_clip = AudioFileClip(output_file)
                audio_clip.write_audiofile(new_file, codec='mp3')
                audio_clip.close()

                # Optionally remove the original download
                os.remove(output_file)
                print("Conversion complete. Saved as:", new_file)
                
        except Exception as e:
            print(f"An error occurred: {e}")