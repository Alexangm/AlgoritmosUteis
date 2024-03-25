from pytube import YouTube
from moviepy.editor import *

# URL do vídeo do YouTube
path = 'C:/Users/Alexsander/Documents/Meus documentos/Temporario'  # Path
url = 'https://www.youtube.com/watch?v=DeumyOzKqgI' # Vídeo

video = YouTube(url)
audioStream = video.streams.filter(only_audio=True).first()

# Baixar o áudio em webm
audioPath = os.path.join(path, video.title + '.webm')
audioStream.download(filename=audioPath, output_path=path)

# Converter para MP3
mp3Path = os.path.join(path, video.title + '.mp3')
audio = AudioFileClip(audioPath)
audio.write_audiofile(mp3Path)

# Remover o áudio em webm
os.remove(audioPath)
print('Conversão concluída! O áudio foi salvo como audio.mp3.')
