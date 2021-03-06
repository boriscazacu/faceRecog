import face_recognition
import cv2
import numpy as np

from train import Train


class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    video_capture = None
    current_name = ''
    # From Train
    faces_encodings = []
    faces_names = []

    # Lista persoanelor pentru care se va deschide usa
    authorization_names = ['Elon Musk', 'Eduard Ignatiuc']

    def __init__(self, faces_encodings, faces_names):
        self.faces_encodings = faces_encodings
        self.faces_names = faces_names
        self.video_capture = cv2.VideoCapture(0)

    def run(self):
        while True:
            ret, frame = self.video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            if self.process_this_frame:
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
                self.face_names = []

                for face_encoding in self.face_encodings:
                    matches = face_recognition.compare_faces(self.faces_encodings, face_encoding)
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(self.faces_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        name = self.faces_names[best_match_index]

                    self.face_names.append(name)

            self.authorization(self.face_names)
            self.process_this_frame = not self.process_this_frame

                # Display the results
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a rectangle around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Input text label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.video_capture.release()
                cv2.destroyAllWindows()
                break

    def authorization(self, names):
        for name in names:
            if name != self.current_name:
                if name in self.authorization_names:
                    print('\nHello boss, You authorized with ' + name)
                    print(' >>> Door is open <<< \n')
                elif name == 'Unknown':
                    print('Unknown person !!')
                else:
                    print('Access denied for ' + name)
                self.current_name = name


# Pentru a opri apas?? ???? q

if __name__ == '__main__':
    # Se seteaz?? formatul imaginilor, tote imaginile trebuie s?? aib?? acela??i format
    train = Train('jpeg')
    fr = FaceRecognition(train.faces_encodings, train.faces_names)
    train.train_from_images()
    fr.run()