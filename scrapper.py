#https://news.ycombinator.com/item?id=31582796
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    url="https://news.ycombinator.com/item?id=31582796"
    response =requests.get(url)
    contentt =response.content
    soup=BeautifulSoup(contentt,"html.parser")
    elements = soup.find_all(class_="ind", indent=0)
    comments = [e.find_next(class_="comment") for e in elements]
    keywords = {
        "python": 0,
        "javascript": 0,
        "typescript": 0,
        "ruby": 0,
        "java": 0,
        "rust": 0,
        "c#": 0,
    }

    for comment in comments:
        comment_text = comment.get_text().lower()
        words = comment_text.split(" ")
        words = {w.strip(".,|/:;!@") for w in words}

        for k in keywords:
            if k in words:
                keywords[k] += 1

    print(keywords)

    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel("Language")
    plt.ylabel("# of Mentions")
    plt.show()

if __name__=="__main__":
    main()