# Foresite

This repository contains a website that allows users to upload csv data of weekly website traffic and obtain a seven day forecast of their web traffic in the future.  This project utilizes an LSTM neural network automation program to process the data and output the result back through the website interface

## Setup/Installation

### Prerequisites

* Python 3.6 or a later version
* Keras: https://keras.io/
    * Follow Theano installation instructions
* Install Python modules below through Anaconda:
    * pandas
    * sqlite3
    * matplotlib
    * Django version 2.1.1

### Running the program

Before running this program, you must create a file called secret_settings.py and place it within the Foresite/foresite directory.  Within this file, write the line below into the file and save it:

secret_key = 'anything'

This key is used to hash the passwords entered in by the users on the website.  Afterwards, navigate to the Foresite folder.  Once you are in that directory, type into the command prompt:

    python manage.py makemigrations
    python manage.py migrate

This sets up the database of the website locally.  Once you do that, open up the Anaconda console and run the lstm_automation_program.py (Note you may have to change the backend of keras from Tensorflow to Theano before running this: https://keras.io/backend/).  Once you run the program, it will be indefinitely be querying the local sqlite database for certain information.  Now navigate to the Foresite directory in command prompt (Not anaconda) and run this command below:

python manage.py runserver

From there you should now be able to access the webpage locally through this link:

http://127.0.0.1:8000/

From here, click on the sign-up tab at the top right.  You will now create an account through the sign-up page.  Once entered in, click on log-in and enter in your password and username.  You should now be logged in.  Type the following url at the top now:

http://127.0.0.1:8000/upload_csv/

You can now upload a csv file, however it must have a specific format.  The format is specified below:

website_traffic_number, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

Depending on what day you get the website_traffic_number, you must set the values of monday-sunday accordingly (i.e.  if the data took pkace on a Tuesday, the data would look like this: number, 0, 1, 0, 0, 0, 0, 0).  Upload the csv and type in the name of the file into the top portion exactly the same, but without the file extension.  Once uploaded, the lstm_automation_program.py should see it and start to process the data.  Now navigate to the link:

http://127.0.0.1:8000/processed_data/

You should see your data being processed.  Once the webpage displays that it is ready, click on the name.  It should now display a seven day forecast with a graph at the bottom.
