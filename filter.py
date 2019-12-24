from google_images_download import google_images_download 
import json

response = google_images_download.googleimagesdownload()

def downloadImage(query):
    parameters = {"keywords": query, 
        "format": "jpg", 
        "limit":1, 
        "image_directory": "mtgImages",
        # "exact_size": (672,936)}
        "size": "medium"}
    try:
        response.download(parameters)
    except FileNotFoundError:
        print("Fail!")

def smooth(cardNames):
    toReturn = []
    for card in range(len(cardNames)):
        if (cardNames[card][0] == '\n'):
            toReturn.append(cardNames[card].strip())
        # cardNames[card] = cardNames[card].strip()
    return toReturn

if __name__ == "__main__":
    file = open('./tappedOutScraper/spiderOutput.json')
    data = json.load(file)
    for dictionary in data:
        cardNames = dictionary.get("card_name")
        cardNames = smooth(cardNames)
        # for card in cardNames:
        #     print(card)

        for card in cardNames:
            query = "mtg scryfall " + card
            print(query)
            downloadImage(query)