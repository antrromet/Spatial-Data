CREATE TABLE InterestingPlaces (id INTEGER, name VARCHAR, description VARCHAR, PRIMARY KEY(id));

SELECT AddGeometryColumn('interestingplaces', 'latlon', '4326', 'POINT', 2 );

INSERT INTO InterestingPlaces(id, name, description, latlon) VALUES (1, 'Portland Place Apartments', 'Home. 2353 Portland St, Los Angeles, CA 90007', ST_GeomFromText('POINT(-118.282182 34.032726)', 4326))
INSERT INTO InterestingPlaces(id, name, description, latlon) VALUES (2, 'Mardette Apartments', 'Balajis Place. 2707 Portland St, Los Angeles, CA 90007', ST_GeomFromText('POINT(-118.283131 34.029700)', 4326))
INSERT INTO InterestingPlaces(id, name, description, latlon) VALUES (3, 'Regal LA LIVE Stadium 14', 'Movies at LA Live. 1000 W Olympic Blvd, Los Angeles, CA 90015', ST_GeomFromText('POINT(-118.270183 34.042645)', 4326))
INSERT INTO InterestingPlaces(id, name, description, latlon) VALUES (4, 'Ronald Tutor Campus Center', 'Lunch and studying the Graduate family room. 3607 Trousdale Pkwy, Los Angeles, CA 90089', ST_GeomFromText('POINT(-118.286469 34.020065)', 4326))
INSERT INTO InterestingPlaces(id, name, description, latlon) VALUES (5, 'Leavey Library', 'Studying and discussing with team members generally. Extremely crowded, cant go if we need to concentrate. 3607 Trousdale Pkwy, Los Angeles, CA 90089', ST_GeomFromText('POINT(-118.282650 34.021779)', 4326))
INSERT INTO InterestingPlaces(id, name, description, latlon) VALUES (6, 'Science and Engineering Library', 'Best place for quite study cubicle. 910 Bloom Walk, Los Angeles, CA 90089', ST_GeomFromText('POINT(-118.288856 34.019662)', 4326))
INSERT INTO InterestingPlaces(id, name, description, latlon) VALUES (7, 'Transamerica Center', 'Office work, School of Social Work. 1150 S Olive St, Los Angeles, CA 90015', ST_GeomFromText('POINT(-118.261750 34.039527)', 4326))
INSERT INTO InterestingPlaces(id, name, description, latlon) VALUES (8, 'Chipotle Mexican Grill', 'Awesome rice bowl with Barbacoa. 3748 S Figueroa St, Los Angeles, CA 90007', ST_GeomFromText('POINT(-118.282258 34.016694)', 4326))
INSERT INTO InterestingPlaces(id, name, description, latlon) VALUES (9, 'El Huero', 'Awesome beef quesadilla. 3000 S Figueroa St, Los Angeles, CA 90007', ST_GeomFromText('POINT(-118.277783 34.024700)', 4326))

SELECT ST_AsText(ST_ConvexHull(ST_Collect(latlon))) FROM InterestingPlaces;

SELECT ST_AsText(latlon), latlon <-> (select latlon from InterestingPlaces WHERE id = 1) as Distance FROM InterestingPlaces WHERE (latlon <-> (select latlon from InterestingPlaces WHERE id = 1) > 0) ORDER BY Distance LIMIT 3;