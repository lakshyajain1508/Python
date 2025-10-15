import time 

def type_lyrics(line, typing_speed=0.065 ):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(typing_speed)
    print()  # Move to the next line after finishing the line

def print_lyrics():
    lyrics = [
    "Haathon ko sambhale mere haathon mein",
    "Kaise haathon ko sambhale mere haathon mein",
    "Jab tak neend na aaye, inn lakeeron mein",
    "Baatein hon..",
    
    "Haann..",
    ]
    
    delays = [2.0, 1.8, 2.1, 2.4, 1.7] # seconds
    print("Arz Kiya hai Lyrics:\n")
    time.sleep(1.5)  # Initial delay before starting
    for i, line in enumerate(lyrics):
        type_lyrics(line)
        time.sleep(delays[i])
        
print_lyrics()
time.sleep(0.02)  # Final delay after finishing
