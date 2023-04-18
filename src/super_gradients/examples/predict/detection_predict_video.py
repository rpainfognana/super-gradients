import requests
from super_gradients.common.object_names import Models
from super_gradients.training import models

# Note that currently only YoloX and PPYoloE are supported.
model = models.get(Models.YOLOX_N, pretrained_weights="coco")
model = model.to("cuda")

video_path = "pose_elephant_flip.mp4"

with open(video_path, mode="wb") as f:
    response = requests.get("https://deci-pretrained-models.s3.amazonaws.com/sample_images/pose_elephant_flip.mp4")
    f.write(response.content)

predictions = model.predict(video_path)
predictions.show()