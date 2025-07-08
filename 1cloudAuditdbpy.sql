-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 17, 2024 at 05:41 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `3cloudAuditdbpy`
--

-- --------------------------------------------------------

--
-- Table structure for table `auditb`
--

CREATE TABLE `auditb` (
  `id` int(10) NOT NULL auto_increment,
  `FileId` int(10) NOT NULL,
  `OwnerName` varchar(500) NOT NULL,
  `FileName` varchar(500) NOT NULL,
  `Status` varchar(500) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `auditb`
--

INSERT INTO `auditb` (`id`, `FileId`, `OwnerName`, `FileName`, `Status`, `Date`) VALUES
(1, 1, 'aarthi', '3211tamil8.txt', 'File Found Modified', '2024-03-17'),
(2, 2, 'aarthi', '8571tamilmv77.txt', 'File Not Found', '2024-03-17'),
(3, 3, 'aarthi', '659Aichatpy.docx', 'File Found', '2024-03-17'),
(4, 4, 'abi', '551123.docx', 'File Found', '2024-03-17');

-- --------------------------------------------------------

--
-- Table structure for table `fileintb`
--

CREATE TABLE `fileintb` (
  `id` bigint(10) NOT NULL auto_increment,
  `FileName` varchar(250) NOT NULL,
  `Size` varchar(250) NOT NULL,
  `DateTime` varchar(250) NOT NULL,
  `Hash1` varchar(500) NOT NULL,
  `Hash2` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `fileintb`
--

INSERT INTO `fileintb` (`id`, `FileName`, `Size`, `DateTime`, `Hash1`, `Hash2`) VALUES
(1, '3211tamil8.txt', '27.10', 'Sun Mar 17 10:59:41 2024', '0', '5965ABF3CC163A55FE22240DA1A0B876E8D62F69D02F0D00B5F7F0889F695ACE'),
(2, '8571tamilmv77.txt', '3.45', 'Sun Mar 17 10:59:52 2024', '5965ABF3CC163A55FE22240DA1A0B876E8D62F69D02F0D00B5F7F0889F695ACE', 'DCB701E3297592FD73CF03A39D31048E50A5603BDE1C77E1A96608572F41ED60'),
(3, '659Aichatpy.docx', '2749.79', 'Sun Mar 17 11:00:04 2024', 'DCB701E3297592FD73CF03A39D31048E50A5603BDE1C77E1A96608572F41ED60', 'EDB0B93CDC9EBE7E9E1D419F7E5D8A26BC261AFF8A3857DC0BAE5688BCABB0EF'),
(4, '551123.docx', '218.08', 'Sun Mar 17 11:09:21 2024', 'EDB0B93CDC9EBE7E9E1D419F7E5D8A26BC261AFF8A3857DC0BAE5688BCABB0EF', '48CA7761FFB5A186760FE9C28493C9B1015C7A896D50FCF14E48E2C1195C9773');

-- --------------------------------------------------------

--
-- Table structure for table `filetb`
--

CREATE TABLE `filetb` (
  `id` bigint(20) NOT NULL auto_increment,
  `OwnerName` varchar(250) NOT NULL,
  `FileInfo` varchar(500) NOT NULL,
  `FileName` varchar(250) NOT NULL,
  `Pukey` varchar(250) NOT NULL,
  `DateTime` varchar(250) NOT NULL,
  `Hash1` varchar(500) NOT NULL,
  `Hash2` varchar(500) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `filetb`
--

INSERT INTO `filetb` (`id`, `OwnerName`, `FileInfo`, `FileName`, `Pukey`, `DateTime`, `Hash1`, `Hash2`) VALUES
(1, 'aarthi', 'my', '3211tamil8.txt', '031d70fa04feddf04be32a0655be2ec24ca2b74fa3e346ff8bb098d181bee82221', 'Sun Mar 17 10:59:41 2024', '0', '5965ABF3CC163A55FE22240DA1A0B876E8D62F69D02F0D00B5F7F0889F695ACE'),
(2, 'aarthi', 'my', '8571tamilmv77.txt', '034ac578c3bbee957701f68befb45207cd32a5548c2bb125784274843ff7bd3940', 'Sun Mar 17 10:59:52 2024', '5965ABF3CC163A55FE22240DA1A0B876E8D62F69D02F0D00B5F7F0889F695ACE', 'DCB701E3297592FD73CF03A39D31048E50A5603BDE1C77E1A96608572F41ED60'),
(3, 'aarthi', 'mynew', '659Aichatpy.docx', '031ac8c3b71ff517bd3288a7ae7e0bddcf6e7c31ee9f5a20ebe21112a1e8520b23', 'Sun Mar 17 11:00:04 2024', 'DCB701E3297592FD73CF03A39D31048E50A5603BDE1C77E1A96608572F41ED60', 'EDB0B93CDC9EBE7E9E1D419F7E5D8A26BC261AFF8A3857DC0BAE5688BCABB0EF'),
(4, 'abi', 'mmm', '551123.docx', '0326815af06f6aaf150804f2e836fcf6cbf570fe9336d678eb4774d69af4c8ac1f', 'Sun Mar 17 11:09:21 2024', 'EDB0B93CDC9EBE7E9E1D419F7E5D8A26BC261AFF8A3857DC0BAE5688BCABB0EF', '48CA7761FFB5A186760FE9C28493C9B1015C7A896D50FCF14E48E2C1195C9773');

-- --------------------------------------------------------

--
-- Table structure for table `ownertb`
--

CREATE TABLE `ownertb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `LoginKey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `ownertb`
--

INSERT INTO `ownertb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`, `Status`, `LoginKey`) VALUES
(1, 'aarthi', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'aarthi', 'aarthi', 'Active', '6612'),
(2, 'abi', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'abi', 'abi', 'Active', '8793');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `LoginKey` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `Address`, `UserName`, `Password`, `Status`, `LoginKey`) VALUES
(1, 'sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san', 'Active', '3598');

-- --------------------------------------------------------

--
-- Table structure for table `userfiletb`
--

CREATE TABLE `userfiletb` (
  `id` bigint(20) NOT NULL auto_increment,
  `FileId` varchar(250) NOT NULL,
  `OwnerName` varchar(250) NOT NULL,
  `Filename` varchar(250) NOT NULL,
  `PrKey` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `userfiletb`
--

INSERT INTO `userfiletb` (`id`, `FileId`, `OwnerName`, `Filename`, `PrKey`, `UserName`, `Status`) VALUES
(1, '1', 'san', '264sad.png', '037dc11012bcf978a2a29142fe0f597cb02d562d0573eeef574f656a9035e337c6', 'san', 'Approved');
