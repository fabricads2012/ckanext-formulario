import os
import json
#import requests

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

#r = requests.post(ckan_url + '/api/action/vocabulary_create',
#                  data=data,
#                  headers=headers)
#groups = json.loads(r.text)['result']['id']

class FormularioPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
	plugins.implements(plugins.IDatasetForm, inherit=True)
	plugins.implements(plugins.IConfigurer, inherit=True)

	def update_config(self, config):
		here = os.path.dirname(__file__)
		rootdir = os.path.dirname(os.path.dirname(here))
		template_dir = os.path.join(rootdir, 'ckanext', 'formulario', 'templates')
		config['extra_template_paths'] = ','.join([
			template_dir, config.get('extra_template_paths', '')
		])

	def package_form(self):
		return 'package/new_package_form.html'

	def new_template(self):
		return 'package/new.html'

	def search_template(self):
		return 'package/search.html'

	def read_template(self):
		return 'package/read.html'

	def history_template(self):
		return 'package/history.html'

	def package_types(self):
		return []

	def is_fallback(self):
		return True

