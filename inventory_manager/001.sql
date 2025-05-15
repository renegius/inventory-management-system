
DROP DATABASE stockmanagementsystem;

CREATE DATABASE stockmanagementsystem;

USE stockmanagementsystem;

CREATE TABLE stocks (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(25) NOT NULL,
    item_price INT NOT NULL,
    item_qnty INT NOT NULL,
    item_category VARCHAR(25),
    item_date DATE NOT NULL DEFAULT (CURRENT_DATE)
);

INSERT INTO stocks (item_name, item_price, item_qnty, item_category, item_date)
VALUES 
    ('Apple Laptop Mac M2', 1200, 5, 'Laptop', '2023-10-15'),
    ('Dell XPS 13', 1000, 3, 'Laptop', '2023-10-16'),
    ('Samsung Galaxy Tab S8', 799, 7, 'Tablet', '2023-10-17'),
    ('Apple Watch Series 9', 399, 15, 'Smartwatch', '2023-10-18'),
    ('Sony WH-1000XM5', 349, 12, 'Headphones', '2023-10-19'),
    ('PlayStation 5', 499, 8, 'Gaming Console', '2023-10-20'),
    ('LG UltraFine 4K Monitor', 699, 5, 'Monitor', '2023-10-21'),
    ('HP LaserJet Pro MFP', 299, 6, 'Printer', '2023-10-22'),
    ('Seagate Backup Plus 2TB', 89, 20, 'Storage', '2023-10-23'),
    ('Logitech MX Keys', 129, 25, 'Accessories', '2023-10-24'),
    ('iPhone 15 Pro', 999, 10, 'Smartphone', '2023-10-16')
    ;
 
SELECT user FROM mysql.user;


/* 
INSERT INTO stocks (item_name, item_price, item_qnty, item_category, item_date)
VALUES 
    -- First 20 entries (2023)
    ('Apple MacBook M2', 1200, 5, 'Laptop', '2023-10-15'),
    ('Dell XPS 13', 1000, 3, 'Laptop', '2023-10-16'),
    ('Samsung Tab S8', 799, 7, 'Tablet', '2023-10-17'),
    ('Apple Watch S9', 399, 15, 'Smartwatch', '2023-10-18'),
    ('Sony WH-1000XM5', 349, 12, 'Headphones', '2023-10-19'),
    ('PlayStation 5', 499, 8, 'Gaming Console', '2023-10-20'),
    ('LG UltraFine 4K', 699, 5, 'Monitor', '2023-10-21'),
    ('HP LaserJet Pro', 299, 6, 'Printer', '2023-10-22'),
    ('Seagate 2TB HDD', 89, 20, 'Storage', '2023-10-23'),
    ('Logitech MX Keys', 129, 25, 'Accessories', '2023-10-24'),
    ('iPhone 15 Pro', 999, 10, 'Smartphone', '2023-10-16'),
    ('Lenovo ThinkPad', 1500, 4, 'Laptop', '2023-10-25'),
    ('Microsoft Surface', 1300, 6, 'Tablet', '2023-10-26'),
    ('Garmin Fenix 7', 599, 10, 'Smartwatch', '2023-10-27'),
    ('Bose QC 45', 329, 8, 'Headphones', '2023-10-28'),
    ('Xbox Series X', 499, 7, 'Gaming Console', '2023-10-29'),
    ('Asus ROG Monitor', 799, 3, 'Monitor', '2023-10-30'),
    ('Canon PIXMA Pro', 499, 4, 'Printer', '2023-10-31'),
    ('WD My Passport', 119, 15, 'Storage', '2023-11-01'),
    ('Razer DeathAdder', 69, 30, 'Accessories', '2023-11-02'),

    -- Next 20 entries (2024)
    ('HP Spectre x360', 1400, 6, 'Laptop', '2024-01-15'),
    ('Samsung Tab S9', 899, 9, 'Tablet', '2024-01-16'),
    ('Apple Watch Ultra', 799, 12, 'Smartwatch', '2024-01-17'),
    ('Sony WH-CH720N', 199, 20, 'Headphones', '2024-01-18'),
    ('PS5 Slim', 449, 10, 'Gaming Console', '2024-01-19'),
    ('LG UltraGear 27', 899, 5, 'Monitor', '2024-01-20'),
    ('Brother HL-L2350', 149, 8, 'Printer', '2024-01-21'),
    ('Samsung T7 2TB', 159, 15, 'Storage', '2024-01-22'),
    ('Logitech G Pro X', 199, 10, 'Accessories', '2024-01-23'),
    ('OnePlus 12', 899, 7, 'Smartphone', '2024-01-24'),
    ('Asus ZenBook 14', 1200, 4, 'Laptop', '2024-02-01'),
    ('Surface Go 4', 599, 10, 'Tablet', '2024-02-02'),
    ('Garmin Venu 3', 449, 14, 'Smartwatch', '2024-02-03'),
    ('Jabra Elite 85h', 249, 12, 'Headphones', '2024-02-04'),
    ('Nintendo Switch 2', 399, 8, 'Gaming Console', '2024-02-05'),
    ('Acer Predator XB', 799, 3, 'Monitor', '2024-02-06'),
    ('HP OfficeJet Pro', 299, 6, 'Printer', '2024-02-07'),
    ('Crucial X9 Pro', 299, 10, 'Storage', '2024-02-08'),
    ('SteelSeries A5', 129, 18, 'Accessories', '2024-02-09'),
    ('Xiaomi 14 Ultra', 999, 5, 'Smartphone', '2024-02-10')
    ;
    
INSERT INTO stocks (item_id, item_name, item_price, item_qnty, item_category, item_date)
VALUES 
    -- Laptops (13-22)
    (13, 'MacBook Air M2', 1200, 8, 'Laptop', '2023-10-15'),
    (14, 'Dell XPS 13', 1000, 5, 'Laptop', '2023-10-16'),
    (15, 'Lenovo ThinkPad X1', 1500, 6, 'Laptop', '2023-10-17'),
    (16, 'HP Spectre x360', 1400, 7, 'Laptop', '2023-10-18'),
    (17, 'Asus ZenBook 14', 1200, 4, 'Laptop', '2023-10-19'),
    (18, 'Acer Swift 3', 899, 9, 'Laptop', '2023-10-20'),
    (19, 'Microsoft Surface L5', 1300, 5, 'Laptop', '2023-10-21'),
    (20, 'Razer Blade 15', 2000, 3, 'Laptop', '2023-10-22'),
    (21, 'LG Gram 17', 1600, 6, 'Laptop', '2023-10-23'),
    (22, 'Samsung Galaxy Book', 1100, 7, 'Laptop', '2023-10-24'),

    -- Tablets (23-32)
    (23, 'iPad Pro 12.9', 1099, 10, 'Tablet', '2023-10-25'),
    (24, 'Samsung Tab S8', 799, 12, 'Tablet', '2023-10-26'),
    (25, 'Microsoft Surface Go', 599, 15, 'Tablet', '2023-10-27'),
    (26, 'Lenovo Tab P11 Pro', 499, 8, 'Tablet', '2023-10-28'),
    (27, 'Amazon Fire HD 10', 149, 20, 'Tablet', '2023-10-29'),
    (28, 'Google Pixel Tablet', 499, 10, 'Tablet', '2023-10-30'),
    (29, 'Huawei MatePad Pro', 699, 7, 'Tablet', '2023-10-31'),
    (30, 'Xiaomi Pad 6', 399, 9, 'Tablet', '2023-11-01'),
    (31, 'Oppo Pad Air', 299, 12, 'Tablet', '2023-11-02'),
    (32, 'Realme Pad X', 349, 11, 'Tablet', '2023-11-03'),

    -- Smartwatches (33-42)
    (33, 'Apple Watch Ultra', 799, 15, 'Smartwatch', '2023-11-04'),
    (34, 'Samsung Galaxy Watch', 349, 18, 'Smartwatch', '2023-11-05'),
    (35, 'Garmin Fenix 7', 599, 10, 'Smartwatch', '2023-11-06'),
    (36, 'Fitbit Sense 2', 299, 20, 'Smartwatch', '2023-11-07'),
    (37, 'Huawei Watch GT 3', 249, 12, 'Smartwatch', '2023-11-08'),
    (38, 'Amazfit GTR 4', 199, 14, 'Smartwatch', '2023-11-09'),
    (39, 'Withings ScanWatch', 299, 8, 'Smartwatch', '2023-11-10'),
    (40, 'Fossil Gen 6', 299, 10, 'Smartwatch', '2023-11-11'),
    (41, 'TicWatch Pro 5', 349, 9, 'Smartwatch', '2023-11-12'),
    (42, 'Polar Vantage V2', 499, 7, 'Smartwatch', '2023-11-13'),

    -- Headphones (43-52)
    (43, 'Sony WH-1000XM5', 349, 12, 'Headphones', '2023-11-14'),
    (44, 'Bose QuietComfort 45', 329, 15, 'Headphones', '2023-11-15'),
    (45, 'Apple AirPods Max', 549, 10, 'Headphones', '2023-11-16'),
    (46, 'Sennheiser HD 660S', 499, 8, 'Headphones', '2023-11-17'),
    (47, 'Jabra Elite 85h', 249, 12, 'Headphones', '2023-11-18'),
    (48, 'Bose NC 700', 379, 9, 'Headphones', '2023-11-19'),
    (49, 'Sony WH-CH720N', 199, 20, 'Headphones', '2023-11-20'),
    (50, 'Beats Studio Pro', 349, 11, 'Headphones', '2023-11-21'),
    (51, 'JBL Live 660NC', 199, 14, 'Headphones', '2023-11-22'),
    (52, 'Skullcandy Crusher', 149, 18, 'Headphones', '2023-11-23'),

    -- Gaming Consoles (53-62)
    (53, 'PlayStation 5', 499, 8, 'Gaming Console', '2023-11-24'),
    (54, 'Xbox Series X', 499, 7, 'Gaming Console', '2023-11-25'),
    (55, 'Nintendo Switch OLED', 349, 10, 'Gaming Console', '2023-11-26'),
    (56, 'Steam Deck 512GB', 649, 5, 'Gaming Console', '2023-11-27'),
    (57, 'PlayStation 4 Slim', 299, 12, 'Gaming Console', '2023-11-28'),
    (58, 'Xbox Series S', 299, 9, 'Gaming Console', '2023-11-29'),
    (59, 'Nintendo Switch Lite', 199, 15, 'Gaming Console', '2023-11-30'),
    (60, 'Atari VCS 800', 399, 6, 'Gaming Console', '2023-12-01'),
    (61, 'Sega Genesis Mini', 79, 20, 'Gaming Console', '2023-12-02'),
    (62, 'NeoGeo Mini', 99, 18, 'Gaming Console', '2023-12-03'),

    -- Monitors (63-72)
    (63, 'LG UltraFine 4K', 699, 5, 'Monitor', '2023-12-04'),
    (64, 'Dell UltraSharp 27', 899, 6, 'Monitor', '2023-12-05'),
    (65, 'Asus ROG Swift', 799, 4, 'Monitor', '2023-12-06'),
    (66, 'Samsung Odyssey G7', 699, 7, 'Monitor', '2023-12-07'),
    (67, 'Acer Predator XB3', 799, 5, 'Monitor', '2023-12-08'),
    (68, 'BenQ PD3220U', 999, 3, 'Monitor', '2023-12-09'),
    (69, 'HP Omen 27i', 499, 8, 'Monitor', '2023-12-10'),
    (70, 'MSI Optix MAG274', 399, 10, 'Monitor', '2023-12-11'),
    (71, 'ViewSonic Elite XG', 599, 6, 'Monitor', '2023-12-12'),
    (72, 'Philips Brilliance', 499, 7, 'Monitor', '2023-12-13'),

    -- Printers (73-82)
    (73, 'HP LaserJet Pro', 299, 6, 'Printer', '2023-12-14'),
    (74, 'Canon PIXMA Pro', 499, 4, 'Printer', '2023-12-15'),
    (75, 'Epson EcoTank Pro', 499, 5, 'Printer', '2023-12-16'),
    (76, 'Brother HL-L2350', 149, 8, 'Printer', '2023-12-17'),
    (77, 'Xerox VersaLink', 399, 7, 'Printer', '2023-12-18'),
    (78, 'Lexmark CX510', 599, 5, 'Printer', '2023-12-19'),
    (79, 'Samsung Xpress', 199, 10, 'Printer', '2023-12-20'),
    (80, 'Ricoh SP C261', 349, 6, 'Printer', '2023-12-21'),
    (81, 'Kyocera Ecosys', 299, 9, 'Printer', '2023-12-22'),
    (82, 'OKI C332dn', 499, 4, 'Printer', '2023-12-23'),

    -- Storage (83-92)
    (83, 'Seagate 2TB HDD', 89, 20, 'Storage', '2023-12-24'),
    (84, 'WD My Passport 4TB', 119, 15, 'Storage', '2023-12-25'),
    (85, 'SanDisk Extreme 1TB', 149, 10, 'Storage', '2023-12-26'),
    (86, 'Samsung T7 Shield', 159, 12, 'Storage', '2023-12-27'),
    (87, 'Crucial X9 Pro 4TB', 299, 8, 'Storage', '2023-12-28'),
    (88, 'LaCie Rugged 5TB', 199, 6, 'Storage', '2023-12-29'),
    (89, 'Kingston XS2000', 129, 14, 'Storage', '2023-12-30'),
    (90, 'ADATA SE800', 99, 18, 'Storage', '2023-12-31'),
    (91, 'G-Technology G-DRIVE', 249, 9, 'Storage', '2024-01-01'),
    (92, 'Toshiba Canvio Flex', 79, 20, 'Storage', '2024-01-02'),

    -- Accessories (93-95)
    (93, 'Logitech MX Keys', 129, 25, 'Accessories', '2024-01-03'),
    (94, 'Razer DeathAdder', 69, 30, 'Accessories', '2024-01-04'),
    (95, 'Corsair K95 RGB', 199, 12, 'Accessories', '2024-01-05');
    */
    -- 
    --
    --
    SELECT * FROM STOCKS;