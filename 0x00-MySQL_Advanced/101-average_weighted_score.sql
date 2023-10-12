DELIMITER $$

-- Procedure: ComputeAverageWeightedScoreForUsers
-- Description: This stored procedure computes and stores the average weighted score for all students.
-- It iterates through each student, calculates the weighted average of their scores in different projects,
-- and updates their average_score in the users table.
-- Requirements:
--   Procedure ComputeAverageWeightedScoreForUsers does not take any input.

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Declare variables to store total_score and total_weight.
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    
    -- Iterate over all user IDs in the users table.
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    
    -- Create a cursor to loop through user IDs.
    DECLARE cur CURSOR FOR SELECT id FROM users;
    
    -- Error handling for the cursor.
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- Create a temporary table to store intermediate results.
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_average (user_id INT, temp_avg FLOAT);
    
    -- Open the cursor.
    OPEN cur;
    
    -- Loop through user IDs.
    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Calculate the total_score and total_weight for each user.
        SELECT SUM(c.score * p.weight) INTO total_score, SUM(p.weight) INTO total_weight
        FROM corrections c
        INNER JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;
        
        -- Calculate the average score for each user.
        INSERT INTO temp_average (user_id, temp_avg) VALUES (user_id, total_score / total_weight);
    END LOOP;
    
    -- Close the cursor.
    CLOSE cur;
    
    -- Update the users table with the computed average scores.
    UPDATE users u
    JOIN temp_average ta ON u.id = ta.user_id
    SET u.average_score = ta.temp_avg;
    
    -- Drop the temporary table.
    DROP TEMPORARY TABLE IF EXISTS temp_average;
    
END$$
DELIMITER ;
