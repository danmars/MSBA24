CREATE DATABASE  IF NOT EXISTS `zagi_retail` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `zagi_retail`;
-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: zagi_retail
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `checkoutsystems`
--

DROP TABLE IF EXISTS `checkoutsystems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `checkoutsystems` (
  `CSID` varchar(3) NOT NULL,
  `CSystem` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`CSID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `checkoutsystems`
--

LOCK TABLES `checkoutsystems` WRITE;
/*!40000 ALTER TABLE `checkoutsystems` DISABLE KEYS */;
INSERT INTO `checkoutsystems` VALUES ('AC','Self Service'),('CR','Cashiers'),('MX','Mixed');
/*!40000 ALTER TABLE `checkoutsystems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `layout`
--

DROP TABLE IF EXISTS `layout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `layout` (
  `Layoutid` varchar(3) NOT NULL,
  `Layout` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Layoutid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `layout`
--

LOCK TABLES `layout` WRITE;
/*!40000 ALTER TABLE `layout` DISABLE KEYS */;
INSERT INTO `layout` VALUES ('M','Modern'),('T','Traditional');
/*!40000 ALTER TABLE `layout` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `store` (
  `store_id` varchar(3) NOT NULL,
  `storesize` int(11) DEFAULT NULL,
  `CSID` varchar(3) DEFAULT NULL,
  `Layoutid` varchar(3) DEFAULT NULL,
  `store_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`store_id`),
  KEY `layout_idx` (`Layoutid`),
  KEY `CSID_idx` (`CSID`),
  CONSTRAINT `CSID` FOREIGN KEY (`CSID`) REFERENCES `checkoutsystems` (`csid`),
  CONSTRAINT `layout` FOREIGN KEY (`Layoutid`) REFERENCES `layout` (`layoutid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store`
--

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES ('S1',51000,'CR','M','ChicagoLandNorth'),('S2',35000,'CR','T','ChicagoLandSouth'),('S3',55000,'MX','T','TriState');
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-05 14:43:14
CREATE DATABASE  IF NOT EXISTS `zagi_small` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `zagi_small`;
-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: zagi_small
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `category` (
  `categoryid` char(2) NOT NULL,
  `categoryname` varchar(25) NOT NULL,
  PRIMARY KEY (`categoryid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES ('CP','Camping'),('FW','Footwear');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `customer` (
  `customerid` char(7) NOT NULL,
  `customername` varchar(15) NOT NULL,
  `customerzip` char(5) NOT NULL,
  PRIMARY KEY (`customerid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('1-2-333','Tina','60137'),('2-3-444','Tony','60611'),('3-4-555','Pam','35401');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `product` (
  `productid` char(3) NOT NULL,
  `productname` varchar(25) NOT NULL,
  `productprice` decimal(7,2) NOT NULL,
  `vendorid` char(2) NOT NULL,
  `categoryid` char(2) NOT NULL,
  PRIMARY KEY (`productid`),
  KEY `vendorid` (`vendorid`),
  KEY `categoryid` (`categoryid`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`vendorid`) REFERENCES `vendor` (`vendorid`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`categoryid`) REFERENCES `category` (`categoryid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('1X1','Zzz Bag',100.00,'PG','CP'),('2X2','Easy Boot',70.00,'MK','FW'),('3X3','Cosy Sock',15.00,'MK','FW'),('4X4','Dura Boot',90.00,'PG','FW'),('5X5','Tiny Tent',150.00,'MK','CP'),('6X6','Biggy Tent',250.00,'MK','CP');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `region`
--

DROP TABLE IF EXISTS `region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `region` (
  `regionid` char(1) NOT NULL,
  `regionname` varchar(25) NOT NULL,
  PRIMARY KEY (`regionid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region`
--

LOCK TABLES `region` WRITE;
/*!40000 ALTER TABLE `region` DISABLE KEYS */;
INSERT INTO `region` VALUES ('C','Chicagoland'),('T','Tristate');
/*!40000 ALTER TABLE `region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salestransaction`
--

DROP TABLE IF EXISTS `salestransaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `salestransaction` (
  `tid` varchar(8) NOT NULL,
  `customerid` char(7) NOT NULL,
  `storeid` varchar(3) NOT NULL,
  `tdate` date NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `customerid` (`customerid`),
  KEY `storeid` (`storeid`),
  CONSTRAINT `salestransaction_ibfk_1` FOREIGN KEY (`customerid`) REFERENCES `customer` (`customerid`),
  CONSTRAINT `salestransaction_ibfk_2` FOREIGN KEY (`storeid`) REFERENCES `store` (`storeid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salestransaction`
--

LOCK TABLES `salestransaction` WRITE;
/*!40000 ALTER TABLE `salestransaction` DISABLE KEYS */;
INSERT INTO `salestransaction` VALUES ('T111','1-2-333','S1','2013-01-01'),('T222','2-3-444','S2','2013-01-01'),('T333','1-2-333','S3','2013-01-02'),('T444','3-4-555','S3','2013-01-02'),('T555','2-3-444','S3','2013-01-02');
/*!40000 ALTER TABLE `salestransaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soldvia`
--

DROP TABLE IF EXISTS `soldvia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `soldvia` (
  `productid` char(3) NOT NULL,
  `tid` varchar(8) NOT NULL,
  `noofitems` int(11) NOT NULL,
  PRIMARY KEY (`productid`,`tid`),
  KEY `tid` (`tid`),
  CONSTRAINT `soldvia_ibfk_1` FOREIGN KEY (`productid`) REFERENCES `product` (`productid`),
  CONSTRAINT `soldvia_ibfk_2` FOREIGN KEY (`tid`) REFERENCES `salestransaction` (`tid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soldvia`
--

LOCK TABLES `soldvia` WRITE;
/*!40000 ALTER TABLE `soldvia` DISABLE KEYS */;
INSERT INTO `soldvia` VALUES ('1X1','T111',1),('1X1','T333',1),('2X2','T222',1),('2X2','T444',2),('3X3','T333',5),('4X4','T444',1),('4X4','T555',4),('5X5','T555',2),('6X6','T555',1);
/*!40000 ALTER TABLE `soldvia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `store` (
  `storeid` varchar(3) NOT NULL,
  `storezip` char(5) NOT NULL,
  `regionid` char(1) NOT NULL,
  PRIMARY KEY (`storeid`),
  KEY `regionid` (`regionid`),
  CONSTRAINT `store_ibfk_1` FOREIGN KEY (`regionid`) REFERENCES `region` (`regionid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store`
--

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES ('S1','60600','C'),('S2','60605','C'),('S3','35400','T');
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor`
--

DROP TABLE IF EXISTS `vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `vendor` (
  `vendorid` char(2) NOT NULL,
  `vendorname` varchar(25) NOT NULL,
  PRIMARY KEY (`vendorid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor`
--

LOCK TABLES `vendor` WRITE;
/*!40000 ALTER TABLE `vendor` DISABLE KEYS */;
INSERT INTO `vendor` VALUES ('MK','Mountain King'),('PG','Pacifica Gear');
/*!40000 ALTER TABLE `vendor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-05 14:43:14
