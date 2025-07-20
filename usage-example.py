from TikSnatch.channel import Channel

"""
This example shows how to initialize TikSnatch to download the latest video from a channel
"""

# Create channel object
channel = Channel("muhmemtb")

# Download & parse channel details
channel.get()

# Select the latest video
video = channel.videos[0]

# Download the video
video.download("downloads/")

# Print video details
print(video)