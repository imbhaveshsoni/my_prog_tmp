import mysql.connector
import time
import pickle
from django.shortcuts import render,redirect
is_login_status_response = 'False'
def login_status_response(request):
	try:
		global is_login_status_response 
		is_login_status_response = 'False'
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

		sql = f"SELECT AES_DECRYPT(login_data,'{EPASS}'),AES_DECRYPT(fname,'{EPASS}'),AES_DECRYPT(lname,'{EPASS}'),AES_DECRYPT(email,'{EPASS}'),AES_DECRYPT(profile_id,'{EPASS}') FROM register_account WHERE account_id = AES_ENCRYPT(%s,'{EPASS}')"
		connCursor.execute(sql, (LAID,))
		conn.commit()

		if(connCursor.rowcount != 1):
			return 'False'

		result = connCursor.fetchall()

		if(len(result) > 0 and len(result[0]) > 0 and result[0][1] != None and len(result[0][1]) > 0):
		    fname = str(result[0][1], encoding='utf-8', errors='strict')
		else:
		    return 'False'

		if(len(result) > 0 and len(result[0]) > 0 and result[0][2] != None and len(result[0][2]) > 0):
		    lname = str(result[0][2], encoding='utf-8', errors='strict')
		else:
		   return 'False'

		if(len(result) > 0 and len(result[0]) > 0 and result[0][3] != None and len(result[0][3]) > 0):
		    email = str(result[0][3], encoding='utf-8', errors='strict')
		else:
		   return 'False'

		if(len(result) > 0 and len(result[0]) > 0 and result[0][4] != None and len(result[0][4]) > 0):
		    profile_id = str(result[0][4], encoding='utf-8', errors='strict')
		else:
		   return 'False'

		if(len(result) > 0 and len(result[0]) > 0 and result[0][0] != None and len(result[0][0]) > 0 and isinstance(result[0][0], bytearray)):
		    try:
		        login_data_fetch = pickle.loads(result[0][0])
		    except:
		        return 'False'
		else:
		    return 'False'


		if "login_id" in login_data_fetch and len(login_data_fetch['login_id']) > 0 and isinstance(login_data_fetch['login_id'], list):
		    login_id_fetch = login_data_fetch['login_id']
		else:
		    return 'False'

		IsLoginVerify = False
		if(len(login_id_fetch) > 0):
		    for item in login_id_fetch:
		        if(item['id'] == LID):
		        	IsLoginVerify = True
		        	break
		else:
			return 'False'

		if(IsLoginVerify == True):
			is_login_status_response = 'True'
			return {'fname':fname,'lname':lname,'email':email,'profile_id':profile_id,'account_id':LAID,'LID':LID}
		else:
			return 'False'
	except:
		return 'False'