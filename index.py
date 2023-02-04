import os
from google.cloud import vision

image_folder_path = "./image"
annotator_client = vision.ImageAnnotatorClient()

image_count = len(os.listdir(image_folder_path))
for i, filename in enumerate(os.listdir(image_folder_path)):
    file_path = os.path.join(image_folder_path, filename)
    with open(file_path,'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response_data = annotator_client.label_detection(image=image)
    labels = response_data.label_annotations
    
    print('---RESULT---')
    for label in labels:
        print(label.description,':',round(label.score * 100, 2),'%')

    print('---RESULT---')
    print('')

    if i < image_count - 1:
        print('next>>')

print('Finish')

