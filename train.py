import face_recognition
import os
import glob

class Train:
    faces_encodings = []
    faces_names = []
    path = None
    list_of_files = None
    number_files = None
    names = None
    images_format = None

    def __init__(self, images_format='jpg'):
        self.images_format = images_format
        self.path = os.path.join(os.getcwd(), 'images/')
        self.list_of_files = [f for f in glob.glob(self.path + '*.' + self.images_format)]
        self.number_files = len(self.list_of_files)
        self.names = self.list_of_files.copy()

    def train_from_images(self):
        print('Train begin !!')
        for i in range(self.number_files):
            globals()['image_{}'.format(i)] = face_recognition.load_image_file(self.list_of_files[i])
            globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
            self.faces_encodings.append(globals()['image_encoding_{}'.format(i)])
            # Create array of known names
            self.names[i] = self.names[i].replace(self.path, "").replace('.' + self.images_format, "")
            self.faces_names.append(self.names[i])
        print('Train finished !!')
        print(self.names)
        print(self.path)
