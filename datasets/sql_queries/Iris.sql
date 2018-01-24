/* === IRIS DATASET - UCI ===
Author:       Santiago S. Silva R.

Description:  This script generates a table corresponding to
              the values of the Iris dataset.
              1. It is necessary to create a [machine] database,
              inside, create a [datasets] schema.

              More info about UCI - Iris
              https://archive.ics.uci.edu/ml/datasets/Iris

Year:         2018
 */
USE machine;

CREATE TABLE machine.datasets.iris
(
    sepal_length INT,
    sepal_width INT,
    petal_length INT,
    petal_width INT,
    class VARCHAR(20)
);

SELECT TOP 10 * FROM datasets.iris;
SELECT COUNT(*) FROM datasets.iris;
