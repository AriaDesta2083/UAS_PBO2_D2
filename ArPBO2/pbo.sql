-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 20 Jun 2021 pada 09.16
-- Versi server: 10.4.18-MariaDB
-- Versi PHP: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbo`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `username` varchar(100) NOT NULL,
  `pw` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`username`, `pw`) VALUES
('aria', 'ar123'),
('Kel2', 'qwe123');

-- --------------------------------------------------------

--
-- Struktur dari tabel `datagrid`
--

CREATE TABLE `datagrid` (
  `id` int(11) NOT NULL,
  `kodelap` varchar(10) NOT NULL,
  `waktu` varchar(50) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `tim` varchar(50) NOT NULL,
  `tanggal` varchar(50) NOT NULL,
  `nohp` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `datagrid`
--

INSERT INTO `datagrid` (`id`, `kodelap`, `waktu`, `nama`, `tim`, `tanggal`, `nohp`) VALUES
(4, 'Lap03', '12.00 - 14.00', 'Aria', 'Winstreak', '2 Februari 2021', '081222333444'),
(6, 'Lap02', '15.00 - 18.00', 'Prabu', 'ProNiBos', '20 Desember 2022', '087123123000'),
(7, 'Lap02', '10.00 - 11.00', 'Hamid', 'Winstreak', '2 Februari 2021', '081222333444'),
(9, 'Lap03', '16.00 - 18.00', 'Messi', 'WinWIn', '20 Desember 2021', '087123123123'),
(11, 'Lap03', '14.00 - 15.00', 'Ronaldo', 'GOGOGO', '4 April 2021', '089888777666'),
(12, 'Lap02', '16.00 - 18.00', 'Messi', 'WinWIn', '20 Desember 2021', '087123123123'),
(15, 'Lap02', '10:00 - 08:00', 'deden', 'epep', '1April 2021', '092111111111'),
(30, 'Lap02', '10:00 - 12:00', 'Hasbie ', 'DikateamHasbie', '4 April 2022', '081234526182'),
(35, 'Lap01', '10:00 - 08:00', 'adek', 'kakak', '1April 2021', '123131312313'),
(36, 'Lap01', '10:00 - 08:00', 'Ordo', 'Sans Team', '1April 2021', '086567625627'),
(37, 'Lap01', '07:00 - 08:00', 'bedos', 'asd', '1April 2021', '123213312313');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`username`);

--
-- Indeks untuk tabel `datagrid`
--
ALTER TABLE `datagrid`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `datagrid`
--
ALTER TABLE `datagrid`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
