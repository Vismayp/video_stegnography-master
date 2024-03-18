import re
import os

from PIL import Image

# Global Variable
global frame_location

# Decode the data in the image
def decode(frame_number, frame_location):
    """Decode the data in the image."""
    data = ''
    numbering = str(frame_number)
    decoder_numbering = os.path.join(frame_location, f"{numbering}.png")
    image = Image.open(decoder_numbering, 'r')
    imagedata = iter(image.getdata())
    while True:
        pixels = [value for value in imagedata.__next__()[:3] + imagedata.__next__()[:3] + imagedata.__next__()[:3]]
        # string of binary data
        binstr = ''
        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'
        if re.match("[ -~]", chr(int(binstr, 2))) is not None:  # only decode printable data
            data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return data

