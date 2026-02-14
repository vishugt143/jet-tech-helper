from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "21419016"))
    API_HASH = getenv("API_HASH", "79198e1eb4cfd0f771a89d83b9144e7e")
    BOT_TOKEN = getenv("BOT_TOKEN", "8535066520:AAF8YnwZHzkkd0fefmUTUze7sxq8gJkPfWg")

    # Admin / Owner IDs (space-separated)
    SUDO = list(map(int, getenv(
        "SUDO",
        "7554081592 8161051200 7564050858 5656436152"
    ).split()))

    MONGO_URI = getenv(
        "MONGO_URI",
        "mongodb+srv://melodysotto4_db_user:BCUKIKDEAqFEzeCj@cluster0.trrt89o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )

    # Posts to copy
    POSTS = [
        "https://t.me/forward_hack_lnx/113",
        "https://t.me/forward_hack_lnx/114",
        "https://t.me/forward_hack_lnx/115"
    ]

    # 🚫 ILLEGAL WORDS (BOT SIDE FILTER)
    ILLEGAL_WORDS = [
        "@controllerbot",
        "creatings",
        "tasks",
        "tasks.",
        "accomplish"
    ]

cfg = Config()
