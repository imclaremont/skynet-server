CREATE TABLE station_table (
    station_id VARCHAR(36) NOT NULL COMMENT 'PK',
    station_name VARCHAR(100) NOT NULL,
    station_longitude DECIMAL(9, 6) NOT NULL COMMENT 'XXX.XXXXXX°',
    station_latitude DECIMAL(9, 6) NOT NULL COMMENT 'XXX.XXXXXX°',
    capacity INT NOT NULL,
    PRIMARY KEY (station_id)
);
