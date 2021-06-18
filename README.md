# Very simple Konachan "downloader"

May improve later. Would call it more of an "API requester" than downloader.

Prints out all the image URLs for a given set of tags

I just redirect the URLs to a text file and then use wget to download every file

```
python3 main.py > urls.txt
wget -i urls.txt
```

Main problem, very slow! wget goes sequentially.
Might add download functionality with multiprocessing to speed things up, but that's later...