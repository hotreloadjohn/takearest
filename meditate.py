import tkinter as tk
from PIL import Image,ImageTk, ImageDraw, ImageFont
from random import randint
import requests
from io import BytesIO
import textwrap
import schedule
import time

root=tk.Tk()

def close_program():
    root.destroy()

def disable_event():
    pass

def createWindow():
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    # root.attributes('-alpha', 0.8)
    root.overrideredirect(True)

def getRndQuote():
    API_URL = "https://api.quotable.io/random"
    res = requests.get(API_URL).json()
    quote = res["content"]
    wrapper = textwrap.TextWrapper(width=40)
    quote_wrap = wrapper.fill(text=quote)
    return quote_wrap


def getRndImage():
    ACCESS_KEY = <your API key>
    API_URL = "https://api.unsplash.com/photos/random/?client_id="+ACCESS_KEY
    params = {
        "query": "nature",
        "orientation": "landscape",
        "count": "1"
    }
    res = requests.get(API_URL, params=params).json()
    img_url = res[0]['urls']['full']
    print(res[0]['urls']['full'])
    response_img = requests.get(img_url)
    img_data = response_img.content
    image = Image.open(BytesIO(img_data))
    w, h = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('FreeSansBold.ttf', size=30)
    (x, y) = ((w/2) - 50, h/2)
    message = getRndQuote()
    color = 'rgb(0, 0, 0)' # black color
    draw.text((x, y), message, fill=color, font=font)
    image.save('greeting_card.png')

    # return img_data


def displayImageToWindow():
    # Get random Image from Unspash
    # photo = ImageTk.PhotoImage(Image.open(BytesIO(getRndImage())))
    getRndImage()
    image = Image.open("greeting_card.png")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.image = photo
    label.pack()

    btn = tk.Button(root, text = "Click me to close", command = close_program)
    btn.pack()

def getRndDuration():
    # Duration at least 5 seconds
    durationToDisplay = randint(10, 30) * 1000
    return durationToDisplay

def main():
    # Create a modal tk window
    createWindow()
    # Display an  image
    displayImageToWindow()
    # Close window after rand duration
    root.after(getRndDuration(), root.destroy)
    
    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.mainloop()


if __name__ == '__main__':
    while(True):
        schedule.every(2).minutes.do(main)
        time.sleep(1)
    # main()
