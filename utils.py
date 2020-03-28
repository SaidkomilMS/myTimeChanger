from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
from pytz import timezone


def get_current_time():
    return datetime.now(timezone('Asia/Tashkent')).strftime('%H:%M')


def generate_image(text):
    image = Image.new('RGB', (500, 500), color='black')
    W, H = image.size
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype( font = "resources/ds-digit.ttf", size = 212)
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2 ), text, font=font, fill='#247ac6')
    font = ImageFont.truetype( font = "resources/ubuntu.ttf", size = 60 )
    text = "Toshkent vaqti:"
    wt1, ht1 = draw.textsize( text, font = font )
    draw.text( ( ( W - wt1 ) / 2, int(0.5*ht1)), text, font = font, fill = '#247ac6' )
    text = "(GMT +5)"
    font = ImageFont.truetype( font = "resources/ubuntu.ttf", size = 50 )
    wt1, ht1 = draw.textsize( text, font = font )
    draw.text( ( ( W - wt1 ) / 2, H-int(1.5*ht1)), text, font = font, fill = '#247ac6' )

    image.save('time_image.jpg')

generate_image(get_current_time())