CREATE DATABASE Honda_Civic_History;

DROP DATABASE Honda_Civic_History; -- Only if mistake is made

USE Honda_Civic_History;

CREATE TABLE Body_Styles (
  Body_Style_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Body_Style_Name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Engine_Types (
  Engine_Type_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Engine_Description VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Civic_Models (
  Model_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Model_Year INT NOT NULL,
  Body_Style_ID INT NOT NULL,
  Engine_Type_ID INT NOT NULL,
  Horsepower INT,
  Transmission VARCHAR(255),
  FOREIGN KEY (Body_Style_ID) REFERENCES Body_Styles(Body_Style_ID),
  FOREIGN KEY (Engine_Type_ID) REFERENCES Engine_Types(Engine_Type_ID)
);

-- Insert Body Styles 
INSERT INTO Body_Styles (Body_Style_Name) VALUES
('Sedan'),
('Coupe'),
('Hatchback');

-- Insert Engine Types 
INSERT INTO Engine_Types (Engine_Description) VALUES
('1.5L Turbocharged I4'),
('2.0L Turbocharged I4'),
('1.8L I4');

-- Insert Civic Models 
INSERT INTO Civic_Models (Model_Year, Body_Style_ID, Engine_Type_ID, Horsepower, Transmission) VALUES
(2023, 1, 1, 180, 'CVT'),
(2023, 1, 2, 200, 'Manual'),
(2020, 3, 1, 174, 'CVT'),
(2018, 3, 1, 170, 'CVT'),
(2015, 1, 3, 140, 'CVT'),
(2024, 2, 2, 220, 'Automatic');

-- Delete a record
DELETE FROM Civic_Models WHERE Model_ID = 3;

-- Update engine type for a model 
UPDATE Civic_Models SET Engine_Type_ID = 2 WHERE Model_ID = 4;

-- Retrieve data


SELECT * FROM Body_Styles;


SELECT * FROM Engine_Types;


SELECT Model_Year, Horsepower FROM Civic_Models WHERE Horsepower > 200;


SELECT * FROM Civic_Models WHERE Model_Year = 2023;


SELECT bs.Body_Style_Name, cm.Model_Year, et.Engine_Description, cm.Horsepower, cm.Transmission
FROM Civic_Models cm
INNER JOIN Body_Styles bs ON cm.Body_Style_ID = bs.Body_Style_ID
INNER JOIN Engine_Types et ON cm.Engine_Type_ID = et.Engine_Type_ID
ORDER BY cm.Model_Year DESC;