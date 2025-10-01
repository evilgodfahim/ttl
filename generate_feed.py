import feedparser
from datetime import datetime, timedelta, timezone
import pytz

# Your feeds dictionary
feeds = {
    "Bangla Editorials": [
        "https://evilgodfahim.github.io/bdpratidin-rss/feed.xml",
        "https://politepol.com/fd/DbgDjmR4B0ua.xml",
        "https://politepol.com/fd/1yC3YJpL3i6t.xml",
        "https://fetchrss.com/feed/aLNkZSZkMOtSaLNkNF2oqA-i.rss",
        "https://politepol.com/fd/lRzLqNhRg2jV.xml",
        "https://politepol.com/fd/LWVzWA8NSHfJ.xml",
        "https://politepol.com/fd/4LWXWOY5wPR9.xml",
        "https://politepol.com/fd/VnoJt9i4mZPJ.xml",
        "https://politepol.com/fd/R6Nj5lriwGBg.xml",
        "https://politepol.com/fd/MMd5ai243dRY.xml",
        "https://politepol.com/fd/aPXIv1Q7cs7S.xml",
        "https://politepol.com/fd/dwg0cNjfFTLe.xml",
        "https://politepol.com/fd/DrjUg80wxrku.xml",
    ],

    "English Editorials": [
        "https://politepol.com/fd/QAIWwDi3wOuZ.xml",
        "https://politepol.com/fd/LONi4mJ2tfbd.xml",
        "https://evilgodfahim.github.io/rss-combo-NA/feed.xml",
        "https://politepol.com/fd/2XdgObSDG4FD.xml",
        "https://politepol.com/fd/xaIRlDYPW0kP.xml",
        "https://politepol.com/fd/LwUmZUwUaj7i.xml",
        "https://politepol.com/fd/Uh7pOg6WWCMR.xml",
        "https://politepol.com/fd/GxmRWljxfGEo.xml",
        "https://politepol.com/fd/oT0YgLtnGzze.xml",
        "https://politepol.com/fd/ggpXf4wO5uEz.xml",
        "https://politepol.com/fd/OAVNbKjejtJQ.xml",
        "https://politepol.com/fd/CnOMC37mGwul.xml",
        "https://politepol.com/fd/qVPraFDG1MNh.xml",
    ],

    "Magazines": [
        "https://www.scientificamerican.com/platform/syndication/rss/",
        "https://feeds.newscientist.com/science-news",
        "https://nautil.us/feed/",
        "http://ftr.fivefilters.org/makefulltextfeed.php?url=http%3A%2F%2Fmentalfloss.com%2Frss.xml&max=9",
        "https://www.theatlantic.com/feed/channel/ideas/",
        "https://www.popsci.com/rss.xml",
        "https://www.psychologytoday.com/intl/front/feed",
        "https://theconversation.com/us/topics/psychology-28/articles.atom",
        "https://theconversation.com/us/topics/artificial-intelligence-ai-90/articles.atom",
        "https://politepol.com/fd/j6weY8TmEdGW.xml",
    ],

    "International": [
        "http://feeds.feedburner.com/dawn-news-world",
        "https://feeds.guardian.co.uk/theguardian/world/rss",
        "https://www.ft.com/rss/world",
        "https://feeds.feedburner.com/AtlanticInternational",
        "https://theconversation.com/articles.atom",
        "https://news.un.org/feed/subscribe/en/news/all/rss.xml",
        "https://politepol.com/fd/IleailW8Do7p.xml",
        "https://www.ft.com/rss/world/brussels",
        "https://www.ft.com/rss/companies/energy",
        "https://www.ft.com/rss/home/asia",
        "https://www.themoscowtimes.com/rss/news",
        "https://politepol.com/fd/x7ZadWalRg3O.xml",
        "https://politepol.com/fd/2wwElTcUpcfo.xml",
        "https://politepol.com/fd/FQtkYoIiTwrT.xml",
        "https://politepol.com/fd/MrLghs9CUuhs.xml",
        "https://politepol.com/fd/nTjHEYiFFmDe.xml",
        "https://www.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://www.aljazeera.com/Services/Rss/?PostingId=2007731105943979989",
        "https://www.scmp.com/rss/5/feed",
        "https://www.indiatoday.in/rss/1206577",
        "https://www.thehindu.com/news/international/?service=rss",
        "https://feeds.bbci.co.uk/news/world/rss.xml",
        "https://politepol.com/fd/IZHDnFfjhvdc.xml",
        "https://politepol.com/fd/iFF48wN05TWX.xml",
        "https://politepol.com/fd/hKA2ZijBkurO.xml",
        "https://politepol.com/fd/ejjxAclQ0Ij0.xml",
        "https://politepol.com/fd/mxmm1zHl3Vkp.xml",
        "https://politepol.com/fd/eU6sPuvezFmi.xml",
        "https://politepol.com/fd/mgL5tJODdXMU.xml",
        "https://politepol.com/fd/jxdB7qx3NSFJ.xml",
        "https://politepol.com/fd/aGCRq4aQKpwL.xml",
        "https://politepol.com/fd/twCQYifhldi8.xml",
        "https://politepol.com/fd/RVHJinKtHIEp.xml",
        "https://politepol.com/fd/MQdEEfACJVgu.xml",
        "https://www.scmp.com/rss/318199/feed",
    ],

    "Geopolitics": [
        "https://www.noemamag.com/article-topic/geopolitics-globalization/feed/",
        "https://zeihan.com/feed/",
        "https://theconversation.com/global/home-page.atom",
        "https://politepol.com/fd/ELc5hcluIkDO.xml",
        "https://evilgodfahim.github.io/eco/combined.xml",
        "https://www.worldpoliticsreview.com/feed/",
        "https://rss.diffbot.com/rss?url=https://www.csis.org/analysis?f%255B0%255D%3Dcontent_type%253Areport",
        "https://original.antiwar.com/feed/",
        "https://evilgodfahim.github.io/ps/combined.xml",
        "https://theconversation.com/global/topics/climate-change-27/articles.atom",
        "https://www.atlanticcouncil.org/feed/",
        "https://www.lowyinstitute.org/the-interpreter/rss.xml",
        "https://politepol.com/fd/BzFhFtawKQrt.xml",
        "https://politepol.com/fd/R39To2fYhqqO.xml",
        "https://asiatimes.com/feed/",
        "https://foreignpolicy.com/feed/",
        "https://www.foreignaffairs.com/rss.xml",
        "https://warontherocks.com/feed/",
        "https://thediplomat.com/feed/",
    ],
}


def fetch_titles():
    bd_tz = pytz.timezone("Asia/Dhaka")
    now = datetime.now(bd_tz)
    cutoff = now - timedelta(days=1)

    section_titles = {}
    for section, urls in feeds.items():
        titles = []
        for url in urls:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries:
                    if hasattr(entry, "published_parsed") and entry.published_parsed:
                        pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc).astimezone(bd_tz)
                        if pub_date > cutoff:
                            titles.append(entry.title)
            except Exception as e:
                print(f"Error fetching {url}: {e}")
        if titles:
            section_titles[section] = titles
    return section_titles, now


def build_rss(section_titles, now):
    rss = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    rss += '<rss version="2.0">\n<channel>\n'
    rss += f"<title>Daily News Titles</title>\n"
    rss += f"<link>https://yourusername.github.io/</link>\n"
    rss += f"<description>News titles from past 24 hours (grouped by section)</description>\n"
    rss += f"<lastBuildDate>{now.strftime('%a, %d %b %Y %H:%M:%S %z')}</lastBuildDate>\n"

    for section, titles in section_titles.items():
        description = "<ul>" + "".join([f"<li>{t}</li>" for t in titles]) + "</ul>"
        rss += "<item>\n"
        rss += f"<title>{section}</title>\n"
        rss += f"<description><![CDATA[{description}]]></description>\n"
        rss += f"<pubDate>{now.strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate>\n"
        rss += "</item>\n"

    rss += "</channel>\n</rss>"
    return rss


if __name__ == "__main__":
    section_titles, now = fetch_titles()
    rss = build_rss(section_titles, now)
    with open("feed.xml", "w", encoding="utf-8") as f:
        f.write(rss)
    print("feed.xml generated successfully")
