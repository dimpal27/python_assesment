from collections import defaultdict


class DataStream:
    def __init__(self):
        self.last_print_time = {}  # Dictionary to store the last print time of each data string

    def should_output_data_str(self, timestamp: int, data_str: str) -> bool:
        if data_str not in self.last_print_time or timestamp - self.last_print_time[data_str] >= 5:
            self.last_print_time[data_str] = timestamp
            return True
        else:
            return False


# Test the DataStream class
if __name__ == "__main__":
    data_stream = DataStream()
    print(data_stream.should_output_data_str(timestamp=0, data_str="hello"))  # Output: True
    print(data_stream.should_output_data_str(timestamp=1, data_str="world"))  # Output: True
    print(data_stream.should_output_data_str(timestamp=6, data_str="hello"))  # Output: True
    print(data_stream.should_output_data_str(timestamp=7, data_str="hello"))  # Output: False
    print(data_stream.should_output_data_str(timestamp=8, data_str="world"))  # Output: True
