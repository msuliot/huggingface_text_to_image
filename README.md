# Hugging Face - Text to Image

This repository is a simple example of how to use the Hugging Face Hub to convert an text to image.

## The basics

1. Must have Python3.
2. Get repository
```bash
git clone https://github.com/msuliot/huggingface_text_to_image.git 
```
3. use pip3 to install any dependencies.
```bash
pip3 install -r requirements.txt
```

## Hugging Face Access Token

You'll need to sign up for an account on https://huggingface.co/ and get an access token.
Make sure to get an access token key from https://huggingface.co/settings/tokens

Create a ".env" file in the project root directory and add the following:
```bash
HUGGINGFACEHUB_API_TOKEN = 'hf_XXXXXXXX'
MODEL_NAME = 'runwayml/stable-diffusion-v1-5'
PIPELINE_TASK = "text-to-image"
```

# Instructions:

There is example of how to use the Hugging Face Hub.

## Run the API script
```bash
python3 api.py
```

## Hugging Face Hub API
https://huggingface.co/runwayml/stable-diffusion-v1-5
- modelId: runwayml/stable-diffusion-v1-5
- pipeline_tag: text-to-image
- library_name: diffusers
- task_specific_params: None