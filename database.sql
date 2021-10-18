-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2021 at 06:45 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mypro_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `project_upload`
--

CREATE TABLE `project_upload` (
  `id` int(11) NOT NULL,
  `status` varchar(100) NOT NULL,
  `project_id` varchar(200) NOT NULL,
  `account_id` varchar(200) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` text NOT NULL,
  `project_category` varchar(200) NOT NULL,
  `project_image` text NOT NULL,
  `create_time` varchar(100) NOT NULL,
  `last_upd_time` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `project_upload`
--

INSERT INTO `project_upload` (`id`, `status`, `project_id`, `account_id`, `title`, `description`, `project_category`, `project_image`, `create_time`, `last_upd_time`) VALUES
(2, '\'#$›`´¾‰ÒwBÄ', 'Y¡—Õk\r€@_£¡p¼59/J€RwÁ¹í[ËÍeÏúÌ', '…]½+Ûp¦Läxa\"SmåŒ•³9ÝæŽÐ—iqX9Š', 'pNÐ¹6,–\nÝ#Jçà¤É<;¼ÂÑ·IÄíw3', 'ë%¨>F¾²¯©y\r€üyìøl¬œº°Ýƒ·aÙêóÁvòªGãMºmÓ?‚O²}T¾¦?eõ\'‘Fz}\\âÏþË¡~0/ã©HÓp¿ê¨Ú©', '¥\Zˆ~þXFÄ¥]L´èª¯ÐÃÒ|Áê¥ïðb‹†í¨', 'dÂÒyÂ0]ì¹%µ{YçeçgââúNÑHc=\Z4`¥»†ëV3ðäæé³×)šF8âè:=Õ>ôxZµ5g–', '#ÑkŠc\rá;•ÛÙsy¹°U?EÀu¡Æƒ\Z2ýy/', '#ÑkŠc\rá;•ÛÙsy¹°U?EÀu¡Æƒ\Z2ýy/'),
(3, '\'#$›`´¾‰ÒwBÄ', 'Â1¬—ž‚—¸Ð\ZaÍÿÀüü.$jÐÄ’\'î»¦ÜI', '…]½+Ûp¦Läxa\"SmåŒ•³9ÝæŽÐ—iqX9Š', '[§g6ÐÝcìñ 3Ód>Ø', 'g}N‚æ±û>³k‚|S0¢Ñ¨Úìë¤\rÁiÆ‹âÿ­ÑìAÇ§ÈV ­ð^\n8ÌS¨ü[þ9ãP¡EŠ\"¡êËÂ«£E<m€á‰ùµGL‘&?¡—ÙfÑÃ$«êOTA¹í‹,nl”ñ8tÜš¦`àuFkàZóli^ìÀ®', '­J¬ŽÇäE¸Ò«ÂŽ	²¼wf„4Læ)tÎ=Ñ<ßòÆ†/ â;/_àÞ<U', '§œO	¥Zeæ‰c(H†7(ž×ÞB,Ó¦Ü ò¹N!y<Ç éO–4g<`xÀòÔ\'÷‘ïŒÕ…l©M”¨]', '¸#Xù¦ \"gË0Ì¯@ƒ“éRQC5!¹’ß¼‚a`›ó', '¸#Xù¦ \"gË0Ì¯@ƒ“éRQC5!¹’ß¼‚a`›ó'),
(4, '\'#$›`´¾‰ÒwBÄ', '<‘+ß5×ÇW…m?»)”Ú\'ÜŒjHšáÌcø†Bp', '…]½+Ûp¦Läxa\"SmåŒ•³9ÝæŽÐ—iqX9Š', 'Eþ—É›è¼‘Ï×´™¡~0/ã©HÓp¿ê¨Ú©', 'eg*$Ž„ôŽ}4\\ $é«î»Ÿ‚ƒRB@©Š“âqj2cK‹~ÆT£ñ\\‹_Ìµ·“­ Ü¾E÷q­ìmŒmï.SYü;Öú(\Z·cPcý§°RžGbélÝ|2Z²A“-R¡E6|÷Ê§O0ÂÄÜ~U)yîZAóËþÊRµnpžë1†èC@Sßžañ/ÊÜŠY_ûÎÂ ãÕ­šªáâYà', '­J¬ŽÇäE¸Ò«ÂŽ	²¼wf„4Læ)tÎ=Ñ<ßòÆ†/ â;/_àÞ<U', '§œO	¥Zeæ‰c(H†7(rJý{;îê3¬\nÒ¥!¬ü±Å¡ —Áçc?zâÌ¤Ô\'÷‘ïŒÕ…l©M”¨]', 'ì>PÚjW°»Ë¼².¢<ÁÒÔ·`Ö›¹Ò(š…m', 'ì>PÚjW°»Ë¼².¢<ÁÒÔ·`Ö›¹Ò(š…m'),
(5, '\'#$›`´¾‰ÒwBÄ', 'ßrmk£@HÀ$GBGc€ÓßjÖ‡äbSëW_r¾T¼', 'ûŽÙ-®.íºÁ©ÌôÅLÄ>ˆ­·S]oïg´ƒ0-', 'Ä[k,Sƒ‘ûjå• 6jD¯,F1šèQVš÷?ùÄR', 'î¢tx54»µÕÁCÃ|g1nÏRVp¥v5E†-ëø?Éø•\0dÐÛ&ìñrù¿äÞ}GbMÿÀÇÝ	²æ1úô\0¯8Suˆ5í`]¦Ú„¢êd7ûæ”hÜwQ™g Úi4ƒ)±¬;@ÖæÉ¡´\n‘“aäÔ…¥ÖÅ!»t', '­J¬ŽÇäE¸Ò«ÂŽ	²¼wf„4Læ)tÎ=Ñ<ßòÆ†/ â;/_àÞ<U', '§œO	¥Zeæ‰c(H†7(Ü°¸¹ÑýýwçÇ[Vø^\0©Î{ÁÌúã¿nÊRXgIæÔ\'÷‘ïŒÕ…l©M”¨]', 'ÅÚu9À¿B\'3çà3}³_•(Q½>4fF Ý0ÚÕ', 'ÅÚu9À¿B\'3çà3}³_•(Q½>4fF Ý0ÚÕ'),
(6, '\'#$›`´¾‰ÒwBÄ', 'ÍãÖü¼û·8õD‚Õ£]í’‘ª™åœ¥yo€ºÃûdŒ', 'ûŽÙ-®.íºÁ©ÌôÅLÄ>ˆ­·S]oïg´ƒ0-', '\0ât¸ÓBskÞÞH‚ý†Û¥žÎóz€2×\'›+CÏ8', '2bA)KEƒ%A/3´”HÄì„n\Zp·tã%aX“ÞpÈ]\'xsA=Ãpx–¬£¿€H7)\\ˆ“Ã’4	á<Ìùi†¢öNï•$%k˜¡âv|¥à&;Ìƒ', '­J¬ŽÇäE¸Ò«ÂŽ	²¼wf„4Læ)tÎ=Ñ<ßG®…Ç½Y›¶üŽQD', '§œO	¥Zeæ‰c(H†7(_çœÙÌHž×\0¡hZÕìÐÌ§{˜DnVUäïÔ\'÷‘ïŒÕ…l©M”¨]', 'AÂç}1“,~º‡z]Ø~ö0ä1_¾DLá¼ÖI‹v®', 'AÂç}1“,~º‡z]Ø~ö0ä1_¾DLá¼ÖI‹v®'),
(7, '\'#$›`´¾‰ÒwBÄ', 'aî\'JizZ£“2ÖÉ™ñ–¶V˜ ·,]c>t8„\\', 'ûŽÙ-®.íºÁ©ÌôÅLÄ>ˆ­·S]oïg´ƒ0-', 'Ç@ãý²o\Zn´³Ú¥ÕéØr¨\nCÅT1µýKé', 'XB)¶“Þ–„äÖ6# ƒý0wÐÕ#a<¶ÓE\n¥=zÅ}ôy<ùØ$*_)æiôÐ¶Y§—zŽPEPû\Z]', '¥\Zˆ~þXFÄ¥]L´èª¯Ð\'lÂØÇB½ÄÚ', '§œO	¥Zeæ‰c(H†7(ZúÚz3‰¾\'˜ùÙB\"*4m¤œRYÔŠgcåß2a4üJÔ\'÷‘ïŒÕ…l©M”¨]', '˜}Æ†Â€Tô\rw›ç„,}Ç!£ðÑ-e\nóè', '˜}Æ†Â€Tô\rw›ç„,}Ç!£ðÑ-e\nóè');

-- --------------------------------------------------------

--
-- Table structure for table `register_account`
--

CREATE TABLE `register_account` (
  `id` int(11) NOT NULL,
  `account_id` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(300) NOT NULL,
  `profile_id` varchar(100) NOT NULL,
  `register_time` varchar(100) NOT NULL,
  `lst_upd_time` varchar(100) NOT NULL,
  `last_activity_time` varchar(100) NOT NULL,
  `pass_upd_time` varchar(100) NOT NULL,
  `login_data` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register_account`
--

INSERT INTO `register_account` (`id`, `account_id`, `status`, `position`, `fname`, `lname`, `email`, `password`, `profile_id`, `register_time`, `lst_upd_time`, `last_activity_time`, `pass_upd_time`, `login_data`) VALUES
(8, '…]½+Ûp¦Läxa\"SmåŒ•³9ÝæŽÐ—iqX9Š', '\'#$›`´¾‰ÒwBÄ', 'Æß¹\ZE³8·Ë£Éf66J', ',W‘eµ}_Gà_‡Û', '\n3éJ&òg¼Ç1gŠñ', 'á!k$rcäÈ¶Ô,Ú2A2¢«L-oþ‚øß¼Je0J', 'Ü<É=´ìÝ2l¥4ºÂïÏÈŒ›Û:¦ùHÚÄ\"¡18²úªŽKœR\'Ô}OÑ\\ø‰³® ‡‹ë˜Èñ3&F\0@Å[ØÛ(Ðªõö»¨äJƒ±‚#ŒØ¦’ROr\\©¦‰Æ@ævšÊ˜µXò\"g‹±rÆnÙûï13“¨*ÈêýQuÝ\'YReþ', ']…Ãûð\rÙ³ÇlMë*M|šÐ’Š(g\\A\'ºÄÖhéºUÿœåŽ›Á¨|ÏR‚§.ŸÉæ/Î¨áéæË\n‘‘', 'ÛJò:™½}|û…¸Iî_ô§çãñÕž¤K-ñá…', 'ÛJò:™½}|û…¸Iî_ô§çãñÕž¤K-ñá…', 'ÛJò:™½}|û…¸Iî_ô§çãñÕž¤K-ñá…', 'ÛJò:™½}|û…¸Iî_ô§çãñÕž¤K-ñá…', '\0‘±ö¯€j?`<—Ø$îw‚¼-© NûgZ³ŒWÓUUVÐÍmH–ù)wªá­zÜ%s›	þmê³n®›íDÎÊnî`´žLZ[æò×€]}ãˆÑ¼©,\'Ï;Eÿ1Wƒlû º)¼ì7–.cÎ%ñ¿ñò¥d(ýßq;¡NtMÕ‘bE‹¨ÊÒ3æhŒ›äÀ«DØÊ:Õ»¿ þøÏ¤¨ÝtwÉy•7.G›UËÛ>'),
(9, 'ûŽÙ-®.íºÁ©ÌôÅLÄ>ˆ­·S]oïg´ƒ0-', '\'#$›`´¾‰ÒwBÄ', 'Æß¹\ZE³8·Ë£Éf66J', 'ÚáÀÉ[iŸ¿†ª£µÅ´4', '¨Ò¶Ç‘­ìÄm\rAŒô·', 'd¬È’°¿íZÄŒLX®ênvQŽ\'”ÆÏì£ÞOÃb-', 'Ü<É=´ìÝ2l¥4ºÂïÏÈŒ›Û:¦ùHÚÄ\"¡18²úªŽKœR\'Ô}OÑ\\ø‰³® ‡‹ë˜Èñ3&F\0@Å[ØÛ(Ðªõö»¨äJƒ±‚#ŒØ¦’ROr\\©¦‰Æ@ævšÊ˜µXò\"g‹±rÆnÙûï13“¨*ÈêýQuÝ\'YReþ', '!Dµ¡µ;lx@8q,–Ý=ì¶Hk-\r—ÿ­ÐŸ´ÞÎÙx‰XHÉB<˜Hb},;Þ·TT«1U°˜&Æ', '½£ëI²oA¨ÆŒ`CZ\Z2qÿsØ{[ÒÂÍ¤?ý', '½£ëI²oA¨ÆŒ`CZ\Z2qÿsØ{[ÒÂÍ¤?ý', '½£ëI²oA¨ÆŒ`CZ\Z2qÿsØ{[ÒÂÍ¤?ý', '½£ëI²oA¨ÆŒ`CZ\Z2qÿsØ{[ÒÂÍ¤?ý', '\0‘±ö¯€j?`<—Ø$îRj[¦’Z‚k\nªò{Y');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `project_upload`
--
ALTER TABLE `project_upload`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register_account`
--
ALTER TABLE `register_account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `project_upload`
--
ALTER TABLE `project_upload`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `register_account`
--
ALTER TABLE `register_account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
