from typing import Dict, List
import urllib.request


def make_file(url: str, filename: str) -> None:
    html_res = urllib.request.urlopen(url)
    html_content = html_res.read()
    with open(f"ServerFile/{filename}", "w") as file:
        file.write(html_content.decode())


def get_websites() -> List[Dict[str, str]]:
    return [
        {
            "url": "https://www.python.org",
            "filename": "python.org.html"
        },
        {
            "url": "https://stackoverflow.com",
            "filename": "stackoverflow.com.html"
        },
        {
            "url": "https://www.rust-lang.org",
            "filename": "rust-lang.org.html"
        },
        {
            "url": "https://github.com",
            "filename": "github.com.html"
        },
        {
            "url": "https://www.typescriptlang.org",
            "filename": "typescriptlang.org.html"
        },
        {
            "url": "https://code.visualstudio.com",
            "filename": "code.visualstudio.com.html"
        },
        {
            "url": "https://www.w3schools.com",
            "filename": "w3schools.com.html"
        },
        {
            "url": "https://aiartists.org",
            "filename": "aiartists.org.html"
        },
        {
            "url": "https://craftinginterpreters.com",
            "filename": "craftinginterpreters.com.html"
        },
        {
            "url": "https://www.notion.so",
            "filename": "notion.so.html"
        },
    ]


if __name__ == "__main__":
    websites = get_websites()
    for website in websites:
        print(website["url"])
        make_file(website["url"], website["filename"])
