from TikSnatch.channel import Channel

"""
This example shows how to initialize TikSnatch to download the latest video 
from a channel and display its internal metadata.
"""

# Create channel object
channel = Channel("muhmemtb")

# Download & parse channel details
channel.get()

# Display available internal channel data
print("=== Channel Info ===")
print(f"Display Name: {channel.name}")
print(f"Username:     @{channel.username}")
print(f"Channel ID:   {channel.channel_id}")
print(f"Total Videos: {len(channel.videos)}")
print("====================\n")

if not channel.videos:
    print(f"⚠️ No videos found for @{channel.username}. Exiting.")
else:
    # Select the latest video
    video = channel.videos[0]

    # Display video data before downloading
    print("=== Latest Video ===")
    print(f"Video ID:    {video.id}")
    print(f"Timestamp:   {video.timestamp}")
    print(f"Description: {video.description}")
    print("====================\n")

    # Download the video
    print(f"Downloading latest video from @{channel.username}...")
    video.download("downloads/")
    
    print("\nDownload complete!")