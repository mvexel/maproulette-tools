#!/usr/bin/env python3

import json
import config

out = []


class MRTask(object):

    def __init__(self, geojson_features):
        self.name = ''
        self.description = ''
        self.instruction = ''
        if geojson_features['type'] == 'FeatureCollection':
            self.geometries = geojson_features
        else:
            self.geometries = {
                'type': 'FeatureCollection',
                'features': [geojson_features]
            }
        super().__init__()


if __name__ == '__main__':
    instruction_template = config.instruction['text']
    placeholders = config.instruction['placeholders']
    count = 0
    files = 0
    with open(config.files['in'], 'r') as fh:
        j = json.load(fh)
        for geom in j['features']:
            t = MRTask(geom)
            t.instruction = instruction_template.format(
                *[geom['properties'][p] for p in placeholders])
            out.append(t.__dict__)
            count += 1
            if count == config.files['chunksize']:
                print('writing file {} with {} tasks.'.format(files, count))
                with open(config.files['out'].format(files), 'w') as fh:
                    fh.write(json.dumps(out, indent=2))
                out = []
                files += 1
                count = 0
    print('done.')
