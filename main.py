import requests, multiprocessing, json, os 

TAGS = "rating:explicit score:>600"
LIMIT = "100" # Effectively the number of concurrent downloads. Max is 100.
STARTING_PAGE = 1

def downloader(file_url):
    filename = file_url.split("/")[-1]
    if not os.path.exists(filename):
        r = requests.get(file_url)
        open(filename, 'wb').write(r.content)

# Create/change into directory
if os.path.exists(TAGS):
    os.chdir(TAGS)
else:
    os.mkdir(TAGS)
    os.chdir(TAGS)


page = STARTING_PAGE
while True:
    req = f"https://konachan.com/post.json?page={page}&limit={LIMIT}&tags={TAGS}"
    req_text = requests.get(req).text
    parsed_req = json.loads(req_text)
    if len(parsed_req) == 0:
        break
    
    # Creating Jobs
    jobs = []
    for image in parsed_req:
        file_url = image["file_url"]
        proc = multiprocessing.Process(target=downloader, args=(file_url,))
        proc.start()
        jobs.append(proc)
    for job in jobs:
        job.join()
        job.close()
    print(f"Done with page {page}")
    page+=1
