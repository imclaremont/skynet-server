CREATE TABLE drone_table (
    drone_id VARCHAR(36) NOT NULL COMMENT 'PK',
    delivery_id VARCHAR(36) NOT NULL COMMENT 'FK',
    drone_status ENUM('available', 'in-flight', 'maintenance') NOT NULL DEFAULT 'available',
    longitude DECIMAL(9, 6) NOT NULL COMMENT 'logging 목적',
    latitude DECIMAL(9, 6) NOT NULL COMMENT 'logging 목적',
    battery INT NOT NULL DEFAULT 100 COMMENT '0% ~ 100%',
    last_update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (drone_id),
    FOREIGN KEY (delivery_id) REFERENCES deliveries_table(delivery_id)
);
