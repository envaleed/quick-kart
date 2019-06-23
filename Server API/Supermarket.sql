-- MySQL dump 10.13  Distrib 8.0.16, for macos10.14 (x86_64)
--
-- Host: localhost    Database: supermarket
-- ------------------------------------------------------
-- Server version	5.7.26

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
-- Table structure for table `grocery`
--

DROP TABLE IF EXISTS `grocery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `grocery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(60) NOT NULL,
  `grocery_type` varchar(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `image` varchar(80) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `isle_no` int(11) NOT NULL,
  `content` varchar(255) NOT NULL,
  `tag` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grocery`
--

LOCK TABLES `grocery` WRITE;
/*!40000 ALTER TABLE `grocery` DISABLE KEYS */;
INSERT INTO `grocery` VALUES (1,'Bananas','Fruit',50,'https://images-na.ssl-images-amazon.com/images/I/71gI-IUNUkL._SY355_.jpg',300.00,1,'One dozen freshly grown bananas. Imported from Jamaica','#bananas, #fruit #banana #yellow #smoothie'),(2,'Apples','Fruit',30,'https://i.imgur.com/nGqHrBl.jpg',203.00,1,'Half dozen freshly grown apples. Imported from Jamaica','#apples, #fruit #apple #yellow #smoothie'),(3,'Grapes','Fruit',20,'https://i.imgur.com/oZT6btS.jpg',475.00,1,'500 Grams of freshly grown grapes. Imported from Jamaica','#grapes, #fruit #green #vine #smoothie'),(4,'Broccoli','Vegetable',25,'https://i.imgur.com/9HjNJWz.jpg',192.00,2,'500 Grams freshly grown broccoli. Imported from Jamaica','#broccoli, #vegetable #green'),(5,'Lettuce','Vegetable',47,'https://i.imgur.com/iYQ9L5E.jpg',49.00,2,'500 Grams freshly grown lettuce. Imported from Jamaica','#lettuce #vegetable #green'),(6,'Carrot','Vegetable',22,'https://i.imgur.com/fE3RxGB.jpg',54.00,2,'500 Grams freshly grown carrot. Imported from Jamaica','#carrot #vegetable #orange'),(7,'Yam','Staple',69,'https://i.imgur.com/pGMhcj3.png',123.00,3,'500 Grams freshly grown yams. Imported from Jamaica','#yams #starch #ground provision #yam'),(8,'Rice','Staple',42,'https://i.imgur.com/WBAysUK.jpg',84.00,3,'1 Kilogram freshly grown rice. Imported from Jamaica','#rice #grain #whole #white #parboiled #starch'),(9,'Flour','Staple',88,'https://i.imgur.com/Tk2oR4J.jpg',46.00,3,'1 Kilogram freshly grown flour. Imported from Jamaica','#starch #flour #wheat #white #allpurpose #baking #bake'),(10,'Chuck Steak','Meat',12,'https://i.imgur.com/qs34b6n.jpg',673.00,4,'500 Grams freshly reared cattle. Imported from Jamaica','#cow #cattle #steak #chuck #kosher #meat #protein'),(11,'Whole Chicken','Meat',32,'https://i.imgur.com/FTwSwjo.jpg',1211.00,4,'One freshly reared chicken. Imported from Jamaica','#whole #chicken #meat #protein #kosher'),(12,'Pork Chops','Meat',2,'https://i.imgur.com/drZoB4F.jpg',520.00,4,'Three freshly chopped slices of Pork. Imported from Jamaica','#pork #chops #pig #meat #protein'),(13,'Black Beans','Legumes',34,'https://i.imgur.com/zdRoMFv.jpg',100.00,5,'500 Grams freshly grown beans. Imported from Jamaica','#beans #black #dry #legumes #nuts'),(14,'Red Peas','Legumes',22,'https://i.imgur.com/GexDt8T.jpg',100.00,5,'500 Grams freshly grown beans. Imported from Jamaica','#beans #red #peas #dry #legumes #nuts'),(15,'Broad Beans','Legumes',33,'https://i.imgur.com/mncCtMW.jpg',100.00,5,'500 Grams freshly grown beans. Imported from Jamaica','#beans #broad #dry #legumes #nuts'),(16,'Whole Milk','Dairy',19,'https://i.imgur.com/kTvtlFy.jpg',320.00,6,'20 OZ of fresh cows milk. Imported from Jamaica','#milk #cow #fat #lactose #bottle'),(17,'Mozzarella','Dairy',29,'https://i.imgur.com/vl3ThIj.jpg',1024.00,6,'500 Grams of cheese. Imported from Jamaica','#cheese #mozzarella #shredded #sandwich #bread'),(18,'Butter','Dairy',28,'https://i.imgur.com/cMm8QER.jpg',404.00,6,'500 Grams of butter. Imported from Jamaica','#butter #fat #cholestorol #bread'),(19,'Spam','Canned Goods',44,'https://i.imgur.com/VtOwFdA.jpg',801.00,7,'Canned Luncheon Meat. Imported from America','#spam #fat #pork #popular #meat #protein #can #canned'),(20,'Ackee','Canned Goods',28,'https://imgur.com/Vc2OM1C',304.00,7,'Canned Ackee. Imported from Jamaica','#ackee #popular #fat #cholestorol #jamaican'),(21,'Breadfruit','Canned Goods',38,'https://i.imgur.com/GewclBX.jpg',240.00,6,'Canned Breadfruit. Imported from Jamaica','#bread fruit #breadfruit #bread #popular'),(22,'Baguette','Breads',28,'https://i.imgur.com/tZmsvfJ.jpg',300.00,6,'Freshly Baked Baguette','#popular #baguette #french #sour dough #bread'),(23,'Moringa Powder','Spices',52,'https://i.imgur.com/1hwLLLA.jpg',252.00,6,'Moringa Powder. Imported from Jamaica','#popular #moringa #herbs #powder #herb #moringa powder'),(24,'Chilli Powder','Spices',12,'https://i.imgur.com/SDBZhGq.jpg',245.00,6,'Chilli Powder. Imported from Jamaica','#popular #chilli #herbs #spices #powder #chilli powder'),(25,'Hershey Milk Chocolate','Dairy',23,'https://i.imgur.com/q5HkOgD.jpg',204.00,6,'Hersheys Chocolate Bar. Imported from Jamaica','#chocolate #hershey #hersheys #popular #fat #cholestorol #bar'),(26,'Extra Virgin Olive Oil','Oils',28,'https://i.imgur.com/07JlZCQ.jpg',1404.00,6,'Bottle of Extra Virgin Olive Oil. Imported from Jamaica','#oil #popular #olive #extra #virgin #fat #cholestorol');
/*!40000 ALTER TABLE `grocery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `pickupcode` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'Oats',3,'list'),(2,'Bread',6,'23456789'),(3,'Trix Cereal',1,'4508d2ee-b64c-a9bc-a9bb-74fb1624b991nill'),(7,'Lasco Milk',3,'4508d2ee-b64c-a9bc-a9bb-74fb1624b991nill'),(8,'National Bread',2,'4508d2ee-b64c-a9bc-a9bb-74fb1624b991nill'),(9,'Serge Milk',2,'4508d2ee-b64c-a9bc-a9bb-74fb1624b991nill'),(10,'Grace Mackerel',5,'4508d2ee-b64c-a9bc-a9bb-74fb1624b991nill');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(320) NOT NULL,
  `password_hash` char(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Person1','example@example.com','password'),(2,'Stop4U','something@example.com','pbkdf2:sha256:150000$YAMIurlX$c26dc2cc8e866ac0faf69253ec00cc1d91678f95a15aa9212bb61dcff385a44f'),(3,'deji','deji@gmail.com','pbkdf2:sha256:150000$xlWk3FoO$5f47de130e88dd3b34a2d0dc1e6bd9db15653c1416ca30b7cb3f1e7dd4b37420'),(4,'kenny','kenn@sixnine.com','pbkdf2:sha256:150000$zKNhmf2S$78e7eac68b81a2535a364bb06db7210093af0a865f0c9e44d17855c600b7e7c6'),(5,'misch','misch@gmail.com','pbkdf2:sha256:150000$NrK4EoFc$460c236d609a738567b1ed5e0d1fb4f0c92719f7d99ea604a5ef49ac1bcf1f57'),(6,'dejeon','dejeon.deji@gmail.com','pbkdf2:sha256:150000$96zl3Aax$3cef82488f563aaa044a60795f3fc2748f4dd48d05ae4819da6df191ae773472'),(7,'soul','pure@soulmail.com','pbkdf2:sha256:150000$HZEDVjJ4$7ce76fbc3e7f8ad49e5608d5d9ad40b2ce759d8110fb2f906ded0c109640fc31'),(8,'user1','user1@gmail.com','pbkdf2:sha256:150000$L5geSlZ5$ac28649e805ca0d6900cdbea7176ee3c296b4771d87ed155e43e3c6bd507618f'),(9,'otto','otto@open.gmail','pbkdf2:sha256:150000$kIOgFs2g$53aaf5fc163d941f9ed08b92a32b5704373778eb6911b0c57e9d95f78778c55b'),(10,'hshd','gegdh','pbkdf2:sha256:150000$wL1U6fiW$27fba2f24169f5cec5f9ed3d479525baa4e7ada06124b545267612f093c3bfe2'),(11,'hshsh','usheh','pbkdf2:sha256:150000$6nWHRV0j$526afcf7f082967960d8eaabb4d22c846396b8ee4501431eeaa7119bf6be1daa'),(12,'davina','dav@gmail.com','pbkdf2:sha256:150000$x0PnAuNW$e816c3415adc1c223a8f2ca1c9c18efa318b44618178ce54966f37ade505eeaa'),(13,'fortest','fortest@gmail','pbkdf2:sha256:150000$ptWzYGTB$e3682fd2a8b2bd031817f4344597e477ae2bd4ae94506b24afdc71f00104098f'),(14,'max','max@yahoo.com','pbkdf2:sha256:150000$VjWu2UHm$b0117d167f4b617129901565a689a99b475324ede8238d0f50cf98b7d8116f6a'),(15,'username','someuser@somemail.com','pbkdf2:sha256:150000$t3nNfhA1$fac34a7a180ced55f97ff82326b2ff9981ca1a29219c13923eda4cc12dee04d4');
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

-- Dump completed on 2019-06-23 19:17:58
