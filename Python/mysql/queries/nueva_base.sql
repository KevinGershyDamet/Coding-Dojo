-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema lead_gen_business
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema lead_gen_business
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lead_gen_business` DEFAULT CHARACTER SET latin1 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `direccion` TEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `location` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_dojos_regiones1_idx` (`region_id` ASC) VISIBLE,
  CONSTRAINT `fk_dojos_regiones1`
    FOREIGN KEY (`region_id`)
    REFERENCES `mydb`.`regiones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `age` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `dojo_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojos_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojos`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `mydb`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `direccion` TEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`libros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`libros` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(255) NULL,
  `editorial` VARCHAR(45) NULL,
  `num_paginas` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`favoritos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`favoritos` (
  `usuario_id` INT NOT NULL,
  `libro_id` INT NOT NULL,
  INDEX `fk_favoritos_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  INDEX `fk_favoritos_libros1_idx` (`libro_id` ASC) VISIBLE,
  CONSTRAINT `fk_favoritos_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favoritos_libros1`
    FOREIGN KEY (`libro_id`)
    REFERENCES `mydb`.`libros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `direccion` TEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`amistades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`amistades` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id` INT NOT NULL,
  `amistad_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_usuarios_has_usuarios_usuarios2_idx` (`amistad_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_usuarios_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_usuarios_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_usuarios_usuarios2`
    FOREIGN KEY (`amistad_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `direccion` TEXT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`eventos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`eventos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` TEXT NULL,
  `descripcion` TEXT NULL,
  `ubicacion` TEXT NULL,
  `hora_inicio` DATETIME NULL,
  `hora_fin` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`asistencias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`asistencias` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id` INT NOT NULL,
  `evento_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_asistencias_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  INDEX `fk_asistencias_eventos1_idx` (`evento_id` ASC) VISIBLE,
  CONSTRAINT `fk_asistencias_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `mydb`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_asistencias_eventos1`
    FOREIGN KEY (`evento_id`)
    REFERENCES `mydb`.`eventos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`regiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`regiones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `location` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_dojos_regiones1_idx` (`region_id` ASC) VISIBLE,
  CONSTRAINT `fk_dojos_regiones1`
    FOREIGN KEY (`region_id`)
    REFERENCES `mydb`.`regiones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`estudiantes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`estudiantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `adress_1` VARCHAR(255) NULL,
  `adress_2` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `dojos_id` INT NOT NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_students_dojos1_idx` (`dojos_id` ASC) VISIBLE,
  INDEX `fk_estudiantes_regiones1_idx` (`region_id` ASC) VISIBLE,
  CONSTRAINT `fk_students_dojos1`
    FOREIGN KEY (`dojos_id`)
    REFERENCES `mydb`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_estudiantes_regiones1`
    FOREIGN KEY (`region_id`)
    REFERENCES `mydb`.`regiones` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`intereses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`intereses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `interes` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`estudiantes_has_intereses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`estudiantes_has_intereses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `estudiante_id` INT NOT NULL,
  `interese_id` INT NOT NULL,
  INDEX `fk_students_has_intereses_intereses1_idx` (`interese_id` ASC) VISIBLE,
  INDEX `fk_students_has_intereses_students1_idx` (`estudiante_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_students_has_intereses_students1`
    FOREIGN KEY (`estudiante_id`)
    REFERENCES `mydb`.`estudiantes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_students_has_intereses_intereses1`
    FOREIGN KEY (`interese_id`)
    REFERENCES `mydb`.`intereses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `lead_gen_business` ;

-- -----------------------------------------------------
-- Table `lead_gen_business`.`clients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lead_gen_business`.`clients` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(25) NOT NULL,
  `last_name` VARCHAR(25) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `joined_datetime` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `lead_gen_business`.`billing`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lead_gen_business`.`billing` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `amount` FLOAT NOT NULL,
  `charged_datetime` DATETIME NOT NULL,
  `clients_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_billing_clients1_idx` (`clients_id` ASC) VISIBLE,
  CONSTRAINT `fk_billing_clients1`
    FOREIGN KEY (`clients_id`)
    REFERENCES `lead_gen_business`.`clients` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `lead_gen_business`.`sites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lead_gen_business`.`sites` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `domain_name` VARCHAR(100) NOT NULL,
  `created_datetime` DATETIME NOT NULL,
  `clients_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_sites_clients_idx` (`clients_id` ASC) VISIBLE,
  CONSTRAINT `fk_sites_clients`
    FOREIGN KEY (`clients_id`)
    REFERENCES `lead_gen_business`.`clients` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `lead_gen_business`.`leads`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lead_gen_business`.`leads` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `registered_datetime` DATETIME NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `sites_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_leads_sites1_idx` (`sites_id` ASC) VISIBLE,
  CONSTRAINT `fk_leads_sites1`
    FOREIGN KEY (`sites_id`)
    REFERENCES `lead_gen_business`.`sites` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 36
DEFAULT CHARACTER SET = latin1;

USE `lead_gen_business` ;

-- -----------------------------------------------------
-- Placeholder table for view `lead_gen_business`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lead_gen_business`.`view1` (`id` INT);

-- -----------------------------------------------------
-- View `lead_gen_business`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `lead_gen_business`.`view1`;
USE `lead_gen_business`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
