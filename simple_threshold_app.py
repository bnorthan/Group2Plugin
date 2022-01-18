from magicgui import magicgui
import napari
from napari.types import LabelsData, ImageData

from skimage.io import imread


@magicgui(call_button='Run Threshold',
          threshold={"widget_type": "Slider", "min": 0, "max": 255},
)
def threshold_segmentation(img: ImageData, threshold: int = 100) -> LabelsData:
    """Threshold an image and return a mask."""
    print(f'threshold = {threshold}')
    labels = (img >= threshold).astype(int)
    print(f'min: {labels.min()}, max = {labels.max()}')
    print(f'labels.shape: {labels.shape}, img.shape = {img.shape}')
    return labels


with napari.gui_qt():
    img = imread('./data/brain_snapshot.png')
    
    viewer = napari.Viewer()
    viewer.add_image(img)

    viewer.window.add_dock_widget(threshold_segmentation)
    # threshold()

def update_slider(event):
    # only trigger if update comes from first axis (optional)
    if event.axis == 0:
        ind_lambda = viewer.dims.indices[0]
        stokes_1d.plot(None, ind_lambda, plot_stokes=False)

viewer.dims.events.axis.connect(update_slider)