DELIMITER $$;
-- Create the stored procedure ComputeAverageScoreForUser
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    -- Calculate the total score and the total number of projects for the user
    SELECT SUM(score) INTO total_score, COUNT(DISTINCT project_id) INTO total_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate and store the average score for the user
    IF total_projects > 0 THEN
        SET total_score = total_score / total_projects;
        UPDATE users SET average_score = total_score WHERE id = user_id;
    END IF;
END;
$$
DELIMITER ;
