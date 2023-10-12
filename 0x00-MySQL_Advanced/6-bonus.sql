DELIMITER $$;
-- Create a stored procedure AddBonus that adds a new correction for a student
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Check if the project exists in the projects table
    IF NOT EXISTS (SELECT name FROM projects WHERE name = project_name) THEN
        -- If the project does not exist, create it
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    
    -- Insert the correction into the corrections table
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;
$$
DELIMITER ;
