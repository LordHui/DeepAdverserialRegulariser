from iterative_denoising import stacked_denoiser
from iterative_denoising import bregmann_denoiser


if 0:
    sd = stacked_denoiser(2, lmb=[44,5])
    # sd.train_layer(1, 50)
    sd.independant_layer(1, 1)
    sd.independant_layer(1, 3)
    sd.independant_layer(1, 5)
    sd.independant_layer(1, 10)

if 1:
    sd = bregmann_denoiser(2, lmb=[25, 25])
    sd.train_layer(0, 100)
    sd.independant_layer(1, 10)
    sd.independant_layer(1, 20)
    sd.independant_layer(1,30)