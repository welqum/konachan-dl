import requests, multiprocessing, json

TAGS = "rating:explicit score:>600"
LIMIT = "100"
STARTING_PAGE = 0

def downloader(file_url):
    pass

page = STARTING_PAGE
while True:
    req = f"https://konachan.com/post.json?page={page}&limit={LIMIT}&tags={TAGS}"
    req_text = requests.get(req).text
    parsed_req = json.loads(req_text)
    if len(parsed_req) == 0:
        break
    jobs = []
    for image in parsed_req:
        file_url = image["jpeg_url"]
        proc = multiprocessing.Process(target=downloader, args=(file_url,))
        proc.start()
        jobs.append(proc)
    for job in jobs:
        job.join()
        job.close()
    exit()
    page+=1