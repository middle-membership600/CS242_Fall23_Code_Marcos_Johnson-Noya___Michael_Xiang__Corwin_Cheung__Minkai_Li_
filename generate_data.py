import requests
import json

url = "https://stablediffusionapi.com/api/v3/text2img"

payload = json.dumps({
    "key": "YOUR KEY HERE",
    "prompt": "a picture of an airplane",
    "negative_prompt": None,
    "width": "512",
    "height": "512",
    "samples": "100",
    "num_inference_steps": "10",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
})

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

folder_name = 'airplane'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Parse the response
data = response.json()

if 'images' in data:
    for i, img_url in enumerate(data['images']):
        image_response = requests.get(img_url)

        if image_response.status_code == 200:
            with open(os.path.join(folder_name, f'airplane_{i}.jpg'), 'wb') as file:
                file.write(image_response.content)
        else:
            print(f"Failed to download image {i}")
else:
    print("No images found in the response.")
