import steganopy.api

output_image = 'my_face.png'

hidden_data = steganopy.api.extract_data_from_stegano_image(
    image=output_image
)

print hidden_data
