# opendailies
An open source framework for creating slated, versioned movie clips

Target users are VFX studios, possibly production companies. 

The Plan
========

Provide a tool that takes an image sequence or movie as input and:
    - adds a slate frame with text fields, thumbnails, logos, etc
    - adds an overlay with text fields, etc
    - optionally registers the current version in a [user provided] database 
    - transcodes to one or more file formats, image dimensions, color encodings
    - inserts metadata into the output file headers (eg timecode)  

Leverages OpenImageIO, OpenColorIO and FFMpeg. 
