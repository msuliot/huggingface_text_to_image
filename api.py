import requests
import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file
model_name = os.getenv('MODEL_NAME') # model name for huggingface.co in .env file
api_url = f"https://api-inference.huggingface.co/models/{model_name}"


def hf_api(text):
    headers = {"Authorization": f"Bearer {hf_api_key}"}

    def query(payload):
        response = requests.post(api_url, headers=headers, json=payload)
        return response.content
    image_bytes = query({
        "inputs": text,
    })
    # You can access the image with PIL.Image for example
    import io
    from PIL import Image
    image = Image.open(io.BytesIO(image_bytes))
    image.save("images/your_image.png")
    print("Image saved at images/your_image.png")


def main():
    text = "a robot watching my videos"
    hf_api(text)
    


if __name__ == "__main__":
    main() 