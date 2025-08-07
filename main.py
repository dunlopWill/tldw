from pydantic import (
    HttpUrl,
)
from tldw import tldw

from config import settings


def main(url: HttpUrl):
    summary = tldw(settings.OPENAI_API_KEY)
    summary.summarize(url)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="the youtube url")
    args = parser.parse_args()
    main(url=args.url)
