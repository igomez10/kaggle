kaggle competitions download -c titanic
unzip titanic.zip
rm titanic.zip

# create virtual environment called titanic
python3 -m venv titanic-env

# activate the virtual environment
source titanic-env/bin/activate

# install the required packages
# install pandas
pip install pandas


# install xgboost
pip install xgboost

# install sklearn
pip install scikit-learn
