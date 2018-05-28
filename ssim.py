#coding=utf-8
#SSIM python代码，大家可以用来验证artifacts是否消除
#结果越小，失真越严重，伪影越重
# import the necessary packages
from skimage.measure import compare_ssim
import cv2
  
# construct the argument parse and parse the arguments
img_source="source.jpg"
img_to_be_compare="gaijinhou.jpg"
 
# load the two input images
imageA = cv2.imread(img_source)
imageB = cv2.imread(img_to_be_compare)
  
# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
 
# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))
