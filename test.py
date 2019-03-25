from keras.models import load_model
from keras.utils.vis_utils import plot_model

model = load_model('41524_2018_86_MOESM3_ESM.h5')
print(model.summary())

plot_model(model, to_file = 'ebeam.png', show_shapes = True, show_layer_names = True)

