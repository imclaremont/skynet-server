CREATE TABLE deliveries_table (
    delivery_id VARCHAR(36) NOT NULL COMMENT 'PK',
    origin_station_id VARCHAR(36) NOT NULL COMMENT 'FK',
    destination_station_id VARCHAR(36) NOT NULL COMMENT 'FK',
    delivery_status VARCHAR(100) NOT NULL DEFAULT 'pending',
    entire_arrival_time TIMESTAMP NULL,
    arrival_time TIMESTAMP NULL,
    PRIMARY KEY (delivery_id),
    FOREIGN KEY (origin_station_id) REFERENCES station_table(station_id),
    FOREIGN KEY (destination_station_id) REFERENCES station_table(station_id)
);
