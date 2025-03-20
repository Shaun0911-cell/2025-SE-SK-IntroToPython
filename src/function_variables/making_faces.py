def making_faces(faces):
    if faces == "Hello :)":
        faces = faces.replace(":)", "😊")
        print = "Hello 😊"
    else:
        print(faces)


faces = input()
making_faces(faces)
