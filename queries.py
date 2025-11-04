"""DDL: DATA DEFINITION LANGUAGE
it includes commands related to structure of table, DB

COMMANDS OF DDL:
1. create:
syntax: create database DName
syntax: crete table TName(ColName1 datatype(size), 
                          ColName2 datatype(size)
                          );
2. use:
syntax: use databaseName

3.description of table:
syntax: desc tablename

4. drop/delete a table: 
syntax: drop table tablename

DML: DATA MANIPULATION LANGUAGE
1. insert:
syntax: a. insert into tablename #to fill all columns present in table
            values(1,'abc');
            
        b. insert into tablename(Name) #to fill only single required column
             values('pqr');
              
        c. insert into tablename #to insert multiple data at a time
             values(1,'abc'),(2,'pqr');

2. select/read: 
syntax: a. select * from tablename #selects all records

        b. select colname from tablename # #select a particular column

        c. select * from tablename #finds whole record based on one 
            where colname=value

3. update:
syntax: a. update tablename  #to update whole column parts
            SET colname=value;
        
        b.  update tablename  #to update particular value
            SET colname=value
            where colname=value;

4. delete:
syntax: a. delete from tablename; #deletes whole column

        b. delete from tablename #deletes particular colname value 
             where colname=value;
        """

