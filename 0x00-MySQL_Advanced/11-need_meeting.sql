-- Creating a view that lists students with a score < 80 and no last_meeting < 1 month ago
CREATE VIEW need_meeting AS
SELECT name FROM students WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
