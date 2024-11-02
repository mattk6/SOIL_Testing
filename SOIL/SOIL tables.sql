CREATE TABLE `Crop`(
    `Crop_ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Seed Provider` LINESTRING NOT NULL,
    `Seed Type` LINESTRING NOT NULL,
    `Hybrid Type` LINESTRING NOT NULL,
    `Seed Number` LINESTRING NOT NULL
);
CREATE TABLE `Farmer`(
    `Farmer_ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `FName` LINESTRING NOT NULL,
    `LName` LINESTRING NOT NULL,
    `Phone Number` LINESTRING NOT NULL,
    `Email` LINESTRING NOT NULL,
    `Street` LINESTRING NOT NULL,
    `City` LINESTRING NOT NULL,
    `State` LINESTRING NOT NULL,
    `Zipcode` INT NOT NULL
);
CREATE TABLE `Field`(
    `Field_ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Farmer_ID` BIGINT NOT NULL,
    `Longitude` FLOAT(53) NOT NULL,
    `Latitude` FLOAT(53) NOT NULL,
    `Soil Type` LINESTRING NOT NULL,
    `Elevation` BIGINT NOT NULL
);
CREATE TABLE `Field Data`(
    `FDID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Field_ID` BIGINT NOT NULL,
    `Water_ID` BIGINT NOT NULL,
    `Irrigation Status` BOOLEAN NOT NULL,
    `Avg`.` Yield` FLOAT(53) NOT NULL,
    `Crop_ID` BIGINT NOT NULL,
    `tillage` LINESTRING NOT NULL,
    `Field Residue` BOOLEAN NOT NULL,
    `Planting Style` LINESTRING NOT NULL,
    `Depth` FLOAT(53) NOT NULL,
    `Cover Crop` BOOLEAN NOT NULL,
    `Row Spacing` FLOAT(53) NOT NULL,
    `Pivot Corners` LINESTRING NOT NULL
);
CREATE TABLE `Probe`(
    `Probe_ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Field_ID` BIGINT NOT NULL,
    `Salinity` FLOAT(53) NOT NULL,
    `Temperature` FLOAT(53) NOT NULL,
    `Moisture` FLOAT(53) NOT NULL,
    `Nitrogen` FLOAT(53) NOT NULL,
    `Phophorus` FLOAT(53) NOT NULL,
    `Potassium` FLOAT(53) NOT NULL,
    `Sunlight` FLOAT(53) NOT NULL,
    `pH` FLOAT(53) NOT NULL
);
CREATE TABLE `Water`(
    `Water_ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Avg`.` Annual Rainfall` FLOAT(53) NOT NULL,
    `Irrigation App`.`` FLOAT(53) NOT NULL,
    `Runoff` FLOAT(53) NOT NULL,
    `Leaching` BOOLEAN NOT NULL
);
ALTER TABLE
    `Field Data` ADD CONSTRAINT `field data_crop_id_foreign` FOREIGN KEY(`Crop_ID`) REFERENCES `Crop`(`Crop_ID`);
ALTER TABLE
    `Probe` ADD CONSTRAINT `probe_field_id_foreign` FOREIGN KEY(`Field_ID`) REFERENCES `Field`(`Field_ID`);
ALTER TABLE
    `Field Data` ADD CONSTRAINT `field data_field_id_foreign` FOREIGN KEY(`Field_ID`) REFERENCES `Field`(`Field_ID`);
ALTER TABLE
    `Field` ADD CONSTRAINT `field_farmer_id_foreign` FOREIGN KEY(`Farmer_ID`) REFERENCES `Farmer`(`Farmer_ID`);
ALTER TABLE
    `Field Data` ADD CONSTRAINT `field data_water_id_foreign` FOREIGN KEY(`Water_ID`) REFERENCES `Water`(`Water_ID`);