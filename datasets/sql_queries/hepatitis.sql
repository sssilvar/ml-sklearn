/* === HEPATITIS DATASET - UCI ===
Author:       Santiago S. Silva R.

Description:  This script generates a table corresponding to
              the values of the hepatitis dataset.
              1. It is necessary to create a [machine] database,
              inside, create a [datasets] schema.

              More info about UCI - hepatitis
              https://archive.ics.uci.edu/ml/datasets/hepatitis

Year:         2018
 */
USE machine;

CREATE TABLE machine.datasets.hepatitis
(
    class INT,
    age INT,
    sex INT,
    steroid INT,
    antivirals INT,
    fatigue INT,
    malaise INT,
    anorexia INT,
    liver_big INT,
    liver_firm INT,
    spleen_palpable INT,
    spiders INT,
    ascites INT,
    varices INT,
    bilirubin FLOAT,
    alk_phosphate INT,
    sgot INT,
    albumin FLOAT,
    protime INT,
    histology INT
);

SELECT TOP 10 * FROM datasets.hepatitis;
SELECT COUNT(*) FROM datasets.hepatitis;
