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

## note on running code 
Run scripts by making the file executable (chmod+x script.sh) and then running with ./script.sh.
Avoid using sh script.sh as it uses a different shell in Ubuntu and can cause issues.

## Data Collection

### laptop_collector
Tested on:
- Framework 13 laptop running Fedora 42

This program is designed to run on a laptop and take images with a built in web cam.
I've noted that it continues to run even when the screen locks, and if the web cam light is lit up that means the program is running.

### server
Tested on :
- Nvidia 4000 ADA 

This is the server program. It is meant to run somewhere with a Nivida graphics card.
I tested it on a desktop running Fedora 42 with a Nvidia 4000 Ada.

It is very light weight and takes about 30ms (self reported) to process a image.

It's main purpose is to receive images from the client program, detect a cat in them, 
and save the images that have a cat in them.

I've found that the current model works very well at detecting my cats, even in poor lighting.

## Data Preprocessing

### filter_humans
Tested on :
- Nvidia 4000 ADA 
- Nvidia DGX Spark

This script checks through a folder of images and sorts folders based on whether a human 
is detected. This could have been done as part of collection, but this way I get to view 
what I'm filtering out and make the choice myself.

In my testing the nano model is quite good at detecting humans but not perfect. Out of 250 images it detected humans in there were a couple that were just cats, so you will want to 
manually check what it is matching.

### identify_duplicates
This is to be done. the data_collection programs result in a large amount of near 
duplicate images when a cat doesn't move and triggers a series of photos. These need 
to be identified and filtered out.

## current status
see change_log.txt for more details


![screenshot](/readme_images/building_cat_dataset.png "Building cat dataset")


