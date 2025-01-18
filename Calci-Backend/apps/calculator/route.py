from fastapi import APIRouter
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
async def run(data: ImageData):
    try:
        # Decode base64 image
        image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
        image_bytes = BytesIO(image_data)
        image = Image.open(image_bytes)
        
        # Analyze image
        responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
        data_list = []  # Renamed to avoid overwriting the `data` parameter
        
        for response in responses:
            data_list.append(response)  # Safely collect responses

        # If `responses` is empty, avoid referencing `response`
        if not responses:
            return {
                "message": "No data found in the image",
                "data": data_list,
                "type": "success"
            }

        print('response in route: ', responses[-1])  # Print the last response
        return {
            "message": "Image processed",
            "data": data_list,
            "type": "success"
        }

    except Exception as e:
        print(f"Error: {e}")
        return {"message": "An error occurred", "type": "error", "details": str(e)}
