import pytube
import  os
import  subprocess

yt = pytube.YouTube("https://www.youtube.com/watch?v=766v4ZXWUcU")

videos = yt.streams.all()

for i in range(len(videos)) :
    print(i,' , ',videos[i])

cNum = int(input("다운받을 화질은?(0~21 입력)"))

down_dir = "g:\youtube"

videos[cNum].download(down_dir)

newFilename = input("변환 할 mp3파일명은?")
oriFIlenName = videos[cNum].default_filename

subprocess.call([
'ffmpeg','-i',
    os.path.join(down_dir,oriFIlenName),
    os.path.join(down_dir,newFilename)
])

print("동영상 다운로드 및 mp3 변환 완료!")
