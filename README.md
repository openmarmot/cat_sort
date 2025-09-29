# cat_sort
identifying and sorting cat photos

## about
cat_sort is a continuation from a previous project, indoor_trail_cam, which explored using a LLM to identify my cat in webcam photos.
[indoor_trail_cam](https://github.com/openmarmot/indoor_trail_cam)

The indoor_trail_cam project was designed to take a photo with a webcam and then immediately classify it with a locally run LLM. I was using the IMP LLM which had worked great initially, but I struggled to get a newer version of it to work. I had intended to get the project running on a Raspberry Pi 5 but the memory requirements for IMP exceeded the PIs hardware. 

In the time since I stopped working on the original project I have adopted a pair of nearly identical black cats. Therefore I started this project
to continue the work of the previous project with the additional goal of trying to tell the cats apart with a LLM.

![screenshot](/readme_images/double_trouble.jpeg "Cat twins")

## objectives
Data Collection
- client app that takes images and sends them to a server
    - should run on a laptop
    - optionally create a version for the pi 
- server app that identifies images with cats and saves them
    - should support GPU compute and CPU compute 
- use the client/server app to create a data set of cat images

Data Labelling
- sort the data set into cat A and cat B
- create any tools necessary to help with data labelling  

Model Training
- train a model to identify the cats

## current status
see chang_log.txt for more details

just getting started


