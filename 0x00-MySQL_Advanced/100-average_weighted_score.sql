-- Creating a stored procedure computing average weighted score
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE weighted_average FLOAT;
    SELECT SUM(c.score * p.weight)
    INTO total_score
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;
    SELECT SUM(p.weight)
    INTO total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;
    IF total_weight > 0 THEN
        SET weighted_average = total_score / total_weight;
    ELSE
        SET weighted_average = 0;
    END IF;
    UPDATE users
    SET average_score = weighted_average
    WHERE id = user_id;
END //

DELIMITER ;
