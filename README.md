# Multi-Class GARBAGE CLASSIFIER (CNN)

Waste sorting is the process by which waste is separated into different elements. Waste sorting can occur manually at the household and collected through curbside collection schemes, or automatically separated in materials recovery facilities or mechanical biological treatment systems.seperation of garbage have been a major issue of the 21st century.In this project using CNN we have created a waste sorting system that is trained to recognise the image and sort the waste as per its category.

## DATA:
The Garbage Classification Dataset contains 6 classifications: cardboard (393), glass (491), metal (400), paper(584), plastic (472) and trash(127).

## How to run:
Libraries needed :
Werkzeug
numpy
keras_nightly
Flask
keras
tensorflow

Fire up CMD > After cd to the desired folder > run this command > git clone {my git repo link} 

## ABOUT THE MODEL
After multiple trial and error we developed a 10 layer CNN model.

## Evaluating the model :
After training our model for 30 epocs the accuracy comes to 0.9980 which is pretty amazing.This should mostly be because of the size of our data which is pretty small.Cnn is a very data hungry model but as we were getting a very high accuracy, we did not augment our data.

