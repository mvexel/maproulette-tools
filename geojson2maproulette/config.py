files = {
    # input file, GeoJSON
    'in': '/Users/martijnv/tmp/tomr.geojson',
    # output file, to be used in MapRoulette challenge creation.
    # Requires one `{}` which will be replaced by the file number
    'out': '/Users/martijnv/tmp/tomr_{}.json',
    # number of tasks per JSON file, 0 to put everything in one file
    # very large JSON files are more likely to cause server trouble
    'chunksize': 1000
}

instruction = {
    # instruction, use {} to add placeholders and use the placeholders dict to connect these to GeoJSON properties in the same order.
    'text': 'There is a business named "{}" at {}. Can you confirm it using street level images or local knowledge? If so, please add it to OSM if it doesn\'t exist already. Thanks!',
    'placeholders': ['business_name', 'address']
}