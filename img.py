import numpy as np
import matplotlib.pyplot as plt
# from tensorflow.keras.layers import Dense, Reshape, Flatten
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.optimizers import Adam
from tensorflow.python.keras.layers import Dense,Reshape,Flatten
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.optimizers import Adam
# Função para criar o gerador da GAN
def build_generator(latent_dim):
    model = Sequential()
    model.add(Dense(256, input_dim=latent_dim, activation='relu'))
    model.add(Dense(784, activation='sigmoid'))
    model.add(Reshape((28, 28, 1)))
    return model

# Função para criar o discriminador da GAN
def build_discriminator(img_shape):
    model = Sequential()
    model.add(Flatten(input_shape=img_shape))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    return model

# Função para compilar o modelo GAN
def build_gan(generator, discriminator):
    discriminator.trainable = False
    model = Sequential()
    model.add(generator)
    model.add(discriminator)
    model.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.0002, beta_1=0.5))
    return model

# Função para treinar a GAN
def train_gan(generator, discriminator, gan, X_train, latent_dim, epochs=10000, batch_size=128, sample_interval=1000):
    half_batch = int(batch_size / 2)

    for epoch in range(epochs):
        # Treinamento do discriminador
        idx = np.random.randint(0, X_train.shape[0], half_batch)
        imgs = X_train[idx]

        noise = np.random.normal(0, 1, (half_batch, latent_dim))
        gen_imgs = generator.predict(noise)

        d_loss_real = discriminator.train_on_batch(imgs, np.ones((half_batch, 1)))
        d_loss_fake = discriminator.train_on_batch(gen_imgs, np.zeros((half_batch, 1)))
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

        # Treinamento do gerador
        noise = np.random.normal(0, 1, (batch_size, latent_dim))
        valid_y = np.ones((batch_size, 1))

        g_loss = gan.train_on_batch(noise, valid_y)

        # Exibição do progresso
        if epoch % sample_interval == 0:
            print(f"{epoch} [D loss: {d_loss[0]}] [G loss: {g_loss}]")

# Carregamento de dados de exemplo (MNIST)
from tensorflow.keras.datasets import mnist

(X_train, _), (_, _) = mnist.load_data()

# Normalização dos dados para o intervalo [-1, 1]
X_train = (X_train.astype(np.float32) - 127.5) / 127.5
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)

latent_dim = 100

# Construção e compilação do modelo GAN
generator = build_generator(latent_dim)
discriminator = build_discriminator(X_train[0].shape)
gan = build_gan(generator, discriminator)

# Treinamento da GAN
train_gan(generator, discriminator, gan, X_train, latent_dim)