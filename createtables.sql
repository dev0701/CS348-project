CREATE TABLE IF NOT EXISTS `Employee` (
  `employee_id` int(10) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `position` varchar(50) NOT NULL,
  `salary` int(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `department_id` int(5) NOT NULL,
  `password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `Employee` (`employee_id`, `first_name`,`last_name`,`position`,`salary`,`city`,`department_id`,`password`) VALUES
(0001,'Jane','Doe','manager',150000,'New York',01,"password1"),
(0002,'Brandon','Doe','engineer',120000,'New York',01,"password2"),
(0003,'Chad','Lowe','engineer',120000,'San Francisco',02,"password3"),
(0004,'Joe','Rogan','manager',150000,'San Francisco',02,"password4"),
(0005,'Claire','Newborn','engineer', 120000, 'San Francisco',02,"password5");

CREATE TABLE IF NOT EXISTS `City` (
  `city_name` varchar(50) NOT NULL,
  `office_address` varchar(150) NOT NULL,
  `num_employees` int(5) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `City` (`city_name`, `office_address`,`num_employees`) VALUES
('New York', '111 8th Ave, New York, NY 10011',2),
('San Francisco', '345 Spear St, San Francisco, CA 94105',3);

