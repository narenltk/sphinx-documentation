import pypandoc

pdoc_args = ['--mathjax','--smart']
filters = ['pandoc-citeproc']

output = pypandoc.convert_file('index.rst',
                         to='html5',
                         format='md',
                         extra_args=pdoc_args,
                         filters=filters)
