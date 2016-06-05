__author__ = 'Bhargav'
import django
import sys,os
#from django.core.management import setup_environ
#from MissionRnD import settings

sys.path.append("C:/MissionRnD/")
os.environ["DJANGO_SETTINGS_MODULE"] = "MissionRnD.settings"
django.setup()



import click
import _mysql
from openpyxl import Workbook
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from College.models import *

book=[]
result=[]
def getExcelData(name):
	origin=load_workbook(filename=name)
	global book 
	for sheet in origin:
		sheet_details=[]
		rows=sheet.rows
		for row in rows:
			row_details=[]
			for cell in row:
				row_details.append(cell.value)
				pass
			sheet_details.append(row_details)
		book.append(sheet_details)
	del book[0][0]
	del book[1][0]
	del book[2][0]
def getHtmlData(name):
	soup = BeautifulSoup(open(name),'html.parser')
	#print (soup.prettify())
	global result
	table= soup.body.table
	for row in table:
		row_value=[]
		for cell in row:
			row_value.append(cell.get_text())
		result.append(row_value)
	del result[0]
def DjangoCollege():
	for row in book[2]:
		college=College(name=row[0],acronym=row[1],location=row[2],email=row[3])
		college.save()
def DjangoStudent():
	for row in book[0]:
		college=College.objects.get(acronym=row[1])
		name=row[3]
		student=Student(name=row[0],college=college,email=row[2],dbfolder=name.lower(),dropout=False)
		student.save()
def DjangoDropOut():
	for row in book[1]:
		try:
			student=Student.objects.get(name=row[0])
			student.dropout=True
			student.save()
		except Exception:
			college=College.objects.get(acronym=row[1])
			name=row[3]
			student =Student(name=row[0],college=college,email=row[2],dbfolder=name.lower(),dropout=True)
			student.save()
def DjangoMarks():
	for row in result:
		try:
			data=row[1]
			data=data.split('_')
			student=Student.objects.get(dbfolder=data[2])
			marks=Marks(name=student,transform=int(row[2]),from_custom_base26=int(row[3]),get_pig_latin=int(row[4]),top_chars=int(row[5]),total=int(row[6]))
			marks.save()
		except Exception:
			pass
@click.group()
def cli():
	pass

@click.command()
@click.argument('arguements',nargs=3)
def createdb(arguements):
	"""pass server,username,database"""
	strings=[]
	for str in arguements:
		strings.append(str)
	db = _mysql.connect("localhost", strings[0], strings[1])
	db.query("create schema "+strings[2])
	click.echo("Database:" + strings[2] + " Created")


@click.command()
@click.argument('arguements',nargs=3)
def dropdb(arguements):
	"""Arguements: username password database_name"""
	strings=[]
	for str in arguements:
		strings.append(str)
	db = _mysql.connect("localhost", strings[0], strings[1])
	db.query("drop schema "+strings[2])
	click.echo("Database:" + strings[2] + " Dropped")

@click.command()
@click.argument('arguements',nargs=2)
def populatedata(arguements):
	"""Arguements: excel_file html_file"""
	strings=[]
	for str in arguements:
		strings.append(str)
	getExcelData(strings[0])
	getHtmlData(strings[1])
	DjangoCollege()
	DjangoStudent()
	DjangoDropOut()
	DjangoMarks()
	click.echo("Data Populated")
	pass

@click.command()
@click.argument('arguements',nargs=3)
def cleardata(arguements):
	"""Arguements: username password database_name"""
	strings=[]
	for str in arguements:
		strings.append(str)
	db = _mysql.connect("localhost", strings[0], strings[1],strings[2])
	db.query("DELETE FROM college_marks where 1")
	db.query("DELETE FROM college_student where 1")
	db.query("DELETE FROM college_college where 1")
	click.echo("Data Cleared")

cli.add_command(createdb)
cli.add_command(dropdb)
cli.add_command(populatedata)
cli.add_command(cleardata)

if __name__ == '__main__':
    cli()