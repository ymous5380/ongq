# Run the file by calling "python generate.py" inside the directory where this file
# and the "dbpedia_instances.csv", "string_instances.csv", "generated", "sql" and "sparql"
# files and directories are located.
import os


def generate_queries(templates, instances, language='sql', data_set_name='dbpedia'):
	current_template_name = ''
	for instance in instances:
		template_name = instance[0]
		if template_name != current_template_name:
			current_template_name = template_name
			i = 0
		i = i + 1
		query_file_path = os.path.join(
			'generated', data_set_name, language, template_name, f'query_{i}.sql')
		template_content = templates[template_name]
		
		query_content = template_content
		for j in range(len(instance) - 1):
			query_content = query_content.replace(f'&{j}', instance[1 + j])
		with open(query_file_path, 'w') as file:
			file.write(query_content)
	

if __name__ == '__main__':
	
	# Read instance files
	with open('dbpedia_instances.csv', 'r') as file:
		dbpedia_instances = [l.strip().split(',') for l in file.readlines()]
	with open('string_instances.csv', 'r') as file:
		string_instances = [l.strip().split(',') for l in file.readlines()]
		
	# Read templates
	sql_templates = dict()
	sparql_templates = dict()
	for template_file_name in os.listdir('sql'):
		template_name = template_file_name.split('.')[0]
		template_file_path = os.path.join('sql', template_file_name)
		with open(template_file_path, 'r') as file:
			template_content = ''.join(file.readlines())
		sql_templates[template_name] = template_content
	for template_file_name in os.listdir('sparql'):
		template_name = template_file_name.split('.')[0]
		template_file_path = os.path.join('sparql', template_file_name)
		with open(template_file_path, 'r') as file:
			template_content = ''.join(file.readlines())
		sparql_templates[template_name] = template_content
	
	# Generate DBPedia queries
	generate_queries(sql_templates, dbpedia_instances, 'sql', 'dbpedia')
	generate_queries(
		sparql_templates,
		[t for t in dbpedia_instances if t[0] != 'rq'],
		'sparql',
		'dbpedia')
		
	# Generate String queries
	generate_queries(sql_templates, string_instances, 'sql', 'string')
	generate_queries(
		sparql_templates,
		[t for t in string_instances if t[0] != 'rq'],
		'sparql',
		'string')
		
