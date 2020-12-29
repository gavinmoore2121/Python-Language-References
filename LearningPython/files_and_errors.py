import pickle

# Use try-except blocks to catch errors.
# Use 'pickle' functions to create, write, and open files.

sample_data = [1, 2, 3, 4, 5]
try:
    # Note: wb means write/binary
    sample_file_writer = open('sample_data.pydata', 'wb')
    pickle.dump(sample_data, sample_file_writer)
    sample_file_writer.close()

    print("Sample file saved.")
except Exception as e:
    print(e)
    print("\nError in writing file.")

try:
    # Note: rb means read/binary
    sample_file_reader = open('sample_data.pydata', 'rb')
    sample_data_extracted = pickle.load(sample_file_reader)
    sample_file_reader.close()
    print("Here is the data you saved.")
    print(sample_data_extracted)

except Exception as e:
    print(e)
    print("Error encountered. File not found.")