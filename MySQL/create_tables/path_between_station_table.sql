CREATE TABLE path_between_station_table (
    path_id VARCHAR(36) NOT NULL COMMENT 'PK',
    origin_station_id VARCHAR(36) NOT NULL COMMENT 'FK',
    destination_station_id VARCHAR(36) NOT NULL COMMENT 'FK',
    distance INT NOT NULL COMMENT 'm',
    PRIMARY KEY (path_id),
    FOREIGN KEY (origin_station_id) REFERENCES station_table(station_id),
    FOREIGN KEY (destination_station_id) REFERENCES station_table(station_id)
);
