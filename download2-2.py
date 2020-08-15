import sys
import io
import urllib.request as dw


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl = "https://cafefiles.pstatic.net/MjAyMDA2MDhfODcg/MDAxNTkxNjA2ODk0ODUx.EKQ_Ywkbdd-iCfU9MOiOMzKZBfcfhQRwMCuD4ujNy4Ug.8-LJoXLNwOYibfcCglXUTW14S3cgZxdNYhD1Em8fU8Ig.JPEG/%EB%9F%B0%EC%B9%AD%EC%9D%BC%EC%9E%90_%EC%B9%B4%ED%8E%98_%EB%B0%B0%EB%84%88.jpg"
htmlURL = "http://google.com"
savePath1 = "g:/python/test1.jpg"
savePath2 = "g:/python/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb')
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
