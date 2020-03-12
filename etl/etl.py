def transform(legacy_data):
    return {x.lower(): i for i in legacy_data for x in legacy_data[i]}
