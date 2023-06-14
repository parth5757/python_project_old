# import cv2
# import dlib
# import pyautogui

# # Set the screen size (adjust these values to match your screen resolution)
# SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080

# # Set the eye position thresholds (adjust these values based on your eye tracking system)
# X_THRESHOLD = 50
# Y_THRESHOLD = 50

# # Initialize the face detector and landmark predictor
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("D:/python/project/shape_predictor_68_face_landmarks.dat")

# # Move the mouse cursor based on the eye position
# def move_mouse(x, y):
#     # Calculate the new mouse position based on eye position and screen size
#     new_x = int((x * SCREEN_WIDTH) / X_THRESHOLD)
#     new_y = int((y * SCREEN_HEIGHT) / Y_THRESHOLD)

#     # Move the mouse to the new position
#     pyautogui.moveTo(new_x, new_y)

# # Variable to track program execution
# running = True

# # Function to handle keyboard events
# def key_handler(key):
#     global running
#     if key == ord('p'):
#         running = False

# # Main loop
# while running:
#     # Capture a frame from the camera
#     # Replace this line with the code to capture a frame from your camera
#     _, frame = capture.read()
    
#     # Convert the frame to grayscale for eye detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     # Detect faces in the grayscale frame
#     faces = detector(gray)
    
#     for face in faces:
#         # Predict the facial landmarks for the detected face
#         landmarks = predictor(gray, face)
        
#         # Extract the eye coordinates from the facial landmarks
#         left_eye_x = landmarks.part(36).x
#         left_eye_y = landmarks.part(36).y
#         right_eye_x = landmarks.part(45).x
#         right_eye_y = landmarks.part(45).y
        
#         # Calculate the average eye position
#         eye_x = (left_eye_x + right_eye_x) / 2
#         eye_y = (left_eye_y + right_eye_y) / 2
        
#         # Move the mouse based on the eye position
#         move_mouse(eye_x, eye_y)
    
#     # Check for keyboard events
#     key = cv2.waitKey(1)
#     key_handler(key)

# # Release resources
# capture.release()
# cv2.destroyAllWindows()

# COPY
# import cv2
# import mediapipe as mp
# import pyautogui
# cam = cv2.VideoCapture(0)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen_w, screen_h = pyautogui.size()
# while True:
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     landmark_points = output.multi_face_landmarks
#     frame_h, frame_w, _ = frame.shape
#     if landmark_points:
#         landmarks = landmark_points[0].landmark
#         for id, landmark in enumerate(landmarks[474:478]):
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (0, 255, 0))
#             if id == 1:
#                 screen_x = screen_w * landmark.x
#                 screen_y = screen_h * landmark.y
#                 pyautogui.moveTo(screen_x, screen_y)
#         left = [landmarks[145], landmarks[159]]
#         for landmark in left:
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 3, (0, 255, 255))
#         if (left[0].y - left[1].y) < 0.004:
#             pyautogui.click()
#             pyautogui.sleep(1)
#     cv2.imshow('Eye Controlled Mouse', frame)
#     cv2.waitKey(1)

# ORIGINAL
import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cam.read()
    frame =   cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks =  landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)
            # print(x, y)
    cv2.imshow('Eye  Controlled Mouse', frame)
    cv2.waitKey(1)

