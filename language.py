def setLang():
    # please, set ES for spanish or EN for english
    lang = "EN"
    if(lang == "ES"):
        prop = {"popup":'Ahora no'}

    elif(lang == "EN"):
        prop = {"popup":'Not now'}

    return prop