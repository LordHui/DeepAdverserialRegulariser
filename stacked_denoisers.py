from iterative_denoising import stacked_denoiser

sd = stacked_denoiser(2)
# sd.train_layer(1, 500)
sd.independant_layer(1, 3)
sd.independant_layer(1, 5)
sd.independant_layer(1, 10)
sd.independant_layer(1, 20)