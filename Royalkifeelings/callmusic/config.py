from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME: str = getenv("SESSION_NAME", "BQGN-6oAs-d4nGJw0LCu2t2jODV7-gNbXZX8PQdOtL4pDd2881pVqKk_0W6xneHko_965ct5RSoKhUBOY_jMt_jRDkgBTSGtidVnSbc1NkPuxRN_U2KuSZqN_Zj-gVQzPN4BQixmLpv2rp0t61pgIpMgafgi_dQaU-hLSd_mhE7vJuDN7m2Eb6jXdh6S5nlCMXtkTZC3N5NRqhh-vDK73-2ubeuanOdZWvJ1no1xjyVSmrF8e5aBJf3VXf7BZZ8TYPLM7g7lJwWbGVerRFa4D1wKLd8kAqAAHvWCAbYQJkOykhyh8LUOyFNI6BhTn_Qcx1tlHU5tZtWJsYjo9qrR5AegSgH0KAAAAAGDG0hoAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
BOT_USERNAME = getenv("BOT_USERNAME", "HTY_music_bot")
BOT_TOKEN = getenv("BOT_TOKEN", "6675977689:AAHfygfHMDYsMhdH-RjWi66R8-fqqtf9KnU")
API_ID = int(getenv("API_ID", "26082218"))
API_HASH = getenv("API_HASH", "ac0fb55d391ea7b98ceac2b72b1a9d59")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "-1002144418547")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "-1002144418547")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6753033991").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6753033991").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "12000"))
PMPERMIT = getenv("PMPERMIT", "ENABLE")
BOT_NAME = getenv("BOT_NAME","Music_robot")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://l.arzfun.com/GvMbc")
