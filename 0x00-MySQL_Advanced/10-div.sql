DELIMITER $$;

-- Create a SafeDiv function that performs safe division.
-- This function takes two integer arguments, 'a' and 'b', and returns the result of 'a / b' or 0 if 'b' is equal to 0.
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10,4)
BEGIN
    DECLARE result DECIMAL(10,4);
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;
    RETURN result;
END$$;

DELIMITER ;
