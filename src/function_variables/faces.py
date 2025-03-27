def making_faces(faces):
    new_faces = ""
    if "Hello :)" in faces:
        faces = faces.replace(":)", "😊")

    if "Goodbye :(" in faces:
        faces = faces.replace(":(", "😒")

    print(faces)


faces = input()
making_faces(faces)
