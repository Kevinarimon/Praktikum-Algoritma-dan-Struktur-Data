songs = [
    {"title": "Golden Hour", "artist": "JVKE", "genre": "Pop", "views": 980000},
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop", "views": 2500000},
    {"title": "Snooze", "artist": "SZA", "genre": "R&B", "views": 1200000},
    {"title": "N95", "artist": "Kendrick Lamar", "genre": "Hip-Hop", "views": 850000},
    {"title": "As It Was", "artist": "Harry Styles", "genre": "Pop", "views": 2100000},
    {"title": "Kill Bill", "artist": "SZA", "genre": "R&B", "views": 1750000}
]

def sort_by_views(songs):
    res = songs.copy()
    n = len(songs)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if songs[j]["views"] < songs[j + 1]["views"]:
                songs[j], songs[j + 1] = songs[j + 1], songs[j]
    return songs   

# hasil_bubble = sort_by_views(songs.copy())
# for item in hasil_bubble:
#     print(f'{item["title"]} - {item["views"]} views') 

def sort_by_favourite_genre(songs, favourite_genre):
    res = songs.copy()
    favourite = []
    other = []
    for song in songs:
        if song["genre"] == favourite_genre:
            favourite.append(song)
        else:
            other.append(song)
    return favourite + other

print("=== SORT BY VIEWS ===")

result_views = sort_by_views(songs)

for song in result_views:
    print(song["title"], "-", song["views"], "views")


print("\n=== SORT BY FAVOURITE GENRE ===")

favourite_genre = "R&B"

result_genre = sort_by_favourite_genre(songs, favourite_genre)

for song in result_genre:
    print(song["title"], "-", song["genre"])