from Cleaner import Cleaner
from fetcher import DataFetcher
from processor import DataProcessor


class AnalysisManager:
    """
    manage the analysis process and get the data
    """

    def __init__(self):
        self.fetcher = DataFetcher()
        self.cleaner = Cleaner()
        self.processor = DataProcessor()

        self.processed_data = None

    def run_full_analysis(self):
        """
        Runs the full pipeline: Fetch -> Clean -> Process
        """
        print("start fetching...")
        raw_data_df = self.fetcher.get_all_records()

        if raw_data_df.empty:
            print("The data is empty. Stopping processing.")
            self.processed_data = []
            return

        print(f"Fetched {len(raw_data_df)} records.")


        print("Start cleaning data...")
        cleaned_df = self.cleaner.data_clean(raw_data_df)

        if cleaned_df.empty:
            print("Data is empty after cleaning. Stopping processing.")
            self.processed_data = []
            return

        print(f"Cleaning complete. {len(cleaned_df)} unique records remain.")
        # --- END OF CLEANING STEP ---

        print("Start processing...")
        # Pass the CLEANED dataframe to the processor
        processed_df = self.processor.process_data(cleaned_df)

        final_columns = ['id', 'original_text', 'rarest_word', 'sentiment', 'weapons_detected']
        # check if all columns exist
        for col in final_columns:
            if col not in processed_df.columns:
                processed_df[col] = ""  # fill with empty string if missing

        final_df = processed_df[final_columns]

        # cast the json to dict
        self.processed_data = final_df.to_dict(orient='records')
        print("Processing done successfully.")

    def get_processed_data(self):
        """
        returns the processed data.
        if the data is not processed, it will run the full analysis.
        """
        if self.processed_data is None:
            self.run_full_analysis()

        return self.processed_data