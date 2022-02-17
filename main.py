import re
import requests
import sys
import bs4
import urllib.parse
import colorama
import json

def capeutservir(url:str, number:str):
    headers = {
        "content-length":"13",
        "cache-control":"max-age=0",
        "sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="92"',
        "sec-ch-ua-mobile":"?0",
        "upgrade-insecure-requests":"1",
        "origin":"https://www.capeutservir.com",
        "content-type":"application/x-www-form-urlencoded",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site":"same-origin",
        "sec-fetch-mode":"navigate",
        "sec-fetch-user":"?1",
        "sec-fetch-dest":"document",
        "referer":"https://www.capeutservir.com/telephonie/",
        "accept-encoding":"gzip, deflate, br",
        "accept-language":"fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie":"_ga=GA1.2.1763083644.1644104418",
        "cookie":"_gid=GA1.2.937535373.1644104418",
        "cookie":"euconsent-v2=CPT6WwAPT6WwABcAIBFRCBCgAP_AAH_AAAIgIDkR_CrETWFiUf59AvsgQYAG10AEIGQADACIAyABAAPA8IQAgCAQAARAAgAIAAAAogJBAAABCAlAAAAAQAAAAAGIAAEAAAAIICAAAAARAgEACAhAAAAAAAAAAABBABAAkAAAABoAQAQAEAAgAAAAAAAACAAAAAAAAAAAAAAAAAAAAAggOACYKkRAAWJQ4EkAaQAAgBBWAAQAIAAIAIACIAAAAADghAAQAAAAAAAAAAgAAACiAgEAAAEACEAAAABAAAAAAAgAAAAAAAgAIAAAAAEAAAAACAAAAAAAAAAAAEEAAACAAAAAEABAAAAQACAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAA.x6fs2cY.dAAAAAAAAAA.4YpAUgBGACyAF0ANgAjwBRADEAGUARAAm4BxQDxAHrASWA9UCIgESQJRASxAlqBL8CZwGDAMLAcyA6cB2EEDAIGgQsgkMBIxCgsKDAVngszBaOC30FzoLyQX5gxSAAgAEABAAEAAgAIA",
        "cookie":"_pbjs_userid_consent_data=8898435508114420",
        "cookie":"sharedid=ddec2b5c-9229-4bed-9f60-258ad32eb831",
        "cookie":"__qca=P0-1693457346-1644104423093",
        "cookie":"__gads=ID=3ff5b6c8d04153fb:T=1644104418:S=ALNI_MYI6jYDZbRyCNgi-5LB7KWpexH-fg",
        "cookie":"PHPSESSID=8da7b4c0c9b4a6deae851a3a0df2c9fd",
        "cookie":"_gat=1",
        "cookie":"cto_bundle=0p8hkF9JdmtQeEtWanBORkhSY05sM21VQ29lRHd6dE9xJTJCVTBHdExGb2lSJTJGQTJiRW92VFlHSVhtNFlpamh1QU01UGFHQ2lKVkpaQU9DWTlpZ2ExTGlVYkFEUlVjRFU2QTN5UHZMJTJGaGROandVME40VUVQMmVQRHR0akxucWpXTzFibk9RT25Iem0wYmN2aGQ1NyUyRk1zTmo1emtvdyUzRCUzRA",
        "cookie":"cto_bundle=0p8hkF9JdmtQeEtWanBORkhSY05sM21VQ29lRHd6dE9xJTJCVTBHdExGb2lSJTJGQTJiRW92VFlHSVhtNFlpamh1QU01UGFHQ2lKVkpaQU9DWTlpZ2ExTGlVYkFEUlVjRFU2QTN5UHZMJTJGaGROandVME40VUVQMmVQRHR0akxucWpXTzFibk9RT25Iem0wYmN2aGQ1NyUyRk1zTmo1emtvdyUzRCUzRA",
        "cookie":"cto_bundle=2GHVB19JdmtQeEtWanBORkhSY05sM21VQ29Xa3BXT1hrQVVHR0FNbTh1Q0ZvS3AxRVolMkJSZ2Y0eUJXcWVoMWZPaUolMkZlRUJKeHl2b1UzV3k1Nk14MXNoYXZvdHBFY1NZSmhqJTJCMSUyRmM4ZnlKSyUyRlc5JTJGQSUyQmowT3RGa1dCU3FWNDVCRmVwWUtIY0Yycjg1M3dpSFUlMkJIUXdyOW85SXZnJTNEJTNE",
        "cookie":"cto_bidid=oubKsF9KdUFnaXdvYVZoJTJCcU5IVCUyQnFnd05GNDlvNW5rbXYlMkJlJTJGJTJCWCUyQnlrMG9zWW0wVHVCMDlpdEo1eWVFc2VCUFR2VFpHdkpZVkw4U2F1R0NkRjlNR3dKNjdubUZZV1Z3JTJCVVV0MnBZdnVKRXpVaURNZVNXbSUyQkduNEdZSUN1akxkVGo0dXM"
    }

    data = {"numero":number[0:6]}
    response = requests.post(url, data=data, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    operateur = soup.find_all("strong", attrs={"style":"margin-top: 1em; display:inline-block; font-size: 2em; font-weight: normal;"})
    for i in operateur:
        print(f"{colorama.Fore.GREEN}{number}: {i.string}{colorama.Fore.RESET}")

def messente(number: str):
    url = "https://messente.com/messente-api/number-lookup/?phone_number="
    response = requests.get(f"{url}{urllib.parse.quote_plus(number)}")
    if (len(list(filter(lambda x: x == "error", json.loads(response.text)))) > 0):
        pass
    else:
        print(f"{number}: {json.loads(response.text)['originalCarrierName']}")

if __name__ == "__main__":
    colorama.init()
    with open(sys.argv[1], mode="r", encoding="utf8") as file:
        numbers = file.readlines()
        numArray = []
        for i in numbers:
            numArray.append(i.strip())

    url = "https://www.capeutservir.com/telephonie/operateur_find.php"

    for i in numArray:
        messente(i)
        capeutservir(url, i)
