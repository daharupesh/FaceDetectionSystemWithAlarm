
# Face Detection with Alarm

This project uses OpenCV for real-time face detection and Pygame for playing an alarm sound when a face is detected. The application captures video from a webcam, detects faces in the frames, and provides audio feedback when faces are detected.

## Requirements

- Python 3.x
- OpenCV
- Pygame

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/daharupesh/FaceDetectionSystemWithAlarm.git
   cd your-repository-name
   ```

2. **Install Dependencies**

   You can install the required Python libraries using pip:

   ```bash
   pip install opencv-python pygame
   ```

3. **Download Haar Cascade File**

   Download the Haar cascade file for face detection from [OpenCV's GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the project directory. The file should be named `haarcascade_frontalface_default.xml`.

4. **Add an Alarm Sound**

   Ensure you have an alarm sound file named `alarm.wav` in the project directory. You can replace `alarm.wav` with any other sound file you prefer, but make sure to update the filename in the code accordingly.

## Usage

1. **Run the Script**

   Execute the Python script to start the face detection application:

   ```bash
   python face_detection_alarm.py
   ```

2. **Interact with the Application**

   - The application will open a window showing the video feed from your webcam.
   - If a face is detected, an alarm sound will play, and a message "Face Detected" will be displayed on the screen.
   - If no face is detected, the message "No Face Detected" will be displayed.
   - Press the `q` key to exit the application.

## Output

Here is a screenshot showing the output of the application:

![Output Screenshot](Screenshot/Screenshot%20(312).png)
![Output Screenshot](Screenshot/Screenshot%20(313).png)
![Output Screenshot](Screenshot/Screenshot%20(314).png)

*The screenshot shows the application running with face detection and the corresponding messages displayed.*

## Code Overview

- **Import Libraries**: Imports OpenCV for face detection and Pygame for sound.
- **Initialize Pygame**: Sets up Pygame and loads the alarm sound.
- **Face Detection**: Uses OpenCV's Haar cascade classifier to detect faces in video frames.
- **Sound Alarm**: Plays an alarm sound when a face is detected.
- **Display Messages**: Shows messages on the screen based on face detection status.
- **Exit Mechanism**: Allows quitting the application by pressing the `q` key.



## Acknowledgements

- OpenCV for providing the Haar cascade classifier.
- Pygame for sound playback functionality.
```
