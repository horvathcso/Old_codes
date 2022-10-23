INSERT INTO Department (idDepartment, Parentid, Title, Description, ShortDescription, Link)
VALUES
   (0,0,"Home","Weblap nyitószöveg. WQERTY123456789", null, "Home"),
  (1, 0, "Electronics", "Electronics Description", "Electronics Short Description", "Home/Electronics"),
  (2, 1, "Computers and Tablets", "Computers and Tablets Description", "Computers and Tablets Short Description", "Home/Electronics/Computers and Tablets"),
  (3, 1, "TV and Video", "TV and Video Description", "TV and Video Short Description", "Home/Electronics/TV and video"),
 
  (4, 2, "Desktops", "Desktops Description", "Desktops Short Description", "Home/Electronics/Computers and Tablets/Desktops"),
  (5, 2, "Laptops", "Laptops Description", "Laptops Short Description", "Home/Electronics/Computers and Tablets/Laptops"),
  (6, 2, "Tablets", "Tablets Description", "Tablets Short Description", "Home/Electronics/Computers and Tablets/Tablets"),
  (7, 2, "Accessories", "Accessories Description", "Accessories Short Description", "Home/Electronics/Computers and Tablets/Accessories"),
  (8, 7, "Accessories For desktops", "Accessories For desktops Description", "Accessories For desktops Short Description", "Home/Electronics/Computers and Tablets/Accessories/For desktops"),
  (9, 7, "Accessories For laptops", "Accessories For laptops Description", "Accessories For laptops Short Description", "Home/Electronics/Computers and Tablets/Accessories/For laptops"),
  (10, 7, "Accessories For tablets", "Accessories For tablets Description", "Accessories For tablets Short Description", "Home/Electronics/Computers and Tablets/Accessories/For tablets"),
  (11, 3, "TVs ", "TVs Description", "TVs Short Description", "Home/Electronics/TV and video/TVs"),
  (12, 3, "Projectors", "Projectors Description", "Projectors Short Description", "Home/Electronics/TV and video/Projectors"),
  (13 , 0, "Kitchen", "Kitchen department description: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer cursus.", "Kitchen department short description", "Home/Kitchen"),
  (14, 13, "Tables", "Tables long descreption: rtzztrew ertzrew wertztre werfghgtree rtzhztre", "Tables section", "Home/Kitchen/Tables"),
  (15, 13, "Chairs", "Chairs long descreption: rtzztrew ertzrew wertztre werfghgtree rtzhztre", "Chairs section", "Home/Kitchen/Chairs");

INSERT INTO Product (idProduct, departmentId, Title, Description, ShortDescription, Stock, IsFeatured, inStore, RetailPrice, Tax, Discount,Link)
VALUES 
	(1, 5, "Mac1 Title", "Mac1 Description", "Mac1 ShortDescription", 10, true, true, 1000, 100, 10,"link1"),
    (2, 5, "Mac2 Title", "Mac2 Description", "Mac2 ShortDescription", 1, false, true, 2000, 100, 5,"link2"),
    (3, 4, "Mac Desktop1 Title", "Mac Desktop1 Description", "Mac Desktop1 ShortDescription", 100, true, true, 3000, 100, 0,"link3"),
    (4, 4, "Mac Desktop2 Title", "Mac Desktop2 Description", "Mac Desktop2 ShortDescription", 50, true, true, 3000, 100, 0,"link4"),
    (5, 8, "Desktop Accessor1 Title", "Desktop Accessor1 Description", "Desktop Accessor1 ShortDescription", 0, true, false, 1000, 100, 10,"link5"),
    (6, 10, "Lablet Accessor1 Title", "Lablet Accessor1 Description", "Lablet Accessor1 ShortDescription", 10, false, true, 1000, 100, 15,"link6"),
    (7, 11, "TVs1 Title", "TVs1 Description", "TVs1 ShortDescription", 10, false, true, 1000, 100, 5,"link7"),
    (8, 12, "Projectors1 Title", "Projectors1 Description", "Projectors1 ShortDescription", 10, false, false, 1000, 100, 5,"link8"),
    (9, 12, "Projectors2 Title", "Projectors2 Description", "Projectors2 ShortDescription", 0, NULL, false, 1000, 100, 5,"link9"),
    (10, 12, "Projectors3 Title", "Projectors3 Description", "Projectors3 ShortDescription", 10, true, true, 1000, 100, 5,"link10"),
	(11, 14, "Table 1", "Table1 Long Description", "Table1 ShortDescription", 100, true, true, 1000, 100, 10,"link11"),
    (12, 14, "Table 2", "Table2 Long Description", "Table2 ShortDescription", 10, false, true, 500, 100, 10,"link12"),
    (13, 15, "Chair 1", "Chair1 Long Description", "Chair1 ShortDescription", 100, false, true, 100, 10, 5,"link13"),
    (14, 15, "Chair 2", "Chair2 Long Description", "Chair2 ShortDescription", 50, true, true, 150, 10, 15,"link14");

INSERT INTO Keywords (idKeywords, Keyword)
VALUES
	(1, "Projectors"),
    (2, "Laptop"),
    (3, "MAC");
    
INSERT INTO Product_has_Keywords (Product_idProduct, KeyProd_idKeywords)
VALUES
	( 10, 1),
    ( 9, 1),
    ( 8, 1),
    ( 1,2),
    ( 2,2),
    (1,3),
    (2,3),
    (3,3),
    (4,3);
    
    
INSERT INTO User (ssn, FirstName, LastName, Password, Phone, NewsCheckbox)
VALUES
	("198901010001", "Vidumini", "Kulathunga", "123", "12345678", true),
    ("198801010002", "Amila", "Kulathunga", "123", "22245688", false),
    ("200001010003", "Ali", "Alanin", "pw", "22245688", false),
    ("199912319999", "Bali", "Bu", "pw123", "11245688", true);
	
INSERT INTO Address (ssn, PostalCode, AddrCity, AddrStreet, AddrBuilding)
VALUES
	("198901010001", 001, "Uppsala", "Strasse1", "42"),
    ("198801010002", 002, "Stockholm", "Strasse2", "1/A"),
    ("200001010003", 002, "Stockholm", "Strasse2", "2/A"),
    ("199912319999", 001, "Uppsala", "Strasse2", "3/A");
    

INSERT INTO Email (ssn, EmailAddress)
VALUES
	("198901010001", "vidumini@gmail.com"),
    ("198801010002", "amila@gmail.com"),
	("199912319999", "email@mail.se"),
	("200001010003", "123@gmail.com");
    
INSERT INTO Review (idReview, ProdId, UserId, Content, Rating)
VALUES
	(1, 1, "198901010001", "Good", "4"),
    (2, 1, "198801010002", "Best", "5"),
    (3, 13, "200001010003", "wertzhujhuztredfgbn  thjzhjghrg wzrhjtuh jhgb", "3"),
    (4, 10, "200001010003", "bad", "2"),
    (5, 9, "199912319999", "Nice product", "5");
    
INSERT INTO Orders (IdOrder, UserId, OrderDate, LastChange, Status, TrackingNum, Payment)
VALUES
	(1, "198901010001", '2020-06-26', '2020-10-26', "dispatched", "0001", "qSM58flL8oazrkvszHUkSRNp6WxMCW43z3yb0TDQXxaRURa3TdWPGGw6J7EHWJ2G"),
	(2, "198901010001", '2020-06-26', '2020-10-27', "new", "0002", "pSM58flL8oazrkvszHUkSRNp6WxMCW43z3yb0TDQXxaRURa3TdWPGGw6J7EHWJ2G");


INSERT INTO Order_has_Product (OrderId, ProductId, NumberOfProduct, PurchasePrice)
VALUES
	(2,13,4,400),
	(1, 1, 2, 2000);
    