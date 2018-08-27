# MapRoulette Tools

Some tools to interact with MapRoulette.

## geojson2maproulette

This python script lets you create JSON files that you can send to the [task upload endpoint](http://maproulette.org/docs/swagger-ui/index.html?url=/assets/swagger.json#/Task/batchUploadPost) of the MapRoulette API. You can upload GeoJSON directly through the MapRoulette administration UI to create tasks as well, but this script lets you create custom instructions per task based on properties in the GeoJSON source.

Basic configuration in `config.py`. The comments in there should get you going.