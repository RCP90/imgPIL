import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = input("請輸入檔名：")
m1=cv2.imread(img ,1)
m1=Image.fromarray(m1)
p1=input("請輸入浮水印：")
t1=input("請輸入大小：")
ImageDraw.Draw(m1).text((0,0), f"{p1}",(0,0,255), ImageFont.truetype("PingFang.ttc",int(t1)))

m1=np.array(m1)

cv2.imshow("m1",m1)
cv2.waitKey(0)
cv2.destroyAllWindows()