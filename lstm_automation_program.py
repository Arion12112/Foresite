import os
import sqlite3
# import MySQLdb
os.environ["MKL_THREADING_LAYER"] = "GNU"

import numpy
import pandas
from matplotlib import pyplot
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

import lstm_neural_network

numpy.random.seed(7)
training_length_percentage = .75
minimum_seasonality = 7
scaler = MinMaxScaler(feature_range=(0, 1))
forecast_length = 7

while True:

    # Check database to see if CSV was uploaded
    csv_name = None
    while csv_name is None:
        conn = sqlite3.connect('Foresite/db.sqlite3')
        # conn = MySQLdb.connect(host="foresite-db.ce1e79fclwa2.us-west-1.rds.amazonaws.com",
        #                       user="PricelessAntonio", passwd="CMPE195BSeniorProject", db="foresitedb", port=3306)
        c = conn.cursor()

        c.execute('SELECT * FROM "upload_csv_csvupload" WHERE data_processed="0" ORDER BY timestamp ASC;')
        store_cursor = c.fetchone()
        if store_cursor is not None:
            csv_name = store_cursor[2]
            id = store_cursor[0]
        else:
            csv_name = None
        conn.close()

    # Remove file extension from csv_name
    full_csv_name = csv_name
    csv_name = os.path.splitext(csv_name)[0]

    # Find file path of CSV file
    csv_file_path = "media/" + csv_name + ".txt"

    model_path = "model.h5"

    processed_image_path = "csv_image/" + csv_name + ".png"
    processed_image_path_for_save = "Foresite/static/" + processed_image_path

    # Get length of CSV csv file
    csv_length = len(pandas.read_csv(csv_file_path)) + 1

    # Split 75% of csv for training and 25% for validation
    training_length = int(csv_length * training_length_percentage)

    # Check if CSV file is in correct format

    # LSTM program

    impressions = pandas.read_csv(csv_file_path, usecols=[0], header=None)
    impressions_data = impressions.values
    impressions_data = impressions_data.astype('float32')

    features = pandas.read_csv(csv_file_path, usecols=[1, 2, 3, 4, 5, 6, 7],
                               header=None)
    features_data = features.values
    features_data = features_data.astype('float32')

    transformed_impressions_data = scaler.fit_transform(impressions_data)

    print("Selecting features to train on\n")
    x_data, y_data = lstm_neural_network.select_features(
        transformed_impressions_data, features_data,
        minimum_seasonality,
        forecast_length)

    print("Configuring single layer LSTM neural network\n")
    model = lstm_neural_network.configure_single_layer(14, forecast_length, 28)

    print("Training model\n")
    model = lstm_neural_network.train_model(x_data[0:training_length, :, :],
                                            y_data[0:training_length, :],
                                            model, model_path, 50)

    print("Make prediction and display it\n")
    prediction = model.predict_on_batch(
        x_data[(training_length+1):(training_length+(csv_length-training_length)), :, :])
    prediction = scaler.inverse_transform(prediction)
    actual = scaler.inverse_transform(y_data)

    pyplot.title("Web Traffic Data")
    pyplot.xlabel("Number of days")
    pyplot.ylabel("Number of visitors")

    pyplot.plot(actual[training_length+6:(training_length +
                                          (csv_length-training_length)+6), 0], color='blue', label='actual')
    pyplot.plot(prediction[:, 6], color='red', label='prediction')
    pyplot.legend(loc='upper left')

    pyplot.savefig(processed_image_path_for_save, bbox_inches='tight')
    pyplot.close()

    conn = sqlite3.connect('Foresite/db.sqlite3')
    c = conn.cursor()
    params1 = (id, float(prediction[49][0]), float(prediction[49][1]), float(prediction[49][2]), float(
        prediction[49][3]), float(prediction[49][4]), float(prediction[49][5]), float(prediction[49][6]), processed_image_path)
    c.execute(
        'INSERT INTO "processed_data_processeddata" VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);', params1)

    params2 = (id, full_csv_name)
    c.execute('UPDATE "upload_csv_csvupload" SET data_processed="1" WHERE id=? AND csv_file=?;', params2)

    conn.commit()
    conn.close()
