from src.data_preprocessing import load_data, show_basic_info, clean_data, convert_target, encode_data, encode_all

data = load_data()

show_basic_info(data)

data = clean_data(data)

data = convert_target(data)

data = encode_data(data)

data = encode_all(data)

print("\n After preprocessing:")
print(data.head())

print("\n Data types:")
print(data.dtypes)