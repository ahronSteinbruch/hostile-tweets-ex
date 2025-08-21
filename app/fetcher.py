import os
import pandas as pd
from pymongo import MongoClient


class DataFetcher:
    """
    return data from MongoDB atlas
    """

    def __init__(self):
        """
        reaset connection to MongoDB
        yse os.getenv("MONGO_CONNECTION_STRING")
        from secret
        """
        connection_string = "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"
        #connection_string = os.getenv("MONGO_CONNECTION_STRING")
        if not connection_string:
            raise ValueError("'MONGO_CONNECTION_STRING' is not set.")

        try:
            self.client = MongoClient(connection_string)
            self.db = self.client['IranMalDB']
            self.collection = self.db['tweets']
            print("connected to MongoDB")
        except Exception as e:
            print(f"error in connection to -MongoDB: {e}")
            self.client = None

    def get_all_records(self):
        """
        return all records
        """
        if not self.client:
            print("no connection")
            return pd.DataFrame()  # return an empty DataFrame

        try:
            records_cursor = self.collection.find({})
            records_list = list(records_cursor)

            # cast _id to string
            for record in records_list:
                record['id'] = str(record['_id'])
                del record['_id']

            # change Text to original_text
            df = pd.DataFrame(records_list)
            if 'Text' in df.columns:
                df.rename(columns={'Text': 'original_text'}, inplace=True)
            return df

        except Exception as e:
            print(f"error accurd in get_all_records: {e}")
            return pd.DataFrame()

