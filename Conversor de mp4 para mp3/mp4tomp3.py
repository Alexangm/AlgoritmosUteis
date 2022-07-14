from moviepy.editor import *

pathmp4 = "C:\\Users\\Alexsander\\Downloads\\mp4\\"  # caminho da pasta onde está o arquivo mp4
pathmp3 = "C:\\Users\\Alexsander\\Downloads\\mp3\\"  # caminho da pasta onde ficará o mp3

lista = [""]  # lista do nome dos arquivos que serão convertidos (em string)

for i in range(len(lista)):
    titulo = lista[i]

    mp4_file = pathmp4 + titulo + ".mp4"
    mp3_file = pathmp3 + titulo + ".mp3"

    videoClip = VideoFileClip(mp4_file)
    audioClip = videoClip.audio
    audioClip.write_audiofile(mp3_file)

    audioClip.close()
    videoClip.close()
    print(f"{mp3_file} finalizado")
