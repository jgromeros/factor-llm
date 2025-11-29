# Description
Factor-LLM is the api for the calls to a LLM models

## Set up
* If the IDE does not do it for you, create a virtual env: python3 -m venv .venv
* Activate virtual env: source .venv/bin/activate
* Install: pip install -r requirements.txt --index-url=https://pypi.org/simple

## Run
Run the app: ```python app.py```

## Usage
The call to extract text from a PDF file given a particular structure (as a JSON file):

```
curl --location 'http://127.0.0.1:5000/extract' \
--form 'file=@"/Users/juansilva/Downloads/Factura_FJEZ65603.pdf"' \
--form 'structure="{\"invoice\": {\"number\": \"\", \"customer\":{\"name\":\"\", identificacionNumber\":\"\", \"email\":\"\", \"country\":\"\"}, \"invoiceTotal\":, \"invoiceTax\":, \"totalBeforeTaxes\":, \"currency\":\"\", \"date\":\"\", \"paymentMethod\":\"\", items:[{\"description\":\"\", \"quantity\":, \"unitPrice\":, \"taxRate\":, \"tax\":, \"totalValue\":}]}}"'
```
