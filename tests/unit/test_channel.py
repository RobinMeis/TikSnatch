import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import datetime
import pytest
from TikSnatch.channel import Channel
from TikSnatch.video import Video
from unittest.mock import patch

mock_info = {'id': 'MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'title': 'muhmemtb', '_type': 'playlist', 'entries': [{'id': '7526904065213730050', 'formats': None, 'subtitles': None, 'http_headers': {'Referer': 'https://www.tiktok.com/@muhmemtb/video/7526904065213730050'}, 'channel': 'MuhmeMTB', 'channel_id': 'MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader': 'muhmemtb', 'uploader_id': '7343331254596650017', 'channel_url': 'https://www.tiktok.com/@MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader_url': 'https://www.tiktok.com/@muhmemtb', 'track': 'Originalton', 'artists': ['MuhmeMTB'], 'duration': 21, 'title': '', 'description': '', 'timestamp': 1752493924, 'view_count': 0, 'like_count': 0, 'repost_count': 0, 'comment_count': 0, 'thumbnails': [{'id': 'cover', 'url': 'https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/o8lL42GSLKRN670uJjQqADaIOeSEIIBeAQdePI~tplv-tiktokx-origin.image?dr=10395&x-expires=1752663600&x-signature=%2FstaGcBMz7IoT6TnJjaAbfpKKNo%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}, {'id': 'dynamicCover', 'url': 'https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/okXLS4QeB7jRINOILdARBIIG0A0I6YaDqYe02e~tplv-tiktokx-origin.image?dr=10395&x-expires=1752663600&x-signature=nMtk7TFSEiYYKBl8Tbg1HYGZQoM%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -2}, {'id': 'originCover', 'url': 'https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/oM2IL6NI2IAdRAkean740eBVqAIeODGxQISjEL~tplv-tiktokx-origin.image?dr=10395&x-expires=1752663600&x-signature=1A120IJramch%2FDpUV65gQ6DQZhI%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}], 'ie_key': 'TikTok', '_type': 'url', 'url': 'https://www.tiktok.com/@muhmemtb/video/7526904065213730050', '__x_forwarded_for_ip': None}, {'id': '7526903061072104726', 'formats': None, 'subtitles': None, 'http_headers': {'Referer': 'https://www.tiktok.com/@muhmemtb/video/7526903061072104726'}, 'channel': 'MuhmeMTB', 'channel_id': 'MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader': 'muhmemtb', 'uploader_id': '7343331254596650017', 'channel_url': 'https://www.tiktok.com/@MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader_url': 'https://www.tiktok.com/@muhmemtb', 'track': 'Originalton', 'artists': ['MuhmeMTB'], 'duration': 2, 'title': 'Muhme mag Dichtmilch', 'description': 'Muhme mag Dichtmilch', 'timestamp': 1752493689, 'view_count': 1, 'like_count': 1, 'repost_count': 0, 'comment_count': 0, 'thumbnails': [{'id': 'cover', 'url': 'https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/o0XaWYTiB0uZLnHcii2vHIIq3z7VkDBBLAE9B~tplv-tiktokx-origin.image?dr=10395&x-expires=1752663600&x-signature=rMdj8gn5FLqPsajFunLVf%2FYJrI4%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}, {'id': 'dynamicCover', 'url': 'https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/osAKGEdmQL6d3XeuADD9DPf6FCyQIQfjPIr4p6~tplv-tiktokx-origin.image?dr=10395&x-expires=1752663600&x-signature=Y2IML29fgb8wjagOV68eMOLxqx4%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -2}, {'id': 'originCover', 'url': 'https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/okc7hWA3lHYyAwA7B3ORGecnpQteG0fgegFF4Y~tplv-tiktokx-origin.image?dr=10395&x-expires=1752663600&x-signature=nhh9LWQ2VrXfuIHYLoyvBA98bz0%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}], 'ie_key': 'TikTok', '_type': 'url', 'url': 'https://www.tiktok.com/@muhmemtb/video/7526903061072104726', '__x_forwarded_for_ip': None}, {'id': '7526902878389210390', 'formats': None, 'subtitles': None, 'http_headers': {'Referer': 'https://www.tiktok.com/@muhmemtb/video/7526902878389210390'}, 'channel': 'MuhmeMTB', 'channel_id': 'MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader': 'muhmemtb', 'uploader_id': '7343331254596650017', 'channel_url': 'https://www.tiktok.com/@MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader_url': 'https://www.tiktok.com/@muhmemtb', 'track': 'motorcycle dududu', 'artists': ['FUNNY '], 'duration': 5, 'title': 'Shredding Muhme', 'description': 'Shredding Muhme', 'timestamp': 1752493648, 'view_count': 42, 'like_count': 1, 'repost_count': 0, 'comment_count': 0, 'thumbnails': [{'id': 'cover', 'url': 'https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/o8QVTQuIeDdSaAjnlagAnLILxuGeU6I6Me8jTI~tplv-tiktokx-origin.image?dr=10395&x-expires=1752663600&x-signature=dng5u6AjZ4w1Wz%2FcGcxi%2FT3fFTw%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}, {'id': 'dynamicCover', 'url': 'https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/ok0rlSGCIITAlyEf5hICJ2B0klPiiCYnAwPc7O~tplv-tiktokx-origin.image?dr=10395&x-expires=1752663600&x-signature=xAooWsy9pp1dRnKcXF5eYO3gc8s%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -2}, {'id': 'originCover', 'url': 'https://p16-pu-sign-no.tiktokcdn-eu.com/tos-no1a-p-0037-no/osTrH8BYIiAcIjAOPBiyQ7C1C5nRfI200JlNwl~tplv-tiktokx-origin.image?dr=10395&x-expires=1752663600&x-signature=s2dVY6wrvLxXkvZteUIK299mMYI%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}], 'ie_key': 'TikTok', '_type': 'url', 'url': 'https://www.tiktok.com/@muhmemtb/video/7526902878389210390', '__x_forwarded_for_ip': None}], 'webpage_url': 'https://www.tiktok.com/@muhmemtb', 'original_url': 'https://www.tiktok.com/@muhmemtb', 'webpage_url_basename': '@muhmemtb', 'webpage_url_domain': 'tiktok.com', 'extractor': 'tiktok:user', 'extractor_key': 'TikTokUser', 'release_year': None, 'playlist_count': 3, 'epoch': 1752493984}
test_videos = {
    0: {
        "url": "https://www.tiktok.com/@muhmemtb/video/7526904065213730050",
        "timestamp": datetime.datetime(2025, 7, 14, 13, 52, 4),
        "title": "",
        "description": ""
    },
    1: {
        "url": "https://www.tiktok.com/@muhmemtb/video/7526903061072104726",
        "timestamp": datetime.datetime(2025, 7, 14, 13, 48, 9),
        "title": "Muhme mag Dichtmilch",
        "description": "Muhme mag Dichtmilch"
    },
    2: {
        "url": "https://www.tiktok.com/@muhmemtb/video/7526902878389210390",
        "timestamp": datetime.datetime(2025, 7, 14, 13, 47, 28),
        "title": "Shredding Muhme",
        "description": "Shredding Muhme"
    }
}

def test_channel_parsing():
    channel = Channel("muhmemtb")
    channel._parse_info(mock_info)

    assert channel.username == "muhmemtb"
    assert channel.name == "MuhmeMTB"
    assert channel.channel_id == "7343331254596650017"
    assert len(channel.videos) == 3

    for index, test_video in test_videos.items():
        video = channel.videos[index]
        assert isinstance(video, Video)
        assert video.url == test_video["url"]
        assert video.timestamp == test_video["timestamp"]
        assert video.title == test_video["title"]
        assert video.description == test_video["description"]

def test_online_channel():
    channel = Channel("muhmemtb")
    channel.get()

    assert channel.username == "muhmemtb"
    assert channel.name == "MuhmeMTB"
    assert channel.channel_id == "7343331254596650017"
    assert len(channel.videos) == 3

    for index, test_video in test_videos.items():
        video = channel.videos[index]
        assert isinstance(video, Video)
        assert video.url == test_video["url"]
        #assert video.timestamp == test_video["timestamp"]
        assert video.title == test_video["title"]
        assert video.description == test_video["description"]