from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

# Load the saved Keras model
model = load_model('my_model.keras')
def testing_image(image_directory):
    test_image = image.load_img(image_directory, target_size = (224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image/255
    result = model.predict(x= test_image)
    print(result)
    if np.argmax(result)  == 0:
      prediction = 'Bread'
    elif np.argmax(result)  == 1:
      prediction = 'Dairyproduct'
    elif np.argmax(result)  == 2:
      prediction ='Dessert'
    elif np.argmax(result)  == 3:
      prediction ='Egg'
    elif np.argmax(result)  == 4:
      prediction ='Friedfood'
    elif np.argmax(result)  == 5:
      prediction ='Meat'
    elif np.argmax(result)  == 6:
      prediction ='Noodles-Pasta'
    elif np.argmax(result)  == 7:
      prediction ='Rice'
    elif np.argmax(result)  == 8:
      prediction ='Seafood'
    print( prediction)


print(testing_image(r'E:\abhi project\evaluation\Bread\15.jpg'))

