import re


async def check_link_instagram(link):
    pattern = r"^https:\/\/(www\.)?instagram\.com\/.*$"
    return re.match(pattern, link) is not None


async def check_link_tiktok(url):
    pattern = r"^https:\/\/(vt\.)?tiktok\.com\/.*$"
    return re.match(pattern, url) is not None


async def check_link_you_tube(url):
    pattern = r"^https:\/\/(www\.)?(youtube\.com\/|youtu\.be\/).*"
    return re.match(pattern, url) is not None
