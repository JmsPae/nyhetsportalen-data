# data/coverage.json

## På Svenska
TODO

---
## In English
This JSON file connects news media outlets to the geographic areas they cover.

### JSON Layout
---
Below is a full example containing all fields.
```json
{
	"coverage" : [
		{
			"media_id": "654321-4321_TL",
			"area_id": "2180",
			"local_coverage": true
		},
		{
			"media_id": "654321-4321_TL",
			"area_id": "21",
			"local_coverage": false
		},
    ]
}
```

#### `media_id` (required)
---
The `id` of the `media.json` entry of which to reference.

#### `area_id` (required)
---
The either 2 or 4 number code corresponding to either a Swedish municipality or council respectively, depending on the 
granularity and just how "local" the reporting of a particular outlet is.

This field can be subject to great interpretation depending on the outlet. Some outlets categorize their articles by
specific municipalities whilst others are significantly more vague. The sections below address some of these
complications.

#### Urban Areas
A common example is that of Stockholm and its massive urban area. Despite often having an inner-city municipality which 
goes by their namesake, the public perception of where these localities start and end is typically broader and often 
varies between those who live within the city limits, the larger metropolitan areas and those even further afield.

Referencing SCB's [urban area](https://www.scb.se/vara-tjanster/oppna-data/oppna-geodata/tatorter/) data as well as 
sampling the outlets reporting is a decent way to whittle down some of this uncertainty.

#### Historical Subdivisions
Sweden's Landskap (lit. "landscapes") are historical subdivisions which still hold a certain cultural relevance to this
day. However, they can complicate the project's system based off of modern and neatly self-contained subdivisions.

Fortunately, many of these historic provinces _mostly_ follow modern subdivisions and can be composed of multiple
communes. In cases where historical province borders do intersect with municipalities in a significant way, check if the
outlet does in fact report on areas within the municipality.

#### Other Areas
Sweden has it's fair share of well-known geographical areas with somewhat poorly defined boundaries which don't coincide
especially well with Sweden's counties and municipalities. 

Skärgården is one example, covering Stockholm's island chains. Fortunately, the site's header includes the phrase
'from Grisslehamn to Landsort'. However, many of these islands and coastal communities belong to municipalities which 
mostly cover the mainland, the largest example being Norrtälje.

In such cases, it is preferable to be more generous with the geographic extent since even if many living outside the
specific area, outlets often cover news from the municipalities at large and people who live there often have some sort
of interest in these areas.

#### `local_coverage` (required)
---
Whether or not the outlet provides 'local' coverage of a municipality or county.

This field can also subject to significant interpretation, but for the purposes of this project it serves as an indicator
to the granularity of an outlet's reporting. The biggest indicator is whether or not the outlet provides a specific
section, issue or category on the particular area.

Some outlets have categories for a few municipalities as well as the county at large. This should be interpreted as
the municipalities having "more local" coverage, and thus this field should set to `true` whilst the other municipalities
are assumed to have less granular coverage, and should have this field set to `false`.

Some outlets, however, have some extremely varied coverage areas. Göteborgs-Posten has sections on rather local areas 
such as Göteborg proper and the greater Göteborg region, as well as sections on both Western Sweden and the rest of the 
country. This makes it rather difficult to determine where exactly to draw the (admittedly quite subjective) line, but
going off of the example above, anything sub-county should be considered granular enough to set this field to `true`.

Another example are national outlets with local sections. SVT is a sprawling organisation with dozens of local offices
and although they don't have sections on specific municipalities, they provide local coverage on a county level.
