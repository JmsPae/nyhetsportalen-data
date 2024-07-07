# data/concerns.json

## På Svenska
TODO

---
## In English
This JSON file contains basic information about Swedish media [concerns](https://en.wikipedia.org/wiki/Concern_(business\))

### JSON Layout

Below is a full example containing all fields.
```json
{
    "concerns" : [
        {
			"id": "123456-1234",

			"name": "FörStort AB",

			"logo": "123456-1234.svg"
        }
    ]
}
```

#### `id` (required)

The legal identification number for the concern.

The structure of, for example, a larger concern such as Bonnier AB in the case of Gefle Dagbladet often vary with 
convoluted ownership structures and varying public profiles. Although Bonnier AB is not the top of the organisational
structure, it has the largest public profile and holds the entire media arm and so should be treated as such
for the purposes of this project.

#### `name` (required)

The name of the concern. Prefer the name of the legal entity, which can be found in the same places as the `id`.

#### `logo`

Refers to an image (ideally of SVG format) in the `images/concerns` folder of the repository. The image's name should be 
coherent with the outlet's `id`.
