-- A stored procedure that computes average weighted score for all students
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Clear existing average scores
    UPDATE users SET average_score = 0;

    -- Calculate and update average scores for each user
    UPDATE users
    JOIN (
        SELECT c.user_id, SUM(c.score * p.weight) / SUM(p.weight) AS average_weighted_score
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        GROUP BY c.user_id
    ) AS temp ON users.id = temp.user_id
    SET users.average_score = temp.average_weighted_score;
END //

DELIMITER ;
