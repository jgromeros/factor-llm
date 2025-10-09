# Description
Factor-LLM is the api for the calls to a LLM models

## Set up
* Create a virtual env: python3 -m venv venv
* Activate virtual env: source venv/bin/activate
* Install: pip install -r requirements.txt --index-url=https://pypi.org/simple

## Run
Run the app: ```python app.py```

## Usage
The call to factorbedrock is slightly different, as its goal is to extract text from a PDF file:

```
curl --location 'http://127.0.0.1:5000/extract' \
--form 'file=@"/path/to/file/filename.pdf"'
```
