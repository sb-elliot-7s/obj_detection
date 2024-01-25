import uvicorn
from fastapi import FastAPI, status, UploadFile
from ultralytics import YOLO

from detect import DetectObject

app = FastAPI(title='Object Detection')
model = YOLO("yolov8n.pt")


@app.get(path='/', status_code=status.HTTP_200_OK)
async def home() -> dict:
    return {'detail': 'home'}


@app.post(path='/detect', status_code=status.HTTP_201_CREATED)
async def detect(file: UploadFile):
    image_bytes = await file.read()
    results = DetectObject(model=model).detect(image_bytes=image_bytes)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
