CREATE DATABASE  IF NOT EXISTS `crosswalk` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `crosswalk`;
-- MySQL dump 10.13  Distrib 5.5.37, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: crosswalk
-- ------------------------------------------------------
-- Server version	5.5.37-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `device` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `platform` varchar(16) DEFAULT NULL,
  `architecture` varchar(16) DEFAULT NULL,
  `sdk` varchar(24) DEFAULT NULL,
  `priority` varchar(2) DEFAULT NULL,
  `type` varchar(24) DEFAULT NULL,
  `asset` varchar(64) DEFAULT NULL,
  `serial` varchar(64) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `note` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `reportcase`
--

DROP TABLE IF EXISTS `reportcase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reportcase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `qa_id` int(11) NOT NULL,
  `qa_id_category` int(11) NOT NULL,
  `qa_id_case` int(11) NOT NULL,
  `result` int(11) DEFAULT NULL,
  `name` varchar(512) DEFAULT NULL,
  `comment` varchar(256) DEFAULT NULL,
  `bugs` varchar(128) DEFAULT NULL,
  `note` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=666898 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `reportcategory`
--

DROP TABLE IF EXISTS `reportcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reportcategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `qa_id` int(11) NOT NULL,
  `qa_id_category` int(11) NOT NULL,
  `name` varchar(256) DEFAULT NULL,
  `total_cases` int(11) DEFAULT NULL,
  `total_pass` int(11) DEFAULT NULL,
  `total_fail` int(11) DEFAULT NULL,
  `total_na` int(11) DEFAULT NULL,
  `total_measured` int(11) DEFAULT NULL,
  `comments` varchar(256) DEFAULT NULL,
  `note` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8245 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `reportsummary`
--

DROP TABLE IF EXISTS `reportsummary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reportsummary` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `qa_id` int(11) NOT NULL,
  `build_id` varchar(16) DEFAULT NULL,
  `profile` varchar(24) DEFAULT NULL,
  `branch` varchar(12) DEFAULT NULL,
  `darchitecture` varchar(24) DEFAULT NULL,
  `testtype` varchar(36) DEFAULT NULL,
  `device` varchar(128) DEFAULT NULL,
  `hardware` varchar(36) DEFAULT NULL,
  `weeknum` int(11) DEFAULT NULL,
  `srelease` varchar(12) DEFAULT NULL,
  `title` varchar(128) DEFAULT NULL,
  `total_cases` int(11) DEFAULT NULL,
  `total_pass` int(11) DEFAULT NULL,
  `total_fail` int(11) DEFAULT NULL,
  `total_na` int(11) DEFAULT NULL,
  `total_measured` int(11) DEFAULT NULL,
  `created_at` varchar(32) DEFAULT NULL,
  `tested_at` varchar(32) DEFAULT NULL,
  `updated_at` varchar(32) DEFAULT NULL,
  `note` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1263 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'crosswalk'
--

--
-- Dumping routines for database 'crosswalk'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-07-01 15:05:11
