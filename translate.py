
def translate(raw):
    import requests
    r = requests.post("https://api.funtranslations.com/translate/shakespeare.json", data={"text": str(raw)})
    print(r.text)
        


translate("hello")