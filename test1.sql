# create database userinfo character set utf8mb3
use test;
select database();
show databases;
show create database test;
#drop database 
use userinfo;
create table userinfo(id double, name varchar(30), sex char(1), age int);
alter table userinfo add userdes varchar(30);
desc userinfo;
show create table userinfo;

use test;
desc test.useraccount;

alter table useraccount change name username varchar(20);
alter table useraccount modify username varchar(40);
insert into useraccount(id,username,password)  values(55,'张三','123456');
select * from useraccount order by id asc;

use userinfo;
desc userinfo.userinfo;
create view view_userinfo1 (s_name, s_sex, s_userdes) as select name, sex, userdes from userinfo;
insert into userinfo values (1,'zxz', '男', 18, '测试数据');

create table productinfo (id int, pname varchar(20), price int,  primary key(id) );
create view view_test (s_id, s_sex, s_pname) as select id, sex, pname from userinfo, productinfo;
