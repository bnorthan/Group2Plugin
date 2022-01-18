from magicgui import magicgui
import napari
from napari.types import  ImageData, LabelsData, LayerDataTuple

import numpy as np
import nibabel as nib
from skimage.io import imread
import nibabel as nib
import numpy as np

from pyift.shortestpath import seed_competition


@magicgui(call_button='Run Segmentation')
def segment_by_seed_competition(img: ImageData, markers: LabelsData) -> LayerDataTuple:
    ### we are considering that:
    # gray 2D image = (width, height)
    # color 2D image = (width, height, n_channels=3)
    # 3D image = (width, height, slices)
    is_3D = (img.ndim == 3) and (img.shape[-1] > 3)
    print(f'Is a 3D image: {is_3D}')

    print('#### Running Segmentation by IFT Seed Competition')
    _, _, _, labels, = seed_competition(markers, img, image_3d=is_3D)

    # remove background
    labels[labels == 1] = 0

    print(f'labels.shape = {labels.shape}')
    print(f'labels.min() = {labels.min()}')
    print(f'labels.max() = {labels.max()}')


    return (labels, {'name': 'labels'}, 'labels')

with napari.gui_qt():
    img = nib.load('./data/healthy_1.nii.gz').get_fdata().astype(np.int)

    viewer = napari.Viewer()
    viewer.add_image(img, name='image')

    blank = np.zeros(img.shape, dtype=img.dtype)
    viewer.add_labels(blank, name='markers', opacity=0.75)

    viewer.window.add_dock_widget(segment_by_seed_competition)
