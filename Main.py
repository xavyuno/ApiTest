import requests
import webbrowser

pokeUrl = "https://pokeapi.co/api/v2/"
waifuUrl = "https://api.waifu.pics/sfw/waifu"
artUrl = "https://api.artic.edu/api/v1/artworks?page=2&limit=100"
memeUrl = "https://meme-api.com/gimme"
recipeURL = "https://serpapi.com/search.json?engine=google_ai_mode&q=yes"

print(f"Choose API: \n1: {pokeUrl}\n2: {waifuUrl}\n3: {memeUrl}\n4: {recipeURL}")
urlChoice = int(input())

def GetMeal(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        Data = response.json()
        print(Data)
        print(response)
    else:
        print("failed to retrieve data")

def GetPokemon(name):
    url = f"{pokeUrl}/pokemon/{name}"
    respone = requests.get(url)
    if respone.status_code == 200:
        print(respone)
        Data = respone.json()
        print(f"Name: {Data["name"]}")
        print(f"Id: {Data["id"]}")
    else:
        print("failed to retrieve data")

def GetImageFromUrl(URL, filePath):
    respone = requests.get(URL)
    if respone.status_code == 200:
        Data = respone.json()
        url = Data["url"]
        newRespone = requests.get(url)
        if newRespone.status_code == 200:
            with open(filePath, 'wb') as file:
                file.write(newRespone.content)
        else:
            print("failed to retrieve Image")
    else:
        print("failed to retrieve Image Link")

match urlChoice:
    case 1:
        print("Enter pokemon name: ")
        pokemonName = input()
        GetPokemon(pokemonName)
    case 2:
        print("Enter Number of waifu pics to retrieve: ")
        amount = int(input())
        for i in range(amount):
            GetImageFromUrl(waifuUrl, f"C:/Users/xavie/OneDrive/Pictures/waifus/{i}.jpg")
            print(i+1,"/",amount)
        print("Done")
    case 3:
        print("Enter Number of memes to retrieve: ")
        amount = int(input())
        for i in range(amount):
            GetImageFromUrl(memeUrl, f"C:/Users/xavie/OneDrive/Pictures/memes/{i}.jpg")
            print(i+1,"/",amount)
        print("Done")
    case 4:
        GetMeal(recipeURL)
    