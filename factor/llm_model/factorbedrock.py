import boto3
import base64
import json
from pdf2image import convert_from_path
import io

# Utility: Read PDF file and convert each page to base64 PNG (see pdf2image library for conversion)
def split_pdf_pages(pdf_path):
    images = convert_from_path(pdf_path)
    encoded_pages = []
    for img in images:
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        encoded_pages.append(base64.b64encode(buf.getvalue()).decode())
    return encoded_pages

# Build request payload for Claude Sonnet in Bedrock
def build_claude_request(pdf_path, structure):
    user_prompt="Extract invoice fields in a JSON similar to this structure: " + structure
    base64_pages = split_pdf_pages(pdf_path)
    messages = [{
        "role": "user",
        "content": [
            *[
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": b64_page
                    }
                } for b64_page in base64_pages
            ],
            {
                "type": "text",
                "text": user_prompt
            }
        ]
    }]
    req_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": messages,
        "max_tokens": 1000
    }
    return req_body

def extract_data_from_pdf(pdf_path, structure):
    client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1', verify=False)
    prompt_body = build_claude_request(pdf_path, structure)
    response = client.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(prompt_body)
    )
    resp_json = json.loads(response['body'].read())
    # Parse Claude JSON-formatted response
    result = json.loads(resp_json['content'][0]['text'])
    return result
