'''
import cv2

# Gets all the trained values
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Saves an image in a var
# img = cv2.imread('ghwalin.jpeg')
webcam = cv2.VideoCapture(0)


while True:
    successful_frame_read, frame = webcam.read()
    # Convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect face
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    if len(face_coordinates) > 1:
        face_coordinates = face_coordinates[:len(face_coordinates) - 1]

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        # (x, y, w, h) = face_coordinates[1]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face detector", frame)
    # Waits until you close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()

print("Code completed")

'''
'''
# TODO Change size of image
import cv2
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("ghwalin.jpeg")                    # Read image             # Resize image
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
for (x, y, w, h) in face_coordinates:
    # (x, y, w, h) = face_coordinates[1]
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("output", img)                       # Show image
cv2.waitKey(0)

'''