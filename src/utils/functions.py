"""
functions.py

Author: Lander Combarro Exposito
Created: 2025/05/17
Last Modified: 2025/05/17

Description
-----------
This module provides a collection of utility functions for loading, processing, and visualizing 
image datasets, especially useful in deep learning and computer vision workflows.
"""

import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread


def read_data(path, reshape_dim=(32, 32)):
    """
    Reads images from a directory structure and returns the data and labels.

    Parameters
    ----------
    path : str
        Path to the root directory. It should contain one subdirectory per class,
        each with its corresponding images.
    reshape_dim : tuple of int, optional
        Dimensions to resize each image to. Default is (32, 32).

    Returns
    -------
    X : np.ndarray
        Array of image data, resized to `reshape_dim`.
    y : np.ndarray
        Array of labels corresponding to each image, derived from folder names.

    Notes
    -----
    - Assumes that each subdirectory of `path` is a class label.
    - Uses `cv2.resize` for resizing and `imread` for reading images.
    """
    X = []
    y = []
    for folder in os.listdir(path):
        print(folder)
        if os.path.isdir('/'.join([path, folder])):
            for file in os.listdir('/'.join([path, folder])):

                image = imread('/'.join([path, folder, file]))
                # Redimensionamos las imágenes a 32x32
                image = cv2.resize(image, reshape_dim) 

                X.append(image)
                y.append(folder)

    return np.array(X), np.array(y)


def show_images_batch(images, titles=[], n_cols=5, size_scale=2, cmap="Greys"):
    """
    Displays a batch of images in a grid layout using matplotlib.

    Parameters
    ----------
    images : list or array-like
        A list or array containing image data to be displayed. Each element
        should be an individual image (2D or 3D array depending on the image type).
    
    titles : list, optional (default=[])
        A list of titles for each image. If provided, each image will be displayed
        with its corresponding title. The length of this list should match the
        number of images. If no titles are provided, no titles will be shown.
    
    n_cols : int, optional (default=5)
        The number of columns in the grid. This determines how many images will
        be displayed per row. The total number of rows will be computed automatically.
    
    size_scale : float, optional (default=2)
        Scaling factor for the size of the images. Larger values will increase the
        size of each individual image in the grid.
    
    cmap : str, optional (default='Greys')
        The color map to use when displaying the images. Useful when showing grayscale
        images. You can change it to other colormaps like 'viridis', 'plasma', etc.
    
    Returns
    -------
    None
        This function displays a plot of the images but does not return any values.

    Examples
    --------
    >>> show_images_batch([image1, image2, image3], titles=['Image 1', 'Image 2', 'Image 3'], n_cols=3)
    """
    
    n_rows = (len(images) - 1) // n_cols + 1
    plt.figure(figsize=(n_cols * size_scale, n_rows * 1.1 * size_scale))
    
    for index, image in enumerate(images):
        plt.subplot(n_rows, n_cols, index + 1)
        plt.imshow(image, cmap=cmap)
        plt.axis("off")
        if len(titles):
            plt.title(titles[index])
    plt.show()
