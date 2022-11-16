-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 16, 2022 at 05:48 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `automobile`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cid` int(11) NOT NULL,
  `email` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `vehicle_id` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cid`, `email`, `name`, `mobile`, `address`, `vehicle_id`) VALUES
(1, 'test123@gmail.com', 'rahul', '8523697412', 'ljbjbjhb', 'DB01PR5006'),
(2, 'test@gmail.com', 'mohan', '7898524561', 'retgeffdgvdsfbsfd', 'DB01PR8807'),
(4, 'rahulmondal779@gmail', 'rahul', '7531598526', 'rtwerwer', 'DB01PR5008');

-- --------------------------------------------------------

--
-- Table structure for table `customer_vehicle`
--

CREATE TABLE `customer_vehicle` (
  `cvid` int(11) NOT NULL,
  `vehicle_id` varchar(20) NOT NULL,
  `cust_id` int(11) NOT NULL,
  `vehicle_name` varchar(20) NOT NULL,
  `model` varchar(20) NOT NULL,
  `color` varchar(1000) NOT NULL,
  `spec` varchar(1000) NOT NULL,
  `num_plate` varchar(50) NOT NULL,
  `warranty` date NOT NULL,
  `manufacture_year` year(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_vehicle`
--

INSERT INTO `customer_vehicle` (`cvid`, `vehicle_id`, `cust_id`, `vehicle_name`, `model`, `color`, `spec`, `num_plate`, `warranty`, `manufacture_year`) VALUES
(1, 'DB01PR5006', 1, 'BMW', 'BMW 5 Series Sedan P', 'Blue', 'Speed', 'HR26DQ1316', '2023-11-01', 2015);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `email` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `username`, `password`) VALUES
(2, 'test123@gmail.com', 'test', 'pbkdf2:sha256:260000$xSbzTKdQrNOr2RBk$6ffbff1ae32e88f1bc2154099f41609522e1dc6fe73465ff5c8decd38994c3f8'),
(5, 'test@gmail.com', 'test', 'pbkdf2:sha256:260000$frXFCsQsCYxncXbK$2478d2ecddb47b2fbcc08b8aeb607f777e90cb67fdd6d2b98857f80579cf573c'),
(6, 'bala@gmail.com', 'Balaji', 'pbkdf2:sha256:260000$hlPNFe4iJn8gAPKI$d78870df67449c28338411d8331d3979eb9a5c868c1761e8a3fdaa7af1cf47c1'),
(7, 'rahulmondal779@gmail', 'rahul', 'pbkdf2:sha256:260000$mkaFdWvWdiRNLjbC$c2d34ace72499031590974c74a8402f0d5315310e12edc7e31725a3bea1fbba3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cid`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `customer_vehicle`
--
ALTER TABLE `customer_vehicle`
  ADD PRIMARY KEY (`cvid`),
  ADD UNIQUE KEY `vehicle_id` (`vehicle_id`),
  ADD UNIQUE KEY `num_plate` (`num_plate`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `customer_vehicle`
--
ALTER TABLE `customer_vehicle`
  MODIFY `cvid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
