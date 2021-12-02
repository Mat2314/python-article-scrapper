# python-article-scrapper

## Serve the victim website and see it in your browser
Go to the catalogue `victim-website` and run python http server by the following command:
```
$ python3 -m http.server
```

Then open your browser and go to 
```
http://127.0.0.1:8000/
```

You should see the website being served properly.

## Run the script
To run the script open the console, go to the project root directory and do the following:
```
### Setup virtual environment for python
$ python3 -m venv myvenv

### Activate virtual environment
$ . myvenv/bin/activate

### Run the script passing full url address of the restricted article
### As article is served locally, pass the url of localhost
(myvenv) $ python main.py http://127.0.0.1:8000/
```

The script will create a new local html file and open it in your browser without JavaScript that hides the content.

Now you can enjoy the article!