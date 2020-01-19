from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

#Test: Album Id, Album Titel und Künstlername in einer Tabelle anzeigen mit Inner Join über den foreign key Artist.Id

#db.pretty_print("""SELECT Album.AlbumId, Album.Title, Album.ArtistID, Artist.Name
#FROM Album
#INNER JOIN Artist ON Album.ArtistId=Artist.ArtistId;""")

# 1: What order (Invoice) was the most expensive? Which one was the cheapest?

#db.pretty_print("""SELECT MIN (Total)
#FROM Invoice""")

#db.pretty_print("""SELECT Max (Total)
#FROM Invoice""")

# 2: Which city (BillingCity) has the most orders?

#db.pretty_print("""SELECT Max ("BillingCity")
#FROM Invoice""")

# 3: Calculate (or count) how many tracks have this MediaType: Protected AAC audio file.

#db.pretty_print("""SELECT COUNT (Name)
#FROM MediaType 
#WHERE Name="Protected AAC audio file";""")

# 4: Find out what Artist has the most albums? (hint: check ORDER BY)

# 5: db.pretty_print("""SELECT Artist.Name, COUNT (Album.AlbumID) AS NumberOfAlbums
#FROM Album
#INNER JOIN Artist ON Album.ArtistID=Artist.ArtistId
#GROUP BY Artist.Name
#ORDER BY COUNT (Album.AlbumID) DESC;""")

#6: What genre has the most tracks?

#db.pretty_print("""SELECT Genre.Name, COUNT (Track.GenreID) AS NumberOfTracks
#FROM Track
#LEFT Join Genre ON Track.GenreID = Genre.GenreID
#GROUP BY Genre.Name
#ORDER BY COUNT (Track.GenreID) DESC;""")

#7: Which customer spent the most money so far?

#db.pretty_print("""SELECT Customer.FirstName, Customer.LastName, Customer.CustomerID, SUM(Invoice.Total) AS TotalSumOfOrders
#FROM Invoice
#INNER JOIN Customer ON Invoice.CustomerID = Customer.CustomerID
#GROUP BY Customer.CustomerID
#ORDER BY Invoice.Total DESC;""")

#8: What songs were bought with each order? (hint: here you have to do a many-to-many SQL query with three tables: Track, Invoice and InvoiceLine. You have to do two JOINS here)

#db.pretty_print("""SELECT Track.TrackID, Track.Name, Invoice.InvoiceID
#FROM (Track
#JOIN InvoiceLine ON Track.TrackID = Invoiceline.TrackID)
#JOIN Invoice ON Invoice.InvoiceID = Invoiceline.InvoiceID
#GROUP BY Invoice.InvoiceID;""")