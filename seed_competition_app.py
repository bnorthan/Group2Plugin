from magicgui import magicgui
import napari
from napari.types import LabelsData, ImageData

from skimage.io import imread
import nibabel as nib
import numpy as np

def segmentation_function(img, annotation):
    labels = annotation
    return labels


@magicgui(call_button='Run Segmentation')
def segmentation_panel() -> LabelsData:
    """Returns the output label."""
    
    labels = segmentation_function(img, viewer.layers[1].data)
    
    return labels


with napari.gui_qt():
    img = imread('./data/brain_snapshot.png')
    
    viewer = napari.Viewer()
    viewer.add_image(img)
    viewer.add_labels(np.zeros(img.shape, 'uint8'))
    
    viewer.window.add_dock_widget(segmentation_panel)

