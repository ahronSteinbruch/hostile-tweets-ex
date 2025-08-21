from fetcher import DataFetcher
from processor import DataProcessor


class AnalysisManager:
    """
    manage the analysis process and get the data
    """

    def __init__(self):
        self.fetcher = DataFetcher()
        self.processor = DataProcessor()
        self.processed_data = None

    def run_full_analysis(self):
        print("start fetching...")
        raw_data_df = self.fetcher.get_all_records()

        if raw_data_df.empty:
            print("the data is empty stop processing.")
            self.processed_data = []
            return

        print(f"נשלפו {len(raw_data_df)} start processing...")
        processed_df = self.processor.process_data(raw_data_df)

        final_columns = ['id', 'original_text', 'rarest_word', 'sentiment', 'weapons_detected']
        # check if all columns exist
        for col in final_columns:
            if col not in processed_df.columns:
                processed_df[col] = ""  # fill with empty string if missing

        final_df = processed_df[final_columns]

        # cast the json to dict
        self.processed_data = final_df.to_dict(orient='records')
        print("processing done successfully.")

    def get_processed_data(self):
        """
        returns the processed data.
        if the data is not processed, it will run the full analysis.
        """
        if self.processed_data is None:
            self.run_full_analysis()

        return self.processed_data
