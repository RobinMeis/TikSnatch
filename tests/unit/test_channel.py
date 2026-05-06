import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import datetime
import pytest
from TikSnatch.channel import Channel
from TikSnatch.video import Video
from unittest.mock import patch

mock_info = {'id': 'MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'title': 'muhmemtb', '_type': 'playlist', 'entries': [{'id': '7601165853668822304', 'formats': None, 'subtitles': None, 'http_headers': {'Referer': 'https://www.tiktok.com/@muhmemtb/video/7601165853668822304'}, 'channel': 'MuhmeMTB', 'channel_id': 'MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader': 'muhmemtb', 'uploader_id': '7343331254596650017', 'channel_url': 'https://www.tiktok.com/@MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader_url': 'https://www.tiktok.com/@muhmemtb', 'track': 'Originalton', 'artists': ['MuhmeMTB'], 'duration': 6, 'title': '', 'description': '', 'timestamp': 1769784350, 'view_count': 399, 'like_count': 11, 'repost_count': 5, 'comment_count': 0, 'save_count': 0, 'thumbnails': [{'id': 'cover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/oI8MO0iCKgSz4EBAiZrXaxaCiBRBpIAvCIEDq~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=vW75%2BIMe3ZLnKTfuuynA1nQmumU%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}, {'id': 'dynamicCover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/osvCjIBvC4CUsDzB50gIxiZqAA8pDaiEMEXAi~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=LMLOBQgyb6VengzDz49XYpDuke0%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -2}, {'id': 'originCover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/oM8DFDAVMIxaSFQ8QCeBEfYKMxfkSQAEnGHjgZ~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=A%2BXg%2BwQpKcoU1GOLwX9FV4Cn31c%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}], 'ie_key': 'TikTok', '_type': 'url', 'url': 'https://www.tiktok.com/@muhmemtb/video/7601165853668822304', '__x_forwarded_for_ip': None}, {'id': '7601165704926170400', 'formats': None, 'subtitles': None, 'http_headers': {'Referer': 'https://www.tiktok.com/@muhmemtb/video/7601165704926170400'}, 'channel': 'MuhmeMTB', 'channel_id': 'MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader': 'muhmemtb', 'uploader_id': '7343331254596650017', 'channel_url': 'https://www.tiktok.com/@MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader_url': 'https://www.tiktok.com/@muhmemtb', 'track': 'Originalton', 'artists': ['MuhmeMTB'], 'duration': 6, 'title': '', 'description': '', 'timestamp': 1769784313, 'view_count': 931, 'like_count': 12, 'repost_count': 3, 'comment_count': 0, 'save_count': 0, 'thumbnails': [{'id': 'cover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/oofjQIPEE7qSLS35pGDqQLlhgCFfGSAMfYDMjE~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=bYyEV4jdKF2BCrlYcNgdK1xasUs%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}, {'id': 'dynamicCover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/oUelIxGDRkG8K51IuhLfVgffNIPvgAG2wSIYJA~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=oeyc%2BkB3lzT9Qw0iEbS4CkXw1DY%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -2}, {'id': 'originCover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-useast2a-p-0037-euttp/ocrgYghmAAfENJ2SGLevwlGGrf8yIIRxfaKVF5~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=K%2FA3E9XyYyirLB%2BomFlVQFy0Yso%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}], 'ie_key': 'TikTok', '_type': 'url', 'url': 'https://www.tiktok.com/@muhmemtb/video/7601165704926170400', '__x_forwarded_for_ip': None}, {'id': '7526904065213730050', 'formats': None, 'subtitles': None, 'http_headers': {'Referer': 'https://www.tiktok.com/@muhmemtb/video/7526904065213730050'}, 'channel': 'MuhmeMTB', 'channel_id': 'MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader': 'muhmemtb', 'uploader_id': '7343331254596650017', 'channel_url': 'https://www.tiktok.com/@MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader_url': 'https://www.tiktok.com/@muhmemtb', 'track': 'Originalton', 'artists': ['MuhmeMTB'], 'duration': 21, 'title': '', 'description': '', 'timestamp': 1752493924, 'view_count': 1082, 'like_count': 39, 'repost_count': 1, 'comment_count': 0, 'save_count': 3, 'thumbnails': [{'id': 'cover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-no1a-p-0037-no/o8lL42GSLKRN670uJjQqADaIOeSEIIBeAQdePI~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=dYgVevik2zBAhSBP3HpbpR81TGI%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}, {'id': 'dynamicCover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-no1a-p-0037-no/okXLS4QeB7jRINOILdARBIIG0A0I6YaDqYe02e~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=5RMRu5%2FwUMA5yfEOvJ2Mc6PLcIE%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -2}, {'id': 'originCover', 'url': 'https://p19-common-sign.tiktokcdn-eu.com/tos-no1a-p-0037-no/oM2IL6NI2IAdRAkean740eBVqAIeODGxQISjEL~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=ZwGRmoXol%2FuYGDjUMRwwO6Ii2eY%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}], 'ie_key': 'TikTok', '_type': 'url', 'url': 'https://www.tiktok.com/@muhmemtb/video/7526904065213730050', '__x_forwarded_for_ip': None}, {'id': '7526903061072104726', 'formats': None, 'subtitles': None, 'http_headers': {'Referer': 'https://www.tiktok.com/@muhmemtb/video/7526903061072104726'}, 'channel': 'MuhmeMTB', 'channel_id': 'MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader': 'muhmemtb', 'uploader_id': '7343331254596650017', 'channel_url': 'https://www.tiktok.com/@MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader_url': 'https://www.tiktok.com/@muhmemtb', 'track': 'Originalton', 'artists': ['MuhmeMTB'], 'duration': 2, 'title': 'Muhme mag Dichtmilch', 'description': 'Muhme mag Dichtmilch', 'timestamp': 1752493689, 'view_count': 131, 'like_count': 11, 'repost_count': 0, 'comment_count': 0, 'save_count': 1, 'thumbnails': [{'id': 'cover', 'url': 'https://p19-common-sign.tiktokcdn-eu.com/tos-no1a-p-0037-no/o0XaWYTiB0uZLnHcii2vHIIq3z7VkDBBLAE9B~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=XHRszoe6%2FycqjlPE3uJAcPMAOoU%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}, {'id': 'dynamicCover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-no1a-p-0037-no/osAKGEdmQL6d3XeuADD9DPf6FCyQIQfjPIr4p6~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=YMnENIc%2FUL76ycEovJNQKO6EWCE%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -2}, {'id': 'originCover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-no1a-p-0037-no/okc7hWA3lHYyAwA7B3ORGecnpQteG0fgegFF4Y~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=CM97bMRJ%2FFi9M7Iz5ChCtEpjh5c%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}], 'ie_key': 'TikTok', '_type': 'url', 'url': 'https://www.tiktok.com/@muhmemtb/video/7526903061072104726', '__x_forwarded_for_ip': None}, {'id': '7526902878389210390', 'formats': None, 'subtitles': None, 'http_headers': {'Referer': 'https://www.tiktok.com/@muhmemtb/video/7526902878389210390'}, 'channel': 'MuhmeMTB', 'channel_id': 'MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader': 'muhmemtb', 'uploader_id': '7343331254596650017', 'channel_url': 'https://www.tiktok.com/@MS4wLjABAAAANz15gBVOXYHqE3I5e19cZ4GLTBsKAIGQUPqcaN3m7ZuIYrHZVa0N73H_IfrHxm1t', 'uploader_url': 'https://www.tiktok.com/@muhmemtb', 'track': 'motorcycle dududu', 'artists': ['FUNNY '], 'duration': 5, 'title': 'Shredding Muhme', 'description': 'Shredding Muhme', 'timestamp': 1752493648, 'view_count': 433, 'like_count': 27, 'repost_count': 2, 'comment_count': 5, 'save_count': 2, 'thumbnails': [{'id': 'cover', 'url': 'https://p19-common-sign.tiktokcdn-eu.com/tos-no1a-p-0037-no/o8QVTQuIeDdSaAjnlagAnLILxuGeU6I6Me8jTI~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=xd3jzuuH3ceminCHQR6B0SkznRI%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}, {'id': 'dynamicCover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-no1a-p-0037-no/ok0rlSGCIITAlyEf5hICJ2B0klPiiCYnAwPc7O~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=WmYf%2FPz%2FdJ2p88rZI08z9Nsxr64%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -2}, {'id': 'originCover', 'url': 'https://p16-common-sign.tiktokcdn-eu.com/tos-no1a-p-0037-no/osTrH8BYIiAcIjAOPBiyQ7C1C5nRfI200JlNwl~tplv-tiktokx-origin.image?dr=10395&x-expires=1778245200&x-signature=4HhPcmwjkoEwaWwYA878UDxsKNY%3D&t=4d5b0474&ps=13740610&shp=81f88b70&shcp=43f4a2f9&idc=no1a', 'preference': -1}], 'ie_key': 'TikTok', '_type': 'url', 'url': 'https://www.tiktok.com/@muhmemtb/video/7526902878389210390', '__x_forwarded_for_ip': None}], 'webpage_url': 'https://www.tiktok.com/@muhmemtb', 'original_url': 'https://www.tiktok.com/@muhmemtb', 'webpage_url_basename': '@muhmemtb', 'webpage_url_domain': 'tiktok.com', 'extractor': 'tiktok:user', 'extractor_key': 'TikTokUser', 'release_year': None, 'playlist_count': 5, 'epoch': 1778075845}
test_videos = {
    0: {
        "url": "https://www.tiktok.com/@muhmemtb/video/7601165853668822304",
        "timestamp": 1769784350.0,
        "title": "",
        "description": ""
    },
    1: {
        "url": "https://www.tiktok.com/@muhmemtb/video/7601165704926170400",
        "timestamp": 1769784313.0,
        "title": "",
        "description": ""
    },
    2: {
        "url": "https://www.tiktok.com/@muhmemtb/video/7526904065213730050",
        "timestamp": 1752493924.0,
        "title": "",
        "description": ""
    },
    3: {
        "url": "https://www.tiktok.com/@muhmemtb/video/7526903061072104726",
        "timestamp": 1752493689.0,
        "title": "Muhme mag Dichtmilch",
        "description": "Muhme mag Dichtmilch"
    },
    4: {
        "url": "https://www.tiktok.com/@muhmemtb/video/7526902878389210390",
        "timestamp": 1752493648.0,
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
    assert len(channel.videos) == 5

    for index, test_video in test_videos.items():
        video = channel.videos[index]
        assert isinstance(video, Video)
        assert video.url == test_video["url"]
        assert video.timestamp.timestamp() == test_video["timestamp"]
        assert video.title == test_video["title"]
        assert video.description == test_video["description"]

def test_online_channel():
    channel = Channel("muhmemtb")
    channel.get()

    assert channel.username == "muhmemtb"
    assert channel.name == "MuhmeMTB"
    assert channel.channel_id == "7343331254596650017"
    assert len(channel.videos) == 5

    for index, test_video in test_videos.items():
        video = channel.videos[index]
        assert isinstance(video, Video)
        assert video.url == test_video["url"]
        assert video.timestamp.timestamp() == test_video["timestamp"]
        assert video.title == test_video["title"]
        assert video.description == test_video["description"]
