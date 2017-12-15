import AR_for_denoising as ar
import numpy as np

denoiser = ar.Denoiser1()

# testing sequence to check methods
if 0:
    denoiser.find_noise_level()
    denoiser.find_good_lambda()

    denoiser.evaluate_Network(0.5)
    denoiser.create_optimized_images(32)

    denoiser.pretrain_Wasser_ini(2)
    denoiser.train(2, 30)

# pretraining
if 0:
    denoiser.pretrain_Wasser_ini(2000)

# try out different regularisation parameters
if 1:
    denoiser.create_optimized_images(64, mu = 40)
    denoiser.create_optimized_images(64, mu=45)
    denoiser.create_optimized_images(64, mu=50)
    denoiser.create_optimized_images(64, mu=55)
    denoiser.create_optimized_images(64, mu=60)

# iterative training
if 0:
    denoiser.train(1000, 20)
