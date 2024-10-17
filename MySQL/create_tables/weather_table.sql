CREATE TABLE weather_table (
    weather_id VARCHAR(36) NOT NULL COMMENT 'PK',
    wind_speed FLOAT NULL DEFAULT 0,
    rainfall FLOAT NULL DEFAULT 0,
    observation_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (weather_id)
);
