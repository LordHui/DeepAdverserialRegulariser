from iterative_denoising import stacked_denoiser

sd = stacked_denoiser(2)
# sd.train_layer(1, 50)
sd.independant_layer(1, 1)
sd.independant_layer(1, 3)
sd.independant_layer(1, 5)
sd.independant_layer(1, 10)
