import sqlite3
import sys

conn = sqlite3.connect('enwiki')
c = conn.cursor()
import sys

category = sys.argv[1]

parents = "SELECT page_title AS parent FROM page JOIN categorylinks ON categorylinks.cl_from=page.page_id WHERE categorylinks.cl_type = 'subcat' AND categorylinks.cl_to = \'{}\';".format(category)
parents_e = [row[0] for row in c.execute(parents)]

print(parents_e)

id_list = [category]

for parent in parents_e:
    id_list.append(parent)
    childs = "SELECT page_title AS parent FROM page JOIN categorylinks ON categorylinks.cl_from=page.page_id WHERE categorylinks.cl_type = 'subcat' AND categorylinks.cl_to = \'{}\';".format(parent)
    childs_e = [row[0] for row in c.execute(childs)]
    id_list.extend(childs_e)
    # pages = "SELECT cl_from AS id FROM page JOIN categorylinks ON categorylinks.cl_from=page.page_id WHERE categorylinks.cl_type = 'page' AND categorylinks.cl_to = \'{}\';".format(parent)
    # pages = "SELECT page_title FROM page JOIN categorylinks ON categorylinks.cl_from=page.page_id WHERE categorylinks.cl_type = 'page' AND categorylinks.cl_to = \'{}\';".format(parent)
    # pages_e = c.execute(pages)
    # for page in pages_e:
    #     id_list.append(str(page[0]))

with open("id_list.txt", mode='w') as f:
    f.write("\n".join(id_list) + "\n")

conn.close()
