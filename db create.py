CREATE SCHEMA `site_ap` ;


CREATE TABLE `site_ap`.`users` (
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `photo` VARCHAR(1000) NULL DEFAULT '__empty__',
  PRIMARY KEY (`username`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC));



CREATE TABLE `site_ap`.`posts` (
  `post_id` INT NOT NULL AUTO_INCREMENT,
  `username_post` VARCHAR(45) NOT NULL,
  `post` VARCHAR(1000) NOT NULL,
  `likes` INT NULL DEFAULT 0,
  `dislikes` INT NULL DEFAULT 0,
  `photo_post` VARCHAR(1000) NULL DEFAULT '__empty__',
  `date_mod` DATETIME NOT NULL,
  PRIMARY KEY (`post_id`),
  UNIQUE INDEX `posst_id_UNIQUE` (`post_id` ASC),
  INDEX `username_post_idx` (`username_post` ASC),
  CONSTRAINT `username_post`
    FOREIGN KEY (`username_post`)
    REFERENCES `site_ap`.`users` (`username`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);




CREATE TABLE `site_ap`.`comments` (
  `comment_id` INT NOT NULL AUTO_INCREMENT,
  `comment_post` INT NOT NULL,
  `comment_username` VARCHAR(45) NOT NULL,
  `comment` VARCHAR(1000) NOT NULL,
  `comment_date` DATETIME NOT NULL,
  `like_cm` INT NOT NULL DEFAULT 0,
  `dislike_cm` INT NOT NULL,
  PRIMARY KEY (`comment_id`),
  UNIQUE INDEX `comment_id_UNIQUE` (`comment_id` ASC),
  INDEX `cm_post_idx` (`comment_post` ASC),
  INDEX `cm_user_idx` (`comment_username` ASC),
  CONSTRAINT `cm_post`
    FOREIGN KEY (`comment_post`)
    REFERENCES `site_ap`.`posts` (`post_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `cm_user`
    FOREIGN KEY (`comment_username`)
    REFERENCES `site_ap`.`users` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


ALTER TABLE `site_ap`.`comments` 
DROP FOREIGN KEY `cm_post`;
ALTER TABLE `site_ap`.`comments` 
ADD CONSTRAINT `cm_post`
  FOREIGN KEY (`comment_post`)
  REFERENCES `site_ap`.`posts` (`post_id`)
  ON DELETE CASCADE
  ON UPDATE NO ACTION;






CREATE TABLE `site_ap`.`replys` (
  `reply_id` INT NOT NULL AUTO_INCREMENT,
  `reply_comment` INT NOT NULL,
  `reply_username` VARCHAR(45) NOT NULL,
  `reply_post` INT NOT NULL,
  `reply` VARCHAR(1000) NOT NULL,
  `reply_date` DATETIME NOT NULL,
  `like_re` INT NOT NULL DEFAULT 0,
  `dislike_re` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`reply_id`),
  UNIQUE INDEX `reply_id_UNIQUE` (`reply_id` ASC),
  INDEX `reply_cm_idx` (`reply_comment` ASC),
  INDEX `reply_ps_idx` (`reply_post` ASC),
  INDEX `reply_user_idx` (`reply_username` ASC),
  CONSTRAINT `reply_cm`
    FOREIGN KEY (`reply_comment`)
    REFERENCES `site_ap`.`comments` (`comment_id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `reply_ps`
    FOREIGN KEY (`reply_post`)
    REFERENCES `site_ap`.`posts` (`post_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `reply_user`
    FOREIGN KEY (`reply_username`)
    REFERENCES `site_ap`.`users` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);





CREATE TABLE `site_ap`.`follow` (
  `follower` VARCHAR(45) NOT NULL,
  `followed` VARCHAR(45) NOT NULL,
  INDEX `f_de_idx` (`followed` ASC),
  INDEX `f_er_idx` (`follower` ASC),
  CONSTRAINT `f_ed`
    FOREIGN KEY (`followed`)
    REFERENCES `site_ap`.`users` (`username`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `f_er`
    FOREIGN KEY (`follower`)
    REFERENCES `site_ap`.`users` (`username`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);




CREATE TABLE `site_ap`.`like_cm` (
  `like_com` INT NOT NULL,
  `like_user` VARCHAR(45) NOT NULL,
  INDEX `LCI_idx` (`like_com` ASC),
  INDEX `LCU_idx` (`like_user` ASC),
  CONSTRAINT `LCI`
    FOREIGN KEY (`like_com`)
    REFERENCES `site_ap`.`comments` (`comment_id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `LCU`
    FOREIGN KEY (`like_user`)
    REFERENCES `site_ap`.`users` (`username`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);

  


CREATE TABLE `site_ap`.`like_re` (
  `like_re` INT NOT NULL,
  `like_user` VARCHAR(45) NOT NULL,
  INDEX `LRI_idx` (`like_re` ASC),
  INDEX `LRU_idx` (`like_user` ASC),
  CONSTRAINT `LRI`
    FOREIGN KEY (`like_re`)
    REFERENCES `site_ap`.`replys` (`reply_id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `LRU`
    FOREIGN KEY (`like_user`)
    REFERENCES `site_ap`.`users` (`username`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);



CREATE TABLE `site_ap`.`likepost` (
  `like_post` INT NOT NULL,
  `like_user` VARCHAR(45) NOT NULL,
  INDEX `LPI_idx` (`like_post` ASC),
  INDEX `LPU_idx` (`like_user` ASC),
  CONSTRAINT `LPI`
    FOREIGN KEY (`like_post`)
    REFERENCES `site_ap`.`posts` (`post_id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `LPU`
    FOREIGN KEY (`like_user`)
    REFERENCES `site_ap`.`users` (`username`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);







ALTER TABLE `site_ap`.`comments` 
DROP FOREIGN KEY `cm_user`;
ALTER TABLE `site_ap`.`comments` 
ADD CONSTRAINT `cm_user`
  FOREIGN KEY (`comment_username`)
  REFERENCES `site_ap`.`users` (`username`)
  ON DELETE CASCADE
  ON UPDATE NO ACTION;





ALTER TABLE `site_ap`.`comments` 
CHANGE COLUMN `dislike_cm` `dislike_cm` INT(11) NOT NULL DEFAULT 0 ;





ALTER TABLE `site_ap`.`replys`
DROP FOREIGN KEY `reply_ps`,
DROP FOREIGN KEY `reply_user`;
ALTER TABLE `site_ap`.`replys`
ADD CONSTRAINT `reply_ps`
  FOREIGN KEY (`reply_post`)
  REFERENCES `site_ap`.`posts` (`post_id`)
  ON DELETE CASCADE
  ON UPDATE NO ACTION,
ADD CONSTRAINT `reply_user`
  FOREIGN KEY (`reply_username`)
  REFERENCES `site_ap`.`users` (`username`)
  ON DELETE CASCADE
  ON UPDATE NO ACTION;








CREATE TABLE `site_ap`.`links` (
  `id_link` INT NOT NULL AUTO_INCREMENT,
  `link` VARCHAR(1000) NOT NULL,
  `name` VARCHAR(100) NOT NULL DEFAULT 'link',
  PRIMARY KEY (`id_link`),
  UNIQUE INDEX `id_link_UNIQUE` (`id_link` ASC),
  CONSTRAINT `LREF`
    FOREIGN KEY (`id_link`)
    REFERENCES `site_ap`.`posts` (`post_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);



