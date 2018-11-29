import numpy
import theano
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
from keras.models import load_model
from keras.models import Sequential


def configure_single_layer(input_data_dim, output_data_dim, neuron_count):
    batch_size = 1
    timestep = 1
    model = Sequential([
        LSTM(
            neuron_count,
            batch_input_shape=(batch_size, timestep, input_data_dim),
            return_sequences=False, unit_forget_bias=True,
            kernel_initializer='glorot_uniform'),
        Dropout(0.05),
        Dense(output_data_dim, activation='sigmoid'),
    ])
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    return model


def configure_double_layer(input_data_dim, output_data_dim, neuron_count):
    batch_size = 1
    timestep = 1
    model = Sequential([
        LSTM(
            neuron_count,
            batch_input_shape=(batch_size, timestep, input_data_dim),
            return_sequences=True, unit_forget_bias=True,
            kernel_initializer='glorot_uniform'),
        Dropout(0.90),
        LSTM(
            neuron_count, return_sequences=False,
            unit_forget_bias=True, kernel_initializer='glorot_uniform'),
        Dropout(0.60),
        Dense(output_data_dim, activation='sigmoid'),
    ])

    model.compile(loss='mean_squared_error', optimizer='adam',
                  metrics=['accuracy'])
    return model


def select_features(impressions, features, window_size, forecast_length):
    x_data, y_data = [], []
    for i in range(len(impressions)-window_size-forecast_length-1):
        x_data.append(numpy.append(impressions[i:(i+window_size), 0],
                                   features[(i+window_size)]))
        y_data.append(
            impressions[(i+window_size):(i+window_size+forecast_length), 0])

    # reshapes dataX to be a 3D array.  Necessary for the input of the LSTM
    x_data = numpy.array(x_data)
    x_data = numpy.reshape(x_data, (x_data.shape[0], 1, x_data.shape[1]))
    y_data = numpy.array(y_data)

    return x_data, y_data


def train_model(x_data, y_data, model, model_name, epoch_number):

    checkpoint = ModelCheckpoint(model_name, monitor='val_acc', verbose=1,
                                 save_best_only=True, mode='max')
    callback_list = [checkpoint]
    # EarlyStopping(monitor='val_acc', patience=30),

    model.fit(x_data, y_data, epochs=epoch_number, callbacks=callback_list, batch_size=1, verbose=2,
              shuffle=False, validation_split=0.33)

    # model2 = load_model(model_name)
    return model


def main():
    print("LSTM Neural Network module")


if __name__ == '__main__':
    main()
