# Import Libraries
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout, add
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Extract Image Features using Pre-trained Model (VGG16)
base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.inputs, outputs=base_model.layers[-2].output)

def extract_features(image_path):
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    feature = model.predict(image, verbose=0)
    return feature

# Example captions
captions = [
    "startseq a dog playing with a ball endseq",
    "startseq a cat sitting on a sofa endseq",
    "startseq a man riding a horse endseq"
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(captions)
vocab_size = len(tokenizer.word_index) + 1
max_length = max(len(c.split()) for c in captions)

# Define the Model (CNN + LSTM)
inputs1 = Input(shape=(4096,))
fe1 = Dropout(0.5)(inputs1)
fe2 = Dense(256, activation='relu')(fe1)

inputs2 = Input(shape=(max_length,))
se1 = Embedding(vocab_size, 256, mask_zero=True)(inputs2)
se2 = Dropout(0.5)(se1)
se3 = LSTM(256)(se2)

decoder1 = add([fe2, se3])
decoder2 = Dense(256, activation='relu')(decoder1)
outputs = Dense(vocab_size, activation='softmax')(decoder2)

model_final = Model(inputs=[inputs1, inputs2], outputs=outputs)
model_final.compile(loss='categorical_crossentropy', optimizer='adam')

model_final.summary()

# Dummy Example (Skip Training for Now)
def generate_caption(photo_feature):
    return "a cat playing in the park"

# Test with an Example Image
image_path = "cat.jpg"  # Change this to your actual image path
photo = extract_features(image_path)
caption = generate_caption(photo)

img = Image.open(image_path)
plt.imshow(img)
plt.axis('off')
plt.title(caption)
plt.show()

print("Generated Caption:", caption)
