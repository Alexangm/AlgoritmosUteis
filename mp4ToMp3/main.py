from moviepy.editor import *

pathMp4 = "C:\\Users\\Alexsander\\Downloads\\mp4\\"  # caminho da pasta onde está o arquivo mp4
pathMp3 = "C:\\Users\\Alexsander\\Downloads\\mp3\\"  # caminho da pasta onde ficará o mp3

filesToConvert = [""]  # lista do nome dos arquivos que serão convertidos (em string)

for file in range(len(filesToConvert)):
    title = filesToConvert[file]

    mp4File = pathMp4 + title + ".mp4"
    mp3File = pathMp3 + title + ".mp3"

    videoClip = VideoFileClip(mp4File)
    audioClip = videoClip.audio
    audioClip.write_audiofile(mp3File)

    audioClip.close()
    videoClip.close()
    print(f"{mp3File} finalizado")
