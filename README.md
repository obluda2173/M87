# M87 image construction




## TOC
- [How (U, V) coordinates relate to spatial frequencies of the image](#how-u-v-coordinates-relate-to-spatial-frequencies-of-the-image)
- [Why the Fourier Transform is needed to reconstruct the image](#why-the-fourier-transform-is-needed-to-reconstruct-the-image)
- [What challenges arise from missing data (sparse UV coverage)](#what-challenges-arise-from-missing-data-sparse-uv-coverage)


## How (U, V) coordinates relate to spatial frequencies of the image.

In image processing and Fourier analysis, the (U, V) coordinates represent the **spatial frequency domain** of an image. When we take the **Fourier Transform** of an image, we convert it from the **spatial domain** (regular images that you can imagine) into the **frequency domain** (how patterns change across the image).

### 1. What Are (U, V) Coordinates
* In the **spatial domain**, an image is defined by pixel locations (x, y).
* In the **frequency domain**, the transformed image is defined by (U, V) coordinates, which represent **spatial frequencies**.
* These coordinates tell us how fast the intensity (brightness) changes in different directions.

### 2. What Do Spatial Frequencies Mean
* **Low frequencies (small U, V values)** -> Represent **smooth areas** with gradual changes (like a sky in an image).
* **High frequencies (high U, V values)** -> Represent **sharp details**, edges, and noises (like a sharp rest or texture). 

| Frequency Type | Effect on Image |
|---|---|
| **Low U, V values** (centre of Fourier domain) | Represents smooth regions and smooth shape |
| **High U, V values** (edges of Fourier domain) | Represent fine details, sharp edges, and noise |


### 3. Where Are (U, V) Coordinates in the Fourier Transform
When we compute the **2D Fourier Transform** of an image, we get a frequency representation where:

* The **centre of the transformed image (U = 0, V = 0)** contains the **low-frequency components** (global brightness).
* As we move outwards from the centre, we encounter **higher frequencies** that represent finer details.
* The **corners of the Fourier-transformed image** correspond to the highest frequencies, which capture rapid intensity changes.

To make it easier to visualise, we usually shift the Fourier Transform so that the (U=0, V=0) low frequency are at the centre (this is done using fftshift NumPy)

### 4. How Are U and V Related to Image Size
The spatial frequency values (U, V) depend on the image dimensions:

<img src="https://latex.codecogs.com/gif.latex?U=\frac{k_{x}}{W},"> <img src="https://latex.codecogs.com/gif.latex?V=\frac{k_{y}}{H}">

where :
* kx, ky are the indices in the Fourier-transformed image.
* W, H are the width and height of the original image.

This means:
* Larger images have finer frequency resolutions in the (U, V) domain.
* Smaller images have coarser frequency resolution since they contain fewer samples.



## Why the Fourier Transform is needed to reconstruct the image?

The image of the M87* black hole wasn't taken like a normal photo. Instead, it was reconstructed from radio waves collected by the telescope around the world. The Fourier Transform (FT) was essential for this process because it allowed scientists to convert scattered data into a visual image.

### 1. The Problem: Telescopes Can't Directly "See" the Black Holes
* The M87* is a 53 million light-years away and increadibly small in the sky.
* No single telescope on Earth is powerful enough to take a direct photo of it.

**Solution:** Use **Very Long Baseline Interferomentry (VLBI)** to combine multiple telescopes into a "visual Earth-sized telescope"

### 2. How Fourier Transform Helps in VLBI
* The radio telescopes don't capture an image directly. Instead, they record **radio wave signals** arriving at different locations.
* These signals are related to the **spatial frequencies** of the black hole's image.
* The Fourier Transform translates these frequency data points into an actual image.

Think of it like:
* The **black hole image** is in **spatial domain** (regular image).
* The **telescopes measure radio waves** in the **frequency domain** (like scattered musical notes).
* The **Fourier Transform converts** the frequency domain data **back into an image**.

### 3. Why the Fourier Transform Is Critical
* **Fills in missign data** -> Since telescope can't cover every point on Earth, the Fourier Transform helps reconstruct missing information.
* **Turns frequency data into an image** -> Without FT, we'd just have meaningless signals.
* **Shrpens resolution** -> By using more telescope data, Fourier techniques improve clarity.

### 4. Final Image Reconstruction
After applying the Fourier Transform, scientists use **image processing algorithms** to refine the details. This is why the famous M87* image looks blurry but still shows the key structure of the black hole (a glowring ring and central shadow).


## What challenges arise from missing data (sparse UV coverage)



**Basics of VLBI and Radio Interferometry** -> [link](https://eventhorizontelescope.org/science)

**Spatial domain image to Frequency domain image (Fourier Transformation)** -> [link](https://matlabhelper.com/blog/matlab/how-to-convert-images-from-spatial-domain-to-frequency-domain/)