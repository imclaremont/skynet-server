CREATE DATABASE IF NOT EXISTS flaskdb;
USE flaskdb;

-- 테이블 생성
SOURCE create_tables/drone_table.sql;
SOURCE create_tables/station_table.sql;
SOURCE create_tables/deliveries_table.sql;
SOURCE create_tables/no_fly_zones_table.sql;
SOURCE create_tables/weather_table.sql;
SOURCE create_tables/path_between_station_table.sql;
SOURCE create_tables/intersection_table.sql;
SOURCE create_tables/delivery_path_table.sql;

-- 외래 키 설정
SET FOREIGN_KEY_CHECKS = 1;
