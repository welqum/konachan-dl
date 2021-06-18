# A Simple Konachan Image Downloader

A simple fast Konachan downloader written in Python that probably works.

Download `git clone https://github.com/welqum/konachan-dl` 

Open the file named `main.py` and modify the `TAGS` constant to download what you like.

```python
TAGS = "rating:explicit score:>600" # The search term.
LIMIT = "100" # Effectively the number of concurrent downloads. Max is 100. Decrease if your computer can't keep up.
STARTING_PAGE = 0 # Likely no need to change this since the program automatically skips files that are already downloaded.
```

Run with `cd konachan-dl` and then `python3 main.py`

Feel free to contribute!