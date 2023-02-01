# Seattle University ECE Team 23.2
# Boeing Automated Inspection Robot Project
# February 1, 2023

# https://towardsdatascience.com/read-and-edit-image-metadata-with-python-f635398cd991
from exif import Image

# Assumes images are in imagesFolder
folder_path = 'imagesFolder'
img_filename = 'MetaTest-0.JPEG'
img_path = f'{folder_path}/{img_filename}'

# Open image
with open(img_path, 'rb') as img_file:
    img = Image(img_file)

# Print if Image has exif (metadata) data
print(img.has_exif)

# List of image attributes
# https://exif.readthedocs.io/en/latest/api_reference.html#image-attributes list of image attributes

# Attribute Formats
# https://exiv2.org/tags.html tag formats

# Print all exif data tiles
for item in sorted(img.list_all()):
    print(item)

# Add new attribute (Copyright)
img.copyright = 'ECE 23.2: 2022'

# Check updated metadata
print(f'Copyright: {img.get("copyright")}')


# Overwirte old version with new version
# Change change path as needed
with open(f'{folder_path}/{img_filename}', 'wb') as new_image_file:
    new_image_file.write(img.get_file())

print("Done")

#####
