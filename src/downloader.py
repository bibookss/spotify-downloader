import yt_dlp 
import os

def download(title, link, path):
  with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': '%(title)s.mp3'}) as video:
    info_dict = video.extract_info(link, download = True)
    video_title = info_dict['title']
    print(video_title)
    video.download(link)    
    os.rename(f'{video_title}.mp3', f'{path}/{title}.mp3')