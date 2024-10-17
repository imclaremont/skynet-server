CREATE TABLE intersection_table (
    intersection_id VARCHAR(36) NOT NULL COMMENT 'PK',
    path1_id VARCHAR(36) NOT NULL COMMENT 'FK',
    path2_id VARCHAR(36) NOT NULL COMMENT 'FK',
    longitude DECIMAL(9, 6) NOT NULL COMMENT 'XXX.XXXXXX°',
    latitude DECIMAL(9, 6) NOT NULL COMMENT 'XXX.XXXXXX°',
    PRIMARY KEY (intersection_id),
    FOREIGN KEY (path1_id) REFERENCES path_between_station_table(path_id),
    FOREIGN KEY (path2_id) REFERENCES path_between_station_table(path_id)
);
