import requests, multiprocessing, json

def downloader():
    pass    


page = 0
while True:
    req = f"https://konachan.com/post.json?page={page}&limit=100&tags=rating:explicit%20score:%3E600"
    req_text = requests.get(req).text
    parsed_req = json.loads(req_text)
    print(json.dumps(parsed_req,indent=2))
    exit()