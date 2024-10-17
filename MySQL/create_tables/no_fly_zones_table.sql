CREATE TABLE no_fly_zones_table (
    zone_id VARCHAR(36) NOT NULL COMMENT 'PK',
    zone_name VARCHAR(100) NOT NULL,
    longitude DECIMAL(9, 6) NOT NULL COMMENT 'XXX.XXXXXX°',
    latitude DECIMAL(9, 6) NOT NULL COMMENT 'XXX.XXXXXX°',
    radius INT NOT NULL COMMENT '[m]',
    PRIMARY KEY (zone_id)
);
