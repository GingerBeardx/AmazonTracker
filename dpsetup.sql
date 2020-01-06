-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema AmazonPriceTracker
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema AmazonPriceTracker
-- -----------------------------------------------------
CREATE SCHEMA
IF NOT EXISTS `AmazonPriceTracker` DEFAULT CHARACTER
SET utf8 ;
USE `AmazonPriceTracker`
;

-- -----------------------------------------------------
-- Table `AmazonPriceTracker`.`users`
-- -----------------------------------------------------
CREATE TABLE
IF NOT EXISTS `AmazonPriceTracker`.`users`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(150) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY(`id`),
  UNIQUE INDEX `id_UNIQUE`(`id` ASC),
  UNIQUE INDEX `email_UNIQUE`(`email` ASC)
)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
