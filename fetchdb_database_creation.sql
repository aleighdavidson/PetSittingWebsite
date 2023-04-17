create database fetchdb;

use fetchdb;

create table user(
	user_id int auto_increment not null primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    city varchar(50) not null,
    phone varchar(20) not null,
    email varchar(254) not null,
    password varchar(100) not null,
    user_type enum('Owner', 'Sitter') not null,
    bio text
    );

create table dog_type(
	dog_type_id int auto_increment not null primary key,
    dog_type varchar(50) not null,
    description text not null
    );

create table dog(
	dog_id int auto_increment not null primary key,
    user_id int not null,
    dog_name varchar(50) not null,
    dog_type_id int not null,
    description text,
    foreign key(user_id) references user(user_id),
    foreign key(dog_type_id) references dog_type(dog_type_id)
    );

create table dog_photos(
	photo_id int auto_increment not null primary key,
    dog_id int not null,
    photo blob not null,
    foreign key(dog_id) references dog(dog_id)
    );
    