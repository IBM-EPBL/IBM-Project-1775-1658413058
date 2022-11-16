import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
print(f'model file path : {BASE_DIR}')



def predict_fruit(image_to_predict):
    
    image_data = f'{BASE_DIR.parent}{image_to_predict}'

    if image_to_predict != None:
        import numpy as np
        from tensorflow.keras.preprocessing import image
        from tensorflow.keras.models import load_model
        classes = ['APPLE', 'BANANA', 'ORANGE', 'PINEAPPLE', 'WATERMELON']

        new_model = load_model(os.path.join(BASE_DIR,'ai_models/binaries/nutrition.h5'))
        fruit_image = image.load_img(image_data, target_size=(64, 64))
        fruit_image = image.img_to_array(fruit_image)   
        fruit_image = np.expand_dims(fruit_image, axis=0)
        result = new_model.predict(fruit_image)
        return classes[np.argmax(result)]
        # result1 = result[0]
        # for i in range(6):
        #     if result1[i] == 1:
        #         print(classes[i])
        #         return classes[i]
        #     else: 
                # return 'No data for given image'
    return 'Please upload image'


