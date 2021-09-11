try:
    import os
    from pytube import YouTube
    import requests
    import random

    os.system("clear")

    num = random.randint(1,100)
    url = input("Enter the video url correctly :\n")
    my_video = YouTube(url)

    print("\n************ Video Title **************\n\n")
    print(my_video.title)

    print("\n\nWe got it your work will be done , just relaxx ")
    a = requests.get(my_video.thumbnail_url)

    with open(f"imagexv12zO{num}xx.png","wb")as f:
        f.write(a.content)


    print('\n\n\nDONE 111')

except Exception as e:
    print(e)
