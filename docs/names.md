# data/names.json

## På Svenska
GÖR FÖRFAN

---
## In English
This JSON file contains the names for each outlet in multiple languages.

### JSON Layout

```json
{
    "names" : [
        ...
        {
            "id": "654321-1234_TL",

            "name_eng": "Testar Lokalt",
            "name_short_swe": "TL",
            
            "name_eng": "Testing Local",
            "name_short_eng": "TL"
        },
        ...
    ]
}
```

#### `id` (required)
A unique identifier for a media outlet, representing an entry in `data/media.json`. See `docs/media.md` 
for details.

#### `name_xxx` (required)
The name used by the outlet for the specified language. Replace `xxx` with an 
[ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) identifier. There **must** be an entry for each language
specified in the outlet's entry in `data/media.json`, even if duplicates occur.

#### `name_short_xxx`
A short acronym or abbreviation used by the outlet in a respective language. See above for more details.

