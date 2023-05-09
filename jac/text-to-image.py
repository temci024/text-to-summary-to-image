import requests
import  base64
from jaseci.jsorc.live_actions import jaseci_action
import traceback
from fastapi import HTTPException


API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}


@jaseci_action(act_group=["text-to-image"], allow_remote=True)

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "Astronaut riding a bicycle in the beach",
})

# You can access the image with PIL.Image for example
import io
from PIL import Image

image = Image.open(io.BytesIO(image_bytes))

def generate(text:str)->str:

    try:
	
        payload = {
            "inputs" : text
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        image_bytes = response.content
        image_bytes= base64.b64decode(image_bytes).decode("utf-8")

        return image_bytes

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
	
	
