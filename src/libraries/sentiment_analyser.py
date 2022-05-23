import pickle

class GroupSentimentAnalyser():

    @classmethod
    def find_sentiment(cls,data):
        model_filename = "Sentiment classifier.sav"

        my_knn_model = pickle.load(open(model_filename, 'rb')) # the model will be read into the object my_knn_model 
                                                            # and you can use the same model to predict the new data.

        result = my_knn_model.predict(data) # X_test is where the new data that is to be predicted is inserted, 
                                            # here X_test is a part of dataset 
 

        if result:
            return result
        return "Not detected"