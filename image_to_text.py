from PIL import Image
import pytesseract as tess

tess.pytesseract.tesseract_cmd=r'C:\Users\vetri\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import cv2

def capture():
    cam = cv2.VideoCapture(0)


    img_counter = 0

    while True:
        res, img = cam.read()
        capturing_box=cv2.imshow("image_to_scan", img)

        if cv2.waitKey(1)==27:
            break
        elif cv2.waitKey(1) == 32:
            img_name = "opencv_frame_{}.png".format(img_counter)
            captured_image=cv2.imwrite(img_name,img)
            print("{} written!".format(img_name))
            img_counter += 1
        
    cam.release()

    cv2.destroyAllWindows()

    
    
    img1=cv2.imread("opencv_frame_0.png")
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    # Perform text extraction
    text = tess.image_to_string(invert, lang='eng', config='--psm 6')
   
    #text=tess.image_to_string(img1)

    return text