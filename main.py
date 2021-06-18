import requests, multiprocessing, json

def downloader():
    pass    

tags = "rating:explicit score:>600"

page = 0
while True:
    req = f"https://konachan.com/post.json?page={page}&limit=100&tags={tags}"
    req_text = requests.get(req).text
    parsed_req = json.loads(req_text)
    if len(parsed_req) == 0:
        break
    for image in parsed_req:
        file_url = image["jpeg_url"]
        print(file_url)
    page+=1