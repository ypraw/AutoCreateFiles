-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jan 24, 2017 at 10:30 PM
-- Server version: 10.1.19-MariaDB
-- PHP Version: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `njajal`
--

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE `files` (
  `id_files` int(255) NOT NULL,
  `name_files` varchar(100) NOT NULL,
  `time_files` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `files`
--

INSERT INTO `files` (`id_files`, `name_files`, `time_files`) VALUES
(1, 'newFile_1-20170125-034837.txt', '2017-01-24 20:48:36'),
(2, 'newFile_2-20170125-034838.txt', '2017-01-24 20:48:36'),
(3, 'newFile_3-20170125-034839.txt', '2017-01-24 20:48:36'),
(4, 'newFile_4-20170125-034840.txt', '2017-01-24 20:48:36'),
(5, 'newFile_5-20170125-034841.txt', '2017-01-24 20:48:36'),
(6, 'newFile_6-20170125-041007.txt', '2017-01-24 21:10:07'),
(7, 'newFile_7-20170125-041143.txt', '2017-01-24 21:11:43'),
(8, 'newFile_8-20170125-041228.txt', '2017-01-24 21:12:28'),
(9, 'newFile_9-20170125-041446.txt', '2017-01-24 21:14:46'),
(10, 'newFile_10-20170125-041447.txt', '2017-01-24 21:14:46');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`id_files`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
