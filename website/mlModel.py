from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import json
import urllib2


class mlModel:
    
    def __init__(self):
        url = 'https://data.seattle.gov/resource/ym38-yn4a.json?$LIMIT=10000'
        df = pd.read_json(url)
        data = df[['latitude', 'longitude', 'summarized_offense_description']]
        data.columns = ['lat', 'long', 'crime']
        X = data[['lat', 'long']].values
        y = data['crime'].values

        X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0)

        sc = StandardScaler()
        sc.fit(X_train)
        X_train_std = sc.transform(X_train)
        X_test_std = sc.transform(X_test)

        knn = KNeighborsClassifier(n_neighbors=10, weights = 'distance', n_jobs = -1)
        knn.fit(X_train_std, y_train)

        y_pred = knn.predict(X_test_std)   

        self.model = knn
        self.score = accuracy_score(y_test, y_pred)

    def predict(self, latitude, longitude):
        return self.model.predict([latitude, longitude])[0]

