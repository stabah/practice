# Create your views here.
#urls
def listing(request, sub):
  import os
  from django.shortcuts import render
  context = { }
  if sub == '':
    context['dir_name'] = '/var/log'
    context['dir_content'] = os.listdir('/var/log')
  else:
    context['dir_name'] = '/var/log' + '/' + str(sub)
    context['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
  return render(request, 'listing.html', context)
#subfolders
def listing(request, sub):
  import os
  from django.shortcuts import render
  context = { }
  dir_name = '/var/log' + '/' + str(sub)
  context['dir_name'] = dir_name
  context['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
  context['dir'] = []
  context['f'] = []
  for f in context['dir_content']:
    fullname = os.path.join(dir_name, f)
    if os.path.isdir(fullname):
      context['dir'].append(f)
    else:
      context['f'].append(f)
  return render(request, 'listing.html', context)
#tables
def listing(request, sub):
  import os
  import time
  from django.shortcuts import render
  context = { }
  dir_name = '/var/log' + '/' + str(sub)
  context['dir_name'] = dir_name
  context['dir_content'] = os.listdir('/var/log' + '/' + str(sub))
  context['tbl_content'] = []
  for f in context['dir_content']:
    row = []
    fullname = os.path.join(dir_name, f)
    sz = os.path.getsize(fullname)
    stat = os.stat(fullname)
    t = time.localtime(stat.st_mtime)
    ct = str(t[2])+'/'+str(t[1])+'/'+str(t[0])+' '+str(t[3])+':'+str(t[4])+':'+str(t[5])
    row.append(f)
    row.append(sz)
    row.append(ct)
    context['tbl_content'].append(row)
  return render(request, 'listing.html', context)

