#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# Open image file for reading (binary mode)
f = open('exif_this.jpg', mode='rb')

# Return Exif tags
# pip install exifread
import exifread
tags = exifread.process_file(f)

if not tags:
    print('Not tags')
    quit()

print('Tags ({}):'.format(len(tags)))

tags_by_value = dict()
categories_by_tag = dict()

for tag, value in tags.items():
    # Process value
    try:
        if value.field_type == 1:
            try:
                # If last 2 items equals [0, 0]
                if value.values[-2:] == [0, 0]:
                    value = bytes(value.values[:-2]).decode('utf-16')
                else:
                    value = bytes(value.values).decode('utf-16')

            except:
                value = str(value.values)
        else:
            value = value.printable

        value = value.strip()

    except:
        # Example tag JPEGThumbnail
        if type(value) == bytes:
            import base64
            value = base64.b64encode(value).decode()

    tags_by_value[tag] = value
    print('  "{}": {}'.format(tag, value))

    # Fill categories_by_tag
    if ' ' in tag:
        category, sub_tag = tag.split(' ')

        if category not in categories_by_tag:
            categories_by_tag[category] = dict()

        categories_by_tag[category][sub_tag] = value

    else:
        categories_by_tag[tag] = value


print('\n')
print('CATEGORIES_BY_TAG:')
import json
print(json.dumps(tags_by_value, sort_keys=True, ensure_ascii=False, indent=4))
print(json.dumps(categories_by_tag, sort_keys=True, ensure_ascii=False, indent=4))
