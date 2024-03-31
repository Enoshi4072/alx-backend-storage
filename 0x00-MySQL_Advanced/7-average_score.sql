-- Creating a stored procedure computing the average score for a student 
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);
    
    -- Calculate average score for the given user
    SELECT AVG(score)
    INTO avg_score
    FROM corrections
    WHERE user_id = user_id;
    
    -- Update the average_score for the user
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
    
END //

DELIMITER ;
