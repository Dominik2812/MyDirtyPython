# Pearl_Chain methode to detect circular objects in an image
rapid method to find circlular objects on an image

## basic mechanism
The code scans the image horizontally from top to bottom. To accalerate the code it is sufficient to consider each 5th or 10th pixel (can be tuned by adjusting 'jump'). If pixel intensity exceed a certain threshold, a line is drawn (see result images with the ending Bulk)
The center of those horizontal lines is calculated. Subsequentially the Centers are grouped by circles and color-coded; THEY line up to a pearlchain within the circles. Pearl chains as well as centers and lines are depicted into the different output images.
Radius and center of the circles is then determined by the length and positon of the pearl_chain and printed out in the terminal. 

## When to apply?
This code is rapid, precise and reliable over a large span of size distibution (see ... ![Output Image_1](output_1_single_circles_pearlchain.jpg?raw=true "Output Image_1")). 

## When it fails?
The circlular objects may however not overlap (see ... ![Output Image_2](output_2_overlapping_circles_pearlchain.jpg?raw=true "Output Image_2")).

## Installation
You need Python >= 3.6 installed on your sytem. To install the required packages, run ...
```
pip install -r requirements.txt
```

## Run pearl_chain code

To start circluar object detection run ....
```
pearl_chain_code.py
```
