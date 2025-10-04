Music_name: str = "Yellow"
name_artist: str = "Coldplay"
likes: float = 78.9
comments: int = 780
views_count: float = 4.5
date: str = "2016/03/29"
music_length_minutes: int = 4
music_length_second: int = 26

print(f"The name of the music is {Music_name} and the artist is {name_artist}")
print(f"The number of likes for this music is {int(likes)}K")
print(f"The number of comments for this music on SoundCloud is {comments}")
print(f"The number of viewer is {views_count}M")
print(f"Release date of the music on SoundCloud: {date}")
print(f"Music time: {music_length_minutes}:{music_length_second}")
