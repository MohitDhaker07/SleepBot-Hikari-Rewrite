import sqlite3

if __name__ == '__main__':
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	
	"""
	sql_cmd = open("./SQL_CMDS/c-channel_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Created Channel Table")
	sql_cmd = open("./SQL_CMDS/c-rule_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Created Rule Table")
	sql_cmd = open("./SQL_CMDS/c-tags_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Created Tags Table")
	"""
	sql_cmd = open("./SQL_CMDS/c-tickets_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Created Tickets Table")
	
	"""
	sql_cmd = open("./SQL_CMDS/i-channel_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Init into channel_table")
	sql_cmd = open("./SQL_CMDS/i-rule_table.txt", 'r').read()
	c.execute(sql_cmd)
	print("Init into Rule Table")
	"""

	conn.commit()
	conn.close()
	print("Done")
	quit()
