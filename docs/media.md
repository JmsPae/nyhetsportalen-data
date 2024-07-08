# data/media.json

## På Svenska
TODO

---
## In English
This JSON file contains basic information about Swedish media organisations and connects them to a potential parent
company or [concern](https://en.wikipedia.org/wiki/Concern_(business\)).

### JSON Layout

Below is a full example containing all fields.
```json
{
    "media" : [
        {
            "id": "654321-1234_TL",
            "org_num": "654321-1234",
            "parent": "123456-1234",

            "logo": "556508-3663_LJ.svg",
			"logo_small": "556508-3663_LJ_small.svg",

            "color": "#ffffff",

            "url": "https://www.doesntexist.se/",
            "languages": "swe,eng",

            "prefer_short": false,

            "web": true,
            "paper": false,
            
            "free": false,
            "paywall": true
        }
    ]
}
```

#### `id` (required)
A unique identifier for a media outlet, consisting of and organisation number and an acronym/abbreviation in upper-case.

Some outlets are either independent or possess their own corporate identity within the larger concern. In such cases, 
their own organisation number should be used. If their corporate identity cannot be easily verified or is otherwise 
uncertain, the organisation number of the parent concern should be used instead.

In a worst-case scenario with no parent concern or organisation number, use `MISSORG-XXXX` instead, replacing 
`XXXX` with an arbitrary number that doesn't conflict with any other instances of `ORGMISS`.

After the organisation number and an underscore, a short identifier such as an acronym or abbreviation should be 
used. This serves as an additional identifier in cases of unclear organisational structure, but should always be 
present regardless.

If the outlet uses such an identifier officially (SVT for Sveriges Television, for example) 
or has a short_name in `names.json` then that is what should be used. 
If that is not the case or multiple outlets within the same concern has an identical short_name, 
then the contributor can come up with something that makes some degree of sense and is unique within the concern
so long as it is somewhat logical.

#### `org_num`
The legal identification number for news outlet used for tax and legal matters. Can be found via sites such as
Bolagsfakta, Allabolag or Proff.

If the organisation number is not easily found or not easily connected to the outlet, then it should be excluded
and thus treated as either unknown or a less autonomous arm of the concern at large.

#### `parent`
The legal identification number for outlet's parent concern, or publisher in cases of a single company publishing
multiple outlets.

The structure of, for example, a larger concern such as Bonnier AB in the case of Gefle Dagbladet often vary with 
convoluted ownership structures and varying public profiles. Although Bonnier AB is not the top of the organisational
structure, it has the largest public profile and holds the entire media arm and so should be treated as such
for the purposes of this project.

This variable is also used as the ID for `concerns.json`, so it is imperative that other outlets within the same
concern share the same `parent`. If you're uncertain, look to other outlets within the same concern or create an issue.

It is legally required for outlets to state their parent concern, so this field should only be excluded in cases
of independent outlets which should ideally possess their own `org_num`.

#### `logo` and `logo_small`
Refers to an image (ideally of SVG format) in the `images/media` folder of the repository. The image's name should be 
coherent with the outlet's `id`.

`logo_small` should refer to an icon with a square aspect ratio whilst `logo` should refer to their main branding.

`logo_small` should be excluded if the main logo is already of a square aspect ratio and easily legible, or is unable
to be found.

#### `color`
The primary branding color used by the outlet as a [hex triplet](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet).

If a branding page cannot be found, sample the primary color of the logo. Prefer lower-case hexadecimal letters.

#### `url`
The URL for the outlet. Exclude only if the outlet has zero web presence regardless of whether or not the outlet
publishes articles online.

#### `languages` (required)
A comma-separated list of languages the outlet publishes in using the [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3)
standard, in order of prominence.

#### `prefer_short`
If the outlet has a name_short in its `names.json` entry, then `prefer_short` can be set to `true` in cases
where the short name is more commonly used in official sources such as for [SVT](https://www.svt.se/).

Will be treated as `false` if excluded.

#### Misc. Categories (required)
The last variables are required categories for filtering by medium and monetization. It should be relatively clear 
whether or not an outlet publishes to specific mediums or it monetized a certain way. In cases of uncertainty,
please specify in the pull request. 

* `web`

Whether or not the outlet publishes articles online.

* `paper`

Whether or not the outlet publishes a newspaper.

* `free`

Whether or not the outlet publishes a [free newspaper](https://en.wikipedia.org/wiki/Free_newspaper). Not mutually
exclusive with `paper`.

* `paywall`

Whether or nor some or all of the outlets web articles are behind a paywall.

### Practical Example: Gefle Dagblad
```json
        {
            "id": "556508-3663_GD",
            "parent": "556508-3663",

			"logo": "556508-3663_GD.svg",
			"logo_small": "556508-3663_GD_small.svg",

			"color": "#285789",

            "url": "https://www.gd.se/",
            "languages": "swe",

            "prefer_short": false,

            "web": true,
            "paper": true,
            
            "free": false,
            "paywall": true
        }
```
