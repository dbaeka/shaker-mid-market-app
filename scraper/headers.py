headers = {
    "currencies": {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "optimizelyEndUserId=oeu1674226228291r0.570224114177605; _y2=1%3AeyJjIjp7fX0%3D%3AMTc0OTg2MjMwNA%3D%3D%3A2; ln_or=eyIxNDA3MDI4IjoiZCJ9; IR_gbd=xe.com; _fbp=fb.1.1674226236874.1329039429; _ga=GA1.2.1288794807.1674226286; _gid=GA1.2.1773360729.1674226286; _ga_KRKJ3PLCP1=GS1.1.1674226286.1.1.1674226473.52.0.0; amp_470887=bwpZO93IivLXhke7cBi_p7...1gn8vo155.1gn8vo157.a.5.f; _uetsid=cb87826098d111ed82b35f3744eea9f5; _uetvid=197750a06cb511ed8a022bbe8070c616; IR_12610=1674265233613%7C0%7C1674265233613%7C%7C; _yi=1%3AeyJsaSI6bnVsbCwic2UiOnsiYyI6MywiZWMiOjY3LCJsYSI6MTY3NDI2NTI0MjI5MSwicCI6NSwic2MiOjM5MDAyfSwidSI6eyJpZCI6IjM3ODgxMTU5LWZmMjgtNGJlNC04Yjk3LTIzZjA0YzBlNjMxOCIsImZsIjoiMCJ9fQ%3D%3D%3ALTE5NjU3ODQwMA%3D%3D%3A2",
        "referer": "https://www.xe.com/currencyconverter/",
        "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    },
    "rates": {
        "authorization": "Basic bG9kZXN0YXI6RDlxT3N3RVg4WEJabjVidGhYRDN5Rk1OOG0yVXE3ZXQ=",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "optimizelyEndUserId=oeu1674226228291r0.570224114177605; _y2=1%3AeyJjIjp7fX0%3D%3AMTc0OTg2MjMwNA%3D%3D%3A2; ln_or=eyIxNDA3MDI4IjoiZCJ9; IR_gbd=xe.com; _fbp=fb.1.1674226236874.1329039429; _ga=GA1.2.1288794807.1674226286; _gid=GA1.2.1773360729.1674226286; _ga_KRKJ3PLCP1=GS1.1.1674226286.1.1.1674226473.52.0.0; amp_470887=bwpZO93IivLXhke7cBi_p7...1gn8vo155.1gn8vo157.a.5.f; _uetsid=cb87826098d111ed82b35f3744eea9f5; _uetvid=197750a06cb511ed8a022bbe8070c616; IR_12610=1674265233613%7C0%7C1674265233613%7C%7C; _yi=1%3AeyJsaSI6bnVsbCwic2UiOnsiYyI6MywiZWMiOjY3LCJsYSI6MTY3NDI2NTI0MjI5MSwicCI6NSwic2MiOjM5MDAyfSwidSI6eyJpZCI6IjM3ODgxMTU5LWZmMjgtNGJlNC04Yjk3LTIzZjA0YzBlNjMxOCIsImZsIjoiMCJ9fQ%3D%3D%3ALTE5NjU3ODQwMA%3D%3D%3A2",
        "referer": "https://www.xe.com/currencyconverter/",
        "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
}


def get_xe_headers(source: str) -> dict:
    return headers[source]
