import Helper as hp
from diffusers import StableDiffusionPipeline
import torch
import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file
model_name = os.getenv('MODEL_NAME') # model name for huggingface.co in .env file  MODEL 1 or MODEL 2
api_url = f"https://api-inference.huggingface.co/models/{model_name}"


def hf_pipeline(text):
    pipe = StableDiffusionPipeline.from_pretrained(model_name) #, torch_dtype=torch.float16 if you have a GPU with Tensor Cores
    try:
        pipe = pipe.to("cuda")
    except Exception as e:
        print(f"Failed to move the model to GPU: {e}")
        pipe = pipe.to("cpu")  # Fallback to CPU

    prompt = "Dog on a treadmill reading a book on mars"
    image = pipe(prompt).images[0]  
    fName = hp.get_random_number()
    image.save(f"images/{fName}.png")
    print(f"Image saved at images/{fName}.png")


def main():
    text = "Dog on a treadmill reading a book on mars"
    hf_pipeline(text)
    

if __name__ == "__main__":
    main() 