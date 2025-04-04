# M87 image construction

**Basics of VLBI and Radio Interferometry**

[link](https://eventhorizontelescope.org/science)

**Spatial domain image to Frequency domain image (Fourier Transformation)**

[link](https://matlabhelper.com/blog/matlab/how-to-convert-images-from-spatial-domain-to-frequency-domain/)

Key concepts to understand:
* How (U, V) coordinates relate to spatial frequencies of the image.
* Why the Fourier Transform is needed to reconstruct the image.
* What challenges arise from missing data (sparse UV coverage).

### How (U, V) coordinates relate to spatial frequencies of the image.
In image processing and Fourier analysis, the (U, V) coordinates represent the **spatial frequency domain** of an image. When we take the **Fourier Transform** of an image, we convert it from the **spatial domain** (regular images that you can imagine) into the **frequency domain** (how patterns change across the image).

### 1. What Are (U, V) Coordinates?
* In the **spatial domain**, an image is defined by pixel locations (x, y).
* In the **frequency domain**, the transformed image is defined by (U, V) coordinates, which represent **spatial frequencies**.
* These coordinates tell us how fast the intensity (brightness) changes in different directions.

### 2. What Do Spatial Frequencies Mean?
* **Low frequencies (small U, V values)** -> Represent **smooth areas** with gradual changes (like a sky in an image).
* **High frequencies (high U, V values)** -> Represent **sharp details**, edges, and noises (like a sharp rest or texture). 

| Frequency Type | Effect on Image |
|---|---|
| **Low U, V values** (centre of Fourier domain) | Represents smooth regions and smooth shape |
| **High U, V values** (edges of Fourier domain) | Represent fine details, sharp edges, and noise |


### 3. Where Are (U, V) Coordinates in the Fourier Transform?
When we compute the **2D Fourier Transform** of an image, we get a frequency representation where:

* The **centre of the transformed image (U = 0, V = 0)** contains the **low-frequency components** (global brightness).
* As we move outwards from the centre, we encounter **higher frequencies** that represent finer details.
* The **corners of the Fourier-transformed image** correspond to the highest frequencies, which capture rapid intensity changes.

To make it easier to visualise, we usually shift the Fourier Transform so that the (U=0, V=0) low frequency are at the centre (this is done using fftshift NumPy)

### 4. How Are U and V Related to Image Size?
The spatial frequency values (U, V) depend on the image dimensions:

<img src="https://latex.codecogs.com/gif.latex?U=\frac{k_{x}}{W},"> <img src="https://latex.codecogs.com/gif.latex?V=\frac{k_{y}}{H}">

where :
* kx, ky are the indices in the Fourier-transformed image.
* W, H are the width and height of the original image.

This means:
* Larger images have finer frequency resolutions in the (U, V) domain.
* Smaller images have coarser frequency resolution since they contain fewer samples.

