## Overview
It's a bird? It's a plane? It's superman? Humans develop the ability to recognize objects by their spacial features at a very young age. It is one of humankinds' skills taken for granted, but it provides unquantified utility in our everyday lives. Circa 1970, scientists began to experiment around a new field known as 'computer vision.' As implied by the name, the goal is to impart the ability to gather useful information from visual stimuli to a processor. In this project I examined an algorithm known as a convolutional neural network, which is a type of artificial neural network. I applied the algorithm to an art collection called the 'Tate Collection' to gather information about the artworks and to observe the algorithm's performance.

## What is an artificial neural network?
The human brain consists of billions of highly interconnected brain cells working in parallel. The goal of an artificial neural network is to provide a viable software simulation of the process by which the brain synthesizes information to the end of procuring new insight. An artificial neural network is constructed by three classes of 'layers.' They are the input layer (information given to the algorithm), one or more hidden layers (analytic processes), and the output layer (information provided by the algorithm). 

## What is a convolutional neural network?
Computation in an artificial neural network largely occurs in the hidden layers. A particular instance of an artificial network used for image processing is known as the convolutional neural network. It gets its name from a type of layer within known as the convolutional layer. Simply put, a 'filter' or specific quality of an image is systematically 'dotted' over the 2 dimensional image producing a 'feature map' to be further analyzed, or even convolved over again. The beauty of the convolutional neural network is that the computer synthetically 'learns' the best filters to be used, wheras previously filters where hand-crafted. The computer updates the filters via 'backpropogation', whereby the algorithm's weights (or filters in the case of a convolutional layer) are reinforced or punished according to distance from the target. In our case the target is the classification of artwork.

## The Tate Collection
The art to be classified was aggregated from the Tate Collection. The Tate Collection is a massive collection of British artwork and both modern and contemporary international works. It includes information about artworks and artists. Essentially, getting the data into 'neural network' (via Tensorflow) condition involved downloading and consolidating the images into folders based upon the intended class. Amazon Web Service's EC2 GPU was utilized to efficiently and programatically download the images into the appropriate directories. 

## Classifying by Artist


## Classifying by Male/Female label

## Takeaways/ Future Work

