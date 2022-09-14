"""In a string we describe a road. There are cars that move to the right
and we denote them with ">" and cars that move to the left and we denote them with "<".
There are also cameras that are indicated by: " . ".
A camera takes a photo of a car if it moves to the direction of the camera."""

def count_photos(road):
    cameras = road.count(".")
    passed_cameras = 0
    photos = 0
    for item in road:
        if item == ".":
            cameras -= 1
            passed_cameras += 1
        if item == ">":
            photos += cameras
        if item == "<":
            photos += passed_cameras
    return photos


print(count_photos(">.>.")) #3
print(count_photos(".>>")) #0
print(count_photos(">.<.")) #3
print(count_photos(".><.>>.<<")) #11
