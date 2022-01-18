from magicgui import magicgui
import napari
from napari.types import LabelsData, ImageData

from skimage.io import imread
import nibabel as nib

@magicgui(call_button='Run Threshold',
          threshold={"widget_type": "Slider", "min": 0, "max": 4095},
)
def threshold_segmentation(img: ImageData, threshold: int = 1000) -> LabelsData:
    """Threshold an image and return a mask."""
    print(f'threshold = {threshold}')
    labels = (img >= threshold).astype(int)
    print(f'min: {labels.min()}, max = {labels.max()}')
    print(f'labels.shape: {labels.shape}, img.shape = {img.shape}')
    return labels


with napari.gui_qt():
    img = nib.load('./data/mni152_nonlinear_sym.nii.gz').get_fdata()
    
    viewer = napari.Viewer()
    viewer.add_image(img)

    viewer.window.add_dock_widget(threshold_segmentation)
    # threshold()

