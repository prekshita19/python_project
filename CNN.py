# importing Libraries
from keras.layers import Convolution2D
from keras.layers import Conv2D
from keras.models import Sequential
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
# Intializing the CNN
classifier=Sequential()

# Step-1 Convolution 
classifier.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation="relu"))

# Step-2 Pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))

# Adding a second convolution layer
classifier.add(Convolution2D(32,3,3,activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2,2)))

# Step-3
classifier.add(Flatten())

# Step-4 Full Connection
classifier.add(Dense(units=128,activation="relu"))
classifier.add(Dense(units=1,activation="sigmoid"))

# Compiling CNN 
classifier.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])

from keras.preprocessing.image import ImageDataGenerator

# We generate more images from the datasets
train_datagen=ImageDataGenerator(rescale=1./255,
                                 shear_range=0.2,
                                 zoom_range=0.2,
                                 horizontal_flip="binary")
test_datagen=ImageDataGenerator(rescale=1./255)

training_set=train_datagen.flow_from_directory("C:/Users/Fly-Emirates/Dropbox/Tops/Machine Learning/CNN/dataset/training_set",
                                               target_size=(64,64),
                                               batch_size=32,
                                               class_mode="binary")

test_set=test_datagen.flow_from_directory("C:/Users/Fly-Emirates/Dropbox/Tops/Machine Learning/CNN/dataset/test_set",
                                               target_size=(64,64),
                                               batch_size=32,
                                               class_mode="binary")


classifier.fit_generator(training_set,
                         samples_per_epoch=8000,
                         nb_epoch=2,
                         validation_data=test_set,
                         nb_val_samples=2000)