CREATE TEMPORARY TABLE temp (from_user_id int PRIMARY KEY);
LOAD DATA LOCAL INFILE 'filtered_users.ids' INTO TABLE temp;
SELECT t1.* FROM Tweets_SD_TJ t1 LEFT JOIN temp t ON t1.from_user_id = t.from_user_id;