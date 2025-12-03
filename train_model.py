# train_model.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(3, activation='softmax')  # 3 jest
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train = datagen.flow_from_directory('dataset', target_size=(64,64), batch_size=16, class_mode='categorical', subset='training')
val = datagen.flow_from_directory('dataset', target_size=(64,64), batch_size=16, class_mode='categorical', subset='validation')

model.fit(train, validation_data=val, epochs=10)
model.save("model/gesture_model.h5")
