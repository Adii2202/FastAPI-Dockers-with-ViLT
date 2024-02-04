from transformers import ViltProcessor, ViltForQuestionAnswering
# import requests
from PIL import Image

# 470MB
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

# prepare image + question
# url = "http://images.cocodataset.org/val2017/000000039769.jpg"
# image = Image.open(requests.get(url, stream=True).raw)

text = "What are the cats doing?"

def model_pipeline(text : str, image: Image):
    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")
    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    return model.config.id2label[idx]
