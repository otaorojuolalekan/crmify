-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: crmify
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,'Funsho','Badmos','Enilolobo Avenue','user@example.com','2023-08-24 17:39:12'),(2,'Jide','Kosoko','2, afolabi str, ifako','abc@d.io','2023-08-24 19:05:04'),(4,'Jide','Johnson','15, folorunsho str, Dugbe','123@122.io','2023-08-24 21:21:23'),(5,'Jide','Johnson','15, folorunsho str, Dugbe','123@122.io','2023-08-24 22:05:53'),(6,'Sade','Cytherea','Blk 15, folorunsho str, Dugbe','123@122.ioda','2023-08-24 22:39:50'),(7,'Sade','Cytherea','Flat 5, folorunsho str, Dugbe','123@122.ioda','2023-08-25 04:54:03'),(8,'Bimpe','Adebanwo','234, Awolowo str, Ikeja','ABanwo@aol.com','2023-08-26 01:07:17'),(9,'Folasade','Oguntade','Awolowo way','foguntade@example.com','2023-08-30 06:20:51'),(10,'Bimbo','Oshin','234, Mushin Idioro str, Lagos','BOshin@aol.com','2023-08-31 06:29:09'),(11,'Bimbo','Oshin','234, Mushin Idioro str, Lagos','BOshin@aol.com','2023-08-31 06:30:21'),(12,'Bimbo2','Oshin123','234, Mushin Idioro str, Lagos','BOshin@aol.com','2023-08-31 06:32:58'),(13,'Bimbo3','Oshin123','i7, Mushin Idioro str, Lagos','BOshin@aol.com','2023-08-31 07:03:02'),(14,'Environment','URL','i7, Mushin Idioro str, Lagos','eurl@aol.com','2023-08-31 07:37:05'),(15,'Inherit JWT from','CRMIFY Environment','27, inheritance@gmail Idioro str, Lagos','inheritance@gmail.com','2023-09-01 06:02:47'),(16,'Sorting Environment variables','CRMIFY Environment','419, envariagles@gmail Idioro str, Lagos','envaribles@gmail.com','2023-09-02 19:51:31'),(17,'Jackie','Chan','419, Jackie Chan Avenue, Shanghai','jackiechan@jchan.com','2023-09-03 16:19:22'),(18,'Bruce','Lee','125, Bumble Bee Avenue, Singapore, China','BucLee@blee.com','2023-09-03 16:32:01'),(19,'Bruce2','Lee323','125, Bumblae Bee Avenue, Singapore, China','BucLeetq@blee.com','2023-09-03 16:41:45'),(20,'Bilikisu','Aminu','Anywhere for that matter','bilikamin@yasin.eu','2023-09-04 02:28:17'),(21,'Created','From Web Form','I don\'t care about this field.','happiness@gmail.com','2023-09-04 02:32:40'),(22,'Created','From Web Form','I don\'t care about this field.','happiness@gmail.com','2023-09-04 02:32:51'),(23,'Musibau','SessionCreate','musession@gmail.com','musession@gmail.com','2023-09-05 07:28:06'),(24,'nosession','nosession','nosession@gmail.com','nosession@gmail.com','2023-09-05 07:30:15'),(25,'UserSade','Abiodun','123, sadeabiodun villa, Ikoyi, Lagos','sadeabiodun@createaccount.com','2023-09-05 15:13:17'),(26,'byrestoreduser','testing','adoija','test1230@da.c','2023-09-05 16:29:11'),(27,'another','user','just another address, NY','anotheruser@aol.com','2023-09-05 17:11:12'),(28,'Bode','Fashola','12, Temidire Street, Orile Iganmu','bod@x.com','2023-09-08 18:01:42'),(29,'daf','adfa expired token','dfadina.wefa','afa@dfa.ca','2023-09-08 18:06:20'),(30,'Checking','Checkbox','currently checked','checking@check.box','2023-09-08 18:19:03'),(31,'Checking','Checkbox','currently checked','checking@check.box','2023-09-08 18:20:36'),(32,'Checking1','Checkbox1','not currently checked','checking@check.box','2023-09-08 18:23:56'),(33,'Checking123','Checkbox241','currently checked','checking@check.box','2023-09-08 18:24:14');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cases`
--

DROP TABLE IF EXISTS `cases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cases` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` enum('Technical','Commercial') NOT NULL,
  `subject` varchar(100) NOT NULL,
  `status` enum('Resolved','Unresolved') NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `account_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `account_id` (`account_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `cases_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `accounts` (`id`) ON DELETE CASCADE,
  CONSTRAINT `cases_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cases`
--

LOCK TABLES `cases` WRITE;
/*!40000 ALTER TABLE `cases` DISABLE KEYS */;
INSERT INTO `cases` VALUES (1,'Technical','Technical','Resolved','2023-09-01 06:41:39',1,1),(2,'Technical','No Power Supply','Unresolved','2023-09-01 06:58:30',2,5),(3,'Commercial','High Bills','Unresolved','2023-09-01 14:25:33',1,5),(4,'Technical','Wire Cut','Resolved','2023-09-01 16:10:20',4,2),(5,'Commercial','Adjustment','Unresolved','2023-09-01 16:18:12',6,5),(6,'Technical','Faulty Transformer','Resolved','2023-09-01 16:18:12',9,2),(7,'Commercial','Bills not Received','Unresolved','2023-09-01 16:18:12',11,10),(8,'Commercial','Marketer Not Found','Resolved','2023-09-01 16:18:12',6,10),(9,'Technical','Sparks','Unresolved','2023-09-01 16:18:12',15,2),(10,'Commercial','Adjustment','Unresolved','2023-09-01 16:18:12',15,5),(11,'Technical','Wire Cut','Resolved','2023-09-01 16:18:12',11,1),(12,'Commercial','Suspend Billing','Unresolved','2023-09-01 16:18:12',6,1),(29,'Commercial','Unsolicted Calls','Unresolved','2023-09-02 13:34:44',5,5),(30,'Commercial','Another Unsolicted Call','Unresolved','2023-09-02 13:37:10',5,5),(31,'Technical','Created by Victoria user 2','Unresolved','2023-09-02 13:38:49',5,2),(32,'Technical','ReRouting Case Creation API','Unresolved','2023-09-04 11:54:01',5,2),(37,'Commercial','Troubleshooting Ajax calls','Unresolved','2023-09-06 03:42:02',11,5),(38,'Technical','A technical complaint','Unresolved','2023-09-07 04:27:38',1,2),(39,'Commercial','Added From Frontend','Unresolved','2023-09-07 04:30:39',1,2),(40,'Technical','Testing AJAX','Unresolved','2023-09-07 04:35:50',1,2),(41,'Technical','Added From Frontend','Unresolved','2023-09-07 04:42:16',5,5),(42,'Commercial','Commercial for Frontend','Unresolved','2023-09-07 05:07:50',24,4),(43,'Commercial','Commercial for Frontend','Unresolved','2023-09-07 05:07:56',24,4),(44,'Commercial','Commercial for Frontend','Unresolved','2023-09-07 05:08:01',24,4),(45,'Technical','Added From Frontend','Unresolved','2023-09-07 05:18:40',15,4),(46,'Technical','Added From Frontend','Unresolved','2023-09-07 05:18:46',15,4),(47,'Technical','A technical complaint frontend','Unresolved','2023-09-07 05:19:40',19,4),(48,'Technical','Commercial for Frontend','Unresolved','2023-09-07 05:20:08',19,4),(49,'Technical','Testing AJAX','Unresolved','2023-09-07 05:23:47',27,4),(50,'Commercial','Commercial for Frontend','Unresolved','2023-09-07 05:28:28',2,10),(51,'Technical','Another Case Added From Frontend','Unresolved','2023-09-07 05:28:56',2,10),(52,'Commercial','Added From Frontend','Unresolved','2023-09-07 09:24:48',1,2),(53,'Commercial','First Commercial Subject','Unresolved','2023-09-07 11:51:34',23,2),(54,'Commercial','Commercial Complaint from AJAX','Unresolved','2023-09-08 13:41:25',14,4);
/*!40000 ALTER TABLE `cases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `updates`
--

DROP TABLE IF EXISTS `updates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `updates` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  `case_id` int NOT NULL,
  `update_text` varchar(255) DEFAULT NULL COMMENT 'update text',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `case_id` (`case_id`),
  CONSTRAINT `updates_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `updates_ibfk_2` FOREIGN KEY (`case_id`) REFERENCES `cases` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `updates`
--

LOCK TABLES `updates` WRITE;
/*!40000 ALTER TABLE `updates` DISABLE KEYS */;
INSERT INTO `updates` VALUES (1,'2023-09-02 18:51:49',1,1,'trying to resolve this'),(2,'2023-09-02 18:52:20',2,5,'coming through'),(3,'2023-09-03 06:07:54',2,5,'Creating update for case 5'),(4,'2023-09-03 12:56:40',2,3,'Creating update for case 5'),(5,'2023-09-04 12:26:03',2,3,'Creating update for case 3'),(6,'2023-09-04 14:21:38',2,11,'Creating update for case 11'),(8,'2023-09-04 14:40:23',2,11,'Creating update for case 11'),(9,'2023-09-04 14:41:57',1,11,'Creating update for case 11'),(10,'2023-09-05 02:36:54',1,32,'Creating update for case 32');
/*!40000 ALTER TABLE `updates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'ootaoroju','ootaoroju@example.com','$2b$12$Q8Rb8snel1xAVqNxGLS19.6dRogVIy/wkxwhDkfPkzewG5wS47LPi','2023-08-30 06:19:05'),(2,'vtitiloye','vtitiloye@example.com','$2b$12$Q8Rb8snel1xAVqNxGLS19.6dRogVIy/wkxwhDkfPkzewG5wS47LPi','2023-08-30 18:21:36'),(4,'sabiodun','sabiodun@example.com','$2b$12$6U50wXPYSPyWdzYvG08jO.8T8MyjTJMXoogC3.KXv96xkyXY95HCS','2023-08-31 05:36:28'),(5,'restoreduser','restoreduser@example.com','$2b$12$im/O38jgpNpthaaRCzyumup2IEFrriv2xw7gxIz/ZH5kbwpbQl//C','2023-09-01 06:05:18'),(10,'restoreduser12','restoreduser12@example.com','$2b$12$3P6fkMxo94SHPqqiKHjldelEFANpG8A0FJ/Bd5Xparq23MfhV22IO','2023-09-01 06:06:47');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-09 17:51:50
