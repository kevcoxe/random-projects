
import steganopy.api

from generate import get_face

input_image = 'my_face.png'
output_image = 'out.png'
file_to_hide = 'message.json'

get_face(input_image, thumbnail=False)

steganopy.api.create_stegano_image(
    original_image=input_image,
    data_to_hide=file_to_hide
).save(input_image)
