create database fetchdb;

use fetchdb;

create table user(
	id int auto_increment not null primary key,
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
	id int auto_increment not null primary key,
    dog_type varchar(50) not null,
    description text not null
    );

create table dog(
	id int auto_increment not null primary key,
    user_id int not null,
    dog_name varchar(50) not null,
    type_id int not null,
    description text,
    foreign key(user_id) references user(id),
    foreign key(type_id) references dog_type(id)
    );

create table dog_photos(
	id int auto_increment not null primary key,
    dog_id int not null,
    photo varchar(260) not null,
    foreign key(dog_id) references dog(id)
    );
    
create table sitter_type(
	sitter_type_id int auto_increment not null primary key,
    sitter_type varchar(50) not null
    );
    
create table sitter_type_link(
	link_id int auto_increment not null primary key,
    user_id int not null,
    sitter_type_id int not null,
    foreign key(user_id) references user(id),
    foreign key(sitter_type_id) references sitter_type(sitter_type_id)
    );
    
create table sitter_dog_link(
	link_id int auto_increment not null primary key,
    dog_type_id int not null,
    sitter_type_id int not null,
    foreign key(dog_type_id) references dog_type(id),
    foreign key(sitter_type_id) references sitter_type(sitter_type_id)
    );
    
    
######## CHECK TABLES ############

select * from user;
select * from dog_type;
select * from dog;
select * from dog_photos;
select * from sitter_type;
select * from sitter_type_link;
select * from sitter_dog_link;

######## INSERTING SAMPLE DATA ########

INSERT INTO user (first_name, last_name, city, phone, email, password, user_type, bio) VALUES
	('James', 'Lee', 'Liverpool', '07567890123', 'james.lee@gmail.com', '0b14d501a594442a01c6859541bcb3e8164d183d32937b851835442f69d5c94e', 'Sitter', "I have experience with rescue dogs and know how to make them feel safe and loved."),
    ('Michael', 'Brown', 'Leeds', '07456789012', 'michael.brown@hotmail.co.uk', '6cf615d5bcaac778352a8f1f3360d23f02f34ec182e259897fd6ce485d7870d4', 'Sitter', "I have a passion for training dogs and can help them learn new skills."),
    ('Tom', 'White', 'Birmingham', '07876543210', 'tom.white@googlemail.com', '5906ac361a137e2d286465cd6588ebb5ac3f5ae955001100bc41577c3d751764', 'Sitter', "I'm a caring and attentive dog walker who will treat your dog as if they were my own. I can provide daily walks, playtime, and companionship."),
    ('Matthew', 'Green', 'Manchester', '07321987654', 'matthew.green@live.co.uk', 'b97873a40f73abedd8d685a7cd5e5f85e4a9cfb83eac26886640a0813850122b', 'Sitter', "I'm an active and outdoorsy person who loves to explore new areas with my furry friends. I'm a reliable dog walker who can provide daily exercise and adventure."),
    ('Daniel', 'Chen', 'Glasgow', '07987654321', 'daniel.chen@outlook.com', '8b2c86ea9cf2ea4eb517fd1e06b74f399e7fec0fef92e3b482a6cf2e2b092023', 'Sitter', 'I''m a responsible and reliable dog walker who can provide your dog with daily exercise and attention. I''m available for both scheduled and occasional walks.'),
    ('Emma', 'Wilson', 'Birmingham', '07234567890', 'emma.wilson@gmail.co.uk', '598a1a400c1dfdf36974e69d7e1bc98593f2e15015eed8e9b7e47a83b31693d5', 'Owner', "I work long hours and need someone who can give my dog the exercise and attention they need during the day. I'm looking for a reliable and caring dog walker who can provide daily walks and playtime."),
    ('Sophie', 'Taylor', 'Glasgow', '07901234567', 'sophie.taylor@yahoo.com', '5860836e8f13fc9837539a597d4086bfc0299e54ad92148d54538b5c3feefb7c', 'Owner', "I have a high-energy dog who needs a lot of exercise and stimulation. I'm looking for a dog walker who can keep up with their energy level and provide them with plenty of playtime and adventure."),
	('Alex', 'Davis', 'Manchester', '07321987654', 'alex.davis@hotmail.com', '57f3ebab63f156fd8f776ba645a55d96360a15eeffc8b0e4afe4c05fa88219aa', 'Owner', 'My dog is elderly and needs a gentle, patient approach when it comes to walking. I''m looking for someone who has experience with senior dogs and can provide them with a comfortable and safe walking experience.'),
    ('Oliver', 'Brown', 'Leeds', '07234567890', 'oliver.brown@hotmail.com', '9323dd6786ebcbf3ac87357cc78ba1abfda6cf5e55cd01097b90d4a286cac90e', 'Owner', 'I''m recovering from an injury and am unable to walk my dog myself. I''m looking for a responsible and caring dog walker who can provide my dog with regular exercise and companionship.'),
    ('Sophia', 'Taylor', 'Glasgow', '07987654381', 'sophia.taylor@yahoo.com', 'aa4a9ea03fcac15b5fc63c949ac34e7b0fd17906716ac3b8e58c599cdc5a52f0', 'Owner', 'I have a busy schedule and need a dog walker who can be flexible with their availability. I''m looking for someone who can provide occasional walks as well as regular scheduled walks.'),
    ('John', 'Smith', 'London', '07201234567', 'john.smith@gmail.com', '53d453b0c08b6b38ae91515dc88d25fbecdd1d6001f022419629df844f8ba433', 'Owner', "I'm a busy professional who loves my dog, but doesn't always have time to give them the exercise they need. Looking for a reliable and caring dog walker to help out a few times a week."),
    ('Lucy', 'Brown', 'Manchester', '07161123456', 'lucy.brown@hotmail.com', 'b3d17ebbe4f2b75d27b6309cfaae1487b667301a73951e7d523a039cd2dfe110', 'Owner', "My dog is my best friend and I want to make sure they stay healthy and happy. I'm looking for a dog walker who can give them the exercise they need and lots of love and attention."),
    ('Mark', 'Johnson', 'Birmingham', '07121456789', 'mark.johnson@outlook.com', '48caafb68583936afd0d78a7bfd7046d2492fad94f3c485915f74bb60128620d', 'Owner', "I have a very energetic dog who needs lots of exercise, but my work schedule doesn't always allow me to give them the attention they need. I'm looking for a reliable and experienced dog walker who can keep up with them."),
    ('Sarah', 'Wilson', 'Glasgow', '07141234567', 'sarah.wilson@gmail.com', 'c6863e1db9b396ed31a36988639513a1c73a065fab83681f4b77adb648fac3d6', 'Owner', "My dog is my baby and I want to make sure they're well taken care of. I'm looking for a dog walker who will treat them like their own and give them the exercise and attention they need."),
    ('Alex', 'Roberts', 'Liverpool', '07151345678', 'alex.roberts@yahoo.com', 'c63c2d34ebe84032ad47b87af194fedd17dacf8222b2ea7f4ebfee3dd6db2dfb', 'Owner', "I'm looking for a dog walker who can take my furry friend out for some exercise and fun while I'm at work. They're a very friendly dog and love meeting new people and other dogs.");

   
INSERT INTO dog_type (dog_type, description) VALUES
    ('Toy Dog', 'These breeds were bred to be small companion dogs and are typically playful and affectionate. Examples of toy dog breeds include the Chihuahua, Pomeranian, and Toy Poodle.'),
    ('Terrier Dog', 'These breeds were originally bred to hunt small game and vermin, and are known for their tenacity and energy. Examples of terrier dog breeds include the Jack Russell Terrier, Scottish Terrier, and West Highland White Terrier.'),
    ('Sporting Dog', 'These breeds were bred for hunting and retrieving game, and are generally active and energetic. Examples of sporting dog breeds include the Labrador Retriever, Golden Retriever, and English Springer Spaniel.'),
    ('Working Dog', 'These breeds were originally bred for various types of work, such as guarding livestock or pulling sleds. Examples of working dog breeds include the Boxer, Great Dane, and Siberian Husky.'),
    ('Herding Dog', 'These breeds were bred to help farmers herd livestock, and are typically intelligent and energetic. Examples of herding dog breeds include the Border Collie, Australian Cattle Dog, and Welsh Corgi.');

INSERT INTO dog (user_id, dog_name, type_id, description) VALUES
    (6, 'Buddy', 3, 'Buddy is a playful and energetic Labrador Retriever who loves to fetch.'),
    (7, 'Daisy', 5, 'Rocky is a loyal and protective Border Collie who excels in obedience training.'),
    (8, 'Papa', 1, 'Papa is a gentle and sweet little Toy Poodle who likes short walks and cuddles.'),
    (9, 'Scotty', 2, 'Scotty is a Scottish Terrier, he is playful and needs someone who will be able to handle his energy.'),
    (10, 'Harriet', 4, 'Harriet is a very vocal Siberian Husky who loves a run in the outdoors.'),
    (11, 'Mabel', 1, 'Mabel is a precious little Chihuahua who loves everyone and everything. She enjoys gentle walks and pets.'),
    (12, 'Archie', 2, " Archie is an adventurous and curious Jack Russell Terrier who loves to explore the great outdoors. He's great with other dogs and loves to go on long hikes in the mountains."),
    (13, 'Lucky', 3, 'Lucky is an English Springer Spaniel who adores playtime. Her favourite activity is playing fetch in the park.'),
    (14, 'Cheese', 4, 'Cheese is a sweet old Great Dane who likes a stroll in the park. He is also crazy for sunbathing!'),
    (15, 'Bandit', 5, 'Bandit is an Australian Cattle Dog. He is super smart so would love someone who can give him extra enrichment in the form of training.');

INSERT INTO dog_photos (dog_id, photo) VALUES
    (1, '/buddy.jpg'),
    (2, '/daisy.jpg'),
    (3, '/papa.jpg'),
    (4, '/scotty.jpg'),
    (5, '/harriet.jpg'),
    (6, '/mabel.jpg'),
    (7, '/archie.jpg'),
    (8, '/lucky.jpg'),
    (9, '/cheese.jpg'),
    (10, '/bandit.jpg');

INSERT INTO sitter_type (sitter_type) VALUES
    ('Toy Dog'),
    ('Terrier Dog'),
    ('Sporting Dog'),
    ('Working Dog'),
    ('Herding Dog');

INSERT INTO sitter_type_link (user_id, sitter_type_id) VALUES
    (1, 1),
    (2, 4),
    (3, 3),
    (4, 5),
    (5, 2);
    
INSERT INTO sitter_dog_link (dog_type_id, sitter_type_id) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5);
    
