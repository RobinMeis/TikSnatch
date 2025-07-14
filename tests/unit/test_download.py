import sys
import os
import shutil
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pytest
from TikSnatch.video import Video

if os.path.isdir('test-downloads/'):
    shutil.rmtree("test-downloads/")
os.makedirs("test-downloads/")

@pytest.mark.parametrize("id, url, timestamp, title, description, sha256_hash", [
    (7526904065213730050, "https://www.tiktok.com/@muhmemtb/video/7526904065213730050", 1752493924.0, "", "", "df881c105dd4aff3afaf34342b8b99e016ccacdecb2034d07589b1421a9e0749"),
    (7526903061072104726, "https://www.tiktok.com/@muhmemtb/video/7526903061072104726", 1752493689.0, "Muhme mag Dichtmilch", "Muhme mag Dichtmilch", "a4a0ca8f2aa51feca340a1ba27de80e59a75c0e970f1b62e744463b484261905"),
    (7526902878389210390, "https://www.tiktok.com/@muhmemtb/video/7526902878389210390", 1752493648.0, "Shredding Muhme", "Shredding Muhme", "8e4baf64cbb8e8b0fd4c0d3dbcd63c6d6feba7a30d95280db039391e3803b3cf"),
])

def test_find_sequence_numbers(id, url, timestamp, title, description, sha256_hash):
    video = Video(
        id = id,
        url = url,
        timestamp = timestamp,
        title = title,
        description = description
    )

    video.download("test-downloads/")

    assert video.sha256_hash == sha256_hash
