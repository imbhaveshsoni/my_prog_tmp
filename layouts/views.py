from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.http import HttpResponse
import bfa
from mypro.login_status import login_status
from mypro import dev_setting
from mypro.project_showcase import project_showcase
import mysql.connector
import pickle
from AptLibrary.Python.Script import ConvertSecToTime
import time

def home(request):
	login_status_server_response = login_status.login_status_response(request)
	domain_name = dev_setting.dev_domain_name_with_protocol
	project_showcase_response = project_showcase.project_showcase(request,[','],{'limit':3})
	try:
		project = project_showcase_response['result']
	except:
		project = list()


	
	context = {
	    'login_status_server_response': login_status_server_response,
	    'is_login_status_response':login_status.is_login_status_response,
	    'domain_name':domain_name,
	    'project':project,
	}
	return render(request,'layouts/home.html',context);

def about(request):
	login_status_server_response = login_status.login_status_response(request)
	domain_name = dev_setting.dev_domain_name_with_protocol
	print(login_status_server_response);
	
	context = {
	    'login_status_server_response': login_status_server_response,
	    'is_login_status_response':login_status.is_login_status_response,
	    'domain_name':domain_name,
	    # 'project':project,
	}
	return render(request,'layouts/about.html',context);

def services(request):
	login_status_server_response = login_status.login_status_response(request)
	domain_name = dev_setting.dev_domain_name_with_protocol
	print(login_status_server_response);
	
	context = {
	    'login_status_server_response': login_status_server_response,
	    'is_login_status_response':login_status.is_login_status_response,
	    'domain_name':domain_name,
	    # 'project':project,
	}
	return render(request,'layouts/services.html',context);





def contact (request):
	login_status_server_response = login_status.login_status_response(request)
	domain_name = dev_setting.dev_domain_name_with_protocol
	
	context = {
	    'login_status_server_response': login_status_server_response,
	    'is_login_status_response':login_status.is_login_status_response,
	    'domain_name':domain_name,
	    # 'project':project,
	}
	return render(request,'layouts/contact.html',context);


def Content(request):
    if(request.GET.get('cat')):
        cat = request.GET['cat']
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    breadcrumb = ''
    cat_list = list()
    i = 0
    for item in cat.split("-"):
        cat_list.append(','+item+',')

        if len(item) > 0:
            tmp_breadcrumb = item.split("_")
            if(len(tmp_breadcrumb) > 1):
                if(i == 0):
                    breadcrumb += tmp_breadcrumb[1]
                else:
                    breadcrumb += ' / '+tmp_breadcrumb[1]
                i = i+1
    login_status_server_response = login_status.login_status_response(request)
    domain_name = dev_setting.dev_domain_name_with_protocol
    project_showcase_response = project_showcase.project_showcase(request,cat_list)
    try:
        project = project_showcase_response['result']
    except:
        project = list()
    context = {
        'login_status_server_response': login_status_server_response,
        'is_login_status_response':login_status.is_login_status_response,
        'domain_name':domain_name,
        'project':project,
        'breadcrumb':breadcrumb
    }
    return render(request,'layouts/content.html',context)

def ProjectShow(request):
    login_status_server_response = login_status.login_status_response(request)
    domain_name = dev_setting.dev_domain_name_with_protocol
    if(request.GET.get('pid')):
        pid = request.GET['pid']
    else:
        return redirect('home')

    # Database connection with mysql#
    conn = mysql.connector.connect(host='3.108.45.242',user='mypro_db',password='mypro_db',database='mypro_db')
    #Creating a cursor object using the cursor() method
    connCursor = conn.cursor(buffered=True)

    EPASS='GFtCtuL7JdCJqmE3CgHBsN3GhPMwAV8pgu8bqKkR8Pg85L8XKJ4Mv2XtwkBvtLtr'

    sql = f"SELECT AES_DECRYPT(project_id,'{EPASS}'),AES_DECRYPT(account_id,'{EPASS}'),AES_DECRYPT(title,'{EPASS}'),AES_DECRYPT(description,'{EPASS}'),AES_DECRYPT(project_category,'{EPASS}'),AES_DECRYPT(project_image,'{EPASS}'),AES_DECRYPT(last_upd_time,'{EPASS}') FROM project_upload WHERE project_id = AES_ENCRYPT(%s,'{EPASS}') and (status = AES_ENCRYPT(%s,'{EPASS}') or status = AES_ENCRYPT(%s,'{EPASS}'))"
    connCursor.execute(sql, (pid,'tmpactive','active'))
    conn.commit()

    if(connCursor.rowcount < 1):
        messages.error(request,"Something going wrong")
        return redirect('home')

    results = connCursor.fetchall()
    if(len(results) < 1):
        messages.error(request,"Something going wrong")
        return redirect('home')

    result = results[0]

    if(result[0] != None and len(result[0]) > 0):
        project_id = str(result[0], encoding='utf-8', errors='strict')
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    if(result[1] != None and len(result[1]) > 0):
        account_id = str(result[1], encoding='utf-8', errors='strict')
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    if(result[2] != None and len(result[2]) > 0):
        title = str(result[2], encoding='utf-8', errors='strict')
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    if(result[3] != None and len(result[3]) > 0):
        description = str(result[3], encoding='utf-8', errors='strict')
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    if(result[4] != None and len(result[4]) > 0):
        project_category = str(result[4], encoding='utf-8', errors='strict')
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    if(result[5] != None and len(result[5]) > 0):
        project_image = result[5]
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')
    if(result[6] != None and len(result[6]) > 0):
        last_upd_time = result[6]
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    if(isinstance(project_image,(bytes,bytearray) )):
        try:
            project_image_array = pickle.loads(project_image)
        except:
            messages.error(request,"Something going wrong")
            return redirect('home')
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    if(len(project_image_array) < 1):
        messages.error(request,"Something going wrong")
        return redirect('home')

    sql = f"SELECT AES_DECRYPT(fname,'{EPASS}'),AES_DECRYPT(lname,'{EPASS}'),AES_DECRYPT(profile_id,'{EPASS}') FROM register_account WHERE account_id = AES_ENCRYPT(%s,'{EPASS}') and (status = AES_ENCRYPT(%s,'{EPASS}') or status = AES_ENCRYPT(%s,'{EPASS}'))"
    connCursor.execute(sql, (account_id,'tmpactive','active'))
    conn.commit()

    if(connCursor.rowcount < 1):
        messages.error(request,"Something going wrong")
        return redirect('home')

    author_results = connCursor.fetchall()
    if(len(author_results) < 1):
        messages.error(request,"Something going wrong")
        return redirect('home')

    author_result = author_results[0]

    if(author_result[0] != None and len(author_result[0]) > 0):
        fname = str(author_result[0], encoding='utf-8', errors='strict')
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    if(author_result[1] != None and len(author_result[1]) > 0):
        lname = str(author_result[1], encoding='utf-8', errors='strict')
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    if(author_result[2] != None and len(author_result[2]) > 0):
        profile_id = str(author_result[2], encoding='utf-8', errors='strict')
    else:
        messages.error(request,"Something going wrong")
        return redirect('home')

    last_upd_local_time = time.asctime( time.localtime(float(last_upd_time)))
    project = {'project_id':project_id,'account_id':account_id,'title':title,'description':description,'project_category':project_category,'project_image':project_image_array,'last_upd_time':last_upd_time,'last_upd_local_time':last_upd_local_time,'last_upd_sort_time':ConvertSecToTime.ConvertSecToSortTime(time.time() - float(last_upd_time)),'fname':fname,'lname':lname,'profile_id':profile_id}
    context = {
        'login_status_server_response': login_status_server_response,
        'is_login_status_response':login_status.is_login_status_response,
        'domain_name':domain_name,
        'project':project
    }
    return render(request,'layouts/ProjectShow.html',context) 
