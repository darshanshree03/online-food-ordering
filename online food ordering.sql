create database online_food_order;
use online_food_order;


create table customer_details (custid int auto_increment primary key, custname varchar(30), phno int, email varchar(40), address varchar(100), password char(4));
desc customer_details;
select * from customer_details;
alter table customer_details drop custid;
alter table customer_details add custid int auto_increment primary key first;
alter table customer_details modify column password char(8);
alter table customer_details add password varchar(30);
drop table customer_details;
alter table customer_details modify column phno char(10);


create table breakfast (foodid char(3) primary key,foodname varchar(30), price int);
select * from breakfast;
insert into breakfast value ('01b', 'idli', 25);
insert into breakfast value ('02b', 'upma', 20);
insert into breakfast value ('03b', 'pongal', 25);
insert into breakfast value ('04b', 'plaindosa', 35);
insert into breakfast value ('05b', 'masaldosa', 45);
insert into breakfast value ('06b', 'ravadosa', 45);
insert into breakfast value ('07b', 'oniondosa', 50);
insert into breakfast value ('08b', 'plain utappam', 35);
insert into breakfast value ('09b', 'onion utappam', 45);
insert into breakfast value ('10b', 'chapati', 40);
insert into breakfast value ('11b', 'parota', 45);
insert into breakfast value('12b','puttu',45);
insert into breakfast value('13b','idiyapam',45);
insert into breakfast value('14b','poori',45);
insert into breakfast value('15b','bread toast',40);
insert into breakfast value('16b','veg sandwich',40);
insert into breakfast value('17b','cheese sandwhich',45);
drop table breakfast;

create table lunch (foodid char(3) primary key,foodname varchar(30), price int);
insert into lunch value('01l','pongal',25);
insert into lunch value('02l','kichady',20);
insert into lunch value('03l','chapati',40);
insert into lunch value('04l','aloo paratha',50);
insert into lunch value('05l','veg noodles','30');
insert into lunch value('06l','gobi noodles','45');
insert into lunch value('07l','mushroom noodles','45');
insert into lunch value('08l','mini meals','40');
insert into lunch value('09l','meals','50');
insert into lunch value('10l','veg biriyani','45');
insert into lunch value('11l','mushroom biriyani','45');

insert into lunch value('012','veg fried rice','45','avail');
insert into lunch value('013','chilli garlic fried rice','50','avail');
insert into lunch value('014','spicy cottage cheese rice','50','avail');
insert into lunch value('015','panner fried rice','45','avail');
insert into lunch value('016','baby corn rice','45','avail');
insert into lunch value('017','gobi rice','40','avail');
insert into lunch value('018','jeera rice','40','avail');
insert into lunch value('019','ghee rice','40','avail');
insert into lunch value('020','peas pulao','50','avail');
insert into lunch value('021','puliogare','35','avail');
select * from lunch;
update lunch set price='40' where foodid='020';
drop table lunch;
delete from lunch where foodid='05l';

create table starters(foodid char(3),foodname varchar(40), price int);
insert into starters value('01s','baby corn soup',80);
insert into starters value('02s','msuhroom soup',80);
insert into starters value('03s','tomato soup',70);
insert into starters value('04s','veg soup',80);
insert into starters value('05s','baby corn manchurian',90);
insert into starters value('06s','panner manchurian',90);
insert into starters value('07s','gobi manchurian',70);
insert into starters value('08s','mushroom manchurian',90);
insert into starters value('09s','panner samosa',30);
insert into starters value('10s','mushroom samosa',30);
insert into starters value('11s','onion samosa',20);
insert into starters value('12s','potato samosa',20);
insert into starters value('13s','noodles samosa',30);
insert into starters value('14s','onion pakoda',30);
insert into starters value('15s','medhu vadai',20);
insert into starters value('16s','masal vadai',10);
select * from starters;

create table sales (custid int, custname varchar(40),date datetime default now(), foodids varchar(1000), bill int,address varchar(100));
desc sales;
select * from sales;