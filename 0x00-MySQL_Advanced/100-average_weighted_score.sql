DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Declare variables to store total_score and total_weight.
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    
    -- Calculate the total_score and total_weight for the student.
    SELECT SUM(c.score * p.weight) INTO total_score, SUM(p.weight) INTO total_weight
    FROM corrections c
    INNER JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;
    
    -- Check if there are corrections with non-zero weights.
    IF total_weight > 0 THEN
        -- Update the user's average_score with the weighted average score.
        UPDATE users
        SET average_score = total_score / total_weight
        WHERE id = user_id;
    ELSE
        -- Set the user's average_score to 0 if no valid corrections are found.
        UPDATE users
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END$$
DELIMITER ;
