import time 

def type_lyrics(line, typing_speed=0.065 ):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(typing_speed)
    print()  # Move to the next line after finishing the line

def print_lyrics():
    """Agar Tum Saath Ho lyrics"""
    
    lyrics = [
    "Teri nazron mein hai tere sapne,",
    "Tere sapno mein hai naraazi.",
    "Mujhe lagta hai ke baatein dil ki,",
    "Hoti lafzon ki dhokebaazi.",
    "Tum saath ho ya na ho kya fark hai,",
    "Bedard thi zindagi bedard hai.",
    "Agar tum saath ho...",
    ]
    delays = [1.2, 1.5, 1.0, 1.8, 1.6, 2.5, 3.0] 
    
    print("\n🎵 Agar Tum Saath Ho Lyrics\n")
    time.sleep(1.0)  # Initial delay before starting
    
    for i, line in enumerate(lyrics):
        type_lyrics(line, typing_speed=0.07) # slightly slower typing for emphasis
        
        # Ensure we don't try to access a delay that doesn't exist
        if i < len(delays):
            time.sleep(delays[i])
        
print_lyrics()
time.sleep(0.02)  # Final small delay