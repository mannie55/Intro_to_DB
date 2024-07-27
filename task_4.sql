USE alx_book_store;

SELECT COLUMN_NAME, DATA_TYPE 
FROM information_schema.columns
WHERE TABLE_SHEMA = 'alx_book_store'
AND TABLE_NAME = 'Books';