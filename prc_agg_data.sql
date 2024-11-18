

CREATE OR REPLACE PROCEDURE "STG".prc_agg_tripdata(
	)
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
    v_runtime TIMESTAMP;
    V_status TEXT;
    v_msg TEXT;
BEGIN
    -- Set initial values
    v_runtime := NOW();
    V_status := 'SUCCESS';
    v_msg := NULL;

    -- INSERT logic for daily_trip_agg table
    INSERT INTO "EDW".daily_trip_agg (
        SELECT 
            CAST(pickup_date AS date),
            SUM(passenger_count) AS tot_passenger_count,
            CAST(AVG(passenger_count) AS DECIMAL(10, 2)) AS avg_passenger_count,
            CAST(SUM(trip_distance) AS DECIMAL(10, 2)) AS tot_distance,
            CAST(AVG(trip_distance) AS DECIMAL(10, 2)) AS avg_distance,
            CAST(SUM(fare_amount) AS DECIMAL(10, 2)) AS tot_fare,
            CAST(AVG(fare_amount) AS DECIMAL(10, 2)) AS avg_fare
        FROM "STG".tripdata
        GROUP BY CAST(pickup_date AS date)
    );

    -- INSERT logic for vendor_daily_trip_agg table
    INSERT INTO "EDW".vendor_daily_trip_agg (
        SELECT 
            CAST(pickup_date AS date),
            payment_type AS vendor,
            SUM(passenger_count) AS tot_passenger_count,
            CAST(AVG(passenger_count) AS DECIMAL(10, 2)) AS avg_passenger_count,
            CAST(SUM(trip_distance) AS DECIMAL(10, 2)) AS tot_distance,
            CAST(AVG(trip_distance) AS DECIMAL(10, 2)) AS avg_distance,
            CAST(SUM(fare_amount) AS DECIMAL(10, 2)) AS tot_fare,
            CAST(AVG(fare_amount) AS DECIMAL(10, 2)) AS avg_fare
        FROM "STG".tripdata
        GROUP BY CAST(pickup_date AS date), payment_type
    );

    -- Log the outcome of the procedure
    INSERT INTO "STG".procedure_logs(run_time, status, msg)
    VALUES (v_runtime, V_status, v_msg);

EXCEPTION
    WHEN OTHERS THEN
        -- On error, log the failure
        V_status := 'FAILED';
        v_msg := SQLERRM;

        INSERT INTO "STG".procedure_logs(run_time, status, msg)
        VALUES (v_runtime, V_status, v_msg);
END;
$BODY$;

