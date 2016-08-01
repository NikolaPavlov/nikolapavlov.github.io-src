import exrex


output_file='dict.lst'
regex='bev[A-Z][0-9]{2}[a-z]{2}[`~!@#$%^&*()_+}{|":;.,/?><\']1995'
generated_strings=list(exrex.generate(regex))

with open(output_file, 'w') as f:
   for str in generated_strings:
      f.write(str + '\n')

