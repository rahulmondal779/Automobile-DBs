-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 05, 2023 at 09:32 PM
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
CREATE DATABASE automobile;
use automobile;
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
(5, 'admin@gmail.com', 'admin', '7531598526', 'Owner', 'DB01PR5006'),
(9, 'adi@gmail.com', 'adi', '7531598526', 'Bangalore', 'DB01PR5008');

-- --------------------------------------------------------

--
-- Table structure for table `customer_vehicle`
--

CREATE TABLE `customer_vehicle` (
  `cvid` int(11) NOT NULL,
  `vehicle_id` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `vehicle_name` varchar(20) NOT NULL,
  `model` varchar(20) NOT NULL,
  `About` mediumtext NOT NULL,
  `color` varchar(1000) NOT NULL,
  `spec` varchar(1000) NOT NULL,
  `num_plate` varchar(50) NOT NULL,
  `warranty` date NOT NULL,
  `manufacture_year` year(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_vehicle`
--

INSERT INTO `customer_vehicle` (`cvid`, `vehicle_id`, `email`, `vehicle_name`, `model`, `About`, `color`, `spec`, `num_plate`, `warranty`, `manufacture_year`) VALUES
(2, 'DB01PR5006', 'admin@gmail.com', 'BMW', 'BMW 5 Series Sedan P', 'The BMW 5 series is here with the power to take you farther. Faster. Best-in-class acceleration that sets you apart from the rest. Adaptive suspension that lets you play with every twist and turn. Coupled with the most advanced driver assistance systems and the BMW Laserlight, it keeps you ahead of the pack. Every single day.', 'Blue', 'Speed', 'HR26DQ1316', '2024-11-01', 2015),
(8, 'DB01PR8807', 'admin@gmail.com', 'SUV', 'Tata Nexon', 'A sport utility vehicle is a car classification that combines elements of road-going passenger cars with features from off-road vehicles, such as raised ground clearance and four-wheel drive. There is no commonly agreed-upon definition of an SUV and usage of the term varies between countries.', 'Black', 'Speed', 'HR26DQ1317', '2032-12-10', 2021),
(9, 'DB01PR5008', 'admin@gmail.com', 'Mahindra', 'New Mahindra Scorpio', 'The All-New Scorpio-N makes every drive an experience with its unmissable design, thrilling performance, advanced technology, intuitive features, superior comfort & safety. It truly is the Big Daddy of SUVs.', 'Black', 'Fuel tank capacity: 57 L', 'HR26DQ1325', '2031-12-31', 2022);

-- --------------------------------------------------------

--
-- Table structure for table `customer_vehicle_service`
--

CREATE TABLE `customer_vehicle_service` (
  `cvs_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `vehicle_id` varchar(20) NOT NULL,
  `num_plate` varchar(10) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `manufacture` date NOT NULL,
  `exp_date` date NOT NULL,
  `textarea` varchar(1000) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_vehicle_service`
--

INSERT INTO `customer_vehicle_service` (`cvs_id`, `name`, `email`, `vehicle_id`, `num_plate`, `description`, `manufacture`, `exp_date`, `textarea`, `status`) VALUES
(17, 'rahul', 'admin@gmail.com', 'None', 'HR26DQ1316', 'Regular Service', '2022-12-30', '2027-07-30', '', 'Done'),
(18, 'test123', 'adi@gmail.com', 'None', 'No Vehicle', 'Parts Replacement', '2023-01-29', '2023-01-25', '', '');



-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `sid` int(11) NOT NULL,
  `services_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`sid`, `services_name`) VALUES
(1, 'Regular Service'),
(2, 'Engine Service'),
(3, 'Tyre Check- Up/Repair'),
(4, 'Transmission Check - Up/Repair'),
(6, 'Oil Check'),
(7, 'Lubricants and Fabricants Check Up'),
(8, 'AC Vent,Coolant,Temperature Check - Up/Repair'),
(9, 'Interior Cleaning'),
(10, 'Steering Throttle Check - Up/Repair'),
(11, 'Gear throttle Check - Up/Repair'),
(12, 'Electric Materials Check - Up/Repair'),
(13, 'Sensors and Cameras Check - Up/Repair'),
(14, 'Acceleration Issure'),
(15, 'Automation Check - Up/Repair'),
(16, 'General Wash'),
(17, 'Polishing and Coating'),
(18, 'Parts Replacement'),
(19, 'Battery Checking'),
(20, 'Break Service');

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
(8, 'admin@gmail.com', 'admin', 'pbkdf2:sha256:260000$StZfGmuFTSZ8y7PA$bd73aba921cd4d7898c4fca974d7d959e395fdfa580a9a6e09abb611e419c27b'),
(11, 'adi@gmail.com', 'adi', 'pbkdf2:sha256:260000$qSf2CtJ5AWxFeeu7$678b4d9ade89f79f33f2243ed564b5f40b2b3df4fa6757d00d8632af644559bf'),
(12, '', '', 'pbkdf2:sha256:260000$xKsVmInK95kujsb4$d5664867c04031796ea852e7fc387b946f4b94f198418a44fb077fcc5ed80a83');

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
-- Indexes for table `customer_vehicle_service`
--
ALTER TABLE `customer_vehicle_service`
  ADD PRIMARY KEY (`cvs_id`);

--
-- Indexes for table `cust_bill`
--
ALTER TABLE `cust_bill`
  ADD PRIMARY KEY (`b_id`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`sid`);

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
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `customer_vehicle`
--
ALTER TABLE `customer_vehicle`
  MODIFY `cvid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `customer_vehicle_service`
--
ALTER TABLE `customer_vehicle_service`
  MODIFY `cvs_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `cust_bill`
--
ALTER TABLE `cust_bill`
  MODIFY `b_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `sid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
