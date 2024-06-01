import cv2
import database
import face_recognition
import datetime

# Function to recognize faces in a frame
def recognize_faces_in_frame(known_face_encodings, img):
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Find all face locations in the current frame
    face_locations = face_recognition.face_locations(rgb_img)

    # If no faces are detected, return False
    if len(face_locations) == 0:
        return False, None, None

    # Encode all faces found in the current frame
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

    # Initialize variables to store match index and face location
    match_index = None
    face_loc = None

    # Iterate through each face encoding found in the current frame
    for i, face_encoding in enumerate(face_encodings):
        # Compare the current face encoding with all known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # Check if there is a match
        if True in matches:
            match_index = matches.index(True)  # Get the index of the first match
            face_loc = face_locations[i]  # Get the location of the matched face
            break

    # If a match is found, return True, match index, and face location
    if match_index is not None:
        return True, match_index, face_loc
    # If no match is found, return False
    else:
        return False, None, None


# Function to find face encodings
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            encodeList.append(encodings[0])
        else:
            print("No faces found in the image")
    return encodeList


# Database configuration
host = 'localhost'
database_name = 'face_smart'
user = 'root'
password = ''

# Table containing employee images
table_name = 'employee'

# Connect to the database
connection = database.connect_to_database(host, database_name, user, password)

# Fetch images from the database
images, ids = database.fetch_images_from_database(connection, table_name)

# Get face encodings for all known images
encode_list_known = findEncodings(images)

# Print a message indicating encoding is complete
print('Encoding Complete.')

# Initialize variables to track time
start_time = None
end_time = None
total_time = datetime.timedelta(0)

# Open the default camera (index 0) - Change to 0 if you only have one camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Loop to continuously process frames from the camera
while True:
    ret, img = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Recognize faces in the frame
    is_face_detected, match_index, face_loc = recognize_faces_in_frame(encode_list_known, img)

    if is_face_detected:
        if start_time is None:
            # If face is detected for the first time, start the time tracking
            start_time = datetime.datetime.now()

        if match_index is not None:
            # Get the employee ID and name
            person_id, person_name = ids[match_index]
            database.mark_presence(connection, person_id)
            today_date = datetime.datetime.now().strftime("%Y-%m-%d")
            database.calculate_work_time(connection, person_id, today_date)

            # Draw rectangle around the detected face
            y1, x2, y2, x1 = face_loc
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Display employee information
            cv2.putText(img, person_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    else:
        # If face is not detected, stop the time tracking
        if start_time is not None:
            end_time = datetime.datetime.now()

    # Display the resulting image
    cv2.imshow('Smart Face', img)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        # Break the loop when 'q' is pressed
        end_time = datetime.datetime.now()
        break

# Calculate total time in front of the camera
if start_time is not None and end_time is not None:
    total_time += end_time - start_time

# Print the total time spent in front of the camera
print(f'Total Time: {total_time}')

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Close database connection
if connection.is_connected():
    connection.close()
    print("MySQL connection closed")
