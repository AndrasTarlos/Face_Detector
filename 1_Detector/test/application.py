from flask import Flask, render_template, Response, request
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0)
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_recognition_on = True


def generate_frames():
    while True:
        success_read, frame = camera.read()
        if not success_read:
            break
        else:
            if face_recognition_on:
                grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

                if len(face_coordinates) > 1:
                    face_coordinates = face_coordinates[:len(face_coordinates) - 1]

                # Draw rectangles around the faces
                for (x, y, w, h) in face_coordinates:
                    # (x, y, w, h) = face_coordinates[1]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'


@app.route("/", methods=["GET", "POST"])
def index():
    global face_recognition_on
    if request.method == "POST":
        if request.form.get("on_button") == "ON":
            face_recognition_on = True
        elif request.form.get("off_button") == "OFF":
            face_recognition_on = False

    return render_template("index.html")


@app.route("/video")
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run()
