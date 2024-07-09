PRAGMA foreign_keys = ON;

CREATE TABLE concerns (
	id TEXT NOT NULL PRIMARY KEY,
	
	name TEXT NOT NULL,

	logo TEXT
) STRICT, WITHOUT ROWID;

CREATE INDEX idx_concerns_name ON concerns(name);

CREATE TABLE media (
	id TEXT NOT NULL PRIMARY KEY,
	org_num TEXT,
	parent TEXT,

	logo TEXT,
	logo_small TEXT,

	color TEXT,

	url TEXT,
	languages TEXT NOT NULL,

	prefer_short INT,

	web INT NOT NULL,
	paper INT NOT NULL,

	free INT NOT NULL,
	paywall INT NOT NULL,

	-- Since a BOOLEAN type doesn't exist, we'll have to type-check ourselves.
	CHECK(prefer_short = NULL OR prefer_short = 0 OR prefer_short = 1),
	CHECK(web = 0 OR web = 1),
	CHECK(paper = 0 OR paper = 1),
	CHECK(free = 0 OR free = 1),
	CHECK(paywall = 0 OR paywall = 1),

	FOREIGN KEY(parent) REFERENCES concerns(id)
) STRICT, WITHOUT ROWID;

CREATE INDEX idx_media_parent ON media(parent);

CREATE TABLE names (
	media_id TEXT NOT NULL PRIMARY KEY,
	
	name_swe TEXT,
	name_short_swe TEXT,

	FOREIGN KEY(media_id) REFERENCES media(id)
) STRICT, WITHOUT ROWID;

CREATE INDEX idx_names_name_swe ON names(name_swe);
CREATE INDEX idx_names_name_short_swe ON names(name_short_swe);

CREATE TABLE coverage (
	media_id TEXT NOT NULL,
	area_id TEXT NOT NULL,
	
	local_coverage INT NOT NULL,

	PRIMARY KEY (media_id, area_id),

	-- Ensure the area_id is or length 2 (county code) or 4 (municipality code)
	CHECK(length(area_id) = 2 OR length(area_id) = 4),
	CHECK(local_coverage = 0 OR local_coverage = 1),

	FOREIGN KEY(media_id) REFERENCES media(id)
) STRICT, WITHOUT ROWID;
