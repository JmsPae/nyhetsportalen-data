CREATE TABLE media (
	id TEXT NOT NULL PRIMARY KEY,
	org_num TEXT,
	parent TEXT,

	logo TEXT,
	logo_small TEXT,

	url TEXT,
	languages TEXT NOT NULL,

	prefer_short BOOLEAN,

	web BOOLEAN NOT NULL,
	paper BOOLEAN NOT NULL,

	free BOOLEAN NOT NULL,
	paywall BOOLEAN NOT NULL
);

CREATE INDEX idx_media_parent ON media(parent);

CREATE INDEX idx_media_web ON media(web);
CREATE INDEX idx_media_paper ON media(paper);
CREATE INDEX idx_media_free ON media(free);
CREATE INDEX idx_media_paywall ON media(paywall);

CREATE TABLE concerns (
	id TEXT NOT NULL PRIMARY KEY,
	
	name TEXT NOT NULL,

	logo TEXT
);

CREATE INDEX idx_concerns_name ON concerns(name);

CREATE TABLE names (
	id TEXT NOT NULL PRIMARY KEY,
	
	name_swe TEXT,
	name_short_swe TEXT
);

CREATE INDEX idx_names_name_swe ON names(name_swe);
CREATE INDEX idx_names_name_short_swe ON names(name_short_swe);

CREATE TABLE coverage (
	media_id TEXT NOT NULL,
	area_id TEXT NOT NULL,
	
	local_coverage BOOLEAN NOT NULL,

	PRIMARY KEY (media_id, area_id),
	CHECK(length(area_id) = 2 OR length(area_id) = 4)
);

CREATE INDEX idx_coverage_local_coverage ON coverage(local_coverage);

