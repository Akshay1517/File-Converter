import os
import pypandoc
source_dir = 'source'
result_dir = 'results'
template_dir = 'templates'
fp = open(template_dir+'/header.html', "r")
header = fp.read()
fp.close()
fp = open(template_dir+'/navigation.html', "r")
navigation = fp.read()
fp.close()
fp = open(template_dir+'/footer.html', "r")
footer = fp.read()
fp.close()
for file in os.listdir(source_dir):
    source_file = source_dir+'/'+file
    output_file = result_dir+'/'+file.replace('.docx','.html')
    pypandoc.convert_file(source_file,'html', outputfile=output_file)
    fp = open(output_file, "r+")
    source = fp.read()
    fp.close()
