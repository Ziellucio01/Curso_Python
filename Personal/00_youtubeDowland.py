import pytube

url = input("Ingresa la url del video: ")

path = "C:"

pytube.YouTube(url).streams.get_highest_resolution().download(path)
