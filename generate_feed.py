import feedparser
from datetime import datetime, timedelta, timezone
import pytz
import os

feeds = {
    "Bangla Editorials": [
        "https://evilgodfahim.github.io/bdpratidin-rss/feed.xml",
        "https://politepol.com/fd/DbgDjmR4B0ua.xml",
        "https://politepol.com/fd/1yC3YJpL3i6t.xml",
    ],
    "English Editorials": [
        "https://politepol.com/fd/QAIWwDi3wOuZ.xml",
        "https://politepol.com/fd/LONi4mJ2tfbd.xml",
    ],
    "Magazines": [
        "https://www.scientificamerican.com/platform/syndication/rss/",
        "https://feeds.newscientist.com/science-news",
    ],
    "International": [
        "http://feeds.feedburner.com/dawn-news-world",
        "https://feeds.guardian.co.uk/theguardian/world/rss",
    ],
    "Geopolitics": [
        "https://www.noemamag.com/article-topic/geopolitics-globalization/feed/",
        "https://zeihan.com/feed/",
    ],
}

OUTPUT_FILE = "feed.xml"
COUNTER_FILE = "counter.txt"

# --- Load counter ---
if os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "r") as f:
        update_counter = int(f.read().strip()) + 1
else:
    update_counter = 1

# --- Time range (24 hours, BD timezone) ---
bd_tz = pytz.timezone("Asia/Dhaka")
now = datetime.now(bd_tz)
yesterday = now - timedelta(days=1)

items = []

# --- Parse feeds ---
for category, urls in feeds.items():
    section_items = []
    for url in urls:
        d = feedparser.parse(url)
        for entry in d.entries:
            if hasattr(entry, "published_parsed"):
                published_dt = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc).astimezone(bd_tz)
            elif hasattr(entry, "updated_parsed"):
                published_dt = datetime(*entry.updated_parsed[:6], tzinfo=timezone.utc).astimezone(bd_tz)
            else:
                continue
            if yesterday <= published_dt <= now:
                title = entry.title
                section_items.append(f"• {title}")
    if section_items:
        section_text = f"{category} (Update #{update_counter})\n" + "\n".join(section_items)
        items.append(f"<item><title>{section_text}</title><guid>{category}-{update_counter}</guid></item>")

# --- Build XML feed ---
rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
<title>Daily News Feed Update #{update_counter}</title>
<link>https://yourgithubusername.github.io/</link>
<description>Daily collected titles from multiple sources</description>
<lastBuildDate>{now.strftime('%a, %d %b %Y %H:%M:%S %z')}</lastBuildDate>
{''.join(items)}
</channel>
</rss>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(rss_content)

# --- Save counter ---
with open(COUNTER_FILE, "w") as f:
    f.write(str(update_counter))
