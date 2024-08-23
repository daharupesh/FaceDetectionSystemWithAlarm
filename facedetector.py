import cv2
import pygame
import time

# Initialize Pygame
pygame.init()

# Load the sound
alarm_sound = pygame.mixer.Sound('alarm.wav')  # Make sure 'alarm.wav' is in your working directory

# Load the face cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Start video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 6)

    if len(faces) > 0:
        # Play alarm sound
        alarm_sound.play()
        # Draw rectangle around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # Display message
        cv2.putText(frame, 'Face Detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        # Display message
        cv2.putText(frame, 'No Face Detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
video_capture.release()
cv2.destroyAllWindows()
pygame.quit()
