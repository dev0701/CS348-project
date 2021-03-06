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
  `num_employees` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `City` (`city_name`, `office_address`,`num_employees`) VALUES
('New York', '111 8th Ave, New York, NY 10011',2),
('San Francisco', '345 Spear St, San Francisco, CA 94105',3);

CREATE TABLE IF NOT EXISTS `Skills` (
  `employee_id` int(10) NOT NULL,
  `skill_name` varchar(50) NOT NULL,
  `years_of_experience` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `Skills` (`employee_id`, `skill_name`, `years_of_experience`) VALUES
(0001,"PROJECT_MANAGEMENT", 20),
(0002,"DATABASE_MANAGEMENT", 5),
(0003,"FRONTEND_PROGRAMMING", 8),
(0004,"CODE_REVIEWING", 9),
(0005,"BACKEND_PROGRAMMING", 16);


CREATE TABLE IF NOT EXISTS `Department` (
  `department_id` int(10) NOT NULL,
  `department_name` varchar(50) NOT NULL,
  `dept_loc_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `Department` (`department_id`,`department_name`,`dept_loc_id`) VALUES
(1,"MONETIZATION", 1),
(2,"RESEARCH",2);


CREATE TABLE IF NOT EXISTS `Dpt_Location` (
  `dpt_loc_id` int(10) NOT NULL,
  `city_name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `Dpt_Location` (`dpt_loc_id`,`city_name`,`address`) VALUES
(1,'New York','111 8th Ave, New York, NY 10011'),
(2,'San Francisco','345 Spear St, San Francisco, CA 94105');


DELIMITER //
create procedure ReturnAllEmployees()
begin
SELECT * FROM Employee;
end
//

DELIMITER //
create procedure sortBySalary()
begin
SELECT * FROM Employee ORDER BY salary DESC;
end
//

