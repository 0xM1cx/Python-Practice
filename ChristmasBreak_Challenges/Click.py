# import vlc
# import pafy

# def main():
#     url = "https://fb.watch/i3M6FHc9fd/"

#     # creating pafy object of the video
#     video = pafy.new(url)
    
#     # getting best stream
#     best = video.getbest()
    
#     # creating vlc media player object
#     media = vlc.MediaPlayer(best.url)
    
#     # start playing video
#     media.play()


    

# main()

# importing vlc module
import vlc

# importing pafy module
import pafy

# url of the video
url = "https://www.youtube.com/watch?v=il_t1WVLNxk&list=PLqM7alHXFySGqCvcwfqqMrteqWukz9ZoE"

# creating pafy object of the video
video = pafy.new(url)

# getting stream at index 0
best = video.streams[0]

# creating vlc media player object
media = vlc.MediaPlayer(best.url)

# start playing video
media.play()
