-- SELECT cl_to AS parent, page_title AS child
-- FROM page JOIN categorylinks ON categorylinks.cl_from=page.page_id
-- WHERE categorylinks.cl_type = "subcat" AND categorylinks.cl_to = "経済";

SELECT cl_from AS id
FROM page JOIN categorylinks ON categorylinks.cl_from=page.page_id
WHERE categorylinks.cl_type = "page" AND categorylinks.cl_to = "経済";
