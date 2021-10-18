from django.shortcuts import render,redirect
from django.contrib import messages
import mysql.connector
import time
from django.conf import settings
import pickle
import mysql.connector
import time
import pickle
from django.shortcuts import render,redirect
from AptLibrary.Python.Script import ConvertSecToTime

def owner_project_responce(request):
	#try:
		# Database connection with mysql#
		conn = mysql.connector.connect(host='3.108.45.242',user='mypro_db',password='mypro_db',database='mypro_db')
		#Creating a cursor object using the cursor() method
		connCursor = conn.cursor(buffered=True)

		EPASS='GFtCtuL7JdCJqmE3CgHBsN3GhPMwAV8pgu8bqKkR8Pg85L8XKJ4Mv2XtwkBvtLtr'

		try:
			LID = request.COOKIES['LID']
			LAID = request.COOKIES['LAID']
		except:
			return 'False'


		sql = f"SELECT AES_DECRYPT(project_id,'{EPASS}'),AES_DECRYPT(account_id,'{EPASS}'),AES_DECRYPT(title,'{EPASS}'),AES_DECRYPT(description,'{EPASS}'),AES_DECRYPT(project_category,'{EPASS}'),AES_DECRYPT(project_image,'{EPASS}'),AES_DECRYPT(last_upd_time,'{EPASS}') FROM project_upload WHERE account_id = AES_ENCRYPT(%s,'{EPASS}')"
		connCursor.execute(sql, (LAID,))
		conn.commit()
		if(connCursor.rowcount < 1):
			return {'status':'False','v':1}

		results = connCursor.fetchall()
		if(len(results) < 1):
			return {'status':'False','v':2}

		result_array = list()
		for result in results:
			if(result[0] != None and len(result[0]) > 0):
			    project_id = str(result[0], encoding='utf-8', errors='strict')
			else:
			   return {'status':'False','v':3}

			if(result[1] != None and len(result[1]) > 0):
			    account_id = str(result[1], encoding='utf-8', errors='strict')
			else:
			    return {'status':'False','v':4}

			if(result[2] != None and len(result[2]) > 0):
			    title = str(result[2], encoding='utf-8', errors='strict')
			else:
			   return {'status':'False','v':5}

			if(result[3] != None and len(result[3]) > 0):
			    description = str(result[3], encoding='utf-8', errors='strict')
			else:
			   return {'status':'False','v':6}

			if(result[4] != None and len(result[4]) > 0):
			    project_category = str(result[4], encoding='utf-8', errors='strict')
			else:
			   return {'status':'False','v':7}

			if(result[5] != None and len(result[5]) > 0):
			    project_image = result[5]
			else:
				return {'status':'False','v':8}
			if(result[6] != None and len(result[6]) > 0):
			    last_upd_time = result[6]
			else:
			   return {'status':'False','v':9}

			if(isinstance(project_image, (bytes,bytearray))):
			    try:
			        project_image_array = pickle.loads(project_image)
			    except:
			        return {'status':'False','v':10}
			else:
				return {'status':'False','v':11}

			if(len(project_image_array) < 1):
				return {'status':'False','v':12}
			
			result_array.append({'project_id':project_id,'account_id':account_id,'title':title,'description':description,'project_category':project_category,'project_image':project_image_array,'last_upd_time':last_upd_time,'last_upd_sort_time':ConvertSecToTime.ConvertSecToSortTime(time.time() - float(last_upd_time))})
		return {'status':'True','result':result_array}
	# except:
	# 	return {'status':'False','v':0}