# config file for bot. rename this to "config.py"

# paste bot token here
bot_token = "5110671020:AAFgnwlOaVcE0uG48kgNiRz0hxzMnziVjDQ"  # "something:something"

# replying mode
# can be one of these: substitute, links
reply_mode = "substitute"

alternative_services_links = {
    "nitter": [https://nitter.kavin.rocks/
    ],
    "bibliogram_userpage": [
    ],
    "bibliogram_post": [
    ],
    "invidious": [https://invidious.flokinet.to/
    ],
    "piped": [https://piped.moomoo.me/
    ],
    "libreddit": [https://libreddit.domain.glass/
    ],
    "teddit": [https://teddit.namazso.eu/
    ],
    "quetre": [https://quetre.pussthecat.org/

    ],

}


alternative_services_regex_noncompiled = {
    "nitter": (r'https://(?:www.)?twitter.com/(.*)\b', r'LINK/\1 '),
    "bibliogram_userpage": (r'https://(?:www.)?instagram.com/(?!p/)(.*)\b', r'LINK/\1 '),
    "bibliogram_post": (r'https://(?:www.)instagram.com/(?:p/)(.*)\b', fr'LINK/\1 '),
    "invidious": (r'https://(?:www.)?youtube.com/(.*)\b', r'LINK/\1'),
    "piped": (r'https://(?:www.)?youtube.com/(.*)\b', r'LINK/\1'),
    "libreddit": (r'https://(?:www.)?reddit.com/(.*)\b', r'LINK/\1'),
    "teddit": (r'https://(?:www.)?reddit.com/(.*)\b', r'LINK/\1'),
    "quetre": (r'https://(?:www.)?quora.com/(.*)\b', r'LINK/\1'),
}
