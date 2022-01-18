from magicgui import magicgui
import napari
from napari.types import LabelsData, ImageData

from skimage.io import imread
import nibabel as nib
import numpy as np

@magicgui(call_button='Run Segmentation')
def threshold_segmentation() -> LabelsData:
    """Returns the output label."""
    labels = viewer.layers[1].data
    return labels


with napari.gui_qt():
    img = nib.load('./data/mni152_nonlinear_sym.nii.gz').get_fdata()
    
    viewer = napari.Viewer()
    viewer.add_image(img)
    viewer.add_labels(np.zeros(img.shape, 'uint8'))

    viewer.window.add_dock_widget(threshold_segmentation)
    
    # threshold()

