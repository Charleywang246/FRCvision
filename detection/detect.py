import cv2

def start (camport : int, xmlpath :str):
    run(camport, xmlpath)

def run (camport, xmlpath):
    cap = cv2.VideoCapture(camport)
    casade = cv2.CascadeClassifier(f'train\\model\\{xmlpath}')

    while True:
        ret, frame = cap.read()
        if ret:
            img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            found = casade.detectMultiScale(img_gray, minSize=(40, 40))
            if len(found):
                for (x, y, width, height) in found:
                    cv2.rectangle(frame, (x, y), (x + height, y + width), (0, 0, 255), 5)
            cv2.imshow('result', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()